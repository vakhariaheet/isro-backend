from flask import Flask,render_template,request,jsonify
from flask_socketio import SocketIO, emit
import whisper
from utils.model import nlp
import numpy as np
import io
from scipy.io import wavfile
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")
model = whisper.load_model("base.en")

@app.route('/',methods=['GET'])
def hello_world():
    text = request.args.get('transcript')
    doc = nlp(text)
    
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    intent = doc._.intent

    return jsonify({
        'entities': entities,
        'intent': intent
    })

@socketio.on('audio_chunk')
def handle_transcription(audio_chunk):
    print('Received audio chunk')
    with io.BytesIO(audio_chunk) as wav_file:
        sample_rate, audio_np = wavfile.read(wav_file)
        print('Received audio chunk with sample rate', sample_rate)
        # Convert to float32 and normalize
        audio_float = audio_np.astype(np.float32) / 32768.0
        result = model.transcribe(audio_float)
        print(result)
        socketio.emit('transcription_result', {'text': result['text']})



@app.route('/train')
def train():
    return render_template('train.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=3004)

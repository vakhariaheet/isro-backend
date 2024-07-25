from flask import Flask,request,jsonify
from flask_socketio import SocketIO, emit
from utils.resp import send_response
import whisper
import numpy as np
import io
import json
from scipy.io import wavfile
import ssl
import time
import os
# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context
model = whisper.load_model('small.en')

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/',methods=['GET'])
def hello_world():
    text = request.args.get('transcript')

    return jsonify({
        
    })

@socketio.on('audio_chunk')
def handle_transcription(data):
    audio_chunk = data['audio_chunk'] 

    print('Received audio chunk');
    current_timestamp = str(time.time()).replace('.', '');
    folder_name = 'audio_chunks';
    # Create folder if it doesn't exist
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass
    

    file_name = f'audio_{current_timestamp}.wav';

    with open(f'{folder_name}/{file_name}', 'wb') as f:
        with io.BytesIO(audio_chunk) as wav_file:
            sample_rate, audio_np = wavfile.read(wav_file)
            f.write(audio_chunk);
            print('Received audio chunk with sample rate', sample_rate)
            # Convert to float32 and normalize
            audio_float = audio_np.astype(np.float32) / 32768.0
            result = model.transcribe(audio_float)
            print(result)
            socketio.emit('transcription_result', {'text': result['text']})

@app.route('/login',methods=['POST'])
def login():
    data = request.json
    print(data['username']);
    return send_response(status=203)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=3004)

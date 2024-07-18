import spacy
from spacy.language import Language

# Load the custom model
nlp = spacy.load("base")

# Ensure the custom components are added
@Language.component("intent_classifier")
def intent_classifier(doc):
    actions = ["zoom", "add marker", "remove marker", "pan", "search"]
    text = doc.text.lower()
    for action in actions:
        if action in text:
            doc._.intent = action
            return doc
    doc._.intent = "unknown"
    return doc

# Add the custom attribute if it doesn't exist
if not spacy.tokens.Doc.has_extension("intent"):
    spacy.tokens.Doc.set_extension("intent", default=None)

# Add the component to the pipeline if it's not already there
if 'intent_classifier' not in nlp.pipe_names:
    nlp.add_pipe("intent_classifier")

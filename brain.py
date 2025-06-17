from transformers import pipeline

# Load pre-trained emotion classifier model
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

def detect_emotion(text):
    emotions = classifier(text)[0]  # Get prediction results
    return sorted(emotions, key=lambda x: x['score'], reverse=True)  # Sort by confidence

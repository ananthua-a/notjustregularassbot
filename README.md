# notjustregularassbot
An emotionally aware chatbot powered by Gemini and HuggingFace, designed to reflect human depth, track emotional states, and remember past conversations. This project explores the intersection of empathy, memory, and A
📁 File Structure
main.py: The core of the chatbot.

Handles user input/output.

Loads the Gemini model.

Builds a custom prompt including live emotion analysis, polarity, and reference to memory.

Calls all components together.

brain.py:

Loads a HuggingFace model (like j-hartmann/emotion-english-distilroberta-base) to detect emotions from user messages.

Returns a list of probable emotions with scores.

memory.py:

Manages reading from and writing to memory.json.

Stores each interaction with: username, user message, emotion, polarity, and bot response.

memory.json:

A local JSON file where ALL interactions are saved permanently.

Used during each conversation to maintain context and build emotional continuity

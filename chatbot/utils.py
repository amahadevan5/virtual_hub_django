import os
import random
import json
from nltk.stem import WordNetLemmatizer

# Load intents data
with open(os.path.join(os.path.dirname(__file__), 'intents.json')) as file:
    intents = json.load(file)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to preprocess text data
def preprocess(text):
    """
    Preprocess text data by removing special characters, converting to lowercase,
    and lemmatizing the words.
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

# Function to predict intent based on user input
def predict_intent(text):
    """
    Predict the intent of user input by comparing the input to known intents
    and returning the intent with the highest probability score.
    """
    # Preprocess user input
    words = preprocess(text)
    # Create bag of words from user input
    bag = [0] * len(words)
    for i, w in enumerate(words):
        for j, word in enumerate(intents['words']):
            if w == word:
                bag[j] = 1
    # Make prediction using model
    predictions = model.predict([bag])
    # Find index of highest probability score
    index = np.argmax(predictions)
    # Return intent with highest probability score
    return intents['intents'][index]['tag']

# Function to generate response to user input
def generate_response(intent):
    """
    Generate a response to user input by randomly selecting a response
    from the appropriate intent in the intents data.
    """
    # Find the appropriate intent in the intents data
    for i in intents['intents']:
        if i['tag'] == intent:
            responses = i['responses']
            # Return a randomly selected response
            return random.choice(responses)

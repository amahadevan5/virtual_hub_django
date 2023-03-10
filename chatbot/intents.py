from collections import defaultdict

# Define a defaultdict to store the intent data
intents = defaultdict(list)

# Define the intents and responses
intents['greeting'].append({'response': 'Hello! How can I assist you today?'})
intents['goodbye'].append({'response': 'Goodbye! Have a great day!'})
intents['thanks'].append({'response': 'You\'re welcome!'})

# Define a function to return the appropriate response for a given intent
def get_response(intent):
    if intent in intents:
        return intents[intent][0]['response']
    else:
        return 'I\'m sorry, I don\'t understand what you\'re asking.'

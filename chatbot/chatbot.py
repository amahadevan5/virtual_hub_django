from chatbot.intents import *
from chatbot.utils import *

class Chatbot:
    def __init__(self):
        self.intents = intents()
        self.context = {}

    def handle_message(self, message):
        # Get the intent with the highest score
        intent_name, intent_score = self.intents.get_intent(message)
        
        if intent_score < 0.5:
            return "I'm sorry, I'm not sure what you mean. Can you please rephrase your question?"

        # Get the appropriate response and context
        intent = self.intents.get_intent_by_name(intent_name)
        response, self.context = intent.get_response(message, self.context)

        # Return the response
        return response

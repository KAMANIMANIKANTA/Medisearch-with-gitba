# test_chatbot.py
from Chatbot.model import ChatbotModel
from Chatbot.utilities import preprocess_text

# Initialize the chatbot model
chatbot = ChatbotModel()

# Test input
test_input = "What is paracetamol used for?"

# Preprocess input
processed_input = preprocess_text(test_input)
print(f"Processed input: {processed_input}")

# Get response from the chatbot model
try:
    response = chatbot.get_response(processed_input)
    print(f"Chatbot response: {response}")
except Exception as e:
    print(f"Error getting response: {e}")

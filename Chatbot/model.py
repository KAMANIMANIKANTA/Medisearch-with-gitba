# Chatbot/model.py

from pymongo import MongoClient

class ChatbotModel:
    def __init__(self):
        """
        Initialize the ChatbotModel by setting up a connection to the MongoDB database.
        """
        # Initialize MongoDB connection
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['medicine_db']
        self.medicines_collection = self.db['medicines']
        print("Chatbot model initialized successfully.")

    def get_response(self, input_text):
        """
        Generate a response based on the input text provided by the user.

        Parameters:
        input_text (str): The text input from the user that needs a response.

        Returns:
        str: The chatbot's response to the input text.
        """
        try:
            # Search for the medicine in the database
            medicine = self.medicines_collection.find_one({"name": input_text.lower()})
            
            if medicine:
                # Construct the response with detailed medicine information
                response = (
                    f"Medicine Name: {medicine['name'].capitalize()}\n"
                    f"Usage: {medicine['usage']}\n"
                    f"Why to Use: {medicine['why_to_use']}\n"
                    f"Advantages: {medicine['advantages']}\n"
                    f"Disadvantages: {medicine['disadvantages']}\n"
                    f"Side Effects: {medicine['side_effects']}\n"
                )
            else:
                # If the medicine is not found, return a default response
                response = "Sorry, I couldn't find information about this medicine."
            
            print(f"Generated response: {response}")  # Debug log
            return response
        except Exception as e:
            # Print the error and return a fallback message
            print(f"Error in generating response: {e}")
            return "Sorry, I couldn't process your request."

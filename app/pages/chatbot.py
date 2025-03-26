import streamlit as sl
import uuid
from datetime import datetime
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

class GeminiLegalChatbot:
    def __init__(self):
        """
        Initialize Gemini chatbot with configuration
        """
        # Load environment variables
        load_dotenv()
        
        # Configure Gemini API
        api_key = os.getenv("API_KEY")
        if not api_key:
            sl.error("API Key not found. Please check your .env file.")
            return None
        
        genai.configure(api_key=api_key)
        
        # Initialize Gemini model and chat
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
        self.chat = self.model.start_chat(history=[])
        
        # Initial system message
        self.chat.send_message("You are a paralegal and legal assistant whose purpose is to create legal documents to be submitted to courts")
        
        # Initialize session state for chat history
        if 'chat_history' not in sl.session_state:
            sl.session_state.chat_history = []
        
        if 'conversation_id' not in sl.session_state:
            sl.session_state.conversation_id = str(uuid.uuid4())

    def _validate_input(self, user_input):
        """
        Validate user input
        """
        if not user_input or len(user_input.strip()) < 2:
            sl.warning("Please enter a valid message")
            return False
        return True

    def generate_response(self, user_input, uploaded_image=None):
        """
        Generate response from Gemini model
        """
        try:
            if uploaded_image:
                # If image is uploaded, include it in the message
                response = self.chat.send_message([user_input, uploaded_image])
            else:
                # Text-only response
                response = self.chat.send_message(user_input)
            
            return response.text
        except Exception as e:
            sl.error(f"Error generating response: {e}")
            return "I'm sorry, but I encountered an error processing your request."

    def display_chat_history(self):
        """
        Render chat history
        """
        for message in sl.session_state.chat_history:
            with sl.chat_message(message['role']):
                sl.markdown(message['content'])

    def handle_user_input(self):
        """
        Process user input and generate bot response
        """
        # Image upload section
        uploaded_file = sl.file_uploader("Upload an image (optional)", type=['png', 'jpg', 'jpeg'])
        uploaded_image = None
        
        if uploaded_file is not None:
            uploaded_image = Image.open(uploaded_file)
            sl.image(uploaded_image, caption="Uploaded Image", width=200)

        # Chat input
        user_input = sl.chat_input("Ask a legal question...")
        
        if user_input and self._validate_input(user_input):
            # Display user message
            sl.chat_message("user").markdown(user_input)
            
            # Add user message to chat history
            sl.session_state.chat_history.append({
                'role': 'user',
                'content': user_input,
                'timestamp': datetime.now()
            })
            
            # Generate and display bot response
            bot_response = self.generate_response(user_input, uploaded_image)
            
            sl.chat_message("assistant").markdown(bot_response)
            
            # Add bot response to chat history
            sl.session_state.chat_history.append({
                'role': 'assistant',
                'content': bot_response,
                'timestamp': datetime.now()
            })

    def show_chat_controls(self):
        """
        Render additional chat management controls
        """
        col1, col2 = sl.columns(2)
        
        with col1:
            if sl.button("🗑️ Clear Conversation"):
                sl.session_state.chat_history = []
                sl.experimental_rerun()
        
        with col2:
            # Download conversation history
            conversation_text = "\n\n".join([
                f"{msg['role'].upper()} [{msg['timestamp']}]: {msg['content']}" 
                for msg in sl.session_state.chat_history
            ])
            
            sl.download_button(
                label="💾 Save Conversation",
                data=conversation_text,
                file_name=f"legal_chat_{sl.session_state.conversation_id}.txt",
                mime="text/plain"
            )

def show():
    """
    Main function to render chat interface
    """
    # Page title
    sl.markdown("# <p style='text-align:center;'>AI Legal Assistant</p>", unsafe_allow_html=True)

    # Initialize and run chat interface
    try:
        chat_interface = GeminiLegalChatbot()
        
        if chat_interface:
            # Display existing chat history
            chat_interface.display_chat_history()
            
            # Handle user input
            chat_interface.handle_user_input()
            
            # Show additional chat controls
            chat_interface.show_chat_controls()
    except Exception as e:
        sl.error(f"Error initializing chatbot: {e}")
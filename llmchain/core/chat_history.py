class ChatHistory:
    """A simple chat history module."""
    def __init__(self):
        self.messages = []

    def add_message(self, sender, message):
        self.messages.append({"sender": sender, "message": message})

    def get_history(self):
        return self.messages

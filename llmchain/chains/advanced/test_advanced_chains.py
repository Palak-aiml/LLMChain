import unittest
from llmchain.chains.advanced.qa_chain import QAChain
from llmchain.chains.advanced.summarization_chain import SummarizationChain
from llmchain.chains.advanced.conversational_chain import ConversationalChain

class DummyLLM:
    def generate(self, prompt, **kwargs):
        return f"LLM output for: {prompt}"

class DummyRetriever:
    def retrieve(self, question):
        return [f"Context for: {question}"]

class DummyPromptManager:
    def build_qa_prompt(self, question, context_docs):
        return f"Q: {question} Context: {context_docs}"
    def build_summarization_prompt(self, documents):
        return f"Summarize: {documents}"
    def build_conversation_prompt(self, user_input, history):
        return f"User: {user_input} History: {history}"

class DummyMemory:
    def __init__(self):
        self.hist = []
    def get_history(self):
        return self.hist
    def append(self, user, resp):
        self.hist.append((user, resp))

class TestAdvancedChains(unittest.TestCase):
    def setUp(self):
        self.llm = DummyLLM()
        self.retriever = DummyRetriever()
        self.prompt_manager = DummyPromptManager()
        self.memory = DummyMemory()

    def test_qa_chain(self):
        chain = QAChain(self.llm, self.retriever, self.prompt_manager)
        result = chain.run("What is AI?")
        self.assertIn("LLM output", result)

    def test_summarization_chain(self):
        chain = SummarizationChain(self.llm, self.prompt_manager)
        result = chain.run(["AI is intelligence demonstrated by machines."])
        self.assertIn("LLM output", result)

    def test_conversational_chain(self):
        chain = ConversationalChain(self.llm, self.memory, self.prompt_manager)
        result = chain.run("Hello!")
        self.assertIn("LLM output", result)
        self.assertEqual(len(self.memory.get_history()), 1)

if __name__ == "__main__":
    unittest.main()

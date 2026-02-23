"""
QA Chain Template: Example of a retrieval-augmented question answering chain.
"""
from llmchain.llms.openai_llm import OpenAILLM
from llmchain.retrievers.simple_retriever import SimpleRetriever
from llmchain.prompts.prompt_manager import PromptManager
from llmchain.chains.advanced.qa_chain import QAChain

if __name__ == "__main__":
    llm = OpenAILLM(api_key="YOUR_OPENAI_API_KEY")
    retriever = SimpleRetriever()
    prompt_manager = PromptManager()
    chain = QAChain(llm, retriever, prompt_manager)
    question = "What is LangChain?"
    answer = chain.run(question)
    print("Answer:", answer)

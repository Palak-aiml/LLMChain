"""
Summarization Chain Template: Example of summarizing documents with an LLM.
"""
from llmchain.llms.openai_llm import OpenAILLM
from llmchain.prompts.prompt_manager import PromptManager
from llmchain.chains.advanced.summarization_chain import SummarizationChain

if __name__ == "__main__":
    llm = OpenAILLM(api_key="YOUR_OPENAI_API_KEY")
    prompt_manager = PromptManager()
    chain = SummarizationChain(llm, prompt_manager)
    docs = ["LangChain is a framework for developing applications powered by language models."]
    summary = chain.run(docs)
    print("Summary:", summary)

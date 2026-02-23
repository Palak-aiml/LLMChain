"""
Conversational Chain Template: Example of a multi-turn conversation with memory.
"""
from llmchain.llms.openai_llm import OpenAILLM
from llmchain.memory.chat_memory import ChatMemory
from llmchain.prompts.prompt_manager import PromptManager
from llmchain.chains.advanced.conversational_chain import ConversationalChain

if __name__ == "__main__":
    llm = OpenAILLM(api_key="YOUR_OPENAI_API_KEY")
    memory = ChatMemory()
    prompt_manager = PromptManager()
    chain = ConversationalChain(llm, memory, prompt_manager)
    user_input = "Hello, who are you?"
    response = chain.run(user_input)
    print("Bot:", response)

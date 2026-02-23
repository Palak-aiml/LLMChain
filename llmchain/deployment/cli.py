"""
llmchain/deployment/cli.py

CLI entry point for LLMChain.
"""
import argparse
from llmchain.llms.dummy_llm import DummyLLM

def main():
    parser = argparse.ArgumentParser(description="LLMChain CLI")
    parser.add_argument("prompt", type=str, help="Prompt for LLM")
    args = parser.parse_args()
    llm = DummyLLM()
    print(llm.generate(args.prompt))

if __name__ == "__main__":
    main()

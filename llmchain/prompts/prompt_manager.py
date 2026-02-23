"""
llmchain/prompts/prompt_manager.py

Manages prompt templates and advanced prompt engineering utilities.
"""
class PromptManager:
    def __init__(self):
        self.prompts = {}

    def add_prompt(self, name: str, template: str):
        self.prompts[name] = template

    def get_prompt(self, name: str):
        return self.prompts.get(name)

    def format_prompt(self, name: str, **kwargs):
        template = self.get_prompt(name)
        if template:
            return template.format(**kwargs)
        raise ValueError(f"Prompt '{name}' not found.")

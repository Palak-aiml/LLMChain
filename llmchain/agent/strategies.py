"""
llmchain/agent/strategies.py

Common agent orchestration strategies for LLMChain.
"""
def round_robin_strategy(agents, input_text):
    return [agent.act(input_text) for agent in agents]

def voting_strategy(agents, input_text):
    results = [agent.act(input_text) for agent in agents]
    # Simple majority vote
    from collections import Counter
    vote = Counter(results).most_common(1)[0][0]
    return vote

def cascading_strategy(agents, input_text):
    data = input_text
    for agent in agents:
        data = agent.act(data)
    return data

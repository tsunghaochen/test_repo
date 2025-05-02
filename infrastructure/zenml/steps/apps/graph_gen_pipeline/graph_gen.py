import os


def my_knowledge_graph_gen(path: str) -> str:
    knowledge_graph = "Automodeling knowledge graph " + path
    knowledge_graph = knowledge_graph + " with Ontology and Riskchains"
    print(f"Knowlege graph of [{path}] is generated!")
    print(f"Graph output: {knowledge_graph}")
    return knowledge_graph


if __name__ == "__main__":
    my_knowledge_graph_gen("AXA_contract.pdf")
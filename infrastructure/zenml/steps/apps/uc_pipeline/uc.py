import os


def my_use_case(graph: str, use_case: str) -> str:
    output = f"{use_case}: {graph}"
    print(f"Use case [{use_case}] is created!")
    print(f"output of uc: {output}")
    return output


if __name__ == "__main__":
    my_use_case(graph="AXA_contract.pdf", use_case="Athoring Tool")
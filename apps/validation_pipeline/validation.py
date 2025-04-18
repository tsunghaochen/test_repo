import os


def my_validation(output: str, validation: str) -> float:
    score = len(output) / 100
    print(f"Validation of [{output}] using [{validation}] is [{score}]")
    return score


if __name__ == "__main__":
    my_validation("AXA_contract.pdf")
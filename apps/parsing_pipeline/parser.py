import os


def my_parser(path: str) -> str:
    print(f"Start parsing [{path}]")
    parsed_data = path.lower()
    print(f"Finish parsing [{path}]")
    print(f"Parsing output: {parsed_data}")
    return parsed_data


if __name__ == "__main__":
    my_parser("AXA_contract.pdf")
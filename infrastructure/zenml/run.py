import os
from zenml import pipeline
from zenml.logger import get_logger
from steps import (
    parsing_pipe,
    graph_gen_pipe,
    uc_pipe,
    validation_pipe,
)

logger = get_logger(__name__)


@pipeline
def automodeling_pipeline(
    parsing_doc: str,
    uc: str = "Athroing Tool",
    validation: str = "LLM_AAJ",
):
    """
    Start of the automodeling pipeline, call each step function
    """
    parsed_data = parsing_pipe(parsing_doc)
    knowlege_graph = graph_gen_pipe(parsed_data)
    output = uc_pipe(knowlege_graph, uc)
    score = validation_pipe(output, validation)

if __name__ == "__main__":
    automodeling_pipeline(parsing_doc="Axa_Contract1.pdf")
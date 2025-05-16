import os
import subprocess


GIT_REPO_PATH = "/Users/z460xj/Documents/airflow_localtest/dag_repo/dags"
BRANCH_NAME = "main"


def git_push():
    os.chdir(GIT_REPO_PATH)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Update DAG from ZenML pipeline"], check=True)
    subprocess.run(["git", "push", "origin", BRANCH_NAME], check=True)


if __name__ == "__main__":
    git_push()
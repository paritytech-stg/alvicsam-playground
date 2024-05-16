import os
import re
import sys

from github import Github
from time import sleep

try:
    access_token = os.getenv("GITHUB_TOKEN")
    sha = os.getenv("GITHUB_SHA")
    gh_repo = os.getenv("GITHUB_REPOSITORY")
    pr_num = os.getenv("GITHUB_REF_NAME").split("/")[0]
except KeyError as error:
    print(f"{error} not found in environment variables")
    sys.exit(1)


def get_workflow_id(url):
    """
    Extracts the workflow ID from a given URL.

    Args:
        url (str): The URL containing the workflow ID.

    Returns:
        str or None: The extracted workflow ID if found, None otherwise.
    """
    pattern = r"/actions/runs/(\d+)/"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None


if __name__ == "__main__":
    sleep(30)
    print("Canceling workflows")
    g = Github(access_token)
    repo = g.get_repo(gh_repo)
    commit = repo.get_commit(sha=sha)
    check_runs = commit.get_check_runs()
    workflow_ids = []

    print(f"Commit: {commit}")
    print(f"Check runs: {check_runs}")

    for check_run in check_runs:
        print(f"Check run: {check_run}")
        id = get_workflow_id(check_run.html_url)
        if id:
            workflow_ids.append(id)

    workflow_ids = list(set(workflow_ids))
    print(workflow_ids)

    # stop all running workflows
    for workflow_id in workflow_ids:
        workflow = repo.get_workflow_run(int(workflow_id))
        print(workflow.status)
        if workflow.status == "in_progress" or workflow.status == "queued":
            workflow.cancel()
            print(f"Workflow {workflow_id} has been cancelled.")
        else:
            print(f"Workflow {workflow_id} is not running.")
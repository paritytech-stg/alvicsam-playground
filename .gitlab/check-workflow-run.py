#script checks that the workflow is completed

import os
import sys
import requests

github_token = os.getenv("GITHUB_TOKEN")
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_token}",
    "X-GitHub-Api-Version": "2022-11-28",
}

def is_run_completed(org_name, repo_name, run_id):
    """
    Check if a workflow is completed.

    Args:
        org_name (str): The name of the organization.
        repo_name (str): The name of the repository.
        run_id (str): The ID of the run.
        uuid (str): The UUID for logging purposes.

    Returns:
        str: The status of the workflow.
    """
    url = f"https://api.github.com/repos/{org_name}/{repo_name}/actions/runs/{run_id}"
    print(f"Checking {url}")
    response = requests.get(url, headers=headers)
    while True:
        if response.status_code == 200:
            data = response.json()
            print(f" Current workflow status: {data['status']}")
            if data["status"] == "in_progress" or data["status"] == "queued":
                print("Workflow is still running")
        else:
            print(f" Request failed with status code {response.status_code}")
            return
    print("Workflow is completed")
    return 
import requests
import os

GITHUB_API = "https://api.github.com"
TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {TOKEN}"
}

def get_repos(username):
    url = f"{GITHUB_API}/users/{username}/repos"
    response = requests.get(url, headers=headers)
    return response.json()


def create_issue(owner, repo, title, body):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues"
    data = {
        "title": title,
        "body": body
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

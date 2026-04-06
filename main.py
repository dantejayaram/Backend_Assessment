from fastapi import FastAPI
from github_service import get_repos, create_issue

app = FastAPI()

@app.get("/repos/{username}")
def fetch_repos(username: str):
    return get_repos(username)


@app.post("/create-issue/")
def create_github_issue(owner: str, repo: str, title: str, body: str):
    return create_issue(owner, repo, title, body)

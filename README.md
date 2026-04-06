# Backend_Assessment

Setup
pip install -r requirements.txt

Run
uvicorn main:app --reload

Endpoints
GET /repos/{username}
POST /create-issue

So the token should not be include in the repos as of assessment scenario use this token it is only create for this assessment and given access to this particular repo alone

Token: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

Create .env  file and add this above token

GITHUB_TOKEN=Token

# 🚀 CI/CD Challenge with GitHub Actions

This project demonstrates a CI/CD pipeline using GitHub Actions to simulate Dev → QA → Prod environments for a simple Streamlit
 app.

The goal is to practice modern DevOps workflows: continuous integration (CI), continuous delivery (CD), environment approvals, and branch protections.

## 📚 Features

### Continuous Integration (CI)

- Runs unit tests automatically on pull requests → main.

- Ensures code quality before merging into production.

### Continuous Delivery (CD)

Automatic deployments triggered by branch pushes:

- dev → deploys to Dev (green background).

- qa → deploys to QA (yellow background).

- main → deploys to Production (red background, requires approval).

Logs deployment step with a 🚀 message.

Environment-Specific UI

The Streamlit app changes its title and background color depending on the environment:

- Dev → 🚀 Dev Environment (green)

- QA → 🔍 QA Environment (yellow)

- Prod → 🔥 Production Environment (red)

## 📂 Project Structure
```
.
├── app/
│   └── main.py              # Streamlit entry point
├── tests/
│   └── test_app.py          # Unit tests (Pytest)
├── .github/
│   └── workflows/
│       ├── ci.yml           # CI workflow
│       └── cd.yml           # CD workflow
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```
## ⚙️ Workflows
🔹 CI (.github/workflows/ci.yml)

Trigger: pull request to main

Jobs:

- Checkout repo

- Install dependencies

- Run unit tests with Pytest

🔹 CD (.github/workflows/cd.yml)

Trigger: push to dev, qa, or main

Jobs:

- Checkout repo

- Install dependencies

- Set environment (APP_ENV) based on branch

-Run deployment script

- Notify on success

## 🖼️ Screenshots

Here you may see the streamlit UI for the development environments:

![devstreamlit](C:\Users\fhaul\Documents\GitHub\challenge-ci-cd-github\devstreamlit.png)

Here you may see the qa branch merging from the dev branch : 

![qamerging](C:\Users\fhaul\Documents\GitHub\challenge-ci-cd-github\qamerging.png)

Here you have the github actions with the qa deployement CD response successfull : 

![qadeployement](C:\Users\fhaul\Documents\GitHub\challenge-ci-cd-github\qadeployement.png)

The deployement branch also worked for production:

![proddeployment](C:\Users\fhaul\Documents\GitHub\challenge-ci-cd-github\proddeployment.png)

Finally, you may see the CI workflow working after pulling request :

![ciworkflow](C:\Users\fhaul\Documents\GitHub\challenge-ci-cd-github\ciworkflow.png)

## 🧪 Running Locally

Clone the repo and install dependencies:
```
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python -m venv .venv
source .venv/bin/activate   # (Linux/Mac)
.venv\Scripts\activate      # (Windows)
pip install -r requirements.txt
```

Run the app locally with an environment:

```
APP_ENV=Dev python -m streamlit run app/main.py    # Linux/Mac
$env:APP_ENV="Dev"; streamlit run app/main.py      # Windows (PowerShell)
```

##  ✅ Unit Tests

Run all tests with Pytest:

```
pytest tests/
```

## 🔒 GitHub Environments

- Dev → automatic deployment, no approval

- QA → automatic deployment, no approval

- Prod → requires manual approval in GitHub before going live

## 🌟 Next Improvements

- Add linting (flake8/black)

- Upload artifacts (test reports, build logs)

- Use GitHub Secrets for credentials simulation
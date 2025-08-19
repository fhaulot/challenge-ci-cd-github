# Challenge: CI/CD with GitHub Actions

- **Repository:** `challenge-ci-cd-github`  
- **Type of Challenge:** Consolidation  
- **Duration:** 2 days  
- **Deadline:** 20/06/2025 - 5:00 PM  
- **Team Challenge:** Solo 


## 🎯 Mission Objectives
Practice **CI/CD with GitHub Actions** by simulating **Dev → QA → Prod environments** within free account limits.


## 📚 Learning Objectives
- Understand GitHub Actions workflows.  
- Run automated build & test jobs (CI).  
- Simulate deployments to multiple environments (CD).  
- Use GitHub Environments & approvals.  
- Work with branches and branch protections.  


## 📝 The Mission
You apply for a junior DevOps position.  
As part of the technical test, you must set up a **GitHub Actions pipeline** that:  
- Builds & tests the code (CI).  
- Deploys to **Dev, QA, and Prod** environments (CD).  
- Requires **approval** before going live in production.  


## ✅ Must-Have Features
- CI workflow runs tests on **pull requests → main**.  
- CD workflow deploys automatically:  
  - To **Dev** on push to `dev` branch.  
  - To **QA** on push to `qa` branch.  
  - To **Prod** on push to `main` branch (**with approval**).  
- Each deploy step outputs a log like:  
    🚀 Deployed to 'environment'


## 🌟 Nice-to-Have Features
- Add linting before build.  
- Upload artifacts (e.g., test reports, build output).  
- Deploy a sample app (streamlit).  
- Use secrets to simulate credentials.  

## ⚙️ Constraints
- Use **Streamlit** for the sample app.  
- The app should display a different message or style depending on the environment:  
  - **Dev** → page title “Dev Environment” + green background.  
  - **QA** → page title “QA Environment” + yellow background.  
  - **Prod** → page title “Production Environment” + red background.  
- Keep **CI** and **CD** in separate workflow files:  
  - `.github/workflows/ci.yml`  
  - `.github/workflows/cd.yml`  
- Use GitHub **Environments** with approvals required for Prod.  
 

## 📂 Repository Structure

- `README.md` → Project documentation (description, usage, screenshots)  
- `app/` → Sample application code  
  - `main.py` → Example entry point (Python/Node.js/etc.)  
- `tests/` → Unit tests for CI  
  - `test_app.py`  
- `.github/workflows/` → GitHub Actions workflows  
  - `ci.yml` → Continuous Integration (tests on PRs)  
  - `cd.yml` → Continuous Delivery (deploy to Dev/QA/Prod)  


## 📦 Deliverables
- Public GitHub repo with workflows enabled.  
- README must include:  
  - Description  
  - How to trigger CI/CD  
  - Example logs or screenshots  

## 🧮 Evaluation Criteria

| Criteria    | Indicator |
|-------------|-----------|
| **Complete** | All must-have features implemented.<br>Repo public & workflows enabled.<br>CI runs on PRs, CD runs on branch pushes. |
| **Correct** | Workflows valid & pass.<br>Prod requires manual approval. |
| **Great**   | README is clear and complete.<br>Stretch goals implemented. |

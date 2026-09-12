# Credit Card Fraud Detection – ML Deployment Pipeline

An end-to-end machine learning deployment project with automated testing, CI/CD, Docker, and Google Cloud deployment for credit card fraud detection.

## Live Demo

[Try the live demo](https://fraud-detection-api-841926338477.europe-west1.run.app)

The demo uses a real fraudulent transaction from the test set and sends it to the deployed model for prediction.

## Deployment Pipeline

Code changes pushed to the `main` branch automatically trigger the CI/CD pipeline:

Git Push → Pytest → Docker Build → Google Artifact Registry → Google Cloud Run

GitHub Actions runs the tests, builds the Docker image, pushes it to Artifact Registry, and deploys the latest version to Cloud Run.

## Model

Two machine learning models were trained and evaluated:

- Random Forest
- XGBoost

Random Forest was selected for deployment based on its performance on fraud detection.

## Dataset

The project uses the **Credit Card Fraud Detection** dataset from Kaggle.

- 284,807 transactions
- 492 fraudulent transactions
- 80/20 train-test split
- 30 input features: `Time`, `Amount`, and `V1–V28`
- `V1–V28` are anonymized PCA-transformed features

[Dataset Source – Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## Tech Stack

- Python
- Scikit-learn
- XGBoost
- FastAPI
- Pytest
- Docker
- GitHub Actions
- Google Cloud Run
- Google Artifact Registry
- Workload Identity Federation
- HTML / JavaScript
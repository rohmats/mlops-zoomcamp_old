# This is my personal repo for MLOps Zoomcamp from DataTalksClub
> Course repository [link](https://github.com/DataTalksClub/mlops-zoomcamp)
## Chapter 1 - Introduction
### Environment preparation
[![Watch the video](https://img.youtube.com/vi/MzcmWXYxi2s/hqdefault.jpg)](https://youtu.be/MzcmWXYxi2s)


## Chapter 2 - Experiment Tracking
### Create environment - GiHub Codespace
``` bash
conda create --name exp-tracking-env python=3.9
```

### Activate experiment tracking environment
``` bash
conda activate exp-tracking-env
```

### Change to directory
```bash
cd 02-experiment-tracking
```
### Install requirements.txt
```bash
pip install -r requirements.txt
```

### Run MLFlow
```bash
mlflow ui --backend-store-uri sqlite:///mlflow.sqlite
```


## Chapter 3 - Orchestration and ML Pipelines
### Clone mage repository
```bash
git clone https://github.com/mage-ai/mlops.git
cd mlops
```

### Launch mage
```bash
./scripts/start.sh
```
### Open mage
Open http://localhost:6789 in your browser.

## Chapter 4 - Model Deployment
### Deploying models with Flask and Docker
#### Initialize Environment
```bash
pipenv shell
pipenv sync # or pipenv sync --dev
```
#### Running App in gunicorn
```bash
gunicorn --bind=0.0.0.0:9696 predict:app
```
#### Test App
```bash
python test.py
```
#### Dockerize it
```bash
docker build -t ride-duration-prediction-service:v1 .
```
#### Run App in Docker
```bash
docker run -it --rm -p 9696:9696  ride-duration-prediction-service:v1
```

## Chapter 5 - Model Monitoring
### Activate Environment
```bash
cd /workspaces/mlops-zoomcamp/05-monitoring/taxi_monitoring
conda activate model_monitoring
```

### Run Grafana Docker
```bash
docker compose up --build
```

### Open in browser
Grafana: http://127.0.0.1:3000/login
Adminer: http://127.0.0.1:8080/index.php

<!-- ## Chapter X - XXX
### Subjudul
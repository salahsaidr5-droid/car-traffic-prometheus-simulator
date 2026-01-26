# Car Traffic Prometheus Simulator

A simple Python exporter that simulates car traffic counts and exposes Prometheus metrics at:
http://localhost:8000/metrics

## Architecture
![Architecture Diagram](images/architecture.png)

## Run
```bash
pip install prometheus_client
python3 car_simulator.py

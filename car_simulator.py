from prometheus_client import start_http_server, Gauge
import random
import time

car_counter = Gauge("car_count", "Number of cars per location per day", ["location", "day"])

locations = [f"a-{i}" for i in range(100)]

def simulate_traffic():
    for day in range(1, 31):
        for loc in locations:
            count = random.randint(50, 500)
            car_counter.labels(location=loc, day=str(day)).set(count)
        time.sleep(5)

if __name__ == "__main__":
    start_http_server(8000)
    print("Metrics available at http://localhost:8000/metrics")
    simulate_traffic()

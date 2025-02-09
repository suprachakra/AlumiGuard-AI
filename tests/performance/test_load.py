from locust import HttpUser, task, between

class LoadTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def predict_task(self):
        with open("data/raw/sample_01.jpg","rb") as img:
            self.client.post("/predict", files={"image": img})

from locust import HttpUser, task

class LoadTest(HttpUser):
    @task(1)
    def predict(self):
        self.client.post("/predict", files={"image": open("data/raw/sample_01.jpg", "rb")})

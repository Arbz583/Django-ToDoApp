from locust import HttpUser, task

class QuickstartUser(HttpUser):


    def on_start(self):
        response=self.client.post("/accounts/api/v1/jwt/create/", data={
            "username":"ali",
            "password":"123"
        }).json()
        self.client.headers={"Authorization": "Bearer %s" % (responce.get('access',None),)}

    @task
    def task_list(self):
        self.client.get("/api/v1/tasks")
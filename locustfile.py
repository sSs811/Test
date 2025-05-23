from locust import HttpUser, task, between

class OpenBMCUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.auth = ('root', '0penBmc')  

    @task(1)
    def get_system_info(self):
        self.client.get("/redfish/v1/Systems/system", auth=self.auth, verify=False)

    @task(1)
    def get_power_state(self):
        self.client.get("/redfish/v1/Systems/system", auth=self.auth, verify=False)

class PublicAPIUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def get_posts(self):
        self.client.get("https://jsonplaceholder.typicode.com/posts")

    @task(1)
    def get_weather(self):
        self.client.get("https://wttr.in/Novosibirsk?format=j1")

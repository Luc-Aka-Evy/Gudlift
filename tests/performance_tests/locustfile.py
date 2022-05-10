from locust import HttpUser, task

class ProjectPerfTest(HttpUser):

    @task(6)
    def index(self):
        self.client.get("/")

    @task(6)
    def points_display(self):
        self.client.get("/pointsDisplay")

    @task(6)
    def login(self):
        email = "john@simplylift.co"
        self.client.post("/showSummary", data={"email": email})

    @task(6)
    def booking_place(self):
        club = "Simply Lift"
        competition = "Fall Classic"
        email = 'john@simplylift.co'
        self.client.post('/showSummary', data={'email': email})
        self.client.post('/purchasePlaces', data={'competition': competition, 'club': club, 'places': 5})

    @task(6)
    def get_booking_page(self):
        club = "Simply Lift"
        competition = "Fall Classic"
        email = 'john@simplylift.co'
        self.client.post('/showSummary', data={'email': email})
        self.client.get('/book/{}/{}'.format(competition, club))

    @task(6)
    def logout(self):
        email = 'kate@shelifts.co.uk'
        self.client.post('/showSummary', data={'email': email})
        self.client.get('/logout')
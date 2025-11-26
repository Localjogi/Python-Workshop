class Application:
    def __init__(self, application_name, category, company, app_size, no_of_user, ratings):
        self.application_name = application_name
        self.category = category
        self.company = company
        self.app_size = app_size
        self.no_of_user = no_of_user
        self.ratings = ratings

    def signup(self):
        print(f"Thank you for signing up for {self.application_name}")

    def login(self):
        print(f"Thank you for logging in to {self.application_name}")

    def logout(self):
        print("Thank you for using the application")

    def info(self):
        print(f"App Name: {self.application_name}, Category: {self.category} Company: {self.company}, Size: {self.app_size} MB, Users: {self.no_of_user}, Ratings: {self.ratings}")

app1 = Application("Instagram", "Social Media", "Meta", 42.47, 1000, 4.4)
app2 = Application("Facebook", "Social Media", "Meta", 10.47, 1000, 4.4)
app3 = Application("YouTube", "Social Media", "Google", 34.47, 1000, 4.4)
app1.info()
app2.info()
app3.info()



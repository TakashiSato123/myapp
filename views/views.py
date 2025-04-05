from app_instance import app

@app.route('/')
def home():
    return "Welcome to the Home Page!"
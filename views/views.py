from test_app import app

@app.route('/')
def home():
    return "Welcome to the Home Page!"
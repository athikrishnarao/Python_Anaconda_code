# Scenario 2: For Route

from flask import Flask

# Create object
app = Flask(__name__)
print(app)

@app.route('/')  # Link the Business logic to Presentation layer
def login_page():
    return "Hellow Everyone, We are developing API using Flask"

@app.route('/home')
def home_page():
    return "Im Homepage"

# Run the Server
if __name__ == "__main__":
    app.run(port=5001)  # Non Debug mode
    #app.run(debug=True)  # Debug mode

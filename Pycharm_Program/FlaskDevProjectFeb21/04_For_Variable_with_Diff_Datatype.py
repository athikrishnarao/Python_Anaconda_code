# Scenario 3: For variable

from flask import Flask

# Create object
app = Flask(__name__)
print(app)

@app.route('/')  # Link the Business logic to Presentation layer
def login_page():
    return "Hellow Everyone, We are developing API using Flask"

@app.route('/<name>')         # <string:name>, <int:name>, <path:name>   but default is string without given string keyword
def home_page(name):
    return f"{name} in Homepage"

# Run the Server
if __name__ == "__main__":
    app.run(port=5001)  # Non Debug mode
    #app.run(debug=True)  # Debug mode

# Scenario 1: FOr installaion and starts the server
# pip install flask

from flask import Flask

# Create object
app = Flask(__name__)

# Run the Server
if __name__ == "__main__":
    app.run()  # Non Debug mode
    #app.run(debug=True)  # Debug mode

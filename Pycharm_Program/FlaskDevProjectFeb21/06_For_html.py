# Scenario 3: For HTML

from flask import Flask

# Create object
app = Flask(__name__)
print(app)

@app.route('/')  # Link the Business logic to Presentation layer
def login_page():
    return '''
    <html>
    <head></head>
    <body>
    <input placeholder ="UserName">
    <input placeholder ="Password">
    <input type=submit>
    <a href="/registartion">Registarion</a>
    </body>
    </html>
    '''

#@app.route('/<name>') # dynamic variable given from user
def home_page(name):
    return f"{name} in Homepage"

@app.route('/registartion')
def registration():
    return "Registration - SignUp"

# Run the Server
if __name__ == "__main__":
    app.run(port=5001)  # Non Debug mode
    #app.run(debug=True)  # Debug mode
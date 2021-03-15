# Scenario 7: For HTML Templates

from flask import Flask,render_template

# Create object
app = Flask(__name__)
print(app)

@app.route('/', methods=['GET','POST'])  # Link the Business logic to Presentation layer
def login_page():
    return render_template('loginpage.html')

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
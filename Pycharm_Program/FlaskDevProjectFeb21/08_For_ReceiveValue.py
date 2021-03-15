# Scenario 7: For HTML Templates

from flask import Flask,render_template,request

# Create object
app = Flask(__name__)
print(app)

@app.route('/', methods=['GET','POST'])  # Link the Business logic to Presentation layer
def login_page():
    if request.method == "POST":
        uName = request.form.get('USERNAME')
        pwd = request.form.get('PASSWORD')
        print(uName,pwd)
        # Fetch the data from database
        if uName == "admin" and pwd == "password":
            return render_template('homepage.html')
        else:
            return render_template('loginpage.html')
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
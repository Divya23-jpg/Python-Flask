from flask import Flask,render_template , request

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit",methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")
    
    #? For Only 1 User 
    """if username=="Divya" and password=="123":
        return render_template("welcome.html",name=username)"""
   
    # ? For Many valid User 
    valid_users={
        "admin":"123",
        "Divya": "123",
        "Rohan": "0795"
    }
    if username in valid_users and password==valid_users[username]:
        return render_template("welcome.html",name=username)
    else:
        return "Invalid credentials"
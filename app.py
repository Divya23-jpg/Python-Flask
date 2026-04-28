from flask import Flask , request

app=Flask(__name__) #It tells to flask ,it is main file


# ?route always be unique , readable and each route will be strickly return something
#it is route decorator .whenever user visit this then execute to below code
@app.route("/")  

def home():
    return "Hello User This is our first Flask app"

"""OUTPUT: http://127.0.0.1:5000:
http: Protocol
127.0.0.1: Ip Addres
5000: Port Number
 """

# This is a another page :about
@app.route("/about") 
def about():
    return "This is about page" 


# This is a another page :contact
@app.route("/contact") 
def contact():
    return "This is a contact Page"


# ?GET: Used for only reading and if we will it puts data to URL
# ?POST: Load or send .it keeps data in the req body
@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method =="POST":
        return "You send the Data of the Fort!!"
    else:
        return "You are only Viewing Form"



"""
We are creating feedback form where user give feedback and we redirect to another page 
it will show thanks with their username


"""

from flask import Flask ,render_template,request

app=Flask(__name__)

@app.route("/feedback",methods=["POST","GET"])
def feedback():
    if request.method=="POST":
        name=request.form.get("username")
        message=request.form.get("message")
        return render_template("thankyou.html",user=name,message=message)
    # else
    return render_template("feedback.html")
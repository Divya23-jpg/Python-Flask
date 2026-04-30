"""
We are creating feedback form where user give feedback and we redirect to another page 
it will show thanks with their username


"""

from flask import Flask ,render_template,request

app=Flask(__name__)

@app.route("/feedback",methods=["POST","GET"])
def feedback():
    if request.method=="POST":

        # ! For Taking Input from html
        # form.get(): return NONE if No value there
        # form["key"]: retun Error which can crash out website
        name=request.form.get("username")
        message=request.form.get("message")
        # ! render_templates moves to page which is menthion in ()
        return render_template("thankyou.html",user=name,message=message)
    
    # else
    return render_template("feedback.html")
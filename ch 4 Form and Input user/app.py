"""
We are creating feedback form where user give feedback and we redirect to another page 
it will show thanks with their username
Directly pass on browser:
     http://127.0.0.1:5000/feedback

"""

from flask import Flask ,render_template,request,redirect,url_for,flash

app=Flask(__name__)
app.secret_key="my-secret-key"


@app.route("/", methods=["GET","POST"])
def form():
    if request.method=="POST":
        name=request.form.get("name")
        if not name:
            flash("Name cannot be Empty")
            return redirect(url_for("form"))
        flash(f"Thanks {name},Your Feedback was saved")
        # redirect used for moving one page to another
        # ! Way to redirect: redirect(url_for("Route_name"))
        return redirect(url_for("thankyou",user=name))
    return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    user=request.args.get("user")
    return render_template("thankyou.html",user=user)


if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/feedback",methods=["POST","GET"])
# def feedback():
#     if request.method=="POST":

#         # ! For Taking Input from html
#         # form.get(): return NONE if No value there
#         # form["key"]: retun Error which can crash out website
      
#         name = request.form.get("username")
#         message = request.form.get("message")
#         # ! render_templates moves to page which is menthion in ()
#         return render_template("thankyou.html",user=name,message=message)
    
#     # else
#     return render_template("feedback.html")
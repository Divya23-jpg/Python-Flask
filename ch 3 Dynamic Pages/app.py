from flask import Flask , render_template

app=Flask(__name__)

# ? Student_profile
# @app.route("/")
# def student_profile():
#     return render_template(
#         "profile.html",
#         name="Arun",
#         is_topper=True,
#         subjects=["Maths","Science","History"]
#         )

# ? Home Page with template extends

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")
from app import create_app
app=create_app()


# ! Execute a file when it directly execute not execute when imported
if __name__=="__main__":
    # ! start Local server
    app.run(debug=True)

# ! run.py is a app Launcher
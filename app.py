from flask import Flask

app=Flask(__name__)
@app.route("/")

def first_flask():
    return "This is my first flask program"

@app.route("/Flask_2")

def second_flask():
    return "This is my second flask program"

app.run(debug=True)
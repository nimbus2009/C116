from flask import Flask,render_template

app=Flask(__name__)
@app.route("/index")

def first_webpage():
    name='Flask'
    myName='Anuj'
    return render_template("index.html",index_variable=name,my_name=myName)

app.run(debug=True)
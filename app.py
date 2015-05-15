from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request
from flask import url_for, request, session, redirect

import euler

app = Flask(__name__)

#allows user to create a username to play under. user is allowed to play under the same username multiple times. also option to play under facebook account
@app.route("/")
def euler():
        if request.method == "GET":
                return render_template("euler.html")
        else:
                points = request.form["points"]
                step = request.form["step"]
                end = request.form["end"]
                input = request.form["input"]
                return render_template("euler.html", output = euler.euler(points,step,end,input))



if __name__ == "__main__":
        app.run(debug = True)
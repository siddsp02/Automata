# !usr/bin/env python3

from flask import Flask, render_template, request, session

from forms import DFAInputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"  # Will be changed afterwards.


@app.route("/")
def main():
    return ""


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from modules import jobs
from datetime import datetime


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    dateTime = datetime.now().strftime("%d - %m - %Y, %H:%M:%S")
    data = jobs.main()
    return render_template('index.html', data = data, date_time = dateTime)


if __name__ == "__main__":
    app.run()

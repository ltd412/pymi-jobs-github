from flask import Flask, render_template, request
from modules import jobs
from datetime import datetime


app = Flask(__name__)


date_time = datetime.now().strftime("%d - %m - %Y, %H:%M:%S")


@app.route("/", methods=['GET'])
def home():
    data = jobs.main()
    return render_template('index.html', data = data, date_time = date_time)


if __name__ == "__main__":
    app.run(debug=True)

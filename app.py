from flask import Flask, render_template, request
from modules import jobs
from datetime import datetime
import sqlite3


app = Flask(__name__)


@app.route("/")
def home():
    date_time = datetime.now().strftime("%d - %m - %Y, %H:%M:%S")
    jobs.main()
    conn = sqlite3.connect('jobs.db')
    data = conn.execute('SELECT * from jobs')
    jobs_db = list(data.fetchall())
    conn.close()
    return render_template('index.html', data = jobs_db, date_time = date_time)


if __name__ == "__main__":
    app.run()

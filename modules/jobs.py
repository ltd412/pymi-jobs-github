import requests
import sqlite3


def crawl_web(url):
    result = []
    page = 1
    while True:
        param = {"page": page}
        r = requests.get(url, params= param)
        data = r.json()
        if data == []:
            break
        else:
            for line in data:
                result.append((line['title'], line['html_url']))
        page +=1
    return result


def db():
    con = sqlite3.connect('jobs.db')
    try:
        con.execute('Create table jobs ("jobs", "url")')
    except sqlite3.OperationalError:
        con.execute('Delete from jobs')
    finally:
        url = f'https://api.github.com/repos/awesome-jobs/vietnam/issues'
        try:
            data = crawl_web(url)
            for name, url in data:
                con.execute('insert into jobs values (?,?)', [name, url])
        except TypeError:
            con = sqlite3.connect('jobs.db')
        con.commit()
        con.close()


def main():
    db()
    conn = sqlite3.connect('jobs.db')
    data = conn.execute('SELECT * from jobs')
    jobs_db = list(data.fetchall())
    conn.close()
    return jobs_db


if __name__ == "__main__":
    main()
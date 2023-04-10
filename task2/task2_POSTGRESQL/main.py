from flask import Flask, render_template, request

from hh_json import parce

import os
import json

import psycopg2

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host="localhost",
                         database="mydatabase",
               user="myuser",
           password="mypassword")
    return conn


def insert_vacancy(conn, vacancy_data):
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS vacancies (id serial PRIMARY KEY,'
    							'vacancy varchar(15000) NOT NULL,' 
    							'up integer NOT NULL,' 
    							'down integer NOT NULL);'
    							)
    # преобразование словаря в строку JSON
    vacancy_json = json.dumps(vacancy_data)

    # преобразование строки JSON в словарь
    vacancy_dict = json.loads(vacancy_json)

    # получение списка ключевых слов
    keywords = vacancy_dict['keywords']
    up = vacancy_dict['up']
    down = vacancy_dict['down']						
    cur.execute('INSERT INTO vacancies (vacancy, up, down)' 
    				'VALUES (%s, %s, %s)', 
    				(keywords,up,down))

    conn.commit()

@app.get('/index')
@app.get('/')
def index():
    return render_template('index.html')

@app.route('/form/')
def form():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM vacancies')
    vaca = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('form.html', vaca=vaca)


@app.post('/result/')
def result():
    conn = get_db_connection()
    vac = request.form
    data = parce(**vac)
    dat = {**data, **vac}
    print(dat)
    insert_vacancy(conn, dat)
    conn.close()
    return render_template('about.html', res=dat)



if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, g
import sqlite3
from hh_json import parce


app = Flask(__name__)

def insert_vacancy(conn, vacancy_data):
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS vacancies (id INTEGER PRIMARY KEY, vacancy TEXT, up REAL, down REAL)')
    cursor.execute('INSERT INTO vacancies (vacancy, up, down) VALUES (?, ?, ?)', (vacancy_data['keywords'], vacancy_data['up'], vacancy_data['down']))
    conn.commit()

@app.route('/form/')
def form():
    # Подключаемся к базе данных
    conn = sqlite3.connect('vacancies.db')

    # Получаем курсор для выполнения запросов
    cursor = conn.cursor()

    # Выбираем все записи из таблицы "вакансии"
    cursor.execute("SELECT * FROM vacancies")

    # Получаем результат выборки
    rows = cursor.fetchall()

    # Закрываем соединение с базой данных
    conn.close()
    
    return render_template('form.html', rows=rows)


@app.post('/result/')
def result():
    conn = sqlite3.connect('vacancies.db')
    vac = request.form
    data = parce(**vac)
    dat = {**data, **vac}  # data | vac - в Python 3.10 можно сделать так
    print(dat)
    insert_vacancy(conn, dat)
    conn.close()
    return render_template('about.html', res=dat)

@app.get('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


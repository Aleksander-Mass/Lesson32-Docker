import os
import random
from pathlib import Path
import json

from filemanager_funcs import*

# Текущая рабочая директория
WORKDIR = Path.cwd()

def create_folder():
    try:
        folder_name = input('Введите название папки: ')
        folder_path = WORKDIR / folder_name

        success = create_dir(folder_path)
        print('Папка создана' if success else 'Папка с таким именем уже существует!')
    except:
        print('Неизвестная ошибка!')


def remove():
    try:
        name = input('Введите название файла/папки: ')
        path = WORKDIR / name

        success = del_file_or_dir(path)
        print('Удаление выполнено' if success else 'Файла/папки с таким именем не существует.')
    except:
        print('Неизвестная ошибка!')


def copy():
    try:
        name = input('Введите название файла/папки: ')
        new_name = input('Введите название новой файла/папки: ')

        path = WORKDIR / name
        new_path = WORKDIR / new_name

        success = copy_file_or_dir(path, new_path)
        print('Копирование завершено' if success else 'Файла/папки с таким именем не существует.')
    except:
        print('Неизвестная ошибка!')


def show_workdir():
    print(*(f'- {item}' for item in get_files_and_dirs(WORKDIR)), sep = '\n')


def show_workdir_folders():
    print(*(f'- {dir}' for dir in get_dirs(WORKDIR)), sep = '\n')


def show_workdir_files():
    print(*(f'- {file}' for file in get_files(WORKDIR)), sep = '\n')


def show_os_info():
    print(get_os_info())


def show_creator_info():
    print(get_creator_info())


def play_quiz():
    ###   СПИСОК ИЗВЕСТНЫХ ЛЮДЕЙ   ###
    """
    1. 10 января - Алексей Николаевич Толстой, писатель, 1883 год
    2. 15 января - Александр Грибоедов Дата рождения:  1795 года
    3. 23 января - Стендаль (Анри Мари Бейль), писатель, 1783 год
    4. 27 января - Вольфанг Амадей Моцарт, композитор, 1756 год.
    5. 29 января - Антон Павлович Чехов, писатель, 1860 год.
    6. 1 февраля - Борис Ельцин Дата рождения:  1931 года
    7. 7 февраля - Чарльз Диккенс, писатель, 1812 год.
    8. 8 февраля - Дмитрий Менделеев, химик, 1834 год.
    9. 15 февраля - Галилео Галилей, астроном, 1564 год.
    10.19 февраля - Николай Коперник, астроном, 1473 год.
    """

    months = {'01': 'января', '02': 'февраля'}

    days = {'10': 'десятое', '15': 'пятнадцатое', '23': 'двадцать третье',
            '27': 'двадцать седьмое', '29': 'двадцать девятое', '01': 'первое',
            '07': 'седьмое', '08': 'восьмое', '19': 'февраля'
            }

    spisok = ['Алексей Николаевич Толстой', 'Александр Грибоедов',
              'Стендаль', 'Вольфанг Амадей Моцарт', 'Антон Павлович Чехов',
              'Борис Ельцин', 'Чарльз Диккенс', 'Дмитрий Менделеев',
              'Галилео Галилей', 'Николай Коперник']

    while True:
        right = 0
        incorrect = 0
        viktorina = random.sample(spisok, 5)

        for element in viktorina:
            if element == 'Алексей Николаевич Толстой':
                year_birth1 = input(
                    'Введите дату рождения А.Н.Толстого: ')  # 10.01.1883
                if year_birth1 == '10.01.1883':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth1 = '10.01.1883'
                    day, month, year = year_birth1.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Александр Грибоедов':
                year_birth2 = input(
                    'Введите дату рождения А. Грибоедова: ')  # 15.01.1795
                if year_birth2 == '15.01.1795':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth2 = '15.01.1795'
                    day, month, year = year_birth2.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Стендаль':
                year_birth3 = input(
                    'Введите дату рождения Стендаля: ')  # 23.01.1783
                if year_birth3 == '23.01.1783':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth3 = '23.01.1783'
                    day, month, year = year_birth3.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Вольфанг Амадей Моцарт':
                year_birth4 = input(
                    'Введите дату рождения В.А. Моцарта: ')  # 27.01.1756
                if year_birth4 == '27.01.1756':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth4 = '27.01.1756'
                    day, month, year = year_birth4.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Антон Павлович Чехов':
                year_birth5 = input(
                    'Введите дату рождения А.П. Чехова: ')  # 29.01.1860
                if year_birth5 == '29.01.1860':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth5 = '29.01.1860'
                    day, month, year = year_birth5.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Борис Ельцин':
                year_birth6 = input(
                    'Введите дату рождения Б. Ельцина: ')  # 01.02.1931
                if year_birth6 == '01.02.1931':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth6 = '01.02.1931'
                    day, month, year = year_birth6.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Чарльз Диккенс':
                year_birth7 = input(
                    'Введите дату рождения Чарльза Диккенса: ')  # 07.02.1812

                if year_birth7 == '07.02.1812':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth7 = '07.02.1812'
                    day, month, year = year_birth7.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Дмитрий Менделеев':
                year_birth8 = input(
                    'Введите дату рождения Д. Менделеева: ')  # 08.02.1834
                if year_birth8 == '08.02.1834':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth8 = '08.02.1834'
                    day, month, year = year_birth8.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Галилео Галилей':
                year_birth9 = input(
                    'Введите дату рождения Галилео Галилея: ')  # 15.02.1564
                if year_birth9 == '15.02.1564':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth9 = '15.02.1564'
                    day, month, year = year_birth9.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

            if element == 'Николай Коперник':
                year_birth10 = input(
                    'Введите дату рождения Николая Коперника: ')  # 19.02.1473
                if year_birth10 == '19.02.1473':
                    right = right + 1
                else:
                    incorrect = incorrect + 1
                    year_birth10 = '19.02.1473'
                    day, month, year = year_birth10.split('.')
                    print('Правильный ответ: ', days[day], months[month], year,
                          'года')

        print('Количество правильных ответов =', right)
        print('Количество ошибок =', incorrect)
        print('Процент правильных ответов =', right * 100 / 5)
        print('Процент неправильных ответов =', incorrect * 100 / 5)

        play_again = input(
            'Хотите начать игру сначала (введите "да" или "нет") ?: '
        )
        while play_again.lower() not in ['нет', 'да']:
            play_again = input(
                'Не могу вас понять. Введите "да" или "нет" ?: '
            )
        if play_again == 'нет':
            return


def my_bank_account():
    bill_sum = 0
    history = []

    fpath = WORKDIR / 'bank_account.json'

    try:
        if os.path.exists(fpath):
            with open(fpath, 'r') as f:
                bank_account = json.load(f)
                bill_sum = bank_account['bill_sum']
                history = bank_account['history']
    except:
        print('Не удалось восстановить данные о счете из файла')

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет: {bill_sum}')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                cost = int(input('Введите сумму пополнения в копейках: '))
            except:
                print('Вы ввели не число')
            else:
                bill_sum += cost
        elif choice == '2':
            try:
                cost = int(input('Введите сумму покупки в копейках: '))
            except:
                print('Вы ввели не число')
            else:
                if cost > bill_sum:
                    print('Недостаточно средств')
                else:
                    bill_sum -= cost
                    name = input('Введите название покупки: ')
                    history.append((name, cost))
        elif choice == '3':
            print('У вас нет покупок.' if history == [] else history)
        elif choice == '4':
            try:
                with open(fpath, 'w') as f:
                    json.dump({
                        'bill_sum': bill_sum,
                        'history': history
                    }, f)
            except:
                print('Не удалось сохранить данные о счете в файл')
            finally:
                break
        else:
            print('Неверный пункт меню')


def change_workdir():
    global WORKDIR

    try:
        new_work_dir = input('Введите путь к новой рабочей директории: ')
        new_work_dir_path = get_new_workdir_path(WORKDIR, new_work_dir)

        if new_work_dir_path is not None:
            WORKDIR = new_work_dir_path
            print('Новая рабочая директория: ', new_work_dir_path)
        else:
            print('Ошибка. Директории не существует.')
    except:
        print('Неизвестная ошибка!')


def save_workdir():
    try:
        success = save_workdir_contents(WORKDIR)
        print('Содержимое рабочей директории сохранено в файл' if success else 'Не удалось сохранить!')
    except:
        print('Неизвестная ошибка!')


def main():
    print('Вас приветствует консольный файловый менеджер.')
    while True:
        print(
            '\nВыберите команду:\n',
            '1 - создать папку\n',
            '2 - удалить (файл/папку)\n',
            '3 - копировать (файл/папку)\n',
            '4 - просмотр содержимого рабочей директории\n',
            '5 - посмотреть только папки\n',
            '6 - посмотреть только файлы\n',
            '7 - просмотр информации об операционной системе\n',
            '8 - создатель программы\n',
            '9 - играть в викторину\n',
            '10 - мой банковский счет\n',
            '11 - смена рабочей директории\n',
            '12 - сохранить содержимое рабочей директории в файл\n',
            '0 - выход\n',
        )
        cmd = input('>: ')
        if cmd == '0':
            print('Завершение работы.')
            break
        elif cmd == '1':
            create_folder()
        elif cmd == '2':
            remove()
        elif cmd == '3':
            copy()
        elif cmd == '4':
            show_workdir()
        elif cmd == '5':
            show_workdir_folders()
        elif cmd == '6':
            show_workdir_files()
        elif cmd == '7':
            show_os_info()
        elif cmd == '8':
            show_creator_info()
        elif cmd == '9':
            play_quiz()
        elif cmd == '10':
            my_bank_account()
        elif cmd == '11':
            change_workdir()
        elif cmd == '12':
            save_workdir()


if __name__ == '__main__':
    main()

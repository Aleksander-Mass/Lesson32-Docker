from filemanager_funcs import*

# тестируем функцию выводящую данные об авторе программы
def test_get_creator_info():
    assert get_creator_info() == 'Александр Масс'

# тестируем функцию создания папки
def test_create_dir():
    new_folder_path = Path.cwd() / "test"
    assert create_dir(new_folder_path) == True
    assert new_folder_path.exists() == True

# тестируем функцию удаления папки
def test_remove_dir():
    folder_path = Path.cwd() / "test"
    assert del_file_or_dir(folder_path) == True

# тестируем функцию копирования папки
def test_copy_dir():
    folder_path = Path.cwd() / "test"
    copy_folder_path = Path.cwd() / "test_copy"
    assert copy_file_or_dir(folder_path, copy_folder_path) == True

# тестируем функцию сохранения содержимого рабочей директории
def test_copy_dir():
    workdir_path = Path.cwd()
    listdir_txt_path = workdir_path / 'listdir.txt'
    save_workdir_contents(workdir_path)
    assert listdir_txt_path.exists() == True
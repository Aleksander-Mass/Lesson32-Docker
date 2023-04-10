import os
import shutil
from pathlib import Path
import platform

"""
создание папки
"""
def create_dir(path: Path):
    try:
        if not path.exists():
            path.mkdir()
            return True
        else:
            return False
    except:
        return False

"""
удаление файла/папки
"""
def del_file_or_dir(path: Path):
    try:
        if path.exists():
            os.remove(path) if path.is_file() else os.rmdir(path)
            return True
        else:
            return False
    except:
        return False

"""
копирование файла/папки
"""
def copy_file_or_dir(path: Path, new_path: Path):
    try:
        if path.exists():
            shutil.copytree(path, new_path) if path.is_dir() else shutil.copy(path, new_path)
            return True
        else:
            return False
    except:
        return False

"""
получение списка файлов/папок
"""
def get_files_and_dirs(path: Path):
    try:
        return [f.name for f in path.glob('*')]
    except:
        return []

"""
получение списка файлов
"""
def get_files(path: Path):
    try:
        return [f.name for f in path.glob('*') if f.is_file()]
    except:
        return []

"""
получение списка папок
"""
def get_dirs(path: Path):
    try:
        return [f.name for f in path.glob('*') if f.is_dir()]
    except:
        return []

"""
сохранение содержимого рабочей директории
"""
def save_workdir_contents(path: Path):
    try:
        files = get_files(path)
        dirs = get_dirs(path)

        with open(path / 'listdir.txt', 'w') as f:
            if len(files) > 0:
                files_str = ', '.join(files)
                f.write(f'files: {files_str}\n')
            if len(dirs) > 0:
                dirs_str = ', '.join(dirs)
                f.write(f'dirs: {dirs_str}')
        return True
    except:
        return False

"""
получение новой рабочей директории
"""
def get_new_workdir_path(current_path: Path, new_work_dir: str):
    try:
        new_work_dir_path = Path(new_work_dir) if Path(new_work_dir).is_absolute() else current_path / new_work_dir
        return new_work_dir_path if new_work_dir_path.exists() else None
    except:
        return None

"""
получение информации об OS
"""
def get_os_info():
    return platform.platform()

"""
получение информации об авторе
"""
def get_creator_info():
    return 'Александр Масс'
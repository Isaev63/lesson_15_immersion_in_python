import os
import argparse
import logging
from collections import namedtuple

# Настройка логирования
log_format = '[%(asctime)s] %(levelname)s -- %(message)s'
logging.basicConfig(filename='directory_contents.log', level=logging.INFO, format=log_format, encoding='utf-8')

# Создаем namedtuple для хранения информации о содержимом директории
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])


def collect_directory_info(directory_path):
    directory_contents = []

    for root, dirs, files in os.walk(directory_path):
        parent_dir = os.path.basename(root)
        for name in dirs:
            directory_contents.append(FileInfo(name=name, extension='', is_dir=True, parent_dir=parent_dir))
        for name in files:
            file_name, file_extension = os.path.splitext(name)
            directory_contents.append(
                FileInfo(name=file_name, extension=file_extension, is_dir=False, parent_dir=parent_dir))

    return directory_contents


def save_directory_info(directory_contents):
    for item in directory_contents:
        logging.info(f"Name: {item.name} | Extension: {item.extension} | Is Directory: {item.is_dir} | "
                     f"Parent Directory: {item.parent_dir}")


def main():
    parser = argparse.ArgumentParser(description="Собрать информацию о содержимом каталога.")
    parser.add_argument('directory_path', type=str, help="Путь к каталогу")
    args = parser.parse_args()

    if not os.path.isdir(args.directory_path):
        print("Указанный путь не является каталогом или не существует.")
        return

    directory_contents = collect_directory_info(args.directory_path)
    save_directory_info(directory_contents)
    print(f"Информация о содержимом каталога' {args.directory_path}' был сохранен в 'directory_contents.log'.")


if __name__ == "__main__":
    main()

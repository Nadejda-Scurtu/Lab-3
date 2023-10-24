import os
import csv

# Путь к корневой директории с данными
root_data_dir = 'C:\\Users\\User\\Desktop\\PythonForLab\\PD\\Lab2\\dataset'

# Относительный путь к корневой директории относительно проекта
project_path = 'C:\\Users\\User\\Desktop\\PythonForLab\\PD\\Lab3'

# Создание или открытие CSV-файла для записи аннотаций
with open("annotation.csv", "w", newline='') as annotation_file:
    annotation_writer = csv.writer(annotation_file)
    annotation_writer.writerow(['C:\\Users\\User\\Desktop\\PythonForLab\\PD\\Lab2\\dataset', '..\\PD\\Lab2\\dataset', 'class'])

    # Пройти по всем файлам и директориям в корневой директории
    for root, dirs, files in os.walk(root_data_dir):
        for filename in files:
            # Получить абсолютный путь к файлу
            absolute_path = os.path.join(root, filename)
            # Получить относительный путь относительно корневой директории
            relative_path = os.path.relpath(absolute_path, project_path)
            # Получить класс из имени директории, в которой находится файл
            class_label = os.path.basename(root)

            # Записать информацию в файл-аннотации
            annotation_writer.writerow([absolute_path, relative_path, class_label])

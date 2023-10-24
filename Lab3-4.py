import os
import random

def get_next_instance(class_label, dataset_path):
    class_files = [f for f in os.listdir(dataset_path) if f.startswith(class_label)]
    if class_files:
        random.shuffle(class_files)
        return os.path.join(dataset_path, class_files.pop())
    else:
        return None


# Пример использования функции
next_instance = get_next_instance('cat', "C:\\Users\\User\\Desktop\\PythonForLab\\PD\\Lab3\\dataset-copy")
print(f'Следующий экземпляр класса cat: {next_instance}')

from Levenshtein import distance
import os


dir1 = input('Введите первую директорию: ')
dir2 = input('Введите вторую директорию: ')
needed_severity = float(input('Введите нужную точность от 0 до 1: '))
precision = 2 ** (-20)

dir1_files = os.listdir(dir1)
dir2_files = os.listdir(dir2)

unfound_files_dir1 = {*dir1_files}
unfound_files_dir2 = {*dir2_files}

for dir1_file in dir1_files:
    with open(f'{dir1}/{dir1_file}', 'r') as f:
        s1 = f.read()
    for dir2_file in dir2_files:
        with open(f'{dir2}/{dir2_file}', 'r') as f:
            s2 = f.read()

        # длины сильно отличаются -> не подходит
        if (max(len(s2), len(s1)) - min(len(s2), len(s1))) / max(len(s2), len(s1)) \
            < needed_severity + precision:
            continue

        percentage = abs(max(len(s1), len(s2)) - distance(s1, s2)) / max(len(s1), len(s2))

        if abs(percentage - 1) < precision:
            print(f'{dir1}/{dir1_file} - {dir2}/{dir2_file}')
            unfound_files_dir1.remove(dir1_file)
            unfound_files_dir2.remove(dir2_file)

        elif percentage > needed_severity - precision:
            print(f'{dir1}/{dir1_file} - {dir2}/{dir2_file} - {percentage}')
            unfound_files_dir1.remove(dir1_file)
            unfound_files_dir2.remove(dir2_file)
        
print(f'Файлы {dir1}, которые не найдены в {dir2}: {unfound_files_dir1}' if len(unfound_files_dir1) > 0 else "")
print(f'Файлы {dir2}, которые не найдены в {dir1}: {unfound_files_dir2}' if len(unfound_files_dir2) > 0 else "")

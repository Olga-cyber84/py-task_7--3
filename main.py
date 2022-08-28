import os


def union_files(files, final_file_name):
    lines_counter = []
    texts = []
    for file_name in files:
        file_value = {}
        with open(file_name, encoding='utf-8') as file:
            counter = 0
            file_text = ''
            for line in file:
                counter += 1
                file_text += line
            file_value[file.name] = file_text
            lines_counter.append(counter)
            texts.append(file_value)
    files_info = zip(lines_counter, texts)
    files_info_dict = dict(files_info)
    files_info_sort = sorted(files_info_dict.items())

    for item in files_info_sort:
        with open(final_file_name, 'a', encoding='utf-8') as final_file:
            final_file.write(str(list(item[1].keys())[0]) + '\n')
            final_file.write(str(item[0]) + '\n')
            final_file.write(str(list(item[1].values())[0]) + '\n')


files = ['1.txt', '2.txt', '3.txt']
final_file_name = 'final_file.txt'
union_files(files, final_file_name)

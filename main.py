import sys
from core import *

save_info('Старт')

command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        crea_file(name)
elif command == 'create_folder':
    name = sys.argv[2]
    creat_folder(name)
elif command == 'delete':
    name =sys.argv[2]
    delete_file(name)
elif command == 'copy':
    name = sys.argv[2]
    new_name = sys.argv[3]
    copy_file(name, new_name)
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файлов')
    print('create_folder - создание папки')
    print('delete - удаление файлов или папки')
    print('copy - копирование файлов или папки')

save_info('Конец')
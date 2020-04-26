# функция для создания файла
import os

def crea_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

def creat_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая пака уже есть')

# def get_list():
#     print(os.listdir())


if __name__ == '__main __':
    creat_folder('new_f')
    print('jsahgd')
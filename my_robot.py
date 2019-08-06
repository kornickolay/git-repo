# импортируем библиотеки, модули
import os, psutil, sys, shutil
# функция для второго пункта меню - выводит максимум системной информации

def sys_info():
    print("Вот что мы знаем о системе:")
    print('Количество процессоров:', psutil.cpu_count())
    print('Платформа:', sys.platform)
    print('Кодировка файловой системы:', sys.getfilesystemencoding())
    print('Текущая папка:', os.getcwd())
    print('Текущий пользователь:', os.getlogin())

# функция, дублирующая файл, подающийся на входе
def duplicate_file(filename):
    if os.path.isfile(filename):
        new_filename = filename + '.dupl'
        shutil.copy(filename, new_filename)
        if os.path.isfile(new_filename):
            print('Файл был успешно создан!')
        else:
            print ('Что-то пошло не так! :(')

# функция удаляющая все файлы дубликатов в папке, подающейся на входе
def del_dupl (dir_name):
    count = 0
    for i in os.listdir(dir_name):
        fullname = os.path.join(dir_name, i)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
        if not os.path.exists(fullname):
            count += 1
            print ('Файл', fullname, 'был успешно удалён!')
    return count

# Будем выполнять запрос до тех пор, пока пользователь не нажмет n или N

def main():
    choice = ''
    while (choice.lower() != 'n'):
        print('Добро пожаловать в мир Python')
        print('Продолжим? (y/n)')
        choice = input()
        if choice.lower() != 'y':
            print('Для выхода должна быть нажата клавиша N')
        else:
            print('Выберите пункт меню:')
            print('  [1]- Вывести список файлов')
            print('  [2]- Вывести информацию о системе')
            print('  [3]- Вывести список процессов')
            print('  [4]- Продублировать файлы в текущей папке')
            print('  [5]- Продублировать указанный файл')
            print('  [6]- Удалить дубликаты файлов')
            print('----------------------------------------------------------------')
            do = int(input())
            if do == 1:
                for i in os.listdir():
                    print(i)
            elif do == 2:
                sys_info()
            elif do == 3:
                for i in psutil.pids():
                    print(i)
            elif do == 4:
                for i in os.listdir():
                    duplicate_file(i)
                print('Дублирование завершено.')
            elif do == 5:
                print('Укажите имя файла:')
                duplicate_file(input())
            elif do == 6:
                dirname = input('Укажите директорию, откуда будут удалены файлы дубликатов:')
                count = del_dupl(dirname)
                print('Было удалено', count, 'файлов')

            print('----------------------------------------------------------------')
    # --Конец while
if __name__ == '__main__':
    main()
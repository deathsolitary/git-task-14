import os
import sys
import operator
print("Данный скрипт покажет содержимое указанного каталога, отсортированное по уменьшению занимаемого размера")
print("Выберите действие:")
print("1 - текущий каталог")
print("2 - указать каталог")
num = int(input())
if num == 1:
    path = os.getcwd()
    print("Выбран текущий католог:", path)
elif num == 2:
    path = os.path.abspath(input("Введите путь до каталога: "))
    if os.path.isdir(path):
        print("Выбран католог:", path)
    else:
        print("Указанный каталог не существует")
else:
    sys.exit("Вы указали отсутствующий вариант, операция прервана")
def get_size(bts, ending='B'):
        for item in ["", "K", "M", "G", "T", "P"]:
            if bts < 1024:
                return f"{bts:.2f} {item}{ending}"
            bts /= 1024
size_dir = 0
size_dir1 = 0
size_file = 0
size_file1 = 0
dir_sort = []
for dirpath, dirnames, filenames in os.walk(path):
    if dirpath[len(path):].count(os.sep) < 1:
        for dirname in dirnames:
            for ele in os.scandir(os.path.join(dirpath,dirname)):
                size_dir += os.stat(ele).st_size
                size_dir1 = get_size(size_dir)
            dir2_sort = ["Каталог:", os.path.join(dirpath, dirname), "размер:", size_dir, ' или ', size_dir1]
            dir_sort.append(dir2_sort)
        for filename in filenames:
            size_file = os.path.getsize(os.path.join(dirpath, filename))
            size_file1 = get_size(os.path.getsize(os.path.join(dirpath, filename)))
            dir2_sort = ["Файл:", os.path.join(dirpath, filename), "размер:", size_file, ' или ', size_file1]
            dir_sort.append(dir2_sort)
print("Отсортированный список по уменьшению:")
def custom_key(s1):
    return s1[3]
dir_sort.sort(key=custom_key, reverse=True)
chunk = 10
pos = 0
for i in [dir_sort[j:j+chunk] for j in range(0, len(dir_sort), chunk)]:
    [print(*x) for x in i][0]
    pos += 10
    if pos>=len(dir_sort):
        print("Конец списка")
        break
    a = input("Вывести еще 10 строк? y - да, n - нет: ")
    if a != 'y':
        print("Отмена операции")
        break


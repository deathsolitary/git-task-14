#!/bin/bash
echo "Данный скрипт покажет содержимое указанного каталога, отсортированное по уменьшению занимаемого размера"
echo "Выберите действие:"
echo "1 - текущий каталог"
echo "2 - указать каталог"
read num
if [[ $num = "1" ]]; then 
	dir=$(pwd)
	echo "Выбран текущий католог: $dir"
elif [[ $num = "2" ]]; then
	echo "Введите путь до каталога"
	read dir
	if [ -d $dir ]; then
		echo "Выбран каталог: $dir"
	else
		echo "Указанный каталог не существует"
	fi
else
	echo "Вы указали отсутствующий вариант"
fi
#IFS=$'\n'
dir_sort=$(for item in $(du --max-depth=1 "$dir" -ah | sort -hr)
do
	if [ -d "$item" ]; then
		echo "Каталог $item  размер: $(du --max-depth=0 "$item" -h | awk '{print $1}')"
        elif [ -f "$item" ]; then
		echo "Файл $item  размер: $(du --max-depth=0 "$item" -h | awk '{print $1}')"
        fi
done )
IFS=$'\n'
echo "Показ содержимого выполняется по 10 строк"
echo "Чтобы показать следующие 10 строк, нажмите "Пробел""
echo "Чтобы прервать операцию, нажмите "q""
echo " "
echo "$dir_sort" | more -10



from pathlib import Path
file_src = Path("cats.txt")


def get_cats_info(file_src):
    try:
        with open( file_src, 'r') as file:
        lines = file.readlines()
        a=[]
        for line in lines:
        id, name, age = line.strip().split(',')
        a.append({"name":name,"age":age,"id":id})
    except OSError as err:  print('Помилка доступу до файлу')
return a
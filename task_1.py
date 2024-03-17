from pathlib import Path
file_src = Path("test.txt")

def total_salary(file_src):
   # try:
     with open(file_src, 'r') as file:
     lines = file.readlines()
    
     total = 0 #Total sum
     counter = 0

     for line in lines:
     _, amount = line.strip().split(',')
     total += int(amount)
     counter += 1

     sr_zp = total / counter
     result = (total, sr_zp)
     return result
   # except OSError as err:  print('Помилка доступу до файлу')

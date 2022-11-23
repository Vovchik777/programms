import os
import time

spisok=[]
for adress, dirs, files in os.walk(r'C:\Users\Sasha\Desktop\для примера'):
    for file in files:
        full=os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400 and '.txt' in full :
            spisok.append(full)
print(spisok)
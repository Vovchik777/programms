import os
import time

spisok=[]
for files in os.walk(r'B:\_Vova'):   #'''(r'C:\Users\Sasha\Desktop\123'): for adress, dirs, files in os.walk(r'B:\_Vova\'):'''
    print(files)
    # for file in files:
    #     full=os.path.join(file)
    #     # if time.time() - os.path.getctime(full) < 86400 and '.txt' in full :
    #     spisok.append(full)
print(spisok)
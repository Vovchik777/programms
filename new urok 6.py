# import os
# list_paths=[]
# for adress,papka,file in os.walk('C:\\'):
# for i in file:
# full_path=os.path.join(adress, i)
# list_paths.append(full_path)


r = open('text2.txt','w',encoding='utf-16')
r.write('stroka текста')



r.close()
h=open('text2.txt' ,encoding='utf-16')
print(h.read())

h.close()
# import threading
# import os

# def read_files(fileName):

#     with open(f'files/{fileName}', 'r') as file:
#         list_lines = file.readlines()

#         for line in list_lines:
#             print(line)


# fileNames = os.listdir('files')

# for file in fileNames:
#     t1 = threading.Thread(target=read_files, args=[file])    
#     t1.start()


lista = [0,1,2,3,4,5]

print(lista)

print(lista.pop(-1))

print (lista)

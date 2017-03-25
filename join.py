import os, sys

def join(file_name):
    output = open('./output/' + file_name + '.jpg', 'wb')
    pic = open('picture.jpg', 'rb')
    ori_file = open('./upload/' + file_name, 'rb')
    output.write(pic.read())
    output.write(ori_file.read())
    output.close()

files = os.listdir('./upload/')
file_names = []
for f in files:
    file_names.append(f)
for f in file_names:
    join(f)

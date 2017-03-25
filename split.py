import os, sys

def split(file_name):
    output = open('./split/' + file_name[:-4], 'wb')
    pic = open('picture.jpg', 'rb')
    pic_b = pic.read()
    ori_file = open('./output/' + file_name, 'rb')

    pic_size = len(pic_b)
    res = ori_file.read(pic_size)
    res = ori_file.read()

    output.write(res)
    output.close()
    pic.close()

files = os.listdir('./output/')
file_names = []
for f in files:
    file_names.append(f)
for f in file_names:
    split(f)

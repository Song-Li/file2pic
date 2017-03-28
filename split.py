import os, sys

def split(path, file_name):
    output = open(path + '/' + file_name[:-4] + '.part', 'wb')
    pic = open('picture.jpg', 'rb')
    pic_b = pic.read()
    ori_file = open(path + '/' + file_name, 'rb')

    pic_size = len(pic_b)
    res = ori_file.read(pic_size)
    res = ori_file.read()

    output.write(res)
    output.close()
    pic.close()
    output.close()
    return 

def join(path, dir_name):
    #os.remove(path + '/' + file_name)
    append = 'song'
    old_name = path + '/' + dir_name
    new_name = path + '/' + dir_name + append
    os.rename(old_name, new_name)
    command = 'cat ' + new_name + '/*.part > ' + old_name
    os.system(command)
    print command

ori_file_dir = raw_input("File dir: ")

for root, subdirs, files in os.walk(ori_file_dir):
    for f in files:
        split(root, f)

for root, subdirs, files in os.walk(ori_file_dir):
    for d in subdirs:
        join(root, d)


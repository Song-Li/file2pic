import os, sys

def split(path, file_name, output_path):
    # make a dir with the name of the file
    os.mkdir (output_path + '/' + file_name)

    # split the file to small pieces
    command = 'split --bytes=10M ' + path + '/' + file_name + ' ' + output_path + '/' + file_name + '/'
    os.system (command)

def join(path, file_name):
    output = open(path + '/' + file_name + '.jpg', 'wb')
    pic = open('picture.jpg', 'rb')
    ori_file = open(path + '/' + file_name, 'rb')
    output.write(pic.read())
    output.write(ori_file.read())
    ori_file.close()
    os.remove(path + '/' + file_name)
    output.close()


ori_file_dir = raw_input("File dir: ")
save_file_dir = raw_input("Output dir: ")


# split big files
for root, subdirs, files in os.walk(ori_file_dir):
    for f in files:
        split(root, f, save_file_dir)

# change to pic
for root, subdirs, files in os.walk(save_file_dir):
    for f in files:
        join(root, f)

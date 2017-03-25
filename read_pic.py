from PIL import Image
import os,sys

def read_file(ori_file, save_file):
    img = Image.open(ori_file)
    data = img.tobytes()

    # get the length of file
    str_len = ""
    for i in range(4):
        str_len += data[i]

    hex_len = str_len.encode('hex_codec')
    int_len = int(hex_len, 16)

    file_data = data[4:4 + int_len]
    out = open(save_file, 'wb')
    out.write(file_data)

ori_file_dir = raw_input("File dir: ")
save_file_dir = raw_input("Output dir: ")

files = os.listdir(ori_file_dir)
file_names = []

for f in files:
    file_names.append(f)

for f in file_names:
    read_file(ori_file_dir + '/' + f, save_file_dir + '/' + f[:-4])

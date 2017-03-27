from PIL import Image
import os, sys
import math


# currently we use gray pictures to make it easier
def gen_pic(ori_file, save_file):
    pic = open(ori_file, 'rb')
    bi = pic.read()

    # get the length of bi
    bi_len = len(bi)

    # convert to hex str
    hex_len = "%0*x" % (8, bi_len)

    # convert hex to str
    str_len = ""
    for i in range(0, 8, 2):
        cur = int(hex_len[i:i + 2], 16)
        str_len += chr(cur)

    bi = str_len + bi

    width = int(math.sqrt(bi_len))
    # add something to the end
    end_str = ""
    for i in range(bi_len):
        end_str += 'a'

    bi = bi + end_str


    img = Image.frombytes('L', (width, bi_len / width + 1), bi)
    img.save(save_file)

ori_file_dir = raw_input("File dir: ")
save_file_dir = raw_input ("Output dir: ")
files = os.listdir(ori_file_dir)
file_names = []
for f in files:
    file_names.append(f)

num_files = len(file_names)
num_finished = 0
for f in file_names:
    num_finished += 1
    gen_pic(ori_file_dir + '/' + f, save_file_dir + '/' + f + '.png')
    print str(num_finished) + " out of " + str(num_files) + " finished." 



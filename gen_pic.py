from PIL import Image


pic = open('firefox.exe', 'rb')
bi = pic.read()

# get the length of bi
bi_len = len(bi)

# convert to hex str
hex_len = "%0*x" % (8, bi_len)
print hex_len

# convert hex to str
str_len = ""
for i in range(0, 8, 2):
    cur = int(hex_len[i:i + 2], 16)
    str_len += chr(cur)

bi = str_len + bi

# add something to the end
end_str = ""
for i in range(2048):
    end_str += 'a'

bi = bi + end_str

i = 0
for b in bi:
    i += 1
    if i > 20:
        break
    print b.encode('hex_codec')

img = Image.frombytes('L', (2048, bi_len / 2048 + 1), bi)
img.save('result.png')


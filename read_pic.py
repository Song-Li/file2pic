from PIL import Image
img = Image.open('result.png')
data = img.tobytes()

# get the length of file
str_len = ""
for i in range(4):
    str_len += data[i]

hex_len = str_len.encode('hex_codec')
int_len = int(hex_len, 16)

file_data = data[4:4 + int_len]
out = open('back.exe', 'wb')
out.write(file_data)

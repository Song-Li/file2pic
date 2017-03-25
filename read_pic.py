from PIL import Image
img = Image.open('result.png')
data = img.tobytes()

out = open('back.exe', 'wb')
out.write(data)

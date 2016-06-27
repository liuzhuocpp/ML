# from numpy import *

# # print zeros((10, 3), int8)
# a = [0, 1, 2]
# print  tile(a, (2, 2))



from PIL import Image
im = Image.open("abc.jpg")
# im.show()
res = im.resize((100, 100))
res.show()

# im.rotate(45).show()
print res.size
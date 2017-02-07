from __future__ import division
from PIL import Image

im = Image.open("../images/vertical_blue.jpg")
#im = im.resize((300, 300))
im.show()
width , height = im.size

flag = False
for x in range(1,width):
    for y in range(1,height):
        p=im.getpixel((x,y))
        if p[0] < 50 and p[1] < 50 and p[2] > 150:   # RGB for blue
            if flag:
            	#first blue already seen
            	if x < X_low :
            		X_low = x
            	if x > X_high :
            		X_high = x	
            	if y < Y_low :
            		Y_low = y
            	if y > Y_high :
            		Y_high = y	

            else:
            	flag = True
            	X_high = X_low = x	
            	Y_high = Y_low = y	

print X_low , Y_low
print X_high , Y_high  

im.crop((X_low, Y_low, X_high, Y_high)).show()  #gets bounding box for color caps

X_diff = X_high - X_low
Y_diff = Y_high - Y_low

if(X_diff > Y_diff) :
	print "line"
else :
	print "block"
            
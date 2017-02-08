from __future__ import division
from PIL import Image

#im = Image.open("../images/line_blue.jpg")
im = Image.open("../images/vertical_blue.jpg")
#im = Image.open("../images/horizontal_blue.jpg")
#im = Image.open("../images/bookmark_blue.jpg")
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

cropped_im = im.crop((X_low, Y_low, X_high, Y_high))  #gets bounding box for color caps
cropped_im.show()

'''
Algo :  find bounding box
        if width > height
            its either highlight a line or search for a word
            if width > 3*height
                search for word
            else
                hightlight a line

        else
            if height > 2*width
                highlight block
            else
                bookmark   
'''

width_cropped, height_cropped = cropped_im.size
cap_height = 0
if width_cropped > height_cropped:
    if width_cropped > 3.5*height_cropped :
        print "searching for a word/phrase"
    else :
        #could be line or boundary condition for bookmark
        #so find cap height
        for x in range(1,width_cropped):
            height = 0
            for y in range(1,height_cropped):   
                p=cropped_im.getpixel((x,y))
                if p[0] < 50 and p[1] < 50 and p[2] > 150:  #if the pixel is blue, increase height
                    height += 1
                else :
                    height = 0
            if height > cap_height :
                cap_height = height

        print cap_height , width_cropped, height_cropped
        #width is greater than 1.5 times cap height, then line else bookmark
        if width_cropped > 1.5 * cap_height :
            print "highlighting line"
        else :
            print "bookmark"                        
else :
    if height_cropped > 2*width_cropped :
        print "highlight a block"
    else : 
        print "bookmark"          


            
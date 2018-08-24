import cv2
import fncropimage
import glob, os
dirList = os.listdir("./")
# os.chdir('/home/mungking/opus/Ladgrabang/')
a = 0
for root, dirs, files in os.walk('./'):
    for dir in dirs:
        for root, dirs, files in os.walk(dir):
            for name in files:
                ff = dir + '/'+ name
                print(ff)
                if name.endswith('.jpg'):
                    # img = cv2.imread(ff)
                    # cv2.imshow('ss',img)
                    # cv2.waitKey(200)


                    b = dir + '/'+ 'New'+name
                    fncropimage.crop(ff,b)
                    os.remove(ff)
    # for name in files:
    # # for file in glob.glob("*.jpg"):
    #     print(name)
    #     a = a +1

print 'Finish'





# cv2.destroyAllWindows()
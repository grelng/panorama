""" Module docstring

This is the docstring for the main module.
"""

import cv2
import numpy
import glob

def greyscale(image):
    '''Convert an image to greyscale.                                                                                                                                                  
                                                                                                                                                                                     
    image  - a numpy array of shape (rows, columns, 3).                                                                                                                                
    output - a numpy array of shape (rows, columns) and dtype same as                                                                                                                  
    image, containing the average of image's 3 channels.                                                                                                                      
                                                                                                                                                                                     
    Please make sure the output shape has only 2 components!                                                                                                                           
    For instance, (512, 512) instead of (512, 512, 1)                                                                                                                                  
    '''
    output = None
  # Insert your code here.----------------------------------------------------                                                                                                       
    output = numpy.zeros( (image.shape[0], image.shape[1]), image.dtype )
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            output[i,j] = numpy.sum(image[i,j])/3
  #---------------------------------------------------------------------------                                                                                                       
    return output

def main():
    print "hello world"
    print cv2.__version__
    # figure out what pictures to work on
    file_list = glob.glob('./pictures/*.jpg')
    print file_list
    # read in all pictures
    images = []
    for file in file_list:
        images.append(cv2.imread(file))
    cv2.namedWindow("image")
#     for img in images:
#         cv2.imshow("image",img)
#         cv2.waitKey()
    # do feature detection on all pictures
    corners = []
    for img in images:
        img_grey = greyscale(img)
        corners.append(cv2.goodFeaturesToTrack(img_grey, 1000, 0.01, 0.01))
        for coord in corners[-1]:
            cv2.circle(img, tuple(coord[0]), 5, 255)
        cv2.imshow("image", img)
        cv2.waitKey()

    
if __name__ == "__main__":
    main()

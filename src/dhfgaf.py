import numpy as np
import cv2
text = '''
    To better understand Kadane’s Algorithm, first, we would go through a short introduction of Dynamic Programming. Then, we would look at a quite popular programming problem, the Maximum Subarray Problem. We would see how this problem can be solved using a brute force approach and then we would try to improve our approach and come up with a better algorithm, aka, Kadane’s Algorithm.
So, let’s get into it.
Dynamic Programming
Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map, etc.). So the next time the same sub-problem occurs, instead of recomputing its solution, one simply looks up the previously computed solution, thereby saving computation time.
Those who cannot remember the past are condemned to repeat it. — Dynamic Programming
Here’s a brilliant explanation on the concept of Dynamic Programming on Quora — Jonathan Paulson’s answer to How should I explain dynamic programming to a 4-year-old?
Though there’s more to dynamic programming, we would move forward to understand the Maximum Subarray Problem.
Maximum Subarray ProblemAn array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.
The maximum subarray problem is the task of finding the largest possible sum of a contiguous subarray, within a given one-dimensional array A[1…n] of numbers.An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key. The simplest type of data structure is a linear array, also called a one-dimensional array.
Arrays are among the oldest and most important data structures and are used by almost every program. They are also used to implement many other data structures, such as lists, heaps, hash tables, deques, queues, stacks, strings.
'''
length = len(text)
# length of the text
width = height = int(np.sqrt(length)) +1
# taking the square root of the length 
# and adding 1 to it 
# and assigning it height and width of
# the image that we want to create
# out of the text

def convert2image(text, length):
  # this function will convert text to image
  image1 = np.zeros(shape = (height,width), dtype = np.uint8)
  # create an empty 2D numpy array 
  # and initialized it with zeros
  i=0
  
  for r in range(height):
    for c in range(width):
      if i>=length:
        break
      image1[r][c]= int(ord(text[i])) 
      # using the ascii values of characters 
      # as pixel intensities
      i+=1
  
  return image1

a = convert2image(text, length)
cv2.imshow('frame',a)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('image1.png',a) # saving the image


def convert(img, target_type_min, target_type_max, target_type):
    imin = img.min()
    imax = img.max()

    a = (target_type_max - target_type_min) / (imax - imin)
    b = target_type_max - a * imax
    new_img = (a * img + b).astype(target_type)
    return new_img
# And then use it like this




def image2text(image_path):
  imag =  cv2.imread(image_path)
  b=imag[:,:,0]
  # extracting only the red channel since
  # all the channels are similar
  
  #print(b.dtype) this will print the data type 
  # of the numpy image array 
  h,w,c = imag.shape
  text_list=[]
  for i in range(h):
    for j in range(w):
      if int(b[i][j])==0:
        break
      text_list.append(chr(int(b[i][j])))
  return ''.join(text_list) 
  
print(image2text('image1.png')) # this should give back the "text"
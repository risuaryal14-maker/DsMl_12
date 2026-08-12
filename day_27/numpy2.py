print('first=========>')
#reshaping matrix
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_arr = arr.reshape(3, 2)

print('second=========>')#reshape give value on tuple
import numpy as np
arr=np.arange(12)
print(arr.reshape(3,4))

print('third=========>')
#flattening matrix will convert multi-dimensional array into 1D array
import numpy as np
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])
flattened_arr = arr.flatten()
print("Flattened Array:")
print(flattened_arr)

print('fourth=========>')
#raveling matrix also convert multi-dimensional array into 1D array but it returns a view of the original array
import numpy as np
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])
raveled_arr = arr.ravel()
print("Raveled Array:")
print(raveled_arr)

print('fifth=========>')
#transpose matrix
import numpy as np
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])
print("Original Array:")
print(arr)
print('shape of original:',arr.shape)
print("Transposed Array:")
print(arr.T)
print('shape of transpose:',arr.T.shape)

print('sixth=========>')
#class task 
#indexing and slicing
#arr[row_start:row_end, col_start:col_end]
import numpy as np
arr = np.array([[1, 2, 3], 
                [4, 5, 6]])
print('array 2d slicing:',arr[0:2, 2:3])  

print('seventh=========>')
arr=np.array([[10, 20, 30, 40],
              [50, 60, 70, 80],
              [90, 100, 110, 120]])
print('array 2d slicing:',arr[0:2])

print('eighth=========>')
arr=np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])
print('array 2d slicing:',arr[:3,0:2])

print('ninth=========>')
#reverse array
import numpy as np
arr=np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]])
print('reverse array:',arr[:,::-1])

print('ten=========>')
#sorting array 
import numpy as np 
arr=np.array([[3, 2, 1],
              [6, 5, 4],
                [9, 8, 7]])
print('sorting array:',np.sort(arr))

print('eleventh=========>')
#filtering array
import numpy as np
arr=np.array([[1, 2, 3, 4, 5, 6, 7]])
even_numbers=arr[arr%2==0]
print('filtering array:',even_numbers)

print('twelfth=========>')
#filter with mask
numbers=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask= numbers>5
filtered_numbers=numbers[mask]

numbers[numbers>5]=100
print(numbers)

print('thirteenth=========>')
#np.where() function, it will show the index position of the value in the array
where_result=np.where(numbers==5)
print('number:',where_result)
print('number_where:',numbers[where_result])

print('fourteenth=========>')
#conditional array selection
numbers=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result=np.where(numbers>5)
conditional_selection=np.where(numbers>5, numbers*5, numbers)
print('conditional selection:',conditional_selection)

print('fifteenth=========>')
#addition of two arrays
import numpy as np
arr1=np.array([[1, 2, 3]])
arr2=np.array([[4, 5, 6]])
print('addition of two arrays:',np.add(arr1,arr2))
print('alternative addition of two arrays:',arr1+arr2)

print('sixteenth=========>')
import numpy as np
orginal_row=np.array([[1, 2, 3],
                        [4, 5, 6]])
new_row=np.array([[7, 8, 9]])
add_row=np.vstack((orginal_row,new_row))
print('addition of row:',add_row)
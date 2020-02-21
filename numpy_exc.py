
import numpy as np

new_array = np.array([1, 22.4, 5, 35, 4, 6.7, 3, 8, 40])
print(new_array.shape)
print(new_array.ndim)
print(new_array.size)
print(new_array.dtype)

new_matrix = np.array([['a','b'],['c','d'],[3,3]])
print(new_matrix)
print(new_matrix.ndim)
print(new_matrix.shape)
print(new_matrix.size)
print(new_matrix.dtype)

print('range_array :' , np.arange(1,8))
print('random_array :' , np.random.rand(1,4))
print('2D_ array :',  np.zeros((2,2)))
print('2D_ array_rand :', np.random.rand(2,2))
print(f' a = {np.zeros((2,2)).shape}')

seven_array =np.array([7]*20)
print(type(seven_array))
print(seven_array.reshape((4,5)))

mix_matrix = np.arange(1,37).reshape((6,6))
print(mix_matrix)
print(mix_matrix[0][0])
print(mix_matrix[-2:,:])  # or print(mix_matrix[4:6,:])
print(mix_matrix[2:4,2:4])
print(mix_matrix.sum(axis=0))

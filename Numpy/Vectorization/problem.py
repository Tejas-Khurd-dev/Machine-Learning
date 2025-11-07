# Vectorization = performing operations on whole arrays.

# Broadcasting = adjusting array shapes so that vectorized operations can work.

lis1 = [1,2,3]
lis2 = [4,5,6]

result1 = [x+y for x, y in zip(lis1, lis2)]
print(result1)

result2 = [x*8 for x in lis1]
print(result2)
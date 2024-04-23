#Write a program to find the largest element in an array.

arr=[12,2,13,1,4,14,5,15,6,78,3,9,59,96,23,1,2,5]



def LargestElementInArray(arr):
    max_val=0
    for val in arr:
        if val>max_val:
            max_val=val
    return max_val

lar_ele=LargestElementInArray(arr)    

print('Largest element in array is {}'.format(lar_ele))
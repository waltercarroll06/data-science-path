# ejericcio 1 


def encontrar(target,lista):
    left = 0
    right = len(lista)-1
    while left <= right:
    
        mid = (left + right) // 2
    
        if lista[mid] == target:
            return f"encontrado {mid}"
        elif lista[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

print(encontrar(5, [1,3,5,6]))
print(encontrar(2, [1,3,5,6]))
print(encontrar(7, [1,3,5,6]))

# ejercicio 2 

class Solution(object):
    def twoSum(self, nums, target): 
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
v1 = Solution()
sum = v1.twoSum([3,3], 6)
print(sum)
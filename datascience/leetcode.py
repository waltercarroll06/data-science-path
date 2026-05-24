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


# ejericio 3
class Solution(object):
    def isPalindrome(self, x):
        try:
                if x < 0 :
                    return False
                elif str(x) == str(x)[::-1]:
                    return True
                else:
                    return False
        except ValueError:
                return False


n1 = Solution()
sol = n1.isPalindrome(121)
print(sol)
    


# ejercicio 4

class Solution(object):
    def check(self, nums):
        bajon = 0
        for n in range(len(nums)-1):
            if nums[n] <= nums[n+1]:
               continue
            else:
                bajon += 1
        if bajon == 0:
            return True
        elif bajon <= 1:
            if nums[0] >= nums[len(nums)-1]:
                return True
            else:
                return False
        else:
            return False
        
        
        

                
            
v1 = Solution()
n = v1.check([1,1,1])
print(n)

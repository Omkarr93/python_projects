# Find the pair 

# input 1,2,3,4,5


def find_pair (input:list,target:int):
    seen = []
    for num in input:
        for i in range(0,len(input)):
           if num not in seen and  num + input[i] == target :
               if  num != input[i] : 
                seen.append(num)
                seen.append(input[i])
                print(num,input[i])
                
  

# find_pair([1,2,3,4,5,6,7,8,9,10/11],6)
find_pair([4,11,12,2,3,5,4,6,8,9,7,5,7,8,4,5,1,5,6,8,20],8)
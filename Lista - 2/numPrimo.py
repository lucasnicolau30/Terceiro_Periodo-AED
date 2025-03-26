def primo(num): 
    if num < 2: 
        return False 
    else: divisores = 2 
        for i in range(divisores , num): 
            if num % i == 0: 
                return False 
        return True

num = int(input()) 
while num != 0: 
    if primo(num): 
        print("{}: primo".format(num)) 
    else: print("{}: composto".format(num)) 
    
    num = int(input())        

t = 0
p = ""


for _ in range(int(input())):
    if  p == "":
        p = str(input())
    else:
        o = str(input())
        if o != p:
            p = o
            t += 1
            


print(t+1)
  
        
    
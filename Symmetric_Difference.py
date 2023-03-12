 # Enter your code here. Read input from STDIN. Print output to STDOUT
 # Symmetric Difference
def sym(inp):
    a =[]
    b =[]
    i = 0
    for line  in inp:
        i+=1
        if i == 2:
            a = line.split(' ')
            a[-1] = a[-1][0:-1]
        if i ==4:
            b = line. split(' ')
            
    a = set(a)
    b = set(b)
   
    result1 = a.difference(b)
    result2 = b.difference(a)
    result3 = result1.union(result2)
    result4 = list(result3)
    result = [int(i) for i in result4]
    result.sort()   
    for item in result:
        print(item)
    
if __name__ == "__main__":
    import sys
    x = sys.stdin
    sym(x)


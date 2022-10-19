def draw(x,y):
    if x==0 and y==0:
        if(y+x>=n-1):
            print('#',end='')
        else:
            print('_',end='')
        return
    if x==0:
        draw(n-1,y-1)
        print()
        if(y+x>=n-1):
            print('#',end='')
        else:
            print('_',end='')
        return
    draw(x-1,y)
    if(y+x>=n-1):
        print('#',end='')
    else:
        print('_',end='')
    
n=int(input())
draw(n-1,n-1)
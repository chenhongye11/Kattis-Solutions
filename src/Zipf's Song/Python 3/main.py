print((lambda n,m: '\n'.join(x for _,_,x in sorted(((lambda a,b: (int(a)*(i+1), i, b))(*input().split()) for i in range(n)), key = lambda z: (-z[0],z[1]))[:m]))(*map(int,input().split())))
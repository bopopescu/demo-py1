from timeit import Timer

s1ttake = Timer('t=a;a=b;b=t','a=1;b=2').timeit()
print(s1ttake)

s2ttake = Timer('a,b=b,a','a=1;b=2').timeit()
print(s2ttake)
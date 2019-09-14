"""
f = open('AdventDay2-input.txt', 'r')
total = 0
dimensions = f.readlines()
for item in dimensions:
    split = item.rstrip('\n').split('x')
    l = int(split[0])
    w = int(split[1])
    h = int(split[2])
    smallest = min(l*w,w*h,h*l)
    surface_area = 2*l*w + 2*w*h + 2*h*l
    total = total + surface_area + smallest
print total
"""
    
#part 2

f = open('AdventDay2-input.txt', 'r')
total = 0
dimensions = f.readlines()
for item in dimensions:
    split = item.rstrip('\n').split('x')
    l = int(split[0])
    w = int(split[1])
    h = int(split[2])
    smallest = min(2*l+2*w,2*w+2*h,2*h+2*l)
    volume = l*w*h
    total = total + volume + smallest
print total
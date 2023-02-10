import math

class append_point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def left_idx(point):
    min = 0
    for i in range(1,len(point)):
        if point[i].x < point[min].x:
            min = i
        elif point[i].x == point[min].x:
            if point[i].y > point[min].y:
                min = i
    return min
 
def orgn(i, j, k):
    tmp = (j.y - i.y) * (k.x - j.x) - (j.x - i.x) * (k.y - j.y)
 
    if tmp == 0:
        return 0
    elif tmp > 0:
        return 1
    else:
        return 2

def in_or_out(polygon, point):
    N = len(polygon)-1    
    count = 0
    p1 = polygon[0]
    for i in range(1, N+1):
        p2 = polygon[i%N]
        if point.y > min(p1.y, p2.y) and point.y <= max(p1.y, p2.y) and point.x <= max(p1.x, p2.x) and p1.y != p2.y:
            xinters = (point.y-p1.y)*(p2.x-p1.x)/(p2.y-p1.y) + p1.x
            if(p1.x==p2.x or point.x<=xinters):
                count += 1
        p1 = p2
        
    if count % 2 == 0:
        result = 0  
    else:
        result = 1 
    return result
 
def Convex_Hull(point, n, idf):
    L = left_idx(point)
 
    hull = []

    p = L
    q = 0
    while(True):
        hull.append(p)

        q = (p + 1) % n
 
        for i in range(n):
            if(orgn(point[p],point[i], point[q]) == 2):
                q = i
        p = q
 
        if(p == L):
            break

    x = []
    y = []
    for i in hull:
        x.append(point[i].x)
        y.append(point[i].y)

    polygon = []
    for j in range(len(x)):
        polygon.append(append_point(x[j], y[j]))

    total = 0
    for i in range(len(x)):
        if i + 1 < len(x):
            total += (x[i] * y[i + 1]) - (x[i + 1] * y[i])
        else:
            total += (x[i] * y[0]) - (x[0] * y[i])

    size = abs(total)/2

    
    if idf == 1:
        f = open("정지석_output1.txt", 'w')
    if idf == 2:
        f = open("정지석_output2.txt", 'w')
    if idf == 3:
        f = open("정지석_output3.txt", 'w')

    f.write(str(size) + '\n') 
        
    for i in range(len(x)):
        f.write(str(x[i]) + ' ' + str(y[i]) + '\n') 
           
    f.close()

    f = open("point_in_polygon_input.txt", 'r')
    input_lines = f.readlines()
    f.close()
    x = [int(x.split(" ")[0]) for x in input_lines]
    y = [int(x.split(" ")[1]) for x in input_lines]

    p = []
    for j in range(len(x)):
        p.append(append_point(x[j], y[j]))

    if idf == 1:
        f = open("정지석_point_in_polygon_output1.txt", 'w')
    if idf == 2:
        f = open("정지석_point_in_polygon_output2.txt", 'w')
    if idf == 3:
        f = open("정지석_point_in_polygon_output3.txt", 'w')

    for i in range(len(p)):
        check = in_or_out(polygon, p[i])
        if check == 0:
            f.write('out\n')
        elif check == 1:
            f.write('in\n')
    f.close()
        
for i in range(1,4):
    if i == 1:
        f = open("input1.txt", 'r')
    if i == 2:
        f = open("input2.txt", 'r')
    if i == 3:
        f = open("input3.txt", 'r')

    input_lines = f.readlines()
    x = [int(x.split(" ")[0]) for x in input_lines]
    y = [int(x.split(" ")[1]) for x in input_lines]

    point = []
    for j in range(len(x)):
        point.append(append_point(x[j], y[j]))

    Convex_Hull(point, len(point), i)
    f.close()

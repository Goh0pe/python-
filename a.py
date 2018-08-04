a=[]
b=[]
for i in range(5):
    n=int(input())
    m=int(input())
    b.append(n)
    print(b)
    b.append(m)
    print(b)
    a.append(b)
    print(a)
    b.clear()
    print(b)
print(a[1])












'''#斐波那契数列计算(自己)
def fei(n):
    if n<=1:
        return n
    else:
        return(fei(n-1)+fei(n-2))


n=eval(input("请输入数字:"))
a=[]
s=0
for i in range(n+1):
    s+=fei(i)
    a.append(fei(i))
x=s//len(a)
a.append(s)
a.append(x)
v=",".join('%s' %id for id in a)
v.replace(" ","")
print(v)

#斐波那契数列计算(网上)
past = 0
now = 1
output = 1
n = eval(input())
if n == 0:
    print("0, 0, 0")
elif n == 1:
    print("0, 1, 1, 2, %d" %(2/3))
else:
    print("0, 1, ", end = '')
    s = 1
    d = 2
    while output <= n:
        print("%d, " %output, end = '')
        s = s + output
        d = d + 1
        past = now
        now = output
        output = past + now
    print("%d, %d" %(s, s/d))

#合法括号组合的生成
def bracket(left = 0, right = 0, s = '', res = []):
    if left == 0 and right == 0:
        res.append(s)
    elif left == right:
        bracket(left-1, right, s + '(', res)
    else:
        if left > 0:
            bracket(left-1, right, s + '(', res)
        bracket(left, right-1, s + ')', res)

res = []
s = ''
bracket(4, 4, s, res)
print(res)



#站队顺序输出
from operator import itemgetter
queue = [[7,0], [4,4], [7,1], [5,2], [6,1], [5,0]]

queue.sort(key = itemgetter(1))
#print(queue)
queue.sort(key = itemgetter(0), reverse = True)
#print(queue)

output = []
for item in queue:
    output.insert(item[1], item)
print(output)
'''

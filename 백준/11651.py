import sys
sys.stdin = open("11651.txt", "r")

n = int(input())
a= []

for _ in range(n):
    x, y = map(int, input().split())
    a.append([x,y])
a.sort(key=lambda x : (x[1], x[0]))

for i in a:
    print(i[0],i[1])
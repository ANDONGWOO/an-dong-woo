import sys
sys.stdin = open("9295.txt", "r")

T=int(input())

for i in range(1,T+1):
    a,b=map(int,input().split())

    print(f'Case {i}:',a+b)

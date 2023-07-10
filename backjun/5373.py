# 위 흰 아래 노 앞 빨(눈에 보이는 방향) 뒷 오렌지 왼쪽 초록 오른쪽 파랑
import sys

input = sys.stdin.readline


def solution():
    # 27조각 9면 54네모
    cube_a = [[["o","o","o",],["o","o","o",],["o","o","o",]],
    [["o","o","o",],["o","o","o",],["o","o","o",]],
    [["o","o","o",],["o","o","o",],["o","o","o",]],
    [["o","o","o",],["o","o","o",],["o","o","o",]],]

    cube_b = [[["o","o","o",],["o","o","o",],["o","o","o",]],
    [["o","o","o",],["o","o","o",],["o","o","o",]],
    [["o","o","o",],["o","o","o",],["o","o","o",]],
    [["o","o","o",],["o","o","o",],["o","o","o",]],]

    n = int(input())
    for i in range(n):
        m = int(input())
        cmd = input()
        cmds = list(input().split())
        for cmd in cmds:
            cmd 



    pass




if __name__ == "__main__":
    solution()
    
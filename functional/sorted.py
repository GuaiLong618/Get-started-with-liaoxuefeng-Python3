#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]



if __name__ == "__main__":
    print("打印初始序列：")
    print(L)

    L2 = sorted(L, key=by_name)
    print("按名字排序：")
    print(L2)

    L3 = sorted(L, key=by_name, reverse=True)
    print("翻转：")
    print(L3)

    L4 = sorted(L,key=by_score)
    print("按成绩排序：")
    print(L4)

    L.sort(key=by_name)
    print() #输出一行空行
    print(L)



import time
import numpy as np


def string_compare(P, T, i, j):
    if i == 0:
        return len(T[0:j])
    if j == 0:
        return len(P[0:i])
    zamian = string_compare(P, T, i - 1, j - 1) + int(P[i] != T[j])
    wstawien = string_compare(P, T, i, j - 1) + 1
    usuniec = string_compare(P, T, i - 1, j) + 1
    min_cost = min(zamian, wstawien, usuniec)
    return min_cost


t_start = time.perf_counter()
res1 = string_compare(" kot", " pies", 3, 4)
t_stop = time.perf_counter()
print(res1)
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


def path(P, T, parent):
    i_path = len(P) - 1
    j_path = len(T) - 1
    my_list = []
    while parent[i_path, j_path] != "X":
        sign = parent[i_path, j_path]
        my_list.append(sign)
        if sign == "M" or sign == "S":
            i_path -= 1
            j_path -= 1
        elif sign == "I":
            j_path -= 1
        else:
            i_path -= 1
    my_list.reverse()
    result = ""
    for char in my_list:
        result += char
    return result


def string_compare_PD(P, T):
    i = len(P) - 1
    j = len(T) - 1
    D = np.zeros((i+1, j+1))
    for x in range(i+1):
        D[x, 0] = x
    for x in range(j+1):
        D[0, x] = x
    parents = np.array([["X" for ij in range(j+1)] for ii in range(i+1)])
    parents[0, 1:] = "I"
    parents[1:, 0] = "D"

    for ii in range(1, i + 1):
        for ij in range(1, j + 1):
            zamian = D[ii - 1, ij - 1] + int(P[ii] != T[ij]), "S"
            wstawien = D[ii, ij - 1] + 1, "I"
            usuniec = D[ii - 1, ij] + 1, "D"
            min_cost = min(zamian, wstawien, usuniec, key=lambda tuple: tuple[0])
            if min_cost[1] == "S" and P[ii] == T[ij]:
                parents[ii, ij] = "M"
            else:
                parents[ii, ij] = min_cost[1]
            D[ii, ij] = min_cost[0]

    return D[i, j], D, parents


t_start = time.perf_counter()
res2 = string_compare_PD(' biały autobus', ' czarny autokar')
t_stop = time.perf_counter()
print(res2[0])
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

P = ' thou shalt not'
T = ' you should not'
res3 = string_compare_PD(P, T)
print(path(P, T, res3[2]))


def string_compare_PD_substring(P, T):
    i = len(P) - 1
    j = len(T) - 1
    D = np.zeros((i+1, j+1))
    for x in range(i+1):
        D[x, 0] = x
    parents = np.array([["X" for ij in range(j+1)] for ii in range(i+1)])
    parents[1:, 0] = "D"

    for ii in range(1, i + 1):
        for ij in range(1, j + 1):
            zamian = D[ii - 1, ij - 1] + int(P[ii] != T[ij]), "S"
            wstawien = D[ii, ij - 1] + 1, "I"
            usuniec = D[ii - 1, ij] + 1, "D"
            min_cost = min(zamian, wstawien, usuniec, key=lambda tuple: tuple[0])
            if min_cost[1] == "S" and P[ii] == T[ij]:
                parents[ii, ij] = "M"
            else:
                parents[ii, ij] = min_cost[1]
            D[ii, ij] = min_cost[0]
    i_goal = len(P) - 1
    j_goal = 0
    for k in range(1, len(T)):
        if D[i_goal, k] < D[i_goal, j_goal]:
            j_goal = k

    return D[i, j], D, parents, j_goal


res4 = string_compare_PD_substring(' ban', ' mokeyssbanana')
res5 = string_compare_PD_substring(' bin', ' mokeyssbanana')
print(res4[3] - 2)


def string_compare_PD_sekwencja(P, T):
    i = len(P) - 1
    j = len(T) - 1
    D = np.zeros((i+1, j+1))
    for x in range(i+1):
        D[x, 0] = x
    for x in range(j+1):
        D[0, x] = x
    parents = np.array([["X" for ij in range(j+1)] for ii in range(i+1)])
    parents[0, 1:] = "I"
    parents[1:, 0] = "D"

    for ii in range(1, i + 1):
        for ij in range(1, j + 1):
            zamian = D[ii - 1, ij - 1] + (float("inf") if P[ii] != T[ij] else 0), "S"
            wstawien = D[ii, ij - 1] + 1, "I"
            usuniec = D[ii - 1, ij] + 1, "D"
            min_cost = min(zamian, wstawien, usuniec, key=lambda tuple: tuple[0])
            if min_cost[1] == "S" and P[ii] == T[ij]:
                parents[ii, ij] = "M"
            else:
                parents[ii, ij] = min_cost[1]
            D[ii, ij] = min_cost[0]
    return D[i, j], D, parents


P = ' democrat'
T = ' republican'
res6 = string_compare_PD_sekwencja(P, T)
path_res6 = path(P, T, res6[2])
idx = len(P) - 1
idxs_in_P = []
for i in range(len(path_res6) - 1, 0, -1):
    if path_res6[i] == "D":
        idx -= 1
    elif path_res6[i] == "M":
        idxs_in_P.append(idx)
        idx -= 1

res_string = ""
for idx in idxs_in_P:
    res_string = P[idx] + res_string
print(res_string)

P = ' 123456789'
T = ' 243517698'

res7 = string_compare_PD_sekwencja(P, T)
path_res7 = path(P, T, res7[2])
idx = len(P) - 1
idxs_in_P = []
for i in range(len(path_res7) - 1, 0, -1):
    if path_res7[i] == "D":
        idx -= 1
    elif path_res7[i] == "M":
        idxs_in_P.append(idx)
        idx -= 1

res_string = ""
for idx in idxs_in_P:
    res_string = P[idx] + res_string
print(res_string)
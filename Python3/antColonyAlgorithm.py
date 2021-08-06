#!/usr/bin/env python
# coding:utf-8
# Filename: test_1.py

import numpy as np


tasknum = 100
nodenum = 7
#itemum = 5000
itemum = 10
antnum = 50
alp = 1
bet = 2
p = 0.5

tasks = np.arange(1,101)
nodes = np.array([0.7, 1.8, 1.5, 3.4, 3.9, 3.0, 4.3])

max_node = max(nodes)
greedy_ = sum(tasks / max_node)

pheromones = np.full(shape=(tasknum,nodenum),fill_value = antnum / greedy_ )

# 初始化距离矩阵
distance = np.zeros_like(pheromones)
for i in range(tasknum):
    for j in range(nodenum):
        distance[i,j] = tasks[i] / nodes[j]

def init_probability(p):
    # p 信息素矩阵， probability 概率矩阵
    probability = p
    p_sum = p.sum(axis=1)
    for i in range(len(p)):
        # 归一化
        probability[i] = p[i] / p_sum[i]

        tmp_sum = 0
        for j in range(len(p[i])):
            tmp_sum += probability[i,j] 
            probability[i,j] = tmp_sum

    return probability

def update_pheromones(pheromones,antnum,path_mat,length):
    p = 0.5
    det_m = np.zeros_like(pheromones)
    for i in range(antnum):
        det_m = det_m + path_mat[i] / length[i]

    new_pheromones = ( 1 - p ) * pheromones + det_m
    return new_pheromones

def get_probability(pheromones,d):
    alp = 1
    bet = 2
    d = 1 / d

    res = np.power(pheromones,alp) + np.power(d,bet)
    return res

def a_group_ants(antnum,pheromones):
    path_mat_all = {}
    c_length_all = {}

    for ant in range(antnum):
        # 概率矩阵
        tmp_1 = get_probability(pheromones,distance)
        # 加和概率矩阵
        probability = init_probability(tmp_1)
        path_mat = np.zeros_like(pheromones)

        for i in range(tasknum):
            n = np.random.rand()
            n_ = np.where(n < probability[i])[0][0]
            path_mat[i,n_] = 1

        t1 = path_mat * distance
        t2 = np.sum(t1,axis = 0)
        t3 = np.max(t2)

        path_mat_all[ant] = path_mat
        c_length_all[ant] = t3

    pheromones =  update_pheromones(pheromones,antnum,path_mat_all,c_length_all)
    return pheromones

if __name__ == '__main__':
    for i in range(itemum):
        pheromones = a_group_ants(antnum,pheromones)

    print("信息素矩阵",pheromones)
    
    d = np.zeros_like(pheromones)
    for i in range(len(pheromones)):
        n = int(np.where(pheromones[i] == max(pheromones[i]))[0])
        d[i,n] = 1

    use_length = np.max(np.sum(d * distance, axis=0))
    print("路径矩阵",d)
    print("最优路径长度",use_length)

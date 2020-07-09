import random

import networkx as nx
import numpy as np


class RWGraph():
    def __init__(self, nx_G, node_type=None):
        self.G = nx_G
        self.node_type = node_type

    def walk(self, walk_length, start, schema=None):
        # Simulate a random walk starting from start node.
        G = self.G

        rand = random.Random()              # 设定随机

        if schema:
            schema_items = schema.split('-')
            assert schema_items[0] == schema_items[-1]

        walk = [start]
        while len(walk) < walk_length:
            cur = walk[-1]                      # 记录最后一步的节点
            candidates = []
            for node in G[cur].keys():          # 遍历邻近节点
                if schema == None or self.node_type[node] == schema_items[len(walk) % (len(schema_items) - 1)]:
                    candidates.append(node)     # 把邻近节点添加到候选列表中
            if candidates:
                walk.append(rand.choice(candidates))    # 从候选者随机抽取
            else:
                break
        return [str(node) for node in walk]

    def simulate_walks(self, num_walks, walk_length, schema=None):
        """
        模拟游走
        :param num_walks: 游走的次数
        :param walk_length: 游走的长度
        :param schema:
        :return:
        """
        G = self.G
        walks = []
        nodes = list(G.nodes())
        # print('Walk iteration:')
        if schema is not None:
            schema_list = schema.split(',')
        for walk_iter in range(num_walks):
            random.shuffle(nodes)
            for node in nodes:
                if schema is None:
                    walks.append(self.walk(walk_length=walk_length, start=node))    # 把随机游走的路径添加
                else:
                    for schema_iter in schema_list:
                        if schema_iter.split('-')[0] == self.node_type[node]:
                            walks.append(self.walk(walk_length=walk_length, start=node, schema=schema_iter))

        return walks

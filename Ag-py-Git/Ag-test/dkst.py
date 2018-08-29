# 使用迪克斯特拉算法来寻找有向无环正权重图中的最短路径


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 创建图的散列表
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}
# 创建开销表
inf = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = inf
# 创建父节点表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
# 记录数组
processed = []
print('##############')
print(costs)
print(parents)
print(processed)
print('##############')
# 算法代码
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # print(new_cost)
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print('@@@@@@@@@@@@@@')
print(costs)
print(parents)
print(processed)
print('@@@@@@@@@@@@@@')

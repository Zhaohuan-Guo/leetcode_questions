from heapq import heappush, heappop
from typing import List

class TreeNode:
    def __init__(self, char: str, freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(freq_list: List[int]) -> TreeNode:
    # 创建叶子节点-所有的节点都是叶子
    nodes = [TreeNode(chr(i + ord('a')), freq) for i, freq in enumerate(freq_list) if freq > 0]
    # 构建优先队列-就是小根堆
    heap = []
    for node in nodes:
        heappush(heap, (node.freq, id(node), node))

    # 构建哈夫曼树
    while len(heap) > 1:
        _, _, left = heappop(heap)
        _, _, right = heappop(heap)
        new_freq = left.freq + right.freq
        new_node = TreeNode('', new_freq)
        new_node.left = left
        new_node.right = right
        heappush(heap, (new_freq, id(new_node), new_node))

    _, _, root = heappop(heap)
    return root

build_huffman_tree()
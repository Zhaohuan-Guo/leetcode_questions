from heapq import heappush, heappop
from typing import List

class TreeNode:
    def __init__(self, char: str, freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(freq_list: List[int]) -> TreeNode:
    # 创建叶子节点
    nodes = [TreeNode(chr(i + ord('a')), freq) for i, freq in enumerate(freq_list) if freq > 0]
    # 构建优先队列
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

freq_list = [5, 2, 1, 1, 2]  # 字符频率列表，对应字符'a'到'e'

root = build_huffman_tree(freq_list)

# 构建编码表
code_table = {}
def build_code_table(node, code):
    if node is None:
        return
    if node.char:
        code_table[node.char] = code
    build_code_table(node.left, code + '0')
    build_code_table(node.right, code + '1')

build_code_table(root, '')

# 打印编码结果
for char, code in code_table.items():
    print(f"{char}: {code}")

# 进行编码
encoded_string = ''.join(code_table[char] for char in "abeacadabea")
print("Encoded string:", encoded_string)

# 进行解码
decoded_string = ""
current_node = root
for bit in encoded_string:
    if bit == '0':
        current_node = current_node.left
    else:
        current_node = current_node.right
    if current_node.char:
        decoded_string += current_node.char
        current_node = root

print("Decoded string:", decoded_string)

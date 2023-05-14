import heapq

length = int(input())
freq_list = list(map(int, input().split()))
heapq.heapify(freq_list)
rs = 0

def Huaffman_tree(list):
    global rs

    while len(freq_list) > 1:
        freq1 = heapq.heappop(freq_list)
        freq2 = heapq.heappop(freq_list)
        new_freq = freq1 + freq2
        rs += new_freq
        heapq.heappush(freq_list, new_freq)


tree_root = Huaffman_tree(freq_list)

print(rs)

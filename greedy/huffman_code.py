"""module to construct haffman trees and codes"""

import heapq
from typing import Optional
from collections import namedtuple
from collections import Counter


TreeNode = namedtuple('TreeNode', ['val', 'freq', 'left', 'right'])


def build_huffman_tree(cnter: Counter)->Optional[TreeNode]:
    min_heap: list[tuple] = []

    for key, count in cnter.items():
        node = TreeNode(key, count, None, None)
        heapq.heappush(min_heap, (count, node))

    while len(min_heap) >= 2:
        cnt_lf, node_lf = heapq.heappop(min_heap)
        cnt_rt, node_rt = heapq.heappop(min_heap)

        node_p = TreeNode(f'{node_lf.val}:{node_rt.val}', cnt_lf+cnt_rt, node_lf, node_rt)
        heapq.heappush(min_heap, (cnt_lf+cnt_rt, node_p))

    _, node_root = heapq.heappop(min_heap)
    return node_root

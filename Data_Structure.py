# 자료구조

# 각 항목 구성
# 1. 각 자료구조에 대한 개념 설명
# 2. 메모리 구조
# 3. 시간 복잡도
# 4. 다른 자료구조와의 비교

# Array(배열)
# 원소를 연속된 메모리 공간에 저장한다.
# 탐색 시간복잡도: 평균 O(1), 최악 O(n)
# 삽입 삭제 시간복잡도: 최고 O(1), 평균 O(n)

arr = [10, 20, 30, 40]

# 파이썬의 list는 C++의 vector와 다르게
# 내부 원소들이 객체 자체가 아니라 객체를 가리키는 포인터들로 저장된다.
# 그래서 서로 다른 타입을 한 list에 저장할 수 있는 것이다.
# 그 덕에 배열을 알고 있다면, 인덱스로 O(1)만에 접근할 수 있다.

# 중간 삽입의 단점도 존재한다.
# 한 묶음으로 메모리에 저장되어 있기 때문에, 삽입할 공간부터 뒤에 존재하는 원소들은
# 모두 복사해서 이동시켜야 한다.
# 최악의 경우, O(n)만큼의 시간이 걸린다.

# 예상 질문 : list의 append 시간복잡도는?
# 답 : 일반적으로 O(1)의 시간을 갖지만,
#      내부 capacity가 부족하여 resize가 발생하는 경우 O(n)이 될 수 있다.

#######################################################################################

# Linked List(연결 리스트)
# 원소를 따로 떼어서 저장하지만,
# 각 노드(객체의 위치)에 다음 노드의 주소를 같이 넣어 연결되어 있다.
# (양방향 연결 리스트의 경우에는 이전 노드의 주소가 같이 저장되어 있다.)
# 탐색 시간복잡도: 평균 O(n), 최악 O(n)
# 삽입 삭제 시간복잡도: 평균 O(1), 최악 O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# 앞선 array와 다르게
# 중간 삽입, 중간 삭제 모두 O(1)의 시간만이 걸려 효율적이다.
# 그러나, 데이터가 따로 떨어져 있기 때문에 인덱스 접근이 불가능하다.
# 그래서 값 검색을 위해서는 항상 O(n)의 시간이 걸린다.

#######################################################################################

# Stack와 Queue
# Array와 Linked List의 차이는 메모리에 어떤 방식으로 데이터를 저장하냐에 가까운 반면
# Stack과 Queue는 어떤 규칙으로 데이터를 넣고 빼냐에 가깝다.

# Stack
# LIFO(Last In First Out)
# 블록 쌓기처럼 가장 늦게 들어온 데이터가 가장 먼저 나간다.
# 삽입 삭제 시간복잡도: 삽입 O(1), 삭제 O(1)

stack = [10, 20, 30]
stack.append(40)
stack.pop()             # 가장 최근에 넣은 40이 튀어나온다.

# Queue
# FIFO(First In First Out)
# 줄 서기처럼 가장 먼저 들어온 데이터가 가장 먼저 나간다.
# 때문에 객체 하나가 삭제되면 모든 요소가 앞으로 한칸 이동해야 한다.
# 삽입 삭제 시간복잡도: 삽입 O(1), 삭제 O(n)

from queue import Queue

my_queue = Queue()

my_queue = []
my_queue.put(10)
my_queue.put(20)
item = my_queue.get()            # 가장 먼저 넣은 10이 튀어나온다.

#######################################################################################

# Deque
# 그렇다면 Deque는 무엇인가?
# 양쪽 끝에서 빠른 추가 및 제거를 지원하는 더블 엔디드 큐(double-ended queue)이다.
# Queue보다 빠른 큐 작업을 제공하고 회전 및 슬라이스와 같은 추가 기능도 지원한다.

from collections import deque

my_deque = deque()

my_deque.append(10) # 덱의 오른쪽에 추가
my_deque.append(20)
item = my_deque.my_deque.popleft()  # Queue와 동일하게 10이 튀어나온다.

# 다만, Deque는 스레드가 안전하지 않아
# 단일 스레드에서 빠른 큐 작업이 필요하고 안전한 스레드 보호가 필요하지 않을 때 사용한다.
# 멀티스레딩 환경에서는 안전한 Queue를 사용한다.

#######################################################################################

# Hash Table
# 파이썬에서는 dict, C++에서는 map과 같은 컨테이너에서는
# index로 객체에 접근하듯, key값으로 객체에 접근할 수 있다.
# key -> hash function -> hash value -> bucket index 형태로 접근하게 된다.
# 즉, hash('a') -> 87329, 테이블 크기가 8이면: 87329 % 8 = 1, index 1에 저장하게 된다.
# hash value는 87329처럼 hash function이 만들어 낸 값을 이야기한다.
# 검색할 때도 동일하다 87329 % 8 = 1 -> table[1]로 접근하게 된다. (순서는 상관없다)
# 탐색 시간복잡도: 평균 O(1), 최악 O(n)

dict = {"alice" : 24, "banana" : 51}
dict["alice"]                           # alice와 짝지어진 값 24가 튀어나온다.

# Bucket
# hash table 내부에서 데이터를 저장하는 위치를 말한다.
# 예를 들어, table 크기가 8이라면, 0~7까지의 위치를 bucket이 된다.
# key -> hash() -> hash value -> tavle 크기에 맞춰 변환 -> bucket

# Hash Collision
# 만약, hash value % table size 연산 결과가 동일할 경우에는 어떻게 될까
# 둘 다 동일한 bucket으로 가게 되는데, 이를 해시 충돌이라고 한다.

# 해결 방법 1. Separate Chaining
# bucket 하나에 여러 값을 연결한다.
# 2번 bucket에 [a, 1] -> [b, 2]를 Linked List를 사용해 연결한다.
# 검색할 때, bucket에 접근해 내부를 탐색한다.

# 해결 방법 2. Open Addressing
# 충돌할 경우 다른 빈 bucket을 찾는다.
# 3번 bucket에 접근하였는데 사용 중일 경우, 빈 4번 bucket에 저장한다.

# 좋은 hash distribution과 적절한 capacity가 유지될 경우,
# 전체 데이터를 순회할 필요가 없어지므로 평균 O(1)의 시간이 걸린다.
# 그러나, 최악의 경우 모든 key가 같은 bucket에 충돌하게 될 수 있다.
# 그러면 특정 key를 찾기 위해 여러 후보를 확인해야 하므로
# 최악의 경우, O(n) 만큼의 시간이 걸릴 수 있다.

# mutable 객체인 list, dict, set은 key값으로 불가능하다.
# 해당 key값을 3번 bucket에 저장했다고 가정하자.
# 그런데, key가 변경되어 hash(key)가 7번 bucket을 가리키게 된다면?
# 실제 데이터를 담고 있는 3번 bucket을 보지 못하므로 안정성이 깨진다.

# Load Factor
# load factor = 저장된 원소 개수 / table capacity이다.
# Open Addressing에서는 테이블이 너무 꽉 차면 collision 처리가 증가해 성능이 저하되기 때문에
# 일정 수준 이상 차면 더 큰 table을 만들고 resize/rehash한다.

# Rehash
# table을 옮길 때 단순 복사로 옮기면 문제가 발생할 수 있다.
# bucket의 위치를 hash % capacity로 계산하기 때문이다.
# 그래서 기존 key들을 새 테이블 위치에 다시 배치하게 된다.
# 따라서 특정 resize는 O(n)의 시간복잡도를 가지게 될 수 있다.

#######################################################################################

# Set
# dict은 key -> value 형태로 저장하였다.
# 그러나 set은
s = {"alice", "banana"}
# 로 key만 중요하는 것을 알 수 있다.

# 둘 다 hash table 기반이므로 평균 O(1)의 시간복잡도를 가지고
# 특정 요소가 존재하는지 연산하는 membership test에서 O(1)로 훨씬 효율적인 경우가 많다.
# 탐색 시간복잡도: 평균 O(1), 최악 O(n)
# 삽입 삭제 시간복잡도: 삽입 O(1), 삭제 O(1)

#######################################################################################

# Heap
# 전체를 정렬하지 않고도 최솟값 또는 최댓값을 빠르게 꺼내기 위한 자료구조
# 삽입 삭제 시간복잡도: 삽입 O(log n), 최솟값 삭제 O(log n)
# 검색 시간복잡도: O(n)

# heapq
# heapq는 기본적으로 Min Heap이다.
# 모든 부모 노드는 자신의 자식보다 작거나 같다는 규칙을 가지고 있다.
# 따라서 가장 작은 값은 항상 root에 있게 된다.
# 즉, 최솟값을 확인할 때에는 heap[0], O(1)의 시간복잡도를 가지게 된다.

import heapq

heap = [8, 3, 10, 1, 6, 14, 4]
heapq.heapify(heap)

def sift_down(arr, n, i):
    while True:
        parent = i

        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[parent]:
            parent = left

        if right < n and arr[right] < arr[parent]:
            parent = right

        if parent == i:
            break

        arr[i], arr[parent] = arr[parent], arr[i]

        i = parent

def heapify(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)

# 정렬된 Tree와의 차이점
# Heap은 parent <= child 라는 조건만 만족하면 되기 때문에
# 정렬된 이진 트리라고 설명하면 틀린 설명이다.
# 정확하게는 '부분적인 순서 관계를 만족하는 Complete Binary Tree'이다.

# Complete Binary Tree(완전 이진 트리)
# 완전 이진 트리는 마지막 레벨을 제외한 모든 레벨이 채워져 있고, 마지막 레벨은 왼쪽부터 채워진 Tree다.
# 이 특성으로 인하여 포인터가 없어도 Tree를 만들 수 있다.
# 그래서 list로 작성하지만, tree 구조로도 그릴 수 있는 것이다.

# 0-based index에서
# 왼쪽 자식 = 2*i + 1
# 오른쪽 자식 = 2*i + 2
# 부모 = (i-1) // 2

# 이러한 특성으로 인하여
# Heap에서는 일반적인 Binary Tree처럼
# node.left, node.right와 같은 포인터를 반드시 저장할 필요가 없다.

heapq.heappush(heap, 2)

# 이렇게 새로운 객체가 삽입되면 어떻게 될까
# 완전 이진 트리를 유지하기 위해 일단 맨 끝에 추가한다.
# 그러나, Min Heap 규칙(parent <= child) 위반으로 부모와 교환한다.
# 규칙이 지켜질 떄까지 이를 반복하는 sift up / bubble up 과정이 진행된다.

# 삽입도 삭제도 모두 규칙을 확인하고 부모와 자식을 교환하는 과정인
# sift up / bubble up (삽입), sift down (삭제) 가 진행되므로
# O(log n)의 시간복잡도를 가진다.

# 또, BST(Binary Search Tree)와 다르게
# 특정 값을 검색할 때, 왼쪽 오른쪽 선택할 수 없으므로
# 탐색 시간복잡도는 O(log n)이 아닌 O(n)이다.

#######################################################################################

# Priority Queue
# 일반적인 큐(FIFO)와 달리, 우선순위에 따라 우선순위가 높은 데이터가 먼저 나오는
# ADT(Abstract Data Type), 즉 추상 자료형이다.

from queue import PriorityQueue

pqueue = PriorityQueue()
item = '작업'

pqueue.put((1, item))
priority, item = pqueue.get()

# list로 Stack의 동작 규칙을 구현하는 것처럼
# Heap으로 Priority Queue의 동작 규칙을 구현할 수 있다.

# 왜 정렬된 list가 아닌 heap을 사용하는가?
# 최솟값 제거는 O(1)이나, 삽입은 최대 O(n)이 소요되는 list와 달리
# heap은 제거와 삽입 모두 O(log n)으로 일정한 시간이 소요되기 때문이다.

#######################################################################################

# Max Heap
# Min Heap의 반대이다.
# 즉, Max Heap에 적용되는 규칙은 parent >= child이다.
# 그래서 root가 최댓값이다.

#######################################################################################

# Tree
# 계층적인 관계를 표현하는 자료구조이다.
# 기본 용어: Root, Parent, Child, Leaf
# Depth = root에서 해당 노드까지의 거리
# Height = 해당 노드에서 가장 깊은 leaf까지의 거리
# 탐색 시간복잡도: 평균 O(log n), 최악 O(n)
# 삽입 삭제 시간복잡도: 삽입 O(log n), 삭제 O(log n)

# Binary Tree
# 각 노드가 최대 2개의 child를 갖는 Tree이다.
# 규칙이 없는 Tree의 경우, 정렬이 되어 있지 않기 때문에
# 최악의 경우, 특정 요소 탐색에 O(n)의 시간이 걸린다.

# BST(Binary Search Tree)
# 이진 탐색 트리의 규칙: 왼쪽 subtree < 현재 node < 오른쪽 subtree
# 특정 값을 찾을 때, 작으면 왼쪽으로, 크면 오른쪽으로 찾게 되어
# 모든 노드를 볼 필요를 없앤다.

# Heap과 동일하게 탐색에는 O(log n)의 시간이 걸린다.
# 한번 비교할 때마다 탐색해야 할 후보가 대략 절반으로 줄어들기 때문이다.
# n -> n/2 -> n/4 -> ...
# 단, 균형이 잡혀있는 경우에만 O(log n)의 시간복잡도가 적용된다.

# 그러나, 한쪽으로 쏠릴 수가 있다.
# 1, 2, 3, 4, 5의 경우 오른쪽으로만 쏠려 사실상 Linked List가 되어버린다.
# 그래서 최악의 경우, 탐색에 O(n)의 시간복잡도가 소요될 수 있다.

# Balanced BST
# 해당 문제를 해결하기 위해
# AVL Tree와 Red-Black Tree와 같은 Self-Balancing BST가 존재한다.
# 이들의 목적은 Tree의 height를 O(log n)으로 유지하는 것이다.

# Tree 순회에도 3가지 방법이 있다.
# Preorder  : root -> left -> right
# Inorder   : left -> root -> right
# Postorder : left -> right -> root
# 특히, BST를 Inorder 방식으로 읽으면 값이 정렬된 순서로 나온다.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#######################################################################################

# Graph
# Tree와 달리 cycle이 있고, 여러 경로가 가능하다.
# 그리고 root가 없어도 가능하다.

# Directed / Undirected Graph
# Undirected는 양방향을 뜻하고
# Directed는 단방향을 뜻한다.

# Weighted Graph
# Edge에 비용을 넣을 수 있다.
# 해당 숫자들은 거리, 비룔, 시간, 가격 등 무엇이든 될 수 있다.
# 그래서 최단 경로 문제에서 Graph가 많이 쓰인다.

# Gragh를 메모리에 저장하는 방법에는 대표적으로 2가지가 있다.

# Adjacency Matrix(인접 행렬)
# 노드가 A B C D 라면 2차원 배열을 만든다.
# A-B가 연결되어 있으면, matrix[A][B] = 1로 표현한다.
# 두 노드가 연결되어 있는지 O(1)로 확인이 가능하지만,
# 노드가 V개면 V*V 만큼의 공간이 필요하다.
# 공간복잡도: O(V²)

# Adjacency List(인접 리스트)
# 각 노드가 자신의 이웃을 저장한다.

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}

from collections import defaultdict

graph = defaultdict(list)

# 공간복잡도: O(Vertices + Edges)

# 그래서 노드(Vertex)들에 비해 간선(Edge)의 수가 매우 적은 희소 그래프(Sparse Graph)에서는
# 인접 리스트를 사용하는 것이 메모리 공간과 탐색 속도에서 압도적으로 유리하다.

#######################################################################################

# DFS
# Depth First Search, 한 방향으로 최대한 깊게 들어갔다가 돌아온다.
# 대표적으로 Stack이 있다.
# 탐색 시간복잡도: 평균 O(V + E)

def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)

    for nxt in graph[node]:
        dfs(graph, nxt, visited)

# Graph에서는 cycle이 존재하기 때문에
# 꼭 visited 옵션이 필요하다.
# 그렇기 떄문에 중복없이 노드를 저장하고 visited 확인을 빨리 할 수 있는
# set 객체로 저장하는 것이다.

visited = set()

# visited 탐색 시간복잡도: 평균 O(1)

#######################################################################################

# BFS
# Breadth First Search, 가까운 노드부터 넓게 탐색한다.
# 대표적으로 Queue를 사용한다.
# 탐색 시간복잡도: 평균 O(V + E)

from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = {start}

    while q:
        node = q.popleft()

    for nxt in graph[node]:
        if nxt not in visited:
            visited.add(nxt)
            q.append(nxt)

# 최종적으로
# BFS     -> Queue -> Deque
# visited -> Set   -> Hash Table

# 가중치가 없는 Graph에서
# BFS는 시작점으로부터 최소 edge 개수의 경로를 찾을 수 있다.
# 가중치가 존재하는 Weighted Graph에서는
# BFS로 edge의 비용을 고려하지 못하기 때문에
# 다익스트라 알고리즘 같은 경우, Priority Queue / Heap 자료구조를 사용하는 것이다.

#######################################################################################

# Trie
# 문자열 검색을 위한 Tree 계열 자료구조이다.
# 탐색 시간복잡도: O(L) - 여기서 L은 문자열의 길이이다.
# 삽입 시간복잡도: O(L)

text = ['car', 'card', 'care', 'cat']

# 다음 단어들을 저장한다고 하였을 때,
# 일반적인 Tree처럼 단어 전체를 하나의 노드에 넣지 않고
# 문자 하나씩 저장한다.
# 마지막에 *를 넣어 '\0'처럼 단어 끝을 알린다.

# set에도 단어를 저장할 수 있다.

words = { "car", "card", "care", "cat" }

# "care" in words를 검사하면 Hash Table도 매우 빠른데, 왜 Trie가 필요할까?
# Prefix 검색 때문이다.
# 만약, "ca" 로 시작하는 모든 단어를 검색하고 싶다면
# Trie에서는 root -> c -> a 까지만 간 다음, 그 아래 subtree를 탐색하면 된다.
# 그래서 Trie는 자동완성, 검색어 추천, 사전 등에 강하다.

class TrieNode:                     # Trie의 전형적인 구조
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):         # Trie의 삽입
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_end = True

    def starts_with(self, prefix):  # Trie의 탐색
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return node.is_end        

    def get_all_words(self):        # Trie 모두 출력
        result = []

        def dfs(node, word):
            # return 하면 X
            # car, care의 경우, r도 is_end=True이고 e도 is_end=True이기 때문
            if node.is_end:
                result.append(word)

            # child_node가 없어도 오류 발생하지 않음
            for ch, child_node in node.children.items():
                dfs(child_node, word + ch)

# Trie의 단점도 존재한다.
# 속도 측면에서 좋아 보이지만 공짜가 아니다.
# 각 단어들을 위한 노드가 많이 필요하기 때문에
# 상당한 메모리 오버헤드가 생길 수 있다.
# 즉, 일반 배열의 경우에는 촘촘하게 저장되어 메모리 낭비가 없으나
# Trie 형태로 저장할 경우, 글자마다 26개짜리 포인터 배열을 통째로 들고 있기 때문에
# 수많은 빈 공간, 즉 오버헤드가 메모리를 차지하게 된다.

# 따라서, Trie는 prefix 연산을 빠르게 하는 대신 메모리를 더 사용하는 경향이 있다.
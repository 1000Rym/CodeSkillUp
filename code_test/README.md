# This is the Coding Test (python)
This book is made for practice coding skills, By challenging the problems listed in the book "이것이 취업을 위한 코딩 테스트이다. with Python"

## Good Sites for learning algorithms.
### For the Beginner 
[Code Signal(코드 시그널)](https://app.codesignal.com)
 - [CodingGame(게임코딩)](https://www.codeingame.com) 

### Most Famous 
[Codeforces(코드 포스)](https://codeforces.com)
- Seperate levels to gray, green mint, blue, purple, orange, red.
    - Testing Hours: 2 ~ 2.5 hours.

### Challanger 
[Jungol(정올)](http://jungol.co.kr): 국내 유명 알고리즘 싸이트.


## Greedy Algorithm
Definition: Always choosing the most obvious and immediate benifit.

### Problem1: change(거스름돈)
Assume that there coins in 500$, 100$ 50$, 10$. How to return minimum Coins. 
- My solution: [change.py](greedy/chagne.py)

### Problem2: bigger numbers(큰 수의 법칙)
Find Bigger numbers(The problem definition is not explained properly though). 
- My solution: [bigger_numbers.py](greedy/bigger_numbers.py)

- Note: Although in hardware design `%, *, div` are costing alot, but in software, it is recommended to use this operators than using `-` or `+` with loop.


## Searching Algorithm
Adjancency Matrix: 2차원 배열로 그래프의 연결관계를 표현하는 방식
- pos: 특정 노드와 연결된 연결된 노드를 순회 할 경우, 공간 낭비가 적음. 
- neg: 모든 노드 관계를 저장함으로 노드 개수가 많을수록 불필요한 메모리 발생 
Adjacency List: 리스트로 그래프의 연결 관계를 표현하는 방식
- pos: 메모리 절약
- neg: 순회 불리

```python
INF = 999999999

# 2 차원 리스트르르 이용해 인접 행렬 표현
graph_matrix = [
    [0, 7, 5], 
    [7, 0, INF],
    [5, INF,0]
]

# Adjecency List로 표현
graph_adjacency = [[] for _ in range(3)]
graph_adjacency[0].append((1,7))
graph_adjacency[0].append((2,5))
graph_adjacency[1].append((0,7))
graph_adjacency[2].append((0,5))
```

### DFS(Depth First Search)
- 그래프에서의 깊은 부분을 우선 탐색하는 방법
    - 주로 stack을 많이 사용하여 풀이 함. 
- 예제: [dfs_example.py](search/dfs_example.py)

### BFS(Breath First Search)
- 너비 우선 탐색, 가까운 노드부터 넓게 탐색하는 알고리즘
    - 주로 queue를 많이 사용하여 풀이 함.
- 예제: [bfs_example.py](search/bfs_example.py)
   



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

- 동작과정: 
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다. 
    1. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접한 노드가 없으면 스택에서 최상단 노드를 꺼낸다. 
    1. 2번과정을 더 이상 수행할 수 없을때까지 반복한다. 

- 예제: [dfs_example.py](search/dfs_example.py)

### BFS(Breath First Search)
- 너비 우선 탐색, 가까운 노드부터 넓게 탐색하는 알고리즘
    - 주로 queue를 많이 사용하여 풀이 함.

- 동작과정: 
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다. 
    1. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다. 
    1. 2번 과정을 더 이상 수행할 수 없을 때까지 반복한다. 
- 예제: [bfs_example.py](search/bfs_example.py)

### 연습문제: 
- 아이스크림 찾기: [ice_cream_maker.py](search/ice_cream_maker.py)
- 미로탈출: [escape_maze.py](search/escape_maze.py) BFS 방식으로 deque(queue)를 사용하여 해결.

## Sorting Algorithm
- 선택 정렬 Selection Sort
    - 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복 
    - 시간 복잡도: O(N²) 소요.
    - 구현하기 쉽지만 느림.

- 삽입정렬 Insertion Sort
    - 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입.
    - 이미 정렬되어 있는 경우, O(N)이 소요된다. 
    
- 퀵 정렬 Quick Sort
    - 기준 데이터(pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법.
    - 시간 복잡도: O(NlogN)

- 합병 정렬 Merge Sort
    - 문제를 쪼갤 수 없는 두개의 문제로 분해하고, 차차 정렬하면서 합병하는 방법.
    - 시간복잡도:  O(n*log n)


- 계수 정렬(Count Sort)
    - __일정한 작은 범위가 정해진 경우__ 사용할 수 있는, 빠른 알고리즘(비교기반의 정렬 알고리즘이 아님).
        - 모든 범위를 담을 수 있는 크기의 리스트(범위)를 미리 선언.
        - 리스트의 원소들은 각각 나타난 count 값을 갖고 있음. 
        - 최종적으로, index 를 순차적으로 나타난 횟수대로 count번 출력함.
    - 시간 복잡도: O(N+K)
    - 장단점:
        - 장점: 정해진 작은 범위내에서 빠르게 정렬 가능.
        - 단점: 범위가 정해지지 않을 경우 사용할 수 없거나,범위가 큰 경우 메모리 수요가 크기에 효율적이지 않음.

- 코드: [sorting_algorithm.py](sorting/sorting_algorithm.py)
- 연습문제: 
    - [ex1_top2bottom.py](sorting/ex1_top2bottom.py)
    - [ex2_exchangearrays.py](sorting/ex2_exchangearrays.py)
    - [ex3_printfromlowscore.py](sorting/ex3_print_from_lowscore.py)

## Searching Algorighm
- Sequential Search(순차 탐색)
    - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.
    - 정렬되지 않은 데이터에서 찾을 시 사용.
    - O(N)
- Binary Search(이진 탐색)
    - 탐색하고자 하는 범위의 __시작점, 끝점, 중간점__ 중, 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 과정이다.
    - 이미 정렬되어 있는 구조에서 사용.
    - O(logN)
    - 코드: [binary_search.py](search/binary_search.py)

### Binary Search Tree(이진 탐색 트리)
- __왼쪽 자식 노드 <  부모노드 < 오른쪽 자식노드__ 의 관계가 성립
#### 빠르게 입력받기
- 데이터가 방대할 경우(1000만개를 넘길경우), 기존의 input()함수를 사용하는것은 비효율적이다. 
- 이를 해결하는 방법으로 `sys.stdin.readline().rstrip()`을 이용한다. 
    - `rstrip()`을 해주는 이유는 엔터마크를 없애기 귀함이다.

- 연습문제: 
    - [ex1_cutcake.py](cut_cake.py)


## Dynamic Programming (다이너믹 프로그래밍)
큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘 기법으로, 메모리 공간을 약간 더 사용하여 연산 속도를 비약적으로 증가시키는 방법. 
-  Memoization(메모제이션): 한 번 구한 결과를 공간해 메모해두고 같은 식을 다시 호출할 시 메모한 결과를 그대로 가져오는 방법, Caching(캐싱)이라고도 함([memoization_fibo.py](dynamic_programming/memoization_fibo.py)).
- 전형적인 형태는 결과 저장용 리스트인 DP-Table로 보관하는 bottom-up 방식을 사용한다([memoization_fibo.py](dynamic_programming/memoization_fibo.py) 의 `bottom_up(n)`). 









   



# 이것이 취업을 위한 코딩 테스트이다
"이것이 취업을 위한 코딩 테스트이다"에 수록 된 코딩문제들을 풀어보고, 나만의 노하우를 정리하려는 목적으로 만들어 짐. 

## Good Sites for learning algorithms.
- Beginner Level
    - [Code Signal(코드 시그널)](https://app.codesignal.com)
    - [CodingGame(게임코딩)](https://www.codeingame.com) 

- Normal Level
    - [Codeforces(코드 포스)](https://codeforces.com)
        - Seperate levels to gray, green mint, blue, purple, orange, red.
            - Testing Hours: 2 ~ 2.5 hours.

- Challanger  Level
   -  [Jungol(정올)](http://jungol.co.kr): 국내 유명 알고리즘 싸이트.

## Greedy Algorithm
Always choosing the most obvious and immediate benifit, generally  we can solve with the following patterns.
1.  sort the data list.
1.  Make the algorithm that choose data from the largest.

### Greedy Problems
1. [거스름 돈](coding_test_with_python/greedy/p1_change.py) 
1. [큰 수의 법칙](coding_test_with_python/greedy/p2_principle_of_big_numbers.py)
1. [숫자카드 게임](coding_test_with_python/greedy/p9_card_game.py)
1. [1이 될 때까지](coding_test_with_python/greedy/)
1. [01 모험가 길드](coding_test_with_python/greedy/p3_advanture_guild.py)
1. [02 곱하기 혹은 더하기](coding_test_with_python/greedy/p4_add_or_mul.py)
1. [03 문자열 뒤집기](coding_test_with_python/greedy/p5_filp_chars.py)
1. [04 만들 수 없는 금액](coding_test_with_python/greedy/p6_unmakable_money.py)
1. [05 볼링공 고르기](coding_test_with_python/greedy/p7_balling_balls.py)
1. [06 무지의 먹방 라이브](coding_test_with_python/greedy/p8_eating_live.py)

## Implementation
- 해결방법:
    - __완전탐색__: 모든 경우의 수를 주저 없이 다 계산하는 해결방법.
    - __시뮬레이션__: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 문제.

- 주의해야 할 사항
    - 메모리 제약사항
        - [C/C++ 에서의 변수의 표현범위](https://github.com/1000Rym/CodeSkillUp/blob/master/cpp/basic/README.md#primitive-data-types) 
        - 파이썬에서의 리스트 크기: 대체적으로 코딩 테스트에서는 128~512MB 사이의 메모리 제약사항을 둔다. 
        
            | 리스트의 길이     | 메모리 사용량     |
            |   :---:       |   :---:       |
            |   1000        |   4KB         |
            | 1,000,000     |   4MB         |
            | 10,000,000    |   40MB        |
    - 채점환경: 파이썬은 C/C++에 비해 동작 속도가 느리다.

- 접근하는 방법 
    - 파이썬: 구현이 쉽다. 하지만 프로그램 실행 시간이 길다. 
    - PyPy: 구현도 쉽고, 프로그램 실행 시간 또한 다소 짧은 편이다. 
    - C/C++: 구현이 어렵지만, 실행시간이 짧은 편이다.

### Implementation Problems
1. [상하좌우](coding_test_with_python/implementation/p1_up_down_left_right.py)
1. [시각](coding_test_with_python/implementation/p2_time.py)
1. [게임개발](coding_test_with_python/implementation/p3_game_development.py)
1. [07 럭키스트레이트](coding_test_with_python/implementation/p4_lucky_straight.py)
1. [08 문자 재정렬](coding_test_with_python/implementation/p5_str_sort.py)
1. [09 문자열 압축](coding_test_with_python/implementation/p06_str_compression.py)
1. [10 자물쇠와 열쇠](coding_test_with_python/implementation/p07_key_and_password.py)
1. [11 뱀](coding_test_with_python/implementation/p08_snake.py)
1. [13 치킨 배달](coding_test_with_python/implementation/p09_chicken_delivery.py)
1. [14 외벽 점검](coding_test_with_python/implementation/p10_wall_check.py)

## Searching Algorithm
맵의 표현방법

- Adjancency Matrix: 2차원 배열로 그래프의 연결관계를 표현하는 방식.
    ```python
    INF = int(1e9)
    # 2 차원 리스트르르 이용해 인접 행렬 표현
    graph_matrix = [
        [0, 7, 5], 
        [7, 0, INF],
        [5, INF,0]
    ]
    ```
    - pos: 특정 노드와 연결된 연결된 노드를 순회 할 경우, 공간 낭비가 적음. 
    - neg: 모든 노드 관계를 저장함으로 노드 개수가 많을수록 불필요한 메모리 발생
   

- Adjacency List: 리스트로 그래프의 연결 관계를 표현하는 방식.
    ```python
    # Adjecency List로 표현
    graph_adjacency = [[] for _ in range(3)]
    graph_adjacency[0].append((1,7))
    graph_adjacency[0].append((2,5))
    graph_adjacency[1].append((0,7))
    graph_adjacency[2].append((0,5))
    ```
    - pos: 메모리 절약
    - neg: 순회 불리


### DFS(Depth First Search)
- 그래프에서의 깊은 부분을 우선 탐색하는 방법
    - 주로 stack을 많이 사용하여 풀이 함. 

- 동작과정: 
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다. 
    1. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접한 노드가 없으면 스택에서 최상단 노드를 꺼낸다. 
    1. 2번과정을 더 이상 수행할 수 없을때까지 반복한다. 

- 예제: [dfs_example.py](coding_test_with_python/search/dfs_example.py)

### BFS(Breath First Search)
- 너비 우선 탐색, 가까운 노드부터 넓게 탐색하는 알고리즘
    - 주로 queue를 많이 사용하여 풀이 함.

- 동작과정: 
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다. 
    1. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다. 
    1. 2번 과정을 더 이상 수행할 수 없을 때까지 반복한다. 
- 예제: [bfs_example.py](coding_test_with_python/search/bfs_example.py)

### Sequential Search(순차 탐색)
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.
- 정렬되지 않은 데이터에서 찾을 시 사용.
- O(N)

### Binary Search(이진 탐색)
- 탐색하고자 하는 범위의 __시작점, 끝점, 중간점__ 중, 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 과정이다.
- 이미 정렬되어 있는 구조에서 사용.
- O(logN)
- 코드: [binary_search.py](coding_test_with_python/search/binary_search.py)

### Binary Search Tree(이진 탐색 트리)
- __왼쪽 자식 노드 <  부모노드 < 오른쪽 자식노드__ 의 관계가 성립

#### 빠르게 입력받기
- 데이터가 방대할 경우(1000만개를 넘길경우), 기존의 input()함수를 사용하는것은 비효율적이다. 
- 이를 해결하는 방법으로 `sys.stdin.readline().rstrip()`을 이용한다. 
    - `rstrip()`을 해주는 이유는 엔터마크를 없애기 위함이다.

### Search Problems: 
- [아이스크림 찾기](coding_test_with_python/search/p01_ice_cream_maker.py)
- [미로 탈출](coding_test_with_python/search/p02_escape_maze.py): BFS 방식으로 deque(queue)를 사용하여 해결.
- [15 특정 거리의 도시 찾기](coding_test_with_python/search/q15_finds_specific_cities.py)
- [16 연구소](coding_test_with_python/search/q16_lab.py)
- [17 경쟁적 전염](coding_test_with_python/search/q17_competitive_transfer.py)
- 18 괄호 변환
- [19 연산자 끼워넣기](coding_test_with_python/search/q19_add_op.py)
- [20 감시피하기](coding_test_with_python/search/q20_avoid_detaction.py)
- [21 인구이동](coding_test_with_python/search/q21_population_movement.py)
- [22 블록이동하기](coding_test_with_python/search/q22_move_blocks.py)
- Binary Search
    - [27 정렬된 배열에서 특정 수의 개수 구하기](coding_test_with_python/search/q27_find_specific_numbers_count.py)
    - [28 고정점 찾기](coding_test_with_python/search/q28_fixed_point.py)
    - [29 공유기 설치](coding_test_with_python/search/q29_setup_routers.py) (Need to fix, didn't use the binary search)
    - [30 가사 검색](coding_test_with_python/search/q30_search_words.py) (Need to fix, didn't use the binary search)

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

- 위상 정렬(Topology Sort)
    - 정의
        - 정해져 있는 일련의 작업을 차례대로 수행해야 할 떄 사용할 수 있는 알고리즘.
        - 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것.
        - Indegree(진입차수) : 특정한 노드로 들어오는 간선의 개수
    - 알고리즘 
        1. 진입차수가 0인 노드를 큐에 넣는다. 
        1. 큐가 빌 때까지 다음의 과정을 반복한다. 
            1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다. 
            1. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다. 

- 코드: [sorting_algorithm.py](coding_test_with_python/sorting/sorting_algorithm.py)


### Sorting Problems
1. [위에서 아래로](coding_test_with_python/sorting/ex1_top2bottom.py)
1. [성적이 낮은 순서로 출력하기](coding_test_with_python/sorting/ex2_exchangearrays.py)
1. [두 배열의 원소 교체](coding_test_with_python/sorting/ex3_print_from_lowscore.py)
1. [23 국영서](coding_test_with_python/sorting/q23_sorting_scores.py)
1. [24 안테나](coding_test_with_python/sorting/q24_setup_antenna.py)
1. [25 실패율](coding_test_with_python/sorting/q25_fail_ratio.py)
1. [26 카드정열하기](coding_test_with_python/sorting/q26_sorting_cards.py)

## Dynamic Programming (다이너믹 프로그래밍)
큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘 기법으로, 메모리 공간을 약간 더 사용하여 연산 속도를 비약적으로 증가시키는 방법. 
-  Memoization(메모제이션): 한 번 구한 결과를 공간해 메모해두고 같은 식을 다시 호출할 시 메모한 결과를 그대로 가져오는 방법, Caching(캐싱)이라고도 함([memoization_fibo.py](coding_test_with_python/dynamic_programming/memoization_fibo.py)).
- 전형적인 형태는 결과 저장용 리스트인 DP-Table로 보관하는 bottom-up 방식을 사용한다([memoization_fibo.py](coding_test_with_python/dynamic_programming/memoization_fibo.py) 의 `bottom_up(n)`).

### Dynamic Programming Problems
1. [31 금광](coding_test_with_python/dynamic_programming/q31_mine_craft.py)
1. [32 정수 삼각형](coding_test_with_python/dynamic_programming/q32_equalateral_triangle.py)
1. [33 퇴사](coding_test_with_python/dynamic_programming/q33_resignation.py)
1. [34 병사 배치하기](coding_test_with_python/dynamic_programming/q34_arrange_military.py)
1. [35 못생긴 수](coding_test_with_python/dynamic_programming/q35_ugly_numbers.py)

## Shortest Path Algorithm
### dijkstra(다익스트라) 최단경로 알고리즘
특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구하는 알고리즘 (음의 간선이 존재하지 않아야 함).
- 알고리즘 절차:
    1. 출발 노드를 설정
    1. 최단 거리 테이블을 초기화
    1. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
    1. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
    1. 위 과정에서 3과 4를 반복 
- 시간 복잡도: O(N²) 소요.
- Priority Queue(Heap Queue)를 사용하여 쉽게 해결
    - Dijkstra Algorithm에서 주로 Heap Queue(Priority Queue)를 사용하여 최적화 할 수있다. 
    - 시간 복잡도: O(NlogN)에 해당
        ```python
        import heapq
        q = []
        # 데이터를 입력하면, priority 에근거하여 queue에 들어간다.
        heapq.heappush(q, (priority, data))

        # 데이터를 출력하면, priority에 근거하여 데이터를 Pop 한다. 
        heapq.heappop(q)
        ```
- 코드: [dijkstra_algorithm.py](coding_test_with_python/shortest_path/dijkstra_algorithm.py) 

### Floyd-Warshall Algorithm
모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용.
- 단계마다 O(N²)를 통해 시간을 소모하여 모든 경로의 최단 경로를 계산한다. 
- 시간 복잡도: O(N^3)
- 단계마다 점화식 Shortest `D[ab] = min(D[ab], D[ak]+D[kb])`를 수행
    - a 와 b의 최소거리는 a, b로 통하는 모든 거리의 최소값이다,.

- 코드: [floyid_wallshall_algorithm..py](coding_test_with_python/shortest_path/floyid_wallshall_algorithm.py)


### Shortest Path Problem
1. [37 플로이드](coding_test_with_python/shortest_path/q37_floyd.py)
1. [38 정확한 순위](coding_test_with_python/shortest_path/q38_correct_rank.py)
1. [39 화성 탐사](coding_test_with_python/shortest_path/q39_mars_exploration.py)
1. [40 숨바꼭질](coding_test_with_python/shortest_path/q40_hide_and_seeks.py)
1. [41 여행 계획](coding_test_with_python/shortest_path/q41_travelling_plans.py)

## Graph Algorithm
### Disjoint Sets(서로소 집합)
서로 중첩이 되지 않은 집합으로 트리를 만드는 경우 절차:
1. Union(합집합) 연산을 확인하여, 서로 연결 된 두 노드, A, B를 확인한다.
    1. A와 B의 루트 노드 A', B'를 각각 찾는다. 
    1. A'를 B의 루트 노드로 설정한다. 
1. 모든 Union 연산을 처리할 때까지 1번과정을 반복한다. 
-  코드 : [disjoint_sets.py](coding_test_with_python/graph/disjoint_sets.py) 

Cycle 검사방법:
1. 각 간선을 확인하며 두 노드의 루트 노드를 확인
    1. 루트 노드가 다르다면 두 노드에 대해 병합 연산을 수행
    1. 루트 노드가 서로 같다면 (Cycle)이 발생
1. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정을 반복
-  Code : [disjoint_sets_check_cycle.py](coding_test_with_python/graph/disjoint_sets_check_cycle.py)
- 시간복잡도: O(V+M(1+log2-M/vV))


#### Kruskal Algorithm (크루스칼 알고리즘)
가장 적은 비용으로 모든 노드를 연결하는 알고리즘. 가장 거리가 짧은 간선부터 집합에 포함시킨다. 다만 사이클이 발생할 경우, 집합에 포함시키지 않는다. 
1. 간선 데이터를 비용에 따라 오름차순으로 정열한다. 
1. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는 간선인지를 확인한다. 
    1. 만약 사이클이 발생하지 않는다면 최소 신장 트리에 포함시킨다. 
    1. 사이클이 발생할 경우, 최소 신장 트리에 포함시키지 않는다. 
1. 모든 절차에 대해 2번 과정을 포함시킨다.
-  Code : [kruskal_algorithm.py](coding_test_with_python/graph/kruskal_algorithm.py) 
- 시간: O(ElogE): E는 E개의 데이터를 상징

### Graph Exercise and Problems
1. [ex1_make_team.py](coding_test_with_python/graph/ex1_make_team.py) 
1. [ex2_city_division.py](coding_test_with_python/graph/ex2_city_division.py) 
1. [ex3_curriculm.py](coding_test_with_python/graph/ex3_curriculm.py)
1. [42 탑승구](coding_test_with_python/graph/q42_board_gate.py)
1. [43 어두운 길](coding_test_with_python/graph/q43_dark_roads.py)

## 코딩 테스트를 위한 파이썬 주요 라이브러리
- 내장 함수: 코딩테스트에서 자주 사용하는 내장 함수는 `min`, `max`, `eval`, `sorted` 등이 있다. 
    - sorted의 key 접근 활용 사례
        ```python
        my_dict = {'john':35, 'may':24, 'kay':23}
        # 내림차순으로 정렬
        result = sorted(my_dict.items(), key=lambda x: x[1], reverse = True)
        ```
- itertools: 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이버리이다. 코딩테스트에는 주로 `permutations`, `combinations`이 사용된다. 
    - `permutations(data, 3)` :data 세개의 원소들로 구성할 수 있는 모든 경우 (순열)을 계산 함.
    - `product(data, repeat=3)`: data에서 중복을 허용하는 세개의 원소를 뽑는 순열을 계산 함.
    - `combinations(data,3)`: data 세개의 원소들로 이루어진 순서를 고려하지 않은 모든 조합. 
    - `combinations_with_replacement(data, 3)`: data에서 중복을 허용하면서 순서에 상관없는 경우의 조합.
        ```python
        from itertools import permutations
        from itertools import product
        from itertools import combinations
        from itertools import combinations_with_replacement

        data = [1,2,3]
        
        # permutations
        print(list(permutations(data,2)))
        # result: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

        # product
        print(list(product(data, repeat = 2)))
        # result: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

        # combinations
        print(list(combinations(data, 2)))
        # result: [(1, 2), (1, 3), (2, 3)]

        # combinations_with_replacement
        print(list(combinations_with_replacement(data,2)))
        # result: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
        ```
- heapq: 다익스트라 최단 경로 알고리즘과 같은 다양한 알고리즘의 Priority Queue 기능을 구현하고자 할 때 사용된다.
    - 데이터 추가 삭제시 O(NlogN)의 시간으로 오름차순이 완성된다. 
    - 파이썬에서 최대힙을 제공하지 않기에, 내림차순 힙 정렬을 구하려면 `-` 값을 대입하는 방식으로 처리할 수 있다. `(heaq.heappush(h, -value))`
- bisect: 이진 탐색을 쉽게 구현하기 위해 사용 됨.
    - 정렬된 배열에서 특정된 원소를 찾아야 할 때 효과적.
        - `bisect_left(a,x)`, `bisect_right(a,x)`: 정렬된 순서를 유지하면서 리스트 a의 왼쪽, 오른쪽에 데이터 x를 삽입할 왼쪽 인덱스를 찾는 메서드
    - 정렬된 배열에서 특정 범위에 속하는 값의 개수를 구할때 효과적
        ```python
        from bisect import bisect_left, bisect_right
        
        data = [12,33,44,55,66,77,88,99,100]
        
        # print value between 50 to 80
        right_index = bisect_right(data, 50)
        left_index = bisect_left(data, 80)

        print(data[right_index: left_index])
        # result: [55, 66, 77]
        ```
- collections: 유용한 자료구조를 제공하는 표준라이브러리. 코딩테스트에서는 `deque`과 `Counter`를 주로 사용한다. 
    - deque: `appendleft`, `append`, `popleft`, `pop` 연산 시간복잡도는 모두 O(1)이다.
    - Counter: 등장 횟수를 세는 기능을 제공
        ```python
        from collections import Counter
        data = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5]
        counter = Counter(data)
        print(counter)
        # result: Counter({5: 4, 1: 3, 2: 3, 3: 3, 4: 3})
        ```
- math: 수학적인 기능을 제공하는 라이브러리이다. 
    - 팩토리얼(`math.factorial(n)`), 제곱근(`math.sqrt(n)`), 최대공약수(greatest common divisor:`math.gcd(n1,n2)`), 최대공배수(largest common multiple: `math.lcm(n1,n2)`, 파이(`math.pi`), 자연상수 e(`math.e`))등을 제공한다.

## 개발형 코딩 테스트에 필요한 지식
### 파이썬으로 웹 요청하기
requests 라이브러리를 필요로 한다. 
- GET: 데이터 조회 요청
- POST: 데이터 생성 요청
- PUT: 데이터 수정 요청
- DELELTE: 데이터 삭제 요청. 
```python
import requests
response = requests.get(url="http://google.com")
print(response.content)
# 응답 내용을 출력
```
### REST API
REST(__Re__ presentational __s__ tate __t__ ransfer) 아키텍처를 따르는 API를 의미
- __resource__:  자원, URL 을 이용하여 표현
- __verb__: 행위, HTTP 메서드를 이용하여 표현
- __representations__: 표현 

#### 실습
- JSON Placeholder 
    - https://jsonplaceholder.typicode.com/
- JSON Placeholder의 데이터 처리
    ```python
    import requests
    target = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url=target)
    data = response.json()

    # print the user name.
    for user in data:
        pint(f"name:{user['name']}")
    ```

## Reference : 
[참고도서: 이것이 취업을 위한 코딩 테스트이다](http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791162243077) 

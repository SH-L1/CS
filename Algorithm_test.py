# Two Pointer

# 입력
# 첫째 줄에 N과 S가 주어진다.
# 둘째 줄에는 수열이 주어진다.
# 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000 이하의 자연수이다.

# 예제 입력: 10 15
#            5 1 3 5 10 7 4 9 2 8
# 예제 출력: 2

class two_pointer:
    N, S = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))

    total = 0
    start = 0
    end = 0
    answer = float("inf")

    while True:
        if total >= S:
            answer = min(answer, end - start)
            total -= nums[start]
            start += 1
        elif total < S:
            if end == len(nums):
                break

            total += nums[end]
            end += 1

    print(0 if answer == float("inf") else answer)

# Sliding Window

# 입력
# 첫째 줄에 DNA 문자열 길이 |S|와 비밀번호로 사용할 부분문자열의 길이 |P| 가 주어진다.
# 둘째 줄에는 DNA 문자열이 주어진다.
# 셋째 줄에는 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수가 공백을 구분으로 주어진다.

# 예제 입력: 4 2
#           GATA
#           1 0 0 1
# 예제 출력: 2

from collections import deque

class sliding_window:
    S, P = map(int, input().strip().split())
    dna = list(str(input()))
    A, C, G, T = map(int, input().strip().split())

    dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    left, right = 0, P - 1
    arr = deque(dna[left:right])
    count = 0

    for i in arr:
        dict[i] += 1

    while True:
        if right > S:
            break
        elif right <= S:
            dict[dna[right]] -= 1

            if dict['A'] >= A and dict['C'] >= C and dict['G'] >= G and dict['T'] >= T:
                count += 1

            dict[dna[left]] += 1
            right += 1
            left += 1

    print(count)

# Prefix Sum

# 입력
# 첫째 줄에 N과 M이 주어진다.
# 둘째 줄에는 N개의 수가 주어진다.
# 셋째 줄에는 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 예제 입력: 5 3
#           5 4 3 2 1
#           1 3
#           2 4
#           5 5
# 예제 출력: 12
#            9
#            1

class prefix_sum:
    N, M = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))

    sum_list = [0] * (N + 1)

    for i in range(N):
        sum_list[i + 1] = sum_list[i] + nums[i]

    for _ in range(M):
        i, j = map(int, input().strip().split())
        print(sum_list[j] - sum_list[i - 1])

# 
# 알고리즘

# 각 항목 구성 
# 1. 시간복잡도 설명
# 2. 자료구조 선택 이유
# 3. edge case 처리
# 4. 읽기 좋은 코드

# Two Pointer

# 예시 문제
# 정렬된 배열에서 합이 target이 되는 두 숫자를 찾아라.

nums = [1, 2, 4, 6, 8, 9]
target = 10

def find_pair(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return nums[left], nums[right]

        if current < target:
            left += 1
        else:
            right -= 1

    return None

# 시간복잡도: O(n)
# left와 right 모두 최대 n번 이동하기 때문이다.

# 해당 알고리즘의 본질은
# 현재 상태를 기반으로 탐색 후보의 일부를 안전하게 제거하는 것이다.
# 그래서 보통 정렬된 배열, 양 끝, 중복 제거 등의 문제에서 사용한다.

#######################################################################################

# Sliding Window

# 예시 문제
# 길이가 k인 연속 부분 배열의 최대 합을 구하라.

nums = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum(nums, k):
    window_sum = sum(nums[:k])
    answer = window_sum

    for right in range(k, len(nums)):
        left = right - k

        window_sum -= nums[left]
        window_sum += nums[right]

        answer = max(answer, window_sum)

    return answer

# 시간복잡도: O(n)

# Two Pointer와 다르게 해당 알고리즘의 본질은
# 연속 구간을 유지하면서 이동하는 것이다.

# Variable Sliding Window

# 예시 문제
# 양수 배열에서 합이 target 이상인 가장 짧은 연속 부분 배열의 길이를 구하라.

nums = [2, 3, 1, 2, 4, 3]
target = 7

def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    answer = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            answer = min(answer, right - left + 1)

            current_sum -= nums[left]
            left += 1

    return 0 if answer == float("inf") else answer

# 시간복잡도: O(n)
# 동일하게 right는 0 -> n-1, left도 0 -> n-1 딱 한 번씩 이동한다.
# 즉, 중첩 반복문이여도 포인터가 몇 번 움직이냐에 따라 O(n²)이 아닐 수 있다.

#######################################################################################

# Prefix Sum
# 매번 인덱스별 연산을 진행하면
# 시간복잡도가 O(nq)만큼 소요되기 때문에
# 미리 누적합을 저장한다.

def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)

    for i, num in enumerate(nums):
        prefix[i + 1] = prefix[i] + num

    return prefix

# 여기까지 정리
# Two Pointer: 불필요한 후보를 다시 검사하지 않는다.
# Sliding Window: 이전 구간의 계산 결과를 다시 사용한다.
# Prefix Sum: 이전 누적 계산 결과를 미리 저장한다.
# ===> 즉, 이미 계산한 것을 다시 계산하지 않는다.

#######################################################################################

# Sort(정렬)

# 이번 챕터에서 알아가야 할 것
# - O(n²) 정렬과 O(n log n) 정렬의 차이
# - Stable / Unstable
# - In-place 여부
# - Merge Sort와 Quick Sort의 trade-off
# - Heap Sort가 왜 O(n log n)인지
# - Python의 sort() / sorted() 특징
# - 이미 거의 정렬된 데이터에서는 어떤 방법이 유리한지
# - 정렬을 활용하면 원래 O(n²) 문제를 O(n log n)으로 바꿀 수 있는 경우

# 비교 정렬의 한계
# 5 < 2 ?, 8 < 5 ?, 3 < 8 ? 처럼 비교만으로 n개의 데이터를 정렬하는 알고리즘은
# 일반적으로 O(n log n)보다 빠른 최악 시간복잡도를 가질 수 없다.

#######################################################################################

# Bubble Sort
# 인접한 두 값을 비교해서 큰 값을 오른쪽으로 밀어낸다
# Stable Sort
# 시간복잡도: 최고 O(n), 평균 O(n²), 최악 O(n²)
# 공간 시간복잡도: O(1)

nums = [5, 2, 8, 1, 3]

def bubble_sort(nums):
    for i in (n - 1, 0, -1):
        swapped = False;

        for j in range(i):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

        if not swapped:
            break

    return nums

#######################################################################################

# Selection Sort
# 매번 가장 작은 값을 찾아 앞으로 보낸다.
# Unstable Sort
# 시간복잡도: O(n²)

nums = [5, 2, 8, 1, 3]

def selection_sort(nums):
    n = len(nums)

    for i in range(n):
        min_idx = i 

        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

# Stable Sort와 Unstable Sort의 차이점은 뭘까
# 동일한 key를 가진 데이터들의 기존 상대적 순서를 유지하는지 변경되는지에 따라
# Stable과 Unstable로 나뉜다.
# 다중 조건 정렬에서 중요하게 쓰인다.

#######################################################################################

# Insertion Sort
# 정렬된 영역에 새로운 값을 적절한 위치에 삽입한다.
# Stable Sort
# 시간복잡도: 최고 O(n), 평균 O(n²), 최악 O(n²)

def insertion_sort(nums):
    temp = nums[:]

    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = current

    return nums

# 거의 정렬된 배열에서 왜 O(n)에 가까운 성능을 낼 수 있는 것일까?
# 데이터가 거의 정렬되어 있으면
# 이동해야 할 거리가 짧아 전체 작업량이 선형 수준에 가까워질 수 있다.

#######################################################################################

# Merge Sort
# 여기서부턴 많이 쓰이는 O(n log n) 알고리즘이다.
# 큰 문제를 작은 문제로 나누고, 각각 해결한 뒤 합친다.
# Stable Sort
# 시간복잡도: O(n log n)

nums = [5, 2, 8, 1, 3]

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 깊이가 O(log n), 병합 작업량이 O(n) 이기 때문에
# 최종 시간복잡도는 O(n) * O(log n) = O(n log n) 이다.

#######################################################################################

# Quick Sort
# pivot을 하나 선택하여 비교한 후,
# 작으면 좌측, 크면 우측으로 계속 정렬한다.
# Unstable Sort
# 시간복잡도: 평균 O(n log n), 최악 O(n²)

nums = [5, 2, 8, 1, 3]

def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]

    left = []
    equal = []
    right = []

    for x in nums:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)

    return quick_sort(left) + equal + quick_sort(right)

# 만약 pivot이 계속 최악으로 선택되어
# left 혹은 right로 객체들이 치우쳐질 경우에는 재귀가 깊어지므로
# O(n²)의 시간복잡도가 소요될 수 있다.
# 그래서 Median-of-Three나 Randomized Pivot 형태로 사용하여
# 항상 안전하게 평균 성능인 O(n log n)을 보장받을 수 있도록 한다.

# 최악의 시간복잡도를 고려하였을 때,
# 항상 O(n log n)을 보장하지 못하는 Quick Sort가 왜 중요할까?
# In-place Partition(제자리 분할), Cache Locality(캐시 지역성) 때문이다.
# 임시 배열을 만들고 메모리를 계속 이동해야 하는 Merge Sort와 달리
# Quick Sort는 현재 배열 내에서 이웃한 데이터까지 정렬하기 때문에
# 실제 실행 속도가 훨씬 빠르다.

#######################################################################################

# Heap Sort
# Heap을 만들어 최솟값과 최댓값을 반복해서 꺼내어 정렬한다.
# Unstable Sort
# heapify의 시간복잡도: O(n)
# heappop n번의 시간복잡도: n * O(log n)
# 전체 시간복잡도: O(n log n)

import heapq

nums = [5, 2, 8, 1, 3]      # heapify시, [1, 2, 8, 5, 3]

def heap_sort(nums):
    heap = nums[:]
    heapq.heapify(heap)     # list를 heap, 즉 완전 이진 트리 형태로 만들어준다.

    result = []

    while heap:
        result.append(heapq.heappop(heap))

    return result

# 파이썬에서는 보통 sort()나 sorted() 함수를 통해
# 직접 구현 없이 배열을 정렬한다.
# sort()와 sorted()의 차이점은
# sort()는 기존 list를 변경하지만, sorted()는 새로운 list을 반환한다.

#######################################################################################

# Timsort
# 파이썬의 sort()는 Timsort 계열의 정렬을 사용한다.
# Merge Sort + Insertion Sort 등의 아이디어를 활용하고,
# 실제 데이터에 이미 존재하는 정렬된 구간을 적극 활용하는
# Adaptive Stable Sort(적응형 안정 정렬)이다.

# 시간복잡도: 최악 O(n log n), 최고 O(n)

# 그렇다면, 왜 파이썬의 Timsort에서는 C++과 달리 Quick Sort를 쓰지 않을까?
# 그 이유는 파이썬 배열의 요소들은 객체 그 자체가 아니라 주소값이기 때문이다.
# 그래서주소값들을 계속 무작위로 swap하며 비교하므로
# CPU의 캐시 메모리를 전혀 활용하지 못해 성능이 떨어진다.

#######################################################################################

# Binary Search
# 정답이 있을 수 없는 절반을 매번 버린다.
# 시간복잡도: O(log n)
# 공간복잡도: O(1)

nums = [1, 3, 5, 7, 9, 11]
target = 9

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# 실전에서 중요한 것은
# 첫 번째로 target 이상인 위치
# 마지막으로 target 이하인 위치
# target이 처음 등장하는 위치
# target이 마지막으로 등장하는 위치
# 조건을 처음 만족하는 값
# 이게 바로 Boundary Binary Search다.

#######################################################################################

# Lower Bound
# target 이상인 값 중 가장 왼쪽에 있는 값의 인덱스를 반환한다.

nums = [1, 2, 2, 2, 5, 8]
target = 2

def lower_bound(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

# Lower Bound에서 왜 right = mid인가?
# nums[mid] >= target인 경우, mid가 답일 수도 있다.
# 우리가 원하는 건 첫 번째 위치이기 때문에
# mid를 버리지 않고 right를 mid로 옮겨서 범위를 좁힌다.
# 즉, mid가 첫 번째 위치일 경우, right = mid - 1 하게 된다면
# mid를 버리게 되어 답을 놓치게 된다.

#######################################################################################

# Upper Bound
# target 초과인 값 중 가장 왼쪽에 있는 값의 인덱스를 반환한다.

nums = [1, 2, 2, 2, 5, 8]
target = 2

def upper_bound(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left

# Lower Bound와 Upper Bound의 차이는
# if nums[mid] < target: / if nums[mid] <= target: 의 차이이다.

# 중복 개수의 경우
# count = upper_bound(nums, target) - lower_bound(nums, target)
# 로 빠르게 구할 수 있다.

from bisect import bisect_left, bisect_right

nums = [1, 2, 2, 2, 5, 8]

print(bisect_left(nums, 2))     # lower bound
print(bisect_right(nums, 2))    # upper bound

# 그러나 nums.insert(index, x) 자체는
# list 중간 삽입이라 O(n)이다.
# bisect으로 index를 찾는 건 O(log n)이지만
# 실제 삽입까지 포함하면 O(n)이다.

#########################################################################################

# Binary Search on Answer
# Binary Search를 배열 검색 뿐만이 아니라
# 정답의 범위 자체를 이분 탐색하여 최적의 값을 찾을 수 있다.

# 예를 들어 [7, 2, 5, 10, 8] 이라는 배열이 있고
# 각 그룹의 합을 x 이하로 유지하면서 2개 이하의 그룹으로 나눌 수 있는지
# 이를 검사할 수 있다.
# 즉, x가 가능한지 여부를 판단하는 함수가 존재한다.
# 쉽게 말해 False False ... True True라는
# monotonicity(단조성)이 생긴다.

# 제곱근 예제: x² >= n 을 만족하는 가장 작은 정수 x를 찾는 문제
n = 30

def ceil_sqrt(n):
    left = 0
    right = n

    while left < right:
        mid = (left + right) // 2

        if mid * mid >= n:
            right = mid
        else:
            left = mid + 1
    
    return left

# 핵심 사고
# 1. 정답의 범위는? left ~ right
# 2. 어떤 후보 x가 가능한 지 검사할 수 있는가?
# 3. feasible 결과가 단조적인가? True True ... False False
# 4. 첫 True / 마지막 True를 Binary Search로 찾는다.

# 대표 문제 패턴
# 최소 가능한 최대값
# 최대 가능한 최소값
# 최소 시간
# 최소 용량
# 최대 거리
# 몇 개 이하로 만들 수 있는가
# 주어진 시간 안에 가능한가

#########################################################################################

#
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

#
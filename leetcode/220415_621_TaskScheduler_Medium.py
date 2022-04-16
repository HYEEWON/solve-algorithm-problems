# Array, Hash Table, Greedy, Heap, Counting, Sorting

from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        answer = 0
        cnt = Counter(tasks)

        h = list(zip([i * j for i, j in zip([-1 for k in range(len(cnt.values()))], list(cnt.values()))], cnt.keys()))
        heapq.heapify(h)

        total = len(tasks)
        while total > 0:
            tmp_cnt, tmp_pop = 0, []
            while tmp_cnt < (n + 1) and h:
                tmp_pop.append(heapq.heappop(h))
                cnt[tmp_pop[-1][1]] -= 1
                total -= 1
                tmp_cnt += 1
                answer += 1

            for ch in tmp_pop:
                if cnt[ch[1]] > 0:
                    heapq.heappush(h, (-cnt[ch[1]], ch[1]))

            while tmp_cnt < n + 1 and total > 0:
                answer += 1
                tmp_cnt += 1
        return answer

    # 참고 링크
    # https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        tasks_count = list(Counter(tasks).values())
        max_count = max(tasks_count)  # 가장 많이 진행되는 작업의 작업 수
        max_count_tasks = tasks_count.count(max_count)  # 가장 많이 진행되는 작업의 수
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)

    # 참고 링크
    # https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation
    def leastInterval3(self, tasks, n):
        curr_time, h = 0, []
        for k, v in Counter(tasks).items():
            heapq.heappush(h, (-1 * v, k))
        while h:
            tmp_cnt, tmp_pop = 0, []
            while tmp_cnt <= n:
                curr_time += 1
                if h:
                    x, y = heapq.heappop(h)
                    if x != -1:
                        tmp_pop.append((x + 1, y))
                # tmp_pop이 없다는 것은 더이상 추가될 것이 없다는 의미 = 프로그램 종료
                if not h and not tmp_pop:
                    break
                else:
                    tmp_cnt += 1
            for item in tmp_pop:
                heapq.heappush(h, item)
        return curr_time
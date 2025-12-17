from collections import defaultdict
from typing import List, Dict, Tuple

class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int
    ) -> int:

        # Build adjacency list (0-based indexing)
        tree = defaultdict(list)
        for boss, employee in hierarchy:
            tree[boss - 1].append(employee - 1)

        # Memo dictionary:
        # key   -> (employee, parent_bought)
        # value -> dict: spent_money -> max_profit
        memo: Dict[Tuple[int, bool], Dict[int, int]] = {}

        def dfs(employee: int, parent_bought: bool) -> Dict[int, int]:
            """
            Returns a dictionary:
            spent_money -> maximum profit achievable
            from the subtree rooted at `employee`
            """

            # Check memo
            if (employee, parent_bought) in memo:
                return memo[(employee, parent_bought)]

            # Determine cost to buy stock of current employee
            buy_cost = present[employee] // 2 if parent_bought else present[employee]
            buy_profit = future[employee] - buy_cost

            # Case 1: Buy current employee's stock
            buy_dp = {}
            if buy_cost <= budget:
                buy_dp[buy_cost] = buy_profit

            # Case 2: Skip current employee's stock
            skip_dp = {0: 0}

            # Process all children
            for child in tree[employee]:

                # If current employee is bought → child gets discount
                child_dp_with_discount = dfs(child, True)

                # If current employee is skipped → child has no discount
                child_dp_no_discount = dfs(child, False)

                # Merge child DP into buy_dp
                new_buy_dp = {}
                for spent_so_far, profit_so_far in buy_dp.items():
                    for child_spent, child_profit in child_dp_with_discount.items():
                        total_spent = spent_so_far + child_spent
                        if total_spent <= budget:
                            total_profit = profit_so_far + child_profit
                            new_buy_dp[total_spent] = max(
                                new_buy_dp.get(total_spent, float('-inf')),
                                total_profit
                            )
                buy_dp = new_buy_dp

                # Merge child DP into skip_dp
                new_skip_dp = {}
                for spent_so_far, profit_so_far in skip_dp.items():
                    for child_spent, child_profit in child_dp_no_discount.items():
                        total_spent = spent_so_far + child_spent
                        if total_spent <= budget:
                            total_profit = profit_so_far + child_profit
                            new_skip_dp[total_spent] = max(
                                new_skip_dp.get(total_spent, float('-inf')),
                                total_profit
                            )
                skip_dp = new_skip_dp

            # Merge buy and skip results
            result_dp = {}

            for spent, profit in buy_dp.items():
                result_dp[spent] = max(result_dp.get(spent, float('-inf')), profit)

            for spent, profit in skip_dp.items():
                result_dp[spent] = max(result_dp.get(spent, float('-inf')), profit)

            # Store in memo
            memo[(employee, parent_bought)] = result_dp
            return result_dp

        # Start DFS from CEO (employee 0), with no discount
        final_dp = dfs(0, False)

        # Answer is the maximum profit among all valid budgets
        return max(final_dp.values()) if final_dp else 0

"""
⏱ Complexity (unchanged, correct)
	•	Time: O(n × k²)
	•	Space: O(n × k)

Where k ≤ budget.

⸻

🎯 One-liner for interviews

I used tree DP with manual memoization where each node returns a cost-to-profit map, allowing safe merging under budget constraints while respecting discount dependencies.

"""



# Second Approach


class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int
    ) -> int:

        # Build tree (0-based indexing)
        # tree[u] = list of direct subordinates of u
        tree = [[] for _ in range(n)]
        for boss, emp in hierarchy:
            tree[boss - 1].append(emp - 1)

        # dp[u][p][b]
        # u : current employee
        # p : whether parent was bought (0 = no, 1 = yes)
        # b : money spent
        # value = maximum profit
        dp = [[[0] * (budget + 1) for _ in range(2)] for _ in range(n)]

        def merge(dp1, dp2):
            """
            Merge two knapsack DP arrays.
            dp1[i] + dp2[j] -> dp[i + j]
            """
            result = [-10**9] * (budget + 1)
            for spent1 in range(budget + 1):
                if dp1[spent1] < 0:
                    continue
                for spent2 in range(budget - spent1 + 1):
                    result[spent1 + spent2] = max(
                        result[spent1 + spent2],
                        dp1[spent1] + dp2[spent2]
                    )
            return result

        def dfs(u):
            # First process all children
            for v in tree[u]:
                dfs(v)

            # Case 1: Skip current employee
            # skip[b] = profit if we skip u and spend b money
            skip = [0] * (budget + 1)

            # base[b] = profit from children assuming current employee IS bought
            base = [0] * (budget + 1)

            for v in tree[u]:
                # If we skip u, children get no discount
                skip = merge(skip, dp[v][0])

                # If we buy u, children get discount
                base = merge(base, dp[v][1])

            # Compute dp for both parent states
            for parent_bought in (0, 1):

                # Cost to buy current employee
                price = present[u] // 2 if parent_bought else present[u]
                profit = future[u] - price

                # take[b] = profit if we buy u with total spend b
                take = [-10**9] * (budget + 1)

                if price <= budget:
                    for b in range(price, budget + 1):
                        take[b] = base[b - price] + profit

                # dp[u][parent_bought][b] =
                # max(skip u, buy u)
                for b in range(budget + 1):
                    dp[u][parent_bought][b] = max(skip[b], take[b])

        # Start DFS from CEO (employee 0)
        dfs(0)

        # Answer is maximum profit with CEO not discounted
        return max(dp[0][0])

"""
DP Meaning

dp[u][p][b]

	•	u → current employee
	•	p → did parent buy stock?
	•	0 = no discount
	•	1 = discount applies
	•	b → money spent
	•	value → max profit

⸻

Two choices at every employee

1️⃣ Skip employee
	•	Spend nothing
	•	Children get no discount
	•	Combine children freely

2️⃣ Buy employee
	•	Spend present[u] (or half if discounted)
	•	Gain future[u] - cost
	•	Children get discount

⸻

Why merge() is needed

Employees can have multiple children, and you may:
	•	Buy stocks from multiple subtrees
	•	As long as budget allows

This is exactly knapsack merging.

⸻

⏱ Complexity
	•	Time: O(n × budget²)
	•	Space: O(n × budget)

Budget ≤ 160 → this passes comfortably.

⸻

🎯 Interview-Level Summary

This is a tree knapsack DP where each node has two states (parent bought or not), and children DP tables are merged using knapsack convolution under a global budget constraint.

⸻

"""



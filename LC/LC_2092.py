'''
🧠 Short Explanation (Conceptual)
	•	People 0 and firstPerson know the secret initially.
	•	Meetings are grouped by time.
	•	For each time:
	•	Build a graph of people meeting at that time.
	•	If any person in a connected component knows the secret, it spreads to the entire component.
	•	DFS is used to spread the secret only within valid components.
	•	Final set contains all people who learned the secret.

⸻

⏱️ Time Complexity (TC)
	•	Sorting meetings: O(M log M)
where M = number of meetings
	•	Building graphs + DFS across all meetings: O(M + N)

✅ Overall:

O(M \log M)

⸻

💾 Space Complexity (SC)
	•	Graph storage per time: O(M)
	•	Visited sets and recursion stack: O(N)
	•	Secret set: O(N)

✅ Overall:

{O(N + M)


'''


from collections import defaultdict
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        # Set to store people who currently know the secret
        people_with_secret = {0, firstPerson}

        # Sort meetings by time (and then by people just for consistency)
        meetings.sort(key=lambda x: (x[2], x[0], x[1]))

        # Group meetings by time
        meetings_by_time = defaultdict(list)
        for person1, person2, time in meetings:
            meetings_by_time[time].append((person1, person2))

        # DFS to spread secret within a connected component
        def dfs(current_person, graph, visited):
            # If already visited, stop
            if current_person in visited:
                return

            # Mark as visited and add to secret holders
            visited.add(current_person)
            people_with_secret.add(current_person)

            # Visit all connected people
            for neighbor in graph[current_person]:
                dfs(neighbor, graph, visited)

        # Process meetings time by time
        for time in meetings_by_time:

            # Graph for meetings happening at the same time
            same_time_graph = defaultdict(list)

            # People who can start spreading the secret at this time
            starting_people = []

            # Build graph and find who already knows the secret
            for person1, person2 in meetings_by_time[time]:
                same_time_graph[person1].append(person2)
                same_time_graph[person2].append(person1)

                if person1 in people_with_secret:
                    starting_people.append(person1)
                if person2 in people_with_secret:
                    starting_people.append(person2)

            # Track visited people for this time frame
            visited = set()

            # Run DFS from each valid starting person
            for person in starting_people:
                if person not in visited:
                    dfs(person, same_time_graph, visited)

        return list(people_with_secret)
    



    # Same but with less code

'''
🧠 Approach (High-Level)
	1.	Initially, only person 0 and firstPerson know the secret.
	2.	Meetings are processed in increasing order of time.
	3.	All meetings happening at the same time are treated together.
	4.	For each time:
	•	Build a graph of people meeting at that time.
	•	If any person in a connected component knows the secret, the secret spreads to the entire component.
	5.	DFS is used to spread the secret inside valid components.
	6.	Finally, return all people who know the secret.

⸻

💭 Thought Process (Why this works)
	•	The secret cannot travel backward in time, so meetings must be processed in time order.
	•	Meetings at the same time allow instantaneous sharing, so they behave like a graph where the secret can spread freely within a connected component.
	•	However, the secret should spread only in components that already contain someone who knows the secret.
	•	DFS ensures that the secret spreads to all reachable people within that component.

⸻

🧩 Logic Used
	•	Sorting → ensures correct time order
	•	HashSet (set) → fast lookup for who knows the secret
	•	Adjacency List Graph → represent same-time meetings
	•	DFS (stack-based) → spread the secret inside connected components
	•	Visited Set → prevent revisiting nodes in the same time frame

⸻

⏱️ Time Complexity
	•	Sorting meetings: O(M log M)
	•	Graph building + DFS over all meetings: O(M + N)

✅ Overall:

O(M \log M)

⸻

💾 Space Complexity
	•	Graph storage: O(M)
	•	Visited set + secret set: O(N)

✅ Overall:

O(N + M)

    '''


from collections import defaultdict
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        # Set to keep track of people who know the secret
        people_with_secret = {0, firstPerson}

        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        # Group all meetings by their time
        meetings_by_time = defaultdict(list)
        for person1, person2, time in meetings:
            meetings_by_time[time].append((person1, person2))

        # DFS function to spread the secret inside a connected component
        def dfs(start_person, graph, visited):
            stack = [start_person]

            while stack:
                current_person = stack.pop()

                if current_person in visited:
                    continue

                visited.add(current_person)
                people_with_secret.add(current_person)

                # Visit all connected people
                for neighbor in graph[current_person]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        # Process meetings time by time
        for time in meetings_by_time:

            # Graph for people meeting at the same time
            same_time_graph = defaultdict(list)

            # Build graph for current time
            for person1, person2 in meetings_by_time[time]:
                same_time_graph[person1].append(person2)
                same_time_graph[person2].append(person1)

            visited = set()

            # People who already know the secret can start spreading it
            starting_people = [person for person in same_time_graph
                               if person in people_with_secret]

            # Spread the secret using DFS from valid starters
            for starter in starting_people:
                if starter not in visited:
                    dfs(starter, same_time_graph, visited)

        return list(people_with_secret)
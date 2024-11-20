from collections import defaultdict, deque

def solution(n, wires):
    def bfs(start, graph, visited):
        queue = deque([start])
        visited[start] = True
        count = 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
        return count

    # Create adjacency list for the graph
    graph = defaultdict(list)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    min_difference = float('inf')

    # Try removing each wire and calculate the difference
    for a, b in wires:
        # Remove the wire
        graph[a].remove(b)
        graph[b].remove(a)

        visited = [False] * (n + 1)

        # Count nodes in the first connected component
        count = bfs(a, graph, visited)
        difference = abs(n - 2 * count)

        # Update the minimum difference
        min_difference = min(min_difference, difference)

        # Restore the wire
        graph[a].append(b)
        graph[b].append(a)

    return min_difference


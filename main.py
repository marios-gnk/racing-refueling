import heapq
import sys


def nearest_station_distances(graph, stations):
    """Find every city's distance to its nearest station using Dijkstra."""
    d = {city: float('inf') for city in graph}
    queue = []
    for station in stations:
        d[station] = 0
        queue.append((0, station))
    heapq.heapify(queue)

    while queue:
        distance, city = heapq.heappop(queue)
        if distance != d[city]:
            continue  # Ignore entries left over from an earlier improvement.

        for neighbor, length in graph[city]:
            new_distance = distance + length
            if new_distance < d[neighbor]:
                d[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return d


def main():
    read_line = sys.stdin.buffer.readline
    N, M, K, L, B = map(int, read_line().split())

    graph = {city: [] for city in range(1, N + 1)}

    for _ in range(M):
        u, v, length = map(int, read_line().split())
        graph[u].append((v, length))
        graph[v].append((u, length))

    route = [int(read_line()) for _ in range(K)]
    stations = [int(read_line()) for _ in range(B)]

    # The driver must follow the fixed route.
    driving_time = 0
    for city, next_city in zip(route, route[1:]):
        for neighbor, length in graph[city]:
            if neighbor == next_city:
                driving_time += length
                break

    d = nearest_station_distances(graph, stations)
    # Choose the L cheapest intermediate cities for refueling.
    waiting_times = sorted(d[city] for city in route[1:-1])
    print(driving_time + sum(waiting_times[:L]))

if __name__ == "__main__":
    main()

def main():
    N, M, K, L, B = map(int, input().split())

    graph = {city: [] for city in range(1, N + 1)}

    for _ in range(M):
        u, v, length = map(int, input().split())
        graph[u].append((v, length))
        graph[v].append((u, length))

    route = [int(input()) for _ in range(K)]
    stations = [int(input()) for _ in range(B)]
    
    print(graph)
    print(route)
    print(stations)


if __name__ == "__main__":
    main()

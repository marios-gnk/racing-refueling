# Racing and Refueling

Python solution to the **Foundations of Computer Science** programming assignment. The program computes the minimum race completion time along a fixed route with at least L refueling stops.

## Algorithm

1. Store the bidirectional roads in a weighted adjacency list and sum the road lengths along the fixed racing route.
2. Run **multi-source Dijkstra**, initializing all gas stations with distance zero in a min-heap. This computes each city's shortest distance to its nearest station in a single run. At a speed of 1 km/s, this distance equals the waiting time for refueling.
3. Sort the waiting times for the intermediate route cities and add the L smallest to the driving time. The starting and finishing cities are excluded.

The driving time is fixed, and refueling costs are independent and nonnegative. Therefore, choosing the L cheapest eligible stops minimizes the total time; extra stops cannot improve it.

## Complexity

Let N be the number of cities, M the number of roads, and K the number of route cities. With unique roads, multi-source Dijkstra takes **O((N + M) log N)** time, and sorting the waiting times takes **O(K log K)**. Since K ≤ N, the overall time complexity is **O((N + M) log N)**. Space complexity is **O(N + M)**, including the graph and heap.

## Usage

Requires Python 3 and only its standard library. From the repository directory:

```bash
python3 main.py < tests/input1.txt
```

The program prints one integer: the minimum total time in seconds.

## Results

- All **10 provided test cases** matched their expected outputs. Input files and corresponding expected output files are stored in `tests/`.

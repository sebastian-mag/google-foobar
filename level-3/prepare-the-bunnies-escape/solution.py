def solution(map_):
    w = len(map_[0])  # Width of the map
    h = len(map_)     # Height of the map

    if 2 <= w <= 20 >= h >= 2:
        # Initialize two maps to store path lengths
        map_a = [[None for _ in range(w)] for _ in range(h)]
        map_b = [[None for _ in range(w)] for _ in range(h)]

        # Calculate shortest path lengths from two different starting points
        for m in [(0, 0, map_a), (h-1, w-1, map_b)]:
            x, y, current_map = m
            current_map[x][y] = 1
            node = [(x, y)]

            while len(node) > 0:
                x, y = node.pop(0)

                # Explore neighboring nodes
                for direction in [(1, 0),  (0, 1), (-1, 0), (0, -1)]:
                    next_x, next_y = x + direction[0], y + direction[1]

                    # Check if neighboring node is within bounds
                    if 0 <= next_x < h and w > next_y >= 0:
                        if current_map[next_x][next_y] is None:
                            current_map[next_x][next_y] = current_map[x][y] + 1

                            # Continue to the next iteration if the node is a wall (1)
                            if map_[next_x][next_y] == 1:
                                continue
                            node.append((next_x, next_y))

        # Find the minimum path length by considering both maps
        path_lengths = []
        for x in range(h):
            for y in range(w):
                if map_a[x][y] and map_b[x][y]:
                    path_lengths.append(map_a[x][y] + map_b[x][y] - 1)

        return min(path_lengths)


print(solution([[0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 1, 0]]))
# output: 7

print(solution([[0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]]))
# output: 11

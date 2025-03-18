import numpy as np
from collections import deque

with open("./data/input_12.txt") as f:
    plot: np.ndarray = np.array([list(line.strip()) for line in f])


def count_sides(grid_points):
    """
    Counts the number of distinct sides (reduced by Manhattan collinearity)
    in a grid-based shape.

    Args:
        grid_points: List of tuples representing filled grid points (e.g., [(x1, y1), (x2, y2), ...])

    Returns:
        int: Total number of sides in the shape.
    """
    from collections import defaultdict

    # Track edges for each orientation
    horizontal_edges = defaultdict(set)
    vertical_edges = defaultdict(set)

    # Collect all edges
    for x, y in grid_points:
        # Horizontal edges
        horizontal_edges[y].add((x, x + 1))
        horizontal_edges[y + 1].add((x, x + 1))
        # Vertical edges
        vertical_edges[x].add((y, y + 1))
        vertical_edges[x + 1].add((y, y + 1))

    def reduce_edges(edges):
        """
        Reduces consecutive edges along the same plane into a single segment.
        """
        total_sides = 0
        for coord, segments in edges.items():
            # Sort and reduce segments
            sorted_segments = sorted(segments)
            merged_segments = []
            current_start, current_end = sorted_segments[0]

            for start, end in sorted_segments[1:]:
                if start == current_end:  # Extend the current segment
                    current_end = end
                else:  # Save the current segment and start a new one
                    merged_segments.append((current_start, current_end))
                    current_start, current_end = start, end

            # Add the last segment
            merged_segments.append((current_start, current_end))
            total_sides += len(merged_segments)
        return total_sides

    # Reduce horizontal and vertical edges
    horizontal_sides = reduce_edges(horizontal_edges)
    vertical_sides = reduce_edges(vertical_edges)

    # Total sides
    return horizontal_sides + vertical_sides


def bfs(matrix, visited, i, j, value, directions):
    queue = deque([(i, j)])
    visited[i][j] = True
    region_cells = [(i, j)]  # Start with the initial cell
    perimeter = 0  # Initialize perimeter count
    sides = 0  # Initialize sides count

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the neighbor is outside the matrix or has a different value
            if not (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0])) or matrix[nx][ny] != value:
                perimeter += 1  # This side contributes to the perimeter
            elif not visited[nx][ny] and matrix[nx][ny] == value:
                visited[nx][ny] = True
                queue.append((nx, ny))
                region_cells.append((nx, ny))  # Add cell to the region
    #print(count_sides(region_cells),"::",region_cells)
    return region_cells, perimeter, count_sides(region_cells)


def find_connected_areas(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                region_value = matrix[i][j]
                # Perform BFS to find all connected cells with the same value, calculate perimeter and sides
                region_cells, perimeter, sides = bfs(matrix, visited, i, j, region_value, directions)
                regions.append({
                    'region': matrix[region_cells[0]],
                    'cells': region_cells,
                    'area': len(region_cells),
                    'perimeter': perimeter,
                    'sides': sides
                })  # Store region's cells, perimeter, and sides
    return regions


print(sum(region['area']*region['perimeter'] for region in find_connected_areas(plot)))
print(sum(region['area']*region['sides'] for region in find_connected_areas(plot)))

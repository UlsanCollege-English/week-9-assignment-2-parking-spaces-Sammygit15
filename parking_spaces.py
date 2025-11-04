import heapq

def min_parking_spots(intervals):
    """
    Given a list of (start, end) times, return the minimum number of parking spots
    so that no car waits. If a car leaves at time t and another arrives at time t,
    the same spot can be reused.

    Example:
    >>> min_parking_spots([(1, 4), (2, 5), (7, 8)])
    2
    """

    if not intervals:
        return 0

    # Step 1: Sort by start time
    intervals.sort(key=lambda x: x[0])

    heap = []  # min-heap for end times
    max_spots = 0

    # Step 2: Process each car interval
    for start, end in intervals:
        # Free all spots where the car has already left (end <= start)
        while heap and heap[0] <= start:
            heapq.heappop(heap)

        # Assign this car a spot (new or reused)
        heapq.heappush(heap, end)

        # Track the maximum number of spots used at once
        max_spots = max(max_spots, len(heap))

    return max_spots

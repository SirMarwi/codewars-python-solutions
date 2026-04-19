def queue_time(customer, n):
    tilts = {i : 0 for i in range(1, n + 1)}

    for person in customer:
        empty_tilt = min(tilts, key=tilts.get)
        tilts[empty_tilt] += person

    return max(tilts.values())

print(queue_time([5,3,4], 2))


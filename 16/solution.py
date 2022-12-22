import re

# find the shortest path from one valve to another
def bfs(src, dest):
    paths = [[src]]

    while len(paths):
        path = paths.pop(0)
        for d in tunnels[path[-1]]:
            if d in path:
                continue

            np = path + [d]
            if d == dest:
                return np

            paths.append(np)


# Create graph consisting of all valves with non-zero flow rates and the
# distances between them
def transform_graph():
    graph = {}
    for n1 in set(valves.keys()) | set(['AA']):
        graph[n1] = {}
        for n2 in valves:
            if n1 == n2:
                continue
            path = bfs(n1, n2)
            graph[n1][n2] = len(path) - 1

    return graph


valves = {}
tunnels = {}
with open('input') as f:
    for l in f:
        match = re.match(
            'Valve (\w+) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (\w+(, \w+)*)',
            l
        )

        v, fr, links, _ = match.groups()
        if int(fr):
            valves[v] = int(fr)
        tunnels[v] = links.split(', ')

graph = transform_graph()

## Part 1

# key: (location, inactive valves, time left)
# value: maximum amount of flow that can be added between now and the end of the
# available time
memo = {}

def subprob_1(location, inactive, time_left):
    if time_left <= 0 or len(inactive) == 0:
        return 0

    key = (location, inactive, time_left)

    if key in memo:
        return memo[key]

    best = 0

    if location in inactive:
        best = valves[location] * (time_left - 1) + subprob_1(
            location, inactive - frozenset([location]), time_left - 1)

    for dest in inactive:
        if dest != location:
            ttd = graph[location][dest]
            best = max(best, subprob_1(dest, inactive, time_left - ttd))

    memo[key] = best
    return best

print(subprob_1('AA', frozenset(valves.keys()), 30))


## Part 2
memo = {}

# actors: tuple of (location, time_left) tuples representing all possible movers
# space/time: K * M**2 * S2(M, 2)
def subprob_2(actors, inactive):
    if all([a[1] <= 0 for a in actors]) or len(inactive) == 0:
        return 0

    key = hash((actors, inactive))

    if key in memo:
        return memo[key]

    best = 0

    # move the actor with the most time left
    location, time_left = sorted(actors, key=lambda a: a[1])[-1]
    others = list(actors)
    others.remove((location, time_left))

    for dest in inactive:
        if dest != location:
            ttd = graph[location][dest] + 1
            flow = valves[dest] * (time_left - ttd)
            new_actors = tuple(sorted(others + [(dest, time_left - ttd)]))
            new_inactive = inactive - frozenset([dest])

            best = max(best, flow + subprob_2(new_actors, new_inactive))

    memo[key] = best
    return best

print(subprob_2((('AA', 26), ('AA', 26)), frozenset(valves.keys())))

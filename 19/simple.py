import re
import multiprocessing as mp

TYPES = [
    'ore',
    'clay',
    'obsidian',
    'geode'
]

class RecipeSolver(object):
    def __init__(self, recipe):
        self.recipe = recipe
        self.memo = {}
        self.best_yet = 0

    def max_geodes(self, resources, robots, time_left):
        max_obs = resources[2]
        obs_bots = robots[2]
        max_geodes = resources[-1]
        geode_cost = self.recipe['geode']['obsidian']
        geode_bots = robots[-1]

        for t in range(time_left):
            # max obsidian we could have at this point in time
            max_obs += obs_bots * time_left
            max_geodes += geode_bots

            if max_obs > geode_cost:
                max_obs -= geode_cost
                geode_bots += 1
            else:
                obs_bots += 1

        return max_geodes

    def subprob(self, resources, robots, time_left):
        if time_left == 0:
            self.best_yet = max(self.best_yet, resources[TYPES.index('geode')])
            return resources[TYPES.index('geode')]

        key = hash((resources, robots, time_left))
        if key in self.memo:
            return self.memo[key]

        # check if we can possibly beat the best score so far using heuristic
        if self.max_geodes(resources, robots, time_left) <= self.best_yet:
            return 0

        # if we can build a geode bot, do that
        reqs = self.recipe['geode']
        if resources[0] > reqs['ore'] and \
                resources[2] > reqs['obsidian']:

            new_res = list(resources)
            for j in range(len(TYPES)):
                new_res[j] -= reqs.get(TYPES[j], 0)
                new_res[j] += robots[j]

            new_robots = robots[:3] + (robots[3] + 1,)

            return self.subprob(tuple(new_res), new_robots, time_left-1)

        # otherwise, start by checking the case where we don't build anything
        new_res = list(resources)
        for i in range(len(TYPES)):
            new_res[i] += robots[i]

        best = self.subprob(tuple(new_res), robots, time_left - 1)

        # if there's only one tick left, no more bot building matters
        # if there are two ticks left, only geode bots matter
        if time_left <= 2:
            return best

        # finally, try building other robots
        for i in range(len(robots)):
            reqs = self.recipe[TYPES[i]]
            # if we can build this kind of robot, do it and create a new branch
            if all(resources[TYPES.index(k)] >= v for k, v in reqs.items()):
                new_res = list(resources)
                # remove resources needed for the new bot, then add resources
                # gathered by the existing bots
                for j in range(len(TYPES)):
                    new_res[j] -= reqs.get(TYPES[j], 0)
                    new_res[j] += robots[j]

                new_robots = [robots[j] + 1 if j == i else robots[j] for j in
                              range(len(robots))]
                best = max(best, self.subprob(tuple(new_res), tuple(new_robots),
                                              time_left - 1))

        self.memo[key] = best
        return best


def solve_1(recipe):
    solver = RecipeSolver(recipe)
    return solver.subprob((0,0,0,0), (1,0,0,0), 24)


def solve_2(recipe):
    solver = RecipeSolver(recipe)
    return solver.subprob((0,0,0,0), (1,0,0,0), 32)


if __name__ == '__main__':
    recipes = []

    with open('input') as f:
        for l in f:
            matches = re.findall(
                'Each (\w+) robot costs (\d+) ore( and (\d+) (clay|obsidian))?\.',
                l
            )

            recipe = {}
            for m in matches:
                recipe[m[0]] = {'ore': int(m[1])}
                if len(m[2]):
                    recipe[m[0]][m[4]] = int(m[3])

            recipes.append(recipe)

    mp.set_start_method('fork')
    p = mp.Pool(4)

    # part 1
    results = p.map(solve_1, recipes)
    result = 0
    for i, r in enumerate(results):
        print('Recipe %d: %d geodes' % (i + 1, r))
        result += (i + 1) * r

    print(result)

    # part 2
    r1, r2, r3 = p.map(solve_2, recipes[:3])
    print(r1 * r2 * r3)

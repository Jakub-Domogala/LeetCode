# Time Complexity:   O(nlogn)
# Memory Complexity: O(n)

from typing import List
from heapq import heappop, heappush

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        prev_pos = 0
        curr_fuel = startFuel
        refuel_queue = []
        stations += [[target, 0]]
        refuel_count = 0
        for curr_pos, fuel_amm in stations:
            curr_fuel -= curr_pos - prev_pos
            while curr_fuel < 0:
                if len(refuel_queue) == 0:
                    return -1
                curr_fuel -= heappop(refuel_queue)
                refuel_count += 1
            heappush(refuel_queue, -fuel_amm)
            prev_pos = curr_pos
        return refuel_count

    # def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int: # time O(n^2), space O(n^2) for n = len(stations)
    #     def pprint(a):
    #         for r in a:
    #             print(r)
    #         print()
    #     def clear_far_stations(stations, target):
    #         i = len(stations) - 1
    #         while i >= 0 and stations[i][0] >= target:
    #             i -= 1
    #         return stations[:i+1]
    #     if target <= startFuel:
    #         return 0
    #     stations = clear_far_stations(stations, target)
    #     stops = [0] + [s[0] for s in stations] + [target]

    #     n = len(stations)
    #     dynamic = [[-1 for i in range(n + 2)] for j in range(n+1)]
    #     for i in range(n+2):
    #         dynamic[0][i] = startFuel - stops[i]
    #     pprint(dynamic)
    #     for refuels_amm in range(1, n+1):
    #         for stop_idx in range(refuels_amm, n+2):
    #             best_score = -1
    #             dynamic[refuels_amm][stop_idx] = max(
    #                 dynamic[refuels_amm][stop_idx-1] - (stops[stop_idx] - stops[stop_idx-1]) if dynamic[refuels_amm][stop_idx-1] >= 0 else -1, # from last station to here but don't refuel here
    #                 dynamic[refuels_amm-1][stop_idx-1] - (stops[stop_idx] - stops[stop_idx-1]) + stations[stop_idx-1][1] if stop_idx <= n and dynamic[refuels_amm-1][stop_idx-1] >= 0 and stops[stop_idx] - stops[stop_idx-1] <= dynamic[refuels_amm-1][stop_idx-1] else -1) # from last station to here but refuel here
    #             if dynamic[refuels_amm][stop_idx] <= 0:
    #                 break
    #     pprint(dynamic)
    #     for i in range(n+1):
    #         if dynamic[i][n+1] >= 0:
    #             return i
    #     return -1


# target = 100
# startFuel = 1
# stations = [[10,100]]
# result = Solution().minRefuelStops(target, startFuel, stations)
# print(result, -1)
# target = 100
# startFuel = 50
# stations = [[25,50],[50,25]]
# result = Solution().minRefuelStops(target, startFuel, stations)
# print(result, 1)
# target = 10
# startFuel = 2
# stations = [[1,5],[2,6],[9,2]]
# result = Solution().minRefuelStops(target, startFuel, stations)
# print(result, 2)
# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40],[100,10],[110,10]]
# result = Solution().minRefuelStops(target, startFuel, stations)
# print(result, 2)
# target = 1000
# startFuel = 299
# stations = [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]
# result = Solution().minRefuelStops(target, startFuel, stations)
# print(result, 4)

from pprint import pprint


ans = [[1,2,3,4,5,1],[5,6,8,7,6,2],[4,7,9,9,8,3],[3,8,9,9,7,4],[2,6,7,8,6,5],[1,5,4,3,2,1]]

ans2 = [list(x) for x in zip(*ans)]

pprint(ans2)
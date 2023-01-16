lines = int(input())
longest_intersection = set()
max_len = 0

for _ in range(lines):
    range1, range2 = [r.split(',') for r in input().split('-')]
    set1 = {n for n in range(int(range1[0]), int(range1[1]) + 1)}
    set2 = {n for n in range(int(range2[0]), int(range2[1]) + 1)}
    intersection = set1 & set2
    if len(intersection) > max_len:
        max_len = len(intersection)
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {max_len}")

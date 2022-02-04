# Find runner-up from given list
#d21cs109 krish pandya
n = int(input())
score = map(int, input().split())
print(sorted(list(set(score)))[-2])

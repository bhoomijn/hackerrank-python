
# runner_up.py

n = int(input())                      # number of participants
scores = list(map(int, input().split()))  # scores list

# duplicates remove karo
unique_scores = list(set(scores))

# ascending sort
unique_scores.sort()

# second last element hi runner-up hoga
print(unique_scores[-2])

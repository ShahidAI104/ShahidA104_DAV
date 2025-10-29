#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

players = ['A', 'B', 'C', 'D', 'E']
points = np.array([
    [20, 15, 25, 18, 17],
    [22, 18, 20, 25, 17],
    [15, 12, 28, 10, 13],
    [18, 20, 22, 15, 13],
    [25, 25, 30, 20, 10],
    [20, 22, 18, 30, 10]
])

total_points = np.sum(points, axis=0)
top_player_index = np.argmax(total_points)
top_player = players[top_player_index]
top_score = total_points[top_player_index]

print("Total points scored by each player:")
for p, s in zip(players, total_points):
    print(f"{p}: {s}")

print(f"\nPlayer {top_player} scored the most points: {top_score}")

plt.figure(figsize=(8, 5))
bars = plt.bar(players, total_points, color='skyblue')
bars[top_player_index].set_color('orange')

plt.title("Total Points Scored by Each Player")
plt.xlabel("Player")
plt.ylabel("Total Points Scored")
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.legend([bars[top_player_index]], [f'Top Scorer: {top_player} ({top_score})'])
plt.tight_layout()
plt.show()


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
points_scored = np.array([95, 102, 78, 88, 110, 100])
threshold = 100
games_above_threshold = np.sum(points_scored > threshold)
print(f"Number of games scoring above {threshold} points: {games_above_threshold}")
bins = [70, 80, 90, 100, 110, 120]
counts, bin_edges = np.histogram(points_scored, bins=bins)
labels = [f"{int(bin_edges[i])}-{int(bin_edges[i+1])}" for i in range(len(bin_edges)-1)]
plt.figure(figsize=(8, 5))
plt.bar(labels, counts, color='lightgreen')
plt.title("Number of Games Scored in Different Point Ranges")
plt.xlabel("Points Scored Range")
plt.ylabel("Number of Games")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
opponents = ['Team1', 'Team2', 'Team3', 'Team4', 'Team5', 'Team6']
points_scored = np.array([95, 102, 78, 88, 110, 100])
plt.figure(figsize=(8, 5))
bars = plt.bar(opponents, points_scored, color='lightgreen')
plt.title("Points Scored Against Each Opponent")
plt.xlabel("Opponent")
plt.ylabel("Points Scored")
plt.grid(axis='y', linestyle='--', alpha=0.6)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}',
             ha='center', va='bottom')
plt.tight_layout()
plt.show()


# In[ ]:





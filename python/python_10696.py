# In python, find minimum subject to a constraint?
min((idx for idx in indexes if not visited[idx]), key=lambda idx: dist[idx])

# How do we use comprehension here
return {m.name: [func(g, m) for g in groups] for m in messages}

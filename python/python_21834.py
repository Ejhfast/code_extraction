# How do you update the weights in function approximation with reinforcement learning?
self.weights[i] += (self.alpha * theta * Fsa[i])
normalize(self.weights[i],wmin,wmax)

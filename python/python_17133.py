# player heal function not working
def heal(hp, max_hp, healed):
    return min(hp + healed, max_hp)

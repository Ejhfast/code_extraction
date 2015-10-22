# Should properties do nontrivial initialization?
Note 3: Avoid using properties for computationally expensive
    operations; the attribute notation makes the caller believe
    that access is (relatively) cheap.

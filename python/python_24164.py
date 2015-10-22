# Returning all objects in list which have the same attribute as another object?
duplicateNotationMoves = list(filter(lambda move : len(m for m in moves if m.notation == move.notation) &gt; 1, moves))

# Traversal with multiple seed nodes
START n=node(1,2,3,4,5) MATCH (n)-[:associatedMusicalArtist*0..2]-(other) RETURN other

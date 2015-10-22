# App engine query retrieve data with index reference
entries = [x for x in Entry.gql("WHERE amount &gt; 0")]

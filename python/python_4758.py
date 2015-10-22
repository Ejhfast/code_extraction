# The best way to get embedded documents in pymongo?
pages.find({"pages.name", "Main"}); //should load all document that contains pages  collection and at least one item in embedded collection with name 'Main'.

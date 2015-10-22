# Getting proper list of members from pymongo
collection.find( { members : { $exists : true } } );

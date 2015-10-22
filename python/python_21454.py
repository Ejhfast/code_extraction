# Updating collections from collections
db.Coll2.find().forEach(function(c2){
 db.Coll1.update({isbn:c2.isbn},{$set: {category:c2.category}},{multi:true})
});

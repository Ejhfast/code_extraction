# PostGres SQL Update Values based on List of IDs or Primary Keys in another table
update TableB set "Column1"=False where TableB."ID" in (select TableA."ID" from TableA)

# Getting all rows through peewee based on foreign key
User.select().join(Game).where(Game.id == game_id)

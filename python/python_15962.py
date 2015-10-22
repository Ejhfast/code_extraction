# Compare DatetimeField with datetime.now()
game.select().where(game.created_at.between(
    datetime.date.today(),
    datetime.date.today() + datetime.timedelta(days=1))

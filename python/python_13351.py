# Peewee - query ['str' in item]
ni = request.args.get('ni')
Knights.select().where(Knights.who_say ** ni.join(('%', '%')))

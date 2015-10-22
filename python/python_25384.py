# Google Datastore: get_by_id with an ancestor
Entity.query(Query.id==int(self.request.get('entityId')), ancestor=ancestor.key)

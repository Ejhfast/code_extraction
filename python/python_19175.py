# How to return an array response in Google App Engine endpoints
class Response(messages.Message):
    items = messages.StringField(1, repeated=True)

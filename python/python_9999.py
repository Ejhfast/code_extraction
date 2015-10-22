# flask peewee REST api authentication to limit GET
# when instantiating your authentication
api_auth = UserAuth(auth, protected_methods=['GET', 'POST', 'PUT', 'DELETE'])
read_only_auth = UserAuth(auth) # default protected methods are POST/PUT/DELETE

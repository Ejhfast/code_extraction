# Accessing user's current company with django social-auth
current_companies = [position['company']['name'] for position in details['positions']['position'] if position['is-current']=='true']

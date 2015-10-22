# Push an element to an array if it is not present (no duplicates)
self.users.update({"user_id": event['userid']}, {'$addToSet': {'campaigns': UserCampaigns[i]}})

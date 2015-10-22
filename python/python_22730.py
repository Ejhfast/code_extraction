# How to write the function in a more pythonic way?
mapping =dict([c["name"],c["id"]) for c in campaigns]) #save this ... dont recreate it all the time
print mapping[campaign_name] # get the id by campaign name

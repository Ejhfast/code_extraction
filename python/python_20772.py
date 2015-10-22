# Google API and Directory SDK : obtaining the number of groups per domain :HttpError("group")
request = groups_sub.list(domain=domain,fields="nextPageToken,groups(directMembersCount,id,name)")

# reading unopened mail from office365 in python using REST API
GET https://outlook.office365.com/ews/odata/Me/Inbox/Messages?$filter=IsRead eq false HTTP/1.1
Accept: application/json;odata.metadata=full

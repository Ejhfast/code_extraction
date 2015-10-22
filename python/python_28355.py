# Beatbox: How do I add a WHERE clause when pulling data from SFDC?
svc.query("SELECT ID,Website FROM Account where ID in (SELECT accountId FROM Opportunity)")

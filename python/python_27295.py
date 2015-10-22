# Alfresco Versioning via cmis setContentStream
pwc = doc.checkout()
pwc.setContentStream(contentFile=tempfile)
pwc.checkin

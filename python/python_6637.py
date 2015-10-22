# Python filter for postfix
client = smtplib.SMTP('127.0.0.1',&lt;yourportnumber for the receiving postfix instance&gt;)
client.sendmail(&lt;envelope from&gt;, &lt;envelope to&gt;, &lt;yourmessageobject&gt;.as_string())

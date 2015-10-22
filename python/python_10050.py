# Using jcifs in jython in order to access site using NTLM security
ai = NTLMAuthenticationInfo("domain", "your host", "user", "password")
result = request101.GET('/')
result = NTLMAuthentication(result, request101, ai)

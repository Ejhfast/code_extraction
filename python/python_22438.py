# What is 'my-creds', 'my-area', and 'my-router' in these Python PySNMP codes?
securityName + securityLevel + snmpMessageProcessingModel (3) -&gt; snmpTargetParameters (see SNMP-TARGET-MIB::snmpTargetParams)
securityName + communityName + snmpMessageVersion (1|2c) -&gt; snmpTargetParameters (see SNMP-COMMUNITY-MIB::snmpCommunity)
snmpTargetParameters + targetAddress + timeout + retries -&gt; snmpTarget (see SNMP-TARGET-MIB::snmpTargetAddr)

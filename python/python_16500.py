# Display a raw string from a "regex-like" string
list = ['State start_ping_3\n{\n   \t// send ping\n\n\tAssign addr Ping_RemoteAddr3;\n\tAssign pingParams Ping_Parameters3;\n\n\tBuild Out GUE_startCommand;\n\tAssign Out.ref\t11;\n\t//Assign Out.command\t"/ercom/bundles/startPing.sh -I %pdn_add% %pingParams% %addr%";\n\tCase(PDNType = 2) // IPv6\n\t{\n\t\tAssign Out.command\t"$BUNDLE_BIN_PATH/ping6 -I %pdn_add% %pingParams% %addr%";\n\t}\n\tDefaultCase(PDNType)\n\t{\n\t\tAssign Out.command\t"$BUNDLE_BIN_PATH/ping -I %pdn_add% %pingParams% %addr%"; // -w 8: 8sec timeout then exit ping\n\t}\n\tSend Out To\tUE;\n\tAdd ping_traffic3 1;\n\t\n\tIf (_ActivateEvents&gt;=1) {Log "Start Ping 3";}\n\tReturn;\n}']
print list[0]

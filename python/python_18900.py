# I hide (not to kill and hide) XBMC for raspberry pi?
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ExecuteAction","params":{"action":"togglefullscreen"},"id":"1"}')
os.system('sh -c "sudo killall -STOP xbmc.bin &amp;&amp; runmyapp &amp;&amp; sudo killall -CONT xbmc.bin"') //run my app
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ExecuteAction","params":{"action":"togglefullscreen"},"id":"1"}')

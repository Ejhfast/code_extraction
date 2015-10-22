# deploying a war to tomcat using python
request = urllib2.Request('http://localhost:8080/manager/deploy?path=/war_file', data=war_file_contents)

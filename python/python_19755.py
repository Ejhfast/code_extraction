# Add build information in Jenkins using REST
p = {'json': '{"displayName":"New Name", "description":"New Description"}'}
requests.post('http://jenkins:8080/job/jobname/5/configSubmit', data=p, auth=(user, token))

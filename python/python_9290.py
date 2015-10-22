# Encoding json data as x-www-form-urlencoded
In [10]: urllib2.unquote("%7B%0A%20%20%22action%22%20%20%20%20%20%20%3A%20%22deploy%5Ffrom%5Fscratch%5Fwith%5Fbundle%22%2C%0A%20%20%22pusher%22%20%20%20%20%20%20%3A%20%7B%20%22email%22%20%3A%20%22my%40email%2Ecom%22%20%7D%2C%0A%20%20%22ref%22%20%20%20%20%20%20%20%20%20%3A%20%22refs%2Fheads%2Fmaster%22%2C%0A%20%20%22repo%5Fchoice%22%20%3A%20%22LOCAL%22%0A%7D%0A")
Out[10]: '{\n  "action"      : "deploy_from_scratch_with_bundle",\n  "pusher"      : { "email" : "my@email.com" },\n  "ref"         : "refs/heads/master",\n  "repo_choice" : "LOCAL"\n}\n'

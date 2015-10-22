# Python nose test failing on JSON response
json_response = json.loads(response.get_data())
assert_equals("Success! Your report has been created.", json_response.get("message", "&lt;no message&gt;"))

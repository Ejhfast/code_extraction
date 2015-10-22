# Can I back reference modified capture using regular expression?
/([a-z]{2,4})(??{reverse($1)})/

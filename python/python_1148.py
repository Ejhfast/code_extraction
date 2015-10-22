# Unable to get results when passing a string via parameter substitution in gql query
p = models.UserDetails.gql('WHERE user_name = :uname', uname = user_name).fetch(1)

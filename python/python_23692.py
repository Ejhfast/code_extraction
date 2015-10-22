# Disabling Angular $http.get URL encoding for query parameters
var queryObject = {filters: [...]};
$http.get('...', {params: {q: queryObject}});

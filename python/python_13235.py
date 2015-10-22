# One server, 2 sites, 1 cached with varnish, the other one can't delete session
if (!req.http.host ~ "^(www\.)?wpsite\.com$") {
     return (hit_for_pass);
  }

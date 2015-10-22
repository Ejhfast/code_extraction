# Using the GeoIP module with Nginx and UWSGI
proxy_set_header X-GeoIP-Country $geoip_country_name;
proxy_set_header X-GeoIP-City    $geoip_city;

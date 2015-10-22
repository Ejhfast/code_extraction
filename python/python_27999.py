# Selenium + Python - how to get the response from the site after uploading an image
ages = driver.execute_script("function get_ages() { arr=[]; $('#faces .tooltip-inner div').each(function () { arr.push($(this).text()); }); return arr;}; return get_ages()")

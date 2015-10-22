# using Selenium, Firefox, Python to save download of EPS files to disk after automated clicking of download link
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                   'image/jpeg,image/png,'
                   'application/octet-stream')

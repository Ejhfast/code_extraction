# Disable firefox save as dialog-selenium
profile.setPreference("browser.download.dir", "c:/yourDownloadDir");
profile.setPreference("browser.download.folderList", 2);
profile.setPreference("browser.helperApps.neverAsk.saveToDisk", "application/csv, text/csv");

# How to Maximize window in chrome using webDriver (python)
options = ChromeOptions();
options.add_argument("--start-maximized");
driver = ChromeDriver(options);

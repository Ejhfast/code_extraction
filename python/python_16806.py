# ChromeDriver/Selenium take a black screenshot when in a separate tab
handles = self.driver.window_handles
self.driver.switch_to_window(handles[-1])

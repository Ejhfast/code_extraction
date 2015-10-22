# Selenium Extraction Problems: Waits/Not Finding Elements
IWebElement headerResult = w.Until(ExpectedConditions.ElementIsVisible(By.CssSelector("div[class=\"text-center displayed\"] h3")));
        string result = headerResult.Text;

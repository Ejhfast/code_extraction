# Selenium Grid2 - Is it possible to run 10 Chrome instances?
java -jar $JARFILE -Dwebdriver.chrome.driver=$CHROMEDRIVER -role webdriver -hub http://$HUB_IP:4444/grid/register -maxSession 10 -browser browserName=chrome,maxInstances=10"

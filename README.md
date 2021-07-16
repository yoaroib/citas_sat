# SAT Citas
Selenium automatization that helps to catch a SAT appointment.

**It needs some tinkering by setting up parameters before making a reservation**

...you could set up a Telegram bot and use it for confirmation, otherwise the script will open up a youtube video to alert if there's availability in the SAT system.

## Requirements & TL;DR

1. Python 3
2. Chrome (could be used with another browser by using the appropriate driver)
3. Install [Selenium WebDriver](https://www.selenium.dev/documentation/en/selenium_installation/installing_selenium_libraries/)
4. Download [chromedriver](https://chromedriver.storage.googleapis.com/index.html) and [put it in the PATH](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)
5. Edit script with valid RFC and mail (optional)
6. Run python script
7. Manually select SAT location and procedure to monitor
8. Solve the captcha
9. Fill out (or set them in the script) the RFC and mail so the calendar shows in the page
10. Press enter for the script to start monitoring for open slots
11. Wait for profit

### Options

`rfc`, `mail` **are needed before the calendar is shown**.

`wait_time` changes how often the script refreshes the page for changes. By default is at 3 minutes.

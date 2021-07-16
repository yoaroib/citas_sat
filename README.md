# SAT Citas
Selenium automatization that helps to catch a SAT appointment.

**It needs some tinkering by setting up parameters before making a reservation**

...you could set up a Telegram bot and use it for confirmation, otherwise the script will open up a youtube video to alert if there's availability in the SAT system.

## Requirements & TL;DR

1. Python 3
2. Firefox (could be used with another browser by using the appropriate driver)
3. Install [Selenium WebDriver](https://www.selenium.dev/documentation/en/selenium_installation/installing_selenium_libraries/)
4. Download [geckodriver](https://github.com/mozilla/geckodriver/releases) and [put it in the PATH](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)
5. Run python script
6. Manually select SAT location and procedure to monitor
7. Solve the captcha
8. Fill out (or set them in the script) the RFC and mail so the calendar shows in the page
9. Press enter for the script to start monitoring for open slots
10. Wait for profit

### Options

`rfc`, `mail` **are needed before the calendar is shown**.

`wait_time` changes how often the script refreshes the page for changes. By default is at 3 minutes.

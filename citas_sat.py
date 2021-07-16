from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

driver = Chrome()

wait_time = 180
# Uncomment the next variable and enter your RFC
#rfc = ''
mail = 'your@mail.com'

driver.get('https://citas.sat.gob.mx/citasat/agregarcita.aspx')

input('Press Enter to start....')

# Uncomment next line to automatically fill the RFC
#driver.find_element_by_id('TXTRFC').send_keys(rfc + Keys.TAB)
#sleep(2)
driver.find_element_by_id('TXTCorreoElectronico').send_keys(mail + Keys.TAB)
sleep(2)

def searchDates():
    try:
        fechas = driver.find_elements_by_css_selector('#Calendario tr td')

        for fecha in fechas:
            verificacion = fecha.get_attribute('style')

            if ('rgb(74, 144, 226)' in verificacion or 'rgb(250, 235, 204)' in verificacion):
                driver.execute_script('''window.open("https://www.youtube.com/watch?v=qe5-ywmuKOg","_blank");''')
                terminar = input('End program (default yes)? [y/n]')

                if terminar == 'y':
                    driver.quit()
                    return True
                elif terminar == 'n':
                    searchDates()
                else:
                    driver.quit()
                    return True

        sleep(wait_time)
        driver.refresh()
        alert = driver.switch_to.alert
        alert.accept()
        searchDates()

    except:
        print('Something went wrong')
        return False

searchDates()

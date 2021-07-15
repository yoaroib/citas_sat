from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys

driver = Firefox()
driver.get('https://citas.sat.gob.mx/citasat/agregarcita.aspx')

input('Press Enter to start....')

def searchDates():
    try:
        fechas = driver.find_elements_by_css_selector('#Calendario tr td')

        for fecha in fechas:
            verificacion = fecha.get_attribute('style')

            if ('rgb(74, 144, 226)' in verificacion or 'rgb(250, 230, 226)' in verificacion):
                driver.execute_script('''window.open("https://youtu.be/gcNEC9NaJuE?t=10","_blank");''')
                terminar = input('End program (default yes)? [y/n]')

                if terminar == 'y':
                    return True
                elif terminar == 'n':
                    searchDates()
                else:
                    return True

        sleep(180)
        driver.refresh()
        alert = driver.switch_to.alert
        alert.accept()
        searchDates()

    except:
        print('Something went wrong')
        return False

searchDates()

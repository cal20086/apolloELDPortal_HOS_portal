#               Apollo Web Portal - Login 2
import time


def login_2_apolloWebPortal (contol_Reportfile, driver, driver_Name, driver_Version, user_ApolloWebPortalVar, password_ApolloWebPortalVar, test_Case_Type, siteAddressVar, carrier, truckDriversList):

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.edge.service import Service
    import tc_reports
    import test_Global_Addresses_apolloWebPortal
    import test_Hierarchy_User_Access_ManagePage_apolloWebPortal
    import test_Global_Variables_apolloWebPortal
    import test_Global_Addresses_apolloWebPortal





#               *************************************************** Element page address ************************************************


#       Carrier details Page Address & Variables
#       Fields Address
    title_UsernameAdr = test_Global_Addresses_apolloWebPortal.title_UsernameAdr_global
    text_UserNameId = test_Global_Addresses_apolloWebPortal.text_UserNameId_global
    text_PasswordId = test_Global_Addresses_apolloWebPortal.text_PasswordId_global
    button_LogInId = test_Global_Addresses_apolloWebPortal.button_LogInId_global
    mouseHover_eDashAdr = test_Global_Addresses_apolloWebPortal.mouseHover_eDashAdr_global


#       Variables
    control_Reportfile = 0
    print_Information_Fix = ""
    print_Information_Var = ""
    driverDriverListVar = "C:\\tools\msedgedriver.exe"
    text_CarrierFull_Var = test_Global_Variables_apolloWebPortal.text_CarrierFull_Var_Global



    print(f'login page 2 = {siteAddressVar}')
    #               Main:

    driver2 = webdriver.Edge(service=Service(driverDriverListVar))
    #print("Login page")
    driver2.get(siteAddressVar)
    driver2.maximize_window()
    w = WebDriverWait(driver2,10)

      #       Login
    text_UserName = w.until(EC.presence_of_element_located((By.ID, text_UserNameId)))
    text_UserName.send_keys(user_ApolloWebPortalVar)
    text_Password = w.until(EC.presence_of_element_located((By.ID, text_PasswordId)))
    text_Password.send_keys(password_ApolloWebPortalVar)
    button_LogIn = w.until(EC.presence_of_element_located((By.ID, button_LogInId)))
    button_LogIn.click()

    driver_temp = driver
    driver = driver2
    text_CarrierType = text_CarrierFull_Var
    test_Hierarchy_User_Access_ManagePage_apolloWebPortal.Hierarchy_User_Access_MenuPage (driver, driver_Name, driver_Version, carrier, truckDriversList, text_CarrierType)

    driver = driver_temp
    return ()
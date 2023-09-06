#               Apollo Web Portal - Login
import time


def login_apolloWebPortal (contol_Reportfile, driver, driver_Name, driver_Version, user_ApolloWebPortalVar, password_ApolloWebPortalVar, siteAddressVar, test_Case_Type):

    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from  selenium.webdriver import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    import tc_reports
    import test_Global_Addresses_apolloWebPortal




#               *************************************************** Element page address ************************************************


#       Carrier details Page Address & Variables
#       Fields Address
    title_UsernameAdr = test_Global_Addresses_apolloWebPortal.title_UsernameAdr_global
    text_UserNameId = test_Global_Addresses_apolloWebPortal.text_UserNameId_global
    text_PasswordId = test_Global_Addresses_apolloWebPortal.text_PasswordId_global
    button_LogInId = test_Global_Addresses_apolloWebPortal.button_LogInId_global
    mouseHover_eDashAdr = test_Global_Addresses_apolloWebPortal.mouseHover_eDashAdr_global

    """    
    title_UsernameAdr = "/html/body/form/div[3]/div/div/table/tbody/tr/td/label[1]"
    text_UserNameId = "username"
    text_PasswordId = "password"
    button_LogInId = "login"
    mouseHover_eDashAdr = "/html/body/form/div[3]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[13]/table/tbody/tr/td/a"
    """
#       Variables
    control_Reportfile = 0
    print_Information_Fix = ""
    print_Information_Var = ""

    #               Main:

    #print("Login page")
    driver.get(siteAddressVar)
    driver.maximize_window()
    w = WebDriverWait(driver,10)

    """
    # Report header:
    contol_Reportfile = 0
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    """

    #       Login Page verify
    """
    title_Username = w.until(EC.presence_of_element_located((By.XPATH, title_UsernameAdr))).text
    test_Name = "Login page open"
    condition1 = "User Name:"
    condition2 = title_Username
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    """



      #       Login
    text_UserName = w.until(EC.presence_of_element_located((By.ID, text_UserNameId)))
    text_UserName.send_keys(user_ApolloWebPortalVar)
    text_Password = w.until(EC.presence_of_element_located((By.ID, text_PasswordId)))
    text_Password.send_keys(password_ApolloWebPortalVar)
    button_LogIn = w.until(EC.presence_of_element_located((By.ID, button_LogInId)))
    button_LogIn.click()

    """
    #       Print Assert OK
    print_Information_Fix = "Login page open:"
    print_Information_Var = title_Username
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    """


    return ()




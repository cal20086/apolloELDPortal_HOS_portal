#               Apollo Web Portal - ADMINISTRATION USERS
#                   LIMITED RESELLER

def Administration_Users_LimitedReseller_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList, siteAddressVar):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import Select
    import tc_reports
    from selenium.webdriver import ActionChains
    from selenium.webdriver.support.select import Select
    import os
    import glob
    import openpyxl
    from pathlib import Path
    from pathlib import Path
    from os import path
    from datetime import datetime, timedelta
    from selenium.common.exceptions import NoSuchElementException
    import test_Report_Categories_Defects_FIELDSInterchanges_apolloWebPortal
    import test_Global_Variables_apolloWebPortal
    import test_Global_Addresses_apolloWebPortal

    #              ADMINISTRATION / ROLES Main
    # GLOBAL ADDRESSES

    #print(dir(test_Global_Addresses_apolloWebPortal))
    #print(dir(test_Global_Variables_apolloWebPortal))


    #       Fields Address
    menuRegion_MainSideBar_ManagePageAdrAsideDiv = test_Global_Addresses_apolloWebPortal.menuRegion_MainSideBar_ManagePageAdrAsideDiv_Global

    # Users page
    button_Administration_ManagePageId = test_Global_Addresses_apolloWebPortal.button_Administration_ManagePageId_Global
    button_Administration_Roles_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Administration_Roles_ManagePageAdr_Global
    button_Administration_Users_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Administration_Users_ManagePageAdr_Global
    title_Users_AdinistrationPageAdr = test_Global_Addresses_apolloWebPortal.title_Users_AdinistrationPageAdr_Global
    title_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.title_Users_AdministrationPageAdr_Global
    button_PlusNew_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_PlusNew_Users_AdministrationPageAdr_Global
    input_Search_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Search_Users_AdministrationPageAdr_Global
    button_1stDelete_Actions_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_1stDelete_Actions_Users_AdministrationPageAdr_Global
    button_EditUser_Actions_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_EditUser_Actions_Users_AdministrationPageAdr_Global
    button_DeleteConfirmation_Actions_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_DeleteConfirmation_Actions_Users_AdministrationPageAdr_Global
    button_SearchClean_Actions_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_SearchClean_Actions_Users_AdministrationPageAdr_Global
    input_Username_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Username_Users_AdministrationPageAdr_Global
    input_Email_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Email_Users_AdministrationPageAdr_Global
    input_Carrier_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Carrier_Users_AdministrationPageAdr_Global
    input_TypeOfUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_TypeOfUser_Users_AdministrationPageAdr_Global
    input_Role_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Role_Users_AdministrationPageAdr_Global
    button_SearchClean_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_SearchClean_Users_AdministrationPageAdr_Global

    # Add User page"
    checkbox_ResellerUser_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.checkbox_ResellerUser_AddUser_Users_AdministrationPageId_Global
    checkbox_CarrierUser_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.checkbox_CarrierUser_AddUser_Users_AdministrationPageId_Global
    input_Username_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.input_Username_AddUser_Users_AdministrationPageId_Global
    input_Email_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Email_AddUser_Users_AdministrationPageAdr_Global
    input_Password_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Password_AddUser_Users_AdministrationPageAdr_Global
    input_ConfirmationPassword_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_ConfirmationPassword_AddUser_AdministrationPageAdr_Global
    dropdown_TypeOfUser_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.dropdown_TypeOfUser_AddUser_Users_AdministrationPageId_Global
    button_SAVE_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_SAVE_AddUser_Users_AdministrationPageAdr_Global
    button_CLOSE_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_CLOSE_AddUser_Users_AdministrationPageAdr_Global
    errorMessage_UsernameAdr = test_Global_Addresses_apolloWebPortal.errorMessage_UsernameAdr_Global
    errorMessage_EmailAdr = test_Global_Addresses_apolloWebPortal.errorMessage_EmailAdr_Global
    errorMessage_PasswordAdr = test_Global_Addresses_apolloWebPortal.errorMessage_PasswordAdr_Global
    errorMessage_ConfirmationPasswordAdr = test_Global_Addresses_apolloWebPortal.errorMessage_ConfirmationPasswordAdr_Global
    errorMessage_UsernameExistAdr = test_Global_Addresses_apolloWebPortal.errorMessage_UsernameExistAdr_Global
    errorMessage_ConfirmationPasswordAdr = test_Global_Addresses_apolloWebPortal.errorMessage_ConfirmationPasswordAdr_Global
    button_CLOSE_Error_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_CLOSE_Error_AddUser_Users_AdministrationPageAdr_Global
    dropdown_Carriers_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.dropdown_Carriers_AddUser_Users_AdministrationPageId_Global
    button_AddCarrier_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_AddCarrier_AddUser_Users_AdministrationPageAdr_Global
    button_AddAllCarrier_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_AddAllCarrier_AddUser_Users_AdministrationPageAdr_Global
    checkbox_AllHomeBases_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.checkbox_AllHomeBases_AddUser_Users_AdministrationPageId_Global
    checkbox_HomeBasesList_HomeTerminal_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.checkbox_HomeBasesList_HomeTerminal_AddUser_Users_AdministrationPageAdr_Global
    checkbox_HomeBasesList_2ndHomeBase_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.checkbox_HomeBasesList_2ndHomeBase_AddUser_Users_AdministrationPageAdr_Global
    text_HomeBasesList_HomeTerminal_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.text_HomeBasesList_HomeTerminal_AddUser_Users_AdministrationPageAdr_Global
    text_HomeBasesList_2ndHomeBase_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.text_HomeBasesList_2ndHomeBase_AddUser_Users_AdministrationPageAdr_Global
    button_AddAllCarrier_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_AddAllCarrier_AddUser_Users_AdministrationPageAdr_Global
    list_CarrierList_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.list_CarrierList_AddUser_Users_AdministrationPageAdr_Global


    table_CarrierList_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.table_CarrierList_AddUser_Users_AdministrationPageAdr_Global
    dropdown_Carriers_AddUserOpen_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.dropdown_Carriers_AddUserOpen_Users_AdministrationPageAdr_Global
    dropdown_Carriers_AddUserSelect_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.dropdown_Carriers_AddUserSelect_Users_AdministrationPageAdr_Global

    #   Global Variables
    workbookDB = test_Global_Variables_apolloWebPortal.workbookDB_Global
    worksheetDB = test_Global_Variables_apolloWebPortal.worksheetDB_Global
    var_LimitedReseller_UsernameVar = test_Global_Variables_apolloWebPortal.var_LimitedReseller_UsernameVar_Global
    text_CarrierFull_Var = test_Global_Variables_apolloWebPortal.text_CarrierFull_Var_Global
    text_CarrierLimited_Var = test_Global_Variables_apolloWebPortal.text_CarrierLimited_Var_Global
    var_Username_ExistVar = test_Global_Variables_apolloWebPortal.var_Username_ExistVar_Global
    var_LimitedReseller_EmailVar = test_Global_Variables_apolloWebPortal.var_LimitedReseller_EmailVar_Global
    var_LimitedReseller_PasswordVar = test_Global_Variables_apolloWebPortal.var_LimitedReseller_PasswordVar_Global
    var_LimitedReseller_ConfirmationPasswordVar = test_Global_Variables_apolloWebPortal.var_LimitedReseller_ConfirmationPasswordVar_Global

    #       Variables
    Ref_DVIR_DVIRPage = "Roles"
    w = WebDriverWait(driver, 30)

    #       #######################################     Main functions    ########################################################
    #   ###############################################################################################################################
    print('******************************Create and Test Limited Reseller')
#   Page Title on TCReport
    function_Name = "LIMITED RESELLER Users - Administration Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

#       Function Administration Users side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_Administration_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv,10).until(EC.element_to_be_clickable((By.ID, button_Administration_ManagePageId))).click()
    button_Administration_Users_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv, 10).until(EC.element_to_be_clickable((By.XPATH, button_Administration_Users_ManagePageAdr))).click()
#
    #       Title of the right page
    title_Users_AdinistrationPage = w.until(EC.presence_of_element_located((By.XPATH, title_Users_AdinistrationPageAdr))).text
    test_Name = "LIMITED RESELLER Users - Administration Function"
    condition1 = "Users"
    condition2 = title_Users_AdinistrationPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "LIMITED RESELLER Users - Administration Function page open:"
    print_Information_Var = title_Users_AdinistrationPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "LR User"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    # Delete "QA_LimitedReseller" User from the Users List to start test
    input_Search_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Users_AdministrationPageAdr)))
    input_Search_Users_AdministrationPage.send_keys(var_LimitedReseller_UsernameVar)
    time.sleep(2)
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, button_1stDelete_Actions_Users_AdministrationPageAdr))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, button_DeleteConfirmation_Actions_Users_AdministrationPageAdr))).click()
    except:
        print('Clean')
    w.until(EC.element_to_be_clickable(((By.XPATH, button_SearchClean_Actions_Users_AdministrationPageAdr)))).click()

    # + New Users button
    button_PlusNew_Users_AdministrationPage = w.until(EC.element_to_be_clickable((By.XPATH, button_PlusNew_Users_AdministrationPageAdr)))
    button_PlusNew_Users_AdministrationPage.click()

    #Select Reseller User
    w.until(EC.element_to_be_clickable((By.ID, checkbox_ResellerUser_AddUser_Users_AdministrationPageId))).click()


    # ******************************************
    # Verify Fields Parameters - Negative Tests
    # Test Username
    input_Username_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.ID, input_Username_AddUser_Users_AdministrationPageId)))
    input_Username_AddUser_Users_AdministrationPage.send_keys("xyz")
    input_Username_AddUser_Users_AdministrationPage.send_keys(Keys.TAB)
    # time.sleep(2)
    try:
        errorMessage_Username = w.until(EC.presence_of_element_located((By.XPATH, errorMessage_UsernameAdr))).text
        #   Assert
        test_Name = "NEGATIVE TEST - Username must have > 4 caracteres - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_UserNamelength_Portal_Global
        condition2 = errorMessage_Username
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test - Username must have > 4 caracteres - Add User - Administration page"
        print_Information_Var = errorMessage_Username
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #   Assert
        test_Name = "Message Username must have > 4 caracteres - Add User - Administration page"
        condition1 = "ERRO message not display- Username must be between 4 and 50 characters."
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    # Test Email
    input_Email_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Email_AddUser_Users_AdministrationPageAdr)))
    input_Email_AddUser_Users_AdministrationPage.send_keys("a@testcom")
    input_Email_AddUser_Users_AdministrationPage.send_keys(Keys.TAB)
    # time.sleep(2)
    try:
        errorMessage_Email = w.until(EC.presence_of_element_located((By.XPATH, errorMessage_EmailAdr))).text
        #   Assert
        test_Name = "Email must be a valid email address - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_InvalidEmail_Portal_Global
        condition2 = errorMessage_Email
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test - Email must be a valid email address - Add User - Administration page"
        print_Information_Var = errorMessage_Email
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #   Assert
        test_Name = "Email must be a valid email address - Add User - Administration page"
        condition1 = "ERROR Message not display - Invalid email format."
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)


    # Test Password (empty)
    input_Password_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Password_AddUser_Users_AdministrationPageAdr)))
    input_Password_AddUser_Users_AdministrationPage.send_keys("")
    input_Password_AddUser_Users_AdministrationPage.send_keys(Keys.TAB)
    # time.sleep(2)
    try:
        errorMessage_Password = w.until(EC.presence_of_element_located((By.XPATH, errorMessage_PasswordAdr))).text
        #   Assert
        test_Name = "Password must have between 1 to 15 characters - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_InvalidPassword_Portal_Global
        condition2 = errorMessage_Password
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test - Password must have between 1 to 15 characters - Add User - Administration page"
        print_Information_Var = errorMessage_Password
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #   Assert
        test_Name = "Negative Test - Password must have between 1 to 15 characters - Add User - Administration page"
        condition1 = "ERROR Message not display - This field is required."
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    input_Password_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Password_AddUser_Users_AdministrationPageAdr)))
    input_Password_AddUser_Users_AdministrationPage.send_keys("a")
    input_Password_AddUser_Users_AdministrationPage.send_keys(Keys.TAB)

        # Test Confirmation Password (empty)
    input_ConfirmationPassword_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_ConfirmationPassword_AddUser_Users_AdministrationPageAdr)))
    input_ConfirmationPassword_AddUser_Users_AdministrationPage.send_keys("")
    input_ConfirmationPassword_AddUser_Users_AdministrationPage.send_keys(Keys.TAB)
    # time.sleep(2)
    try:
        errorMessage_ConfirmationPassword = w.until(EC.presence_of_element_located((By.XPATH, errorMessage_ConfirmationPasswordAdr))).text
        #   Assert
        test_Name = "Negative Test - Password and Confirmation do not match - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_InvalidConfirmationPassword_Portal_Global
        condition2 = errorMessage_ConfirmationPassword
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test - Password and Confirmation do not match - Add User - Administration page"
        print_Information_Var = errorMessage_ConfirmationPassword
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #   Assert
        test_Name = "Negative Test - Password and Confirmation do not match - Add User - Administration page"
        condition1 = "ERROR Message not display - Password and Confirmation do not match"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    # Select Type of User = Limited Reseller
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_TypeOfUser_AddUser_Users_AdministrationPageId))))
    dropdown_TypeOfUser_AddUser_Users_AdministrationPage = dropDown.select_by_visible_text("Limited Reseller")
    dropdown_TypeOfUser_AddUser_Users_AdministrationPageRead = dropDown.first_selected_option.text


    # Select Carrier
    # DropDown Angular, Selenium Select function can't be use with DropDown Angular.
    # Angular dropDown
    # 1st step: open all option from dropDown field
    #dropDown = w.until(EC.presence_of_element_located((By.XPATH, dropdown_Carriers_AddUserOpen_Users_AdministrationPageAdr)))
    #dropDown.click()
    # 2nd step: Send keys to the input field
    dropDown_Client = w.until(EC.presence_of_element_located((By.XPATH, dropdown_Carriers_AddUserSelect_Users_AdministrationPageAdr)))
    dropDown_Client.send_keys(text_CarrierFull_Var)
    time.sleep(2)
    dropDown_Client.send_keys(Keys.ENTER)
    #w.until(EC.element_to_be_clickable((By.XPATH, button_AddCarrier_AddUser_Users_AdministrationPageAdr))).click()

    # SELECT ALL CARRIER AND VERIFY THE CARRIER LIST SELECTED
    w.until(EC.element_to_be_clickable((By.XPATH, button_AddAllCarrier_AddUser_Users_AdministrationPageAdr))).click()

    w.until(EC.element_to_be_clickable((By.XPATH, button_CLOSE_AddUser_Users_AdministrationPageAdr))).click()

    ################################################################################################################################
    #Create a User with a Username already on the system (other partner) - Negative Test
    # + New Users button
    button_PlusNew_Users_AdministrationPage = w.until(EC.element_to_be_clickable((By.XPATH, button_PlusNew_Users_AdministrationPageAdr)))
    button_PlusNew_Users_AdministrationPage.click()
    # Select Reseller
    w.until(EC.element_to_be_clickable((By.ID, checkbox_ResellerUser_AddUser_Users_AdministrationPageId))).click()

    # New User with Username exist
    input_Username_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.ID, input_Username_AddUser_Users_AdministrationPageId)))
    input_Username_AddUser_Users_AdministrationPage.send_keys(var_Username_ExistVar)
    input_Email_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Email_AddUser_Users_AdministrationPageAdr)))
    input_Email_AddUser_Users_AdministrationPage.send_keys(var_LimitedReseller_EmailVar)
    input_Password_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Password_AddUser_Users_AdministrationPageAdr)))
    input_Password_AddUser_Users_AdministrationPage.send_keys(var_LimitedReseller_PasswordVar)
    input_ConfirmationPassword_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_ConfirmationPassword_AddUser_Users_AdministrationPageAdr)))
    input_ConfirmationPassword_AddUser_Users_AdministrationPage.send_keys(var_LimitedReseller_ConfirmationPasswordVar)
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_TypeOfUser_AddUser_Users_AdministrationPageId))))
    dropdown_TypeOfUser_AddUser_Users_AdministrationPage = dropDown.select_by_visible_text("Limited Reseller")

    # DropDown Angular, Selenium Select function can't be use with DropDown Angular.
    dropDown_Client = w.until(EC.presence_of_element_located((By.XPATH, dropdown_Carriers_AddUserSelect_Users_AdministrationPageAdr)))
    dropDown_Client.send_keys(text_CarrierFull_Var)
    time.sleep(2)
    dropDown_Client.send_keys(Keys.ENTER)

    w.until(EC.element_to_be_clickable((By.XPATH, button_AddCarrier_AddUser_Users_AdministrationPageAdr))).click()

    # SAVE new user with Username exist
    w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_AddUser_Users_AdministrationPageAdr))).click()
    try:
        errorMessage_UsernameExist = w.until(EC.presence_of_element_located((By.XPATH, errorMessage_UsernameExistAdr))).text
        #   Assert
        test_Name = "Username EXIST - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_UsernameExist_Portal_Global
        condition2 = errorMessage_UsernameExist
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test - Username already EXIST - Add User - Administration page"
        print_Information_Var = errorMessage_UsernameExist
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        errorMessage_UsernameExist = ""
        #   Assert
        test_Name = "Username EXIST FAILED- Add User - Administration page"
        condition1 = "ERROR Message not display - Username already exist."
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Screenshot
    test_Name = "User EXIST LR"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    w.until(EC.element_to_be_clickable((By.XPATH, button_CLOSE_Error_AddUser_Users_AdministrationPageAdr))).click()


    #***************************************
    # Create a New Limited Reseller User
    # + New Users button
    button_PlusNew_Users_AdministrationPage = w.until(EC.element_to_be_clickable((By.XPATH, button_PlusNew_Users_AdministrationPageAdr)))
    button_PlusNew_Users_AdministrationPage.click()
    #Select Reseller
    w.until(EC.element_to_be_clickable((By.ID, checkbox_ResellerUser_AddUser_Users_AdministrationPageId))).click()

    # New User informations
    input_Username_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.ID, input_Username_AddUser_Users_AdministrationPageId)))
    input_Username_AddUser_Users_AdministrationPage.send_keys(var_LimitedReseller_UsernameVar)
    input_Email_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Email_AddUser_Users_AdministrationPageAdr)))
    input_Email_AddUser_Users_AdministrationPage.send_keys(var_LimitedReseller_EmailVar)
    input_Password_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Password_AddUser_Users_AdministrationPageAdr)))
    input_Password_AddUser_Users_AdministrationPage.send_keys(var_LimitedReseller_PasswordVar)
    input_ConfirmationPassword_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_ConfirmationPassword_AddUser_Users_AdministrationPageAdr)))
    input_ConfirmationPassword_AddUser_Users_AdministrationPage.send_keys(var_LimitedReseller_ConfirmationPasswordVar)
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_TypeOfUser_AddUser_Users_AdministrationPageId))))
    dropdown_TypeOfUser_AddUser_Users_AdministrationPage = dropDown.select_by_visible_text("Limited Reseller")
    dropdown_TypeOfUser_AddUser_Users_AdministrationPageRead = dropDown.first_selected_option.text

    # DropDown Angular, Selenium Select function can't be use with DropDown Angular.
    dropDown_Client = w.until(EC.presence_of_element_located((By.XPATH, dropdown_Carriers_AddUserSelect_Users_AdministrationPageAdr)))
    dropDown_Client.send_keys(text_CarrierFull_Var)
    time.sleep(0.5)
    dropDown_Client.send_keys(Keys.ENTER)


    # HOME BASES SELECTED
    w.until(EC.element_to_be_clickable((By.ID, checkbox_AllHomeBases_AddUser_Users_AdministrationPageId))).click()
    w.until(EC.element_to_be_clickable((By.XPATH, checkbox_HomeBasesList_HomeTerminal_AddUser_Users_AdministrationPageAdr))).click()
    w.until(EC.element_to_be_clickable((By.XPATH, checkbox_HomeBasesList_2ndHomeBase_AddUser_Users_AdministrationPageAdr))).click()
    homeBase1 = w.until(EC.presence_of_element_located((By.XPATH, text_HomeBasesList_HomeTerminal_AddUser_Users_AdministrationPageAdr))).text
    homeBase2 = w.until(EC.presence_of_element_located((By.XPATH, text_HomeBasesList_2ndHomeBase_AddUser_Users_AdministrationPageAdr))).text

    w.until(EC.element_to_be_clickable((By.XPATH, button_AddCarrier_AddUser_Users_AdministrationPageAdr))).click()

    test_Global_Variables_apolloWebPortal.carriers_List_Global = [text_CarrierFull_Var]
    test_Global_Variables_apolloWebPortal.homeBase_List_Global = [homeBase1, homeBase2]
    

    list_CarrierList_AddUser_Users_AdministrationPageRead = w.until(EC.presence_of_element_located((By.XPATH, list_CarrierList_AddUser_Users_AdministrationPageAdr))).text
    #   Assert
    test_Name = "New Limited Reseller Carrier List"
    condition1 = list_CarrierList_AddUser_Users_AdministrationPageRead
    condition2 = text_CarrierFull_Var

    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New Limited Reseller Carrier List"
    print_Information_Var = list_CarrierList_AddUser_Users_AdministrationPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    #SAVE new user
    w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_AddUser_Users_AdministrationPageAdr))).click()

    # Verify New User Information on Users page
    # Search new user
    input_Search_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Users_AdministrationPageAdr)))
    time.sleep(2)
    input_Search_Users_AdministrationPage.send_keys(var_LimitedReseller_UsernameVar)
    time.sleep(2)

    input_Username_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Username_Users_AdministrationPageAdr))).text
    test_Name = "New User USERNAME Saved - Administration page"
    condition1 = var_LimitedReseller_UsernameVar
    condition2 = input_Username_Users_AdministrationPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New User USERNAME Saved - Administration page"
    print_Information_Var = input_Username_Users_AdministrationPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    input_Email_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Email_Users_AdministrationPageAdr))).text
    test_Name = "New User EMAIL Saved - Administration page"
    condition1 = var_LimitedReseller_EmailVar
    condition2 = input_Email_Users_AdministrationPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New User EMAIL Saved - Administration page"
    print_Information_Var = input_Email_Users_AdministrationPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)



    input_TypeOfUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_TypeOfUser_Users_AdministrationPageAdr))).text
    #   Assert
    test_Name = "New User TYPE OF USER Saved - Administration page"
    condition1 = dropdown_TypeOfUser_AddUser_Users_AdministrationPageRead
    condition2 = input_TypeOfUser_Users_AdministrationPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New User TYPE OF USER Saved - Administration page"
    print_Information_Var = input_TypeOfUser_Users_AdministrationPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    input_Role_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Role_Users_AdministrationPageAdr))).text
    #   Assert
    test_Name = "New User ROLE Check - Administration page"
    condition1 = "Reseller Full Client Access"
    condition2 = input_Role_Users_AdministrationPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New User ROLE Check - Administration page"
    print_Information_Var = input_Role_Users_AdministrationPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "NewLRUser"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    input_Search_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Users_AdministrationPageAdr)))
    input_Search_Users_AdministrationPage.send_keys("A")
    w.until(EC.element_to_be_clickable((By.XPATH, button_SearchClean_Users_AdministrationPageAdr))).click()

    #########################################################################################################################################
    # LOGIN WITH THE NEW USER AND CHECK ALL ACCESS FUNCTION ON THE MAIN MENU
    # BASED ON THE USER HIERARCHY
    #########################################################################################################################################
    print('******************************Verifying the Limited Reseller Functions Available - Edge Browser')
    import test_NewUser_Check_Hierarchy_User_Access_ManagePage_apolloWebPortal
    var_UsernameVar = var_LimitedReseller_UsernameVar
    var_PasswordVar = var_LimitedReseller_PasswordVar
    text_CarrierType = text_CarrierFull_Var
    test_Global_Variables_apolloWebPortal.userROLE_Global = int()
    test_Global_Variables_apolloWebPortal.userTYPE_Global = 3
    test_NewUser_Check_Hierarchy_User_Access_ManagePage_apolloWebPortal.NewUser_Check_Hierarchy_User_Access_MenuPage (driver, driver_Name, driver_Version, carrier, truckDriversList, var_UsernameVar, var_PasswordVar, text_CarrierType, siteAddressVar)

    print("********** END LIMITED RESELLER TEST **********")
    return()

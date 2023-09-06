#               Apollo Web Portal - ADMINISTRATION USERS
#                   LIMITED CLIENT


def Administration_Users_LimitedClient_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList, siteAddressVar):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    import tc_reports
    from selenium.webdriver import ActionChains
    from selenium.webdriver.support.select import Select
    import test_Global_Variables_apolloWebPortal
    import test_Global_Addresses_apolloWebPortal
    import test_NewUser_Check_Hierarchy_User_Access_ManagePage_apolloWebPortal

    #              ADMINISTRATION / ROLES Main

    # Global Fields Address
    #print(dir(test_Global_Addresses_apolloWebPortal))
    #print(dir(test_Global_Variables_apolloWebPortal))

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

    # Carrier Add User page"
    checkbox_ResellerUser_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.checkbox_ResellerUser_AddUser_Users_AdministrationPageId_Global
    checkbox_CarrierUser_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.checkbox_CarrierUser_AddUser_Users_AdministrationPageId_Global
    input_Username_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.input_Username_AddUser_Users_AdministrationPageId_Global
    input_Email_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Email_AddUser_Carrier_Users_AdministrationPageAdr_Global

#    input_Password_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_ConfirmationPassword_Carrier_AddUser_Users_AdministrationPageAdr_Global
#    input_ConfirmationPassword_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_ConfirmationPassword_Carrier_AddUser_Users_AdministrationPageAdr_Global

    input_Password_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Password_AddUser_Carrier_Users_AdministrationPageAdr_Global
    input_ConfirmationPassword_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_ConfirmationPassword_Carrier_AddUser_Users_AdministrationPageAdr_Global

    dropdown_Carrier_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.dropdown_Carrier_AddUser_Carrier_Users_AdministrationPageAdr_Global
    dropdown_Role_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.dropdown_Role_AddUser_Carrier_Users_AdministrationPageId_Global
    dropdown_TypeOfUser_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.dropdown_TypeOfUser_AddUser_Carrier_Users_AdministrationPageId_Global
    checkbox_HomeTerminal_HomeBasesList_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.checkbox_HomeTerminal_HomeBasesList_AddUser__CarrierUsers_AdministrationPageAdr_Global
    button_SAVE_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_SAVE_AddUser_Carrier_Users_AdministrationPageAdr_Global
    button_CLOSE_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_CLOSE_AddUser_Carrier_Users_AdministrationPageAdr_Global
    errorMessage_UsernameAdr = test_Global_Addresses_apolloWebPortal.errorMessage_UsernameAdr_Carrier_Global
    errorMessage_EmailAdr = test_Global_Addresses_apolloWebPortal.errorMessage_EmailAdr_Carrier_Global
    errorMessage_PasswordAdr = test_Global_Addresses_apolloWebPortal.errorMessage_PasswordAdr_Carrier_Global
    errorMessage_ConfirmationPasswordAdr = test_Global_Addresses_apolloWebPortal.errorMessage_ConfirmationPasswordAdr_Carrier_Global
    errorMessage_UsernameExistAdr = test_Global_Addresses_apolloWebPortal.errorMessage_UsernameExist_AddUser_UserAdr_Global
    button_CLOSE_Error_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.button_CLOSE_Error_AddUser_Carrier_Users_AdministrationPageAdr_Global
    footer_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.footer_AddUser_Users_AdministrationPageAdr_Global
    text_HomeBasesList_HomeTerminal_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.text_HomeBasesList_HomeTerminal_AddUser_Users_AdministrationPageAdr_Global
    text_HomeBasesList_HomeTerminal_AddUserClient_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.text_HomeBasesList_HomeTerminal_AddUserClient_Users_AdministrationPageAdr_Global
    #   Global Variables

    workbookDB = test_Global_Variables_apolloWebPortal.workbookDB_Global
    worksheetDB = test_Global_Variables_apolloWebPortal.worksheetDB_Global
    var_TypeOfUserVar = test_Global_Variables_apolloWebPortal.var_LimitedClient_TypeOfUserVar_Global
    var_RoleVar = test_Global_Variables_apolloWebPortal.var_LimitedClient_RoleVar_Global
    var_LimitedClient_UsernameVar = test_Global_Variables_apolloWebPortal.var_LimitedClient_UsernameVar_Global
    var_LimitedClient_EmailVar = test_Global_Variables_apolloWebPortal.var_LimitedClient_EmailVar_Global
    var_LimitedClient_PasswordVar = test_Global_Variables_apolloWebPortal.var_LimitedClient_PasswordVar_Global
    var_LimitedClient_ConfirmationPasswordVar = test_Global_Variables_apolloWebPortal.var_LimitedClient_ConfirmationPasswordVar_Global
    var_Username_ExistVar = test_Global_Variables_apolloWebPortal.var_Username_ExistVar_Global
    var_CarrierFull_Var = test_Global_Variables_apolloWebPortal.var_CarrierFull_Var_Global
    text_CarrierLimited_Var = test_Global_Variables_apolloWebPortal.text_CarrierLimited_Var_Global
    global carriers_List_Global
    global homeBase_List_Global

    #       Variables

    Ref_DVIR_DVIRPage = "Roles"

    w = WebDriverWait(driver, 40)

    #       #######################################     Main functions    ########################################################
    #   ###############################################################################################################################
    print('******************************Create and Test Limited Client')
#   Page Title on TCReport
    function_Name = "LIMITED CLIENT Users - Administration Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

#       Function Administration Users side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_Administration_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv,10).until(EC.element_to_be_clickable((By.ID, button_Administration_ManagePageId))).click()
    button_Administration_Users_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv, 10).until(EC.element_to_be_clickable((By.XPATH, button_Administration_Users_ManagePageAdr))).click()
#
    #       Title of the right page
    title_Users_AdinistrationPage = w.until(EC.presence_of_element_located((By.XPATH, title_Users_AdinistrationPageAdr))).text
    test_Name = "LIMITED CLIENT Users - Administration Function page open"
    condition1 = "Users"
    condition2 = title_Users_AdinistrationPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "LIMITED CLIENT Users - Administration Function page open"
    print_Information_Var = title_Users_AdinistrationPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "LC Users"
    tc_reports.screenshot(driver, driver_Name, test_Name)


    # Delete "QA_FullAccessClient" User from the Users List to start test
    input_Search_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Users_AdministrationPageAdr)))
    input_Search_Users_AdministrationPage.send_keys(var_LimitedClient_UsernameVar)
    time.sleep(2)
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, button_1stDelete_Actions_Users_AdministrationPageAdr))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, button_DeleteConfirmation_Actions_Users_AdministrationPageAdr))).click()
    except:
        print('Clean')
    w.until(EC.element_to_be_clickable(((By.XPATH, button_SearchClean_Actions_Users_AdministrationPageAdr)))).click()


    # ******************************************
    # Verify Fields Parameters - Negative Tests
    # + New Users button
    button_PlusNew_Users_AdministrationPage = w.until(EC.element_to_be_clickable((By.XPATH, button_PlusNew_Users_AdministrationPageAdr)))
    button_PlusNew_Users_AdministrationPage.click()

    #Select Carrier User
    w.until(EC.element_to_be_clickable((By.ID, checkbox_CarrierUser_AddUser_Users_AdministrationPageId))).click()


    # Test Username
    input_Username_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.ID, input_Username_AddUser_Users_AdministrationPageId)))
    input_Username_AddUser_Users_AdministrationPage.send_keys("xyz")
    input_Username_AddUser_Users_AdministrationPage.send_keys(Keys.TAB)
    # time.sleep(2)
    try:
        errorMessage_Username = w.until(EC.presence_of_element_located((By.XPATH, errorMessage_UsernameAdr))).text
        #   Assert
        test_Name = "Negative Test PASSED - Username must have > 4 caracteres - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_UserNamelength_Portal_Global
        condition2 = errorMessage_Username
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test PASSED - Username must have > 4 caracteres - Add User - Administration page"
        print_Information_Var = errorMessage_Username
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #   Assert
        test_Name = "Negative Test FAILED - Message Username must have > 4 caracteres - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_UserNamelength_Portal_Global
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
        test_Name = "Negative Test PASSED - Email must be a valid email address - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_InvalidEmail_Portal_Global
        condition2 = errorMessage_Email
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test PASSED - Email must be a valid email address - Add User - Administration page"
        print_Information_Var = errorMessage_Email
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #   Assert
        test_Name = "Negative Test FAILED - Email must be a valid email address - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_InvalidEmail_Portal_Global
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
        test_Name = "Negative Test PASSED - Password must have between 1 to 15 characters - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_InvalidPassword_Portal_Global
        condition2 = errorMessage_Password
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test PASSED - Password must have between 1 to 15 characters - Add User - Administration page"
        print_Information_Var = errorMessage_Password
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #   Assert
        test_Name = "Negative Test FAILED - Password must have between 1 to 15 characters - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_InvalidPassword_Portal_Global
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #Type any password
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
        test_Name = "Negative Test PASSED - Password and Confirmation do not match - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_InvalidConfirmationPassword_Portal_Global
        condition2 = errorMessage_ConfirmationPassword
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test PASSED - Password and Confirmation do not match - Add User - Administration page"
        print_Information_Var = errorMessage_ConfirmationPassword
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #   Assert
        test_Name = "Negative Test FAILED - Password and Confirmation do not match - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_InvalidConfirmationPassword_Portal_Global
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    w.until(EC.element_to_be_clickable((By.XPATH, button_CLOSE_AddUser_Users_AdministrationPageAdr))).click()


    #Create a User with a Username already on the system (other partner) - Negative Test
    # + New Users button
    button_PlusNew_Users_AdministrationPage = w.until(EC.element_to_be_clickable((By.XPATH, button_PlusNew_Users_AdministrationPageAdr)))
    button_PlusNew_Users_AdministrationPage.click()
    # Select Reseller
    w.until(EC.element_to_be_clickable((By.ID, checkbox_CarrierUser_AddUser_Users_AdministrationPageId))).click()

    # New User with an Exist Username
    input_Username_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.ID, input_Username_AddUser_Users_AdministrationPageId)))
    input_Username_AddUser_Users_AdministrationPage.send_keys(var_Username_ExistVar)
    input_Email_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Email_AddUser_Users_AdministrationPageAdr)))
    input_Email_AddUser_Users_AdministrationPage.send_keys(var_LimitedClient_EmailVar)
    input_Password_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Password_AddUser_Users_AdministrationPageAdr)))
    input_Password_AddUser_Users_AdministrationPage.send_keys(var_LimitedClient_PasswordVar )
    input_ConfirmationPassword_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_ConfirmationPassword_AddUser_Users_AdministrationPageAdr)))
    input_ConfirmationPassword_AddUser_Users_AdministrationPage.send_keys(var_LimitedClient_ConfirmationPasswordVar)

    dropDown_Carrier = w.until(EC.presence_of_element_located((By.XPATH, dropdown_Carrier_AddUser_Users_AdministrationPageAdr)))
    dropDown_Carrier.send_keys(text_CarrierLimited_Var)
    time.sleep(2)
    dropDown_Carrier.send_keys(Keys.ENTER)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_Role_AddUser_Users_AdministrationPageId))))
    dropdown_Role_AddUser_Users_AdministrationPage = dropDown.select_by_visible_text(var_RoleVar)


    a = w.until(EC.presence_of_element_located((By.XPATH, footer_AddUser_Users_AdministrationPageAdr)))
    actions = ActionChains(driver)
    actions.move_to_element(a)
    actions.perform()

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_TypeOfUser_AddUser_Users_AdministrationPageId))))
    dropdown_TypeOfUser_AddUser_Users_AdministrationPage = dropDown.select_by_visible_text(var_TypeOfUserVar)
    w.until(EC.element_to_be_clickable((By.XPATH, checkbox_HomeTerminal_HomeBasesList_AddUser_Users_AdministrationPageAdr))).click()

    # HOME BASES SELECTED

    homeBase1 = w.until(EC.presence_of_element_located((By.XPATH, text_HomeBasesList_HomeTerminal_AddUserClient_Users_AdministrationPageAdr))).text
    test_Global_Variables_apolloWebPortal.homeBase_List_Global = [homeBase1,]

    # SAVE new user with Username EXIST
    w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_AddUser_Users_AdministrationPageAdr))).click()
    try:
        errorMessage_UsernameExist = w.until(EC.presence_of_element_located((By.XPATH, errorMessage_UsernameExistAdr))).text
        #   Assert
        test_Name = "Negative Test PASSED - Username EXIST - Add User - Administration page"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_UsernameExist_Portal_Global
        condition2 = errorMessage_UsernameExist
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test PASSED - Username already EXIST - Add User - Administration page"
        print_Information_Var = errorMessage_UsernameExist
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        errorMessage_UsernameExist = ""
        #   Assert
        test_Name = "Negative Test FAILED - Username EXIST FAILED- Add User - Administration page:"
        condition1 = test_Global_Variables_apolloWebPortal.errorMessage_UsernameExist_Portal_Global
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    #       Screenshot
    test_Name = "User EXIST LC"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    w.until(EC.element_to_be_clickable((By.XPATH, button_CLOSE_Error_AddUser_Users_AdministrationPageAdr))).click()


    #***************************************
    # Create a New Limited Access Reseller User
    # + New Users button
    button_PlusNew_Users_AdministrationPage = w.until(EC.element_to_be_clickable((By.XPATH, button_PlusNew_Users_AdministrationPageAdr)))
    button_PlusNew_Users_AdministrationPage.click()
    #Select Carrier
    w.until(EC.element_to_be_clickable((By.ID, checkbox_CarrierUser_AddUser_Users_AdministrationPageId))).click()

    # New User informations
    input_Username_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.ID, input_Username_AddUser_Users_AdministrationPageId)))
    input_Username_AddUser_Users_AdministrationPage.send_keys(var_LimitedClient_UsernameVar)
    input_Email_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Email_AddUser_Users_AdministrationPageAdr)))
    input_Email_AddUser_Users_AdministrationPage.send_keys(var_LimitedClient_EmailVar)
    input_Password_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Password_AddUser_Users_AdministrationPageAdr)))
    input_Password_AddUser_Users_AdministrationPage.send_keys(var_LimitedClient_PasswordVar )
    input_ConfirmationPassword_AddUser_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_ConfirmationPassword_AddUser_Users_AdministrationPageAdr)))
    input_ConfirmationPassword_AddUser_Users_AdministrationPage.send_keys(var_LimitedClient_ConfirmationPasswordVar)

    #dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_Carrier_AddUser_Users_AdministrationPageId))))
    #dropdown_Carrier_AddUser_Users_AdministrationPage = dropDown.select_by_index(1)
    # Selenium can’t use Select with Angular dropDown
    dropDown_Carrier = w.until(EC.presence_of_element_located((By.XPATH, dropdown_Carrier_AddUser_Users_AdministrationPageAdr)))
    dropDown_Carrier.send_keys(text_CarrierLimited_Var)
    time.sleep(2)
    dropDown_Carrier.send_keys(Keys.ENTER)

    test_Global_Variables_apolloWebPortal.carriers_List_Global = text_CarrierLimited_Var

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_Role_AddUser_Users_AdministrationPageId))))
    dropdown_Role_AddUser_Users_AdministrationPage = dropDown.select_by_visible_text(var_RoleVar)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_TypeOfUser_AddUser_Users_AdministrationPageId))))
    dropDown = dropDown.select_by_visible_text(var_TypeOfUserVar)
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_TypeOfUser_AddUser_Users_AdministrationPageId))))
    dropdown_TypeOfUser_AddUser_Users_AdministrationPage_Read = dropDown.first_selected_option.text
    w.until(EC.element_to_be_clickable((By.XPATH, checkbox_HomeTerminal_HomeBasesList_AddUser_Users_AdministrationPageAdr))).click()

    #Home Base List
    test_Global_Variables_apolloWebPortal.homeBase_List_Global = [w.until((EC.presence_of_element_located((By.XPATH, "/html/body/ngb-modal-window/div/div/app-user-form/div[2]/user-modal-form-carrier/div/form/div[1]/div/div/div[8]/homebase-limit-list/div/div/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[2]")))).text]


    #print(f"Home Base    {homeBase}")

    #SAVE new user
    w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_AddUser_Users_AdministrationPageAdr))).click()

    # Verify New User Information on Users page
    # Search new user
    input_Search_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Users_AdministrationPageAdr)))
    time.sleep(2)
    input_Search_Users_AdministrationPage.send_keys(var_LimitedClient_UsernameVar)
    time.sleep(2)

    input_Username_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Username_Users_AdministrationPageAdr))).text
    test_Name = "New User USERNAME Saved - Administration page"
    condition1 = var_LimitedClient_UsernameVar
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
    condition1 = var_LimitedClient_EmailVar
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
    test_Name = "New User TYPE OF USER Saved - Administration page:"
    condition1 = dropdown_TypeOfUser_AddUser_Users_AdministrationPage_Read
    condition2 = input_TypeOfUser_Users_AdministrationPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New User TYPE OF USER Saved - Administration page:"
    print_Information_Var = dropdown_TypeOfUser_AddUser_Users_AdministrationPage_Read
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    input_Role_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Role_Users_AdministrationPageAdr))).text
    #   Assert
    test_Name = "New User ROLE Check - Administration page"
    condition1 = var_RoleVar
    condition2 = input_Role_Users_AdministrationPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New User ROLE Check - Administration page"
    print_Information_Var = input_Role_Users_AdministrationPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "New LC User"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    input_Search_Users_AdministrationPage = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Users_AdministrationPageAdr)))
    input_Search_Users_AdministrationPage.send_keys("A")
    w.until(EC.element_to_be_clickable((By.XPATH, button_SearchClean_Users_AdministrationPageAdr))).click()

    #########################################################################################################################################
    # LOGIN WITH THE NEW USER AND CHECK ALL ACCESS FUNCTION ON THE MAIN MENU
    # BASED ON THE USER HIERARCHY
    #########################################################################################################################################
    print('******************************Verifying the Limited Client Functions Available - Edge Browser')

    var_UsernameVar = var_LimitedClient_UsernameVar
    var_PasswordVar = var_LimitedClient_PasswordVar
    text_CarrierType = var_CarrierFull_Var
    print(f'Adm Limited Client = {siteAddressVar}')
    test_Global_Variables_apolloWebPortal.userROLE_Global = int()
    test_Global_Variables_apolloWebPortal.userTYPE_Global = 5
    test_NewUser_Check_Hierarchy_User_Access_ManagePage_apolloWebPortal.NewUser_Check_Hierarchy_User_Access_MenuPage(driver, driver_Name, driver_Version, carrier, truckDriversList, var_UsernameVar, var_PasswordVar, text_CarrierType, siteAddressVar)

    print("********** END LIMITED CLIENT TEST **********")
    return()


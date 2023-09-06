#               Apollo Web Portal - ADMINISTRATION USERS
#                   FULL ACCESS CLIENT


def Administration_Users_MasterReseller_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList,siteAddressVar):

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
    import test_Hierarchy_User_Access_ManagePage_apolloWebPortal

    #              ADMINISTRATION / ROLES Main

   #       Global Fields Address
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
    button_Manage_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Manage_ManagePageAdr_Global
    dropdown_Carrier_Manage_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.dropdown_Carrier_Manage_AdministrationPageAdr_Global

    # Add User page"
    checkbox_ResellerUser_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.checkbox_ResellerUser_AddUser_Users_AdministrationPageId_Global
    checkbox_CarrierUser_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.checkbox_CarrierUser_AddUser_Users_AdministrationPageId_Global
    input_Username_AddUser_Users_AdministrationPageId = test_Global_Addresses_apolloWebPortal.input_Username_AddUser_Users_AdministrationPageId_Global
    input_Email_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Email_AddUser_Users_AdministrationPageAdr_Global
    input_Password_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Password_AddUser_Users_AdministrationPageAdr_Global
    input_ConfirmationPassword_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.input_Password_AddUser_Users_AdministrationPageAdr_Global
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
    table_CarrierList_AddUser_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.table_CarrierList_AddUser_Users_AdministrationPageAdr_Global
    dropdown_Carriers_AddUserOpen_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.dropdown_Carriers_AddUserOpen_Users_AdministrationPageAdr_Global
    dropdown_Carriers_AddUserSelect_Users_AdministrationPageAdr = test_Global_Addresses_apolloWebPortal.dropdown_Carriers_AddUserSelect_Users_AdministrationPageAdr_Global

    #   Global Variables
    var_MasterReseller_UsernameVar = test_Global_Variables_apolloWebPortal.var_MasterReseller_UsernameVar_Global
    var_MasterReseller_EmailVar = test_Global_Variables_apolloWebPortal.var_MasterReseller_EmailVar_Global
    var_MasterReseller_PasswordVar = test_Global_Variables_apolloWebPortal.var_MasterReseller_PasswordVar_Global
    var_MasterReseller_ConfirmationPasswordVar = test_Global_Variables_apolloWebPortal.var_MasterReseller_ConfirmationPasswordVar_Global
    var_Username_ExistVar = test_Global_Variables_apolloWebPortal.var_Username_ExistVar_Global
    var_MasterReseller_TypeOfUserVar = test_Global_Variables_apolloWebPortal.var_MasterReseller_TypeOfUserVar_Global
    text_CarrierFull_Var = test_Global_Variables_apolloWebPortal.text_CarrierFull_Var_Global
    text_CarrierLimited_Var = test_Global_Variables_apolloWebPortal.text_CarrierLimited_Var_Global
    workbookDB = test_Global_Variables_apolloWebPortal.workbookDB_Global
    worksheetDB = test_Global_Variables_apolloWebPortal.worksheetDB_Global

    #       Variables

    Ref_DVIR_DVIRPage = "Roles"


    w = WebDriverWait(driver, 40)

    #       #######################################     Main functions    ########################################################
    #   ###############################################################################################################################
    print('******************************Test Master Reseller')
#   Page Title on TCReport
    function_Name = "MASTER RESELLER Users - Administration Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

#       Function Administration Users side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_Administration_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv,10).until(EC.element_to_be_clickable((By.ID, button_Administration_ManagePageId))).click()
    button_Administration_Users_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv, 10).until(EC.element_to_be_clickable((By.XPATH, button_Administration_Users_ManagePageAdr))).click()
    time.sleep(2)
    #       Title of the right page
    title_Users_AdinistrationPage = w.until(EC.presence_of_element_located((By.XPATH, title_Users_AdinistrationPageAdr))).text
    test_Name = "Admin page" + " MR"
    condition1 = "Users"
    condition2 = title_Users_AdinistrationPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "MASTER RESELLER Users - Administration Function"
    print_Information_Var = title_Users_AdinistrationPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)

    # Test Master Reseller Functions Access

    #########################################################################################################################################
    # LOGIN WITH THE NEW USER AND CHECK ALL ACCESS FUNCTION ON THE MAIN MENU
    # BASED ON THE USER HIERARCHY
    #########################################################################################################################################
    print('******************************Verifying the Master Reseller Functions Available - Edge Browser')
    text_CarrierType = text_CarrierFull_Var
    test_Global_Variables_apolloWebPortal.userROLE_Global = int()
    test_Global_Variables_apolloWebPortal.userTYPE_Global = 1
    test_Hierarchy_User_Access_ManagePage_apolloWebPortal.Hierarchy_User_Access_MenuPage(driver, driver_Name, driver_Version, carrier, truckDriversList, text_CarrierType)

    text_CarrierType = text_CarrierLimited_Var
    test_Global_Variables_apolloWebPortal.userROLE_Global = int()
    test_Global_Variables_apolloWebPortal.userTYPE_Global = 1
    test_Hierarchy_User_Access_ManagePage_apolloWebPortal.Hierarchy_User_Access_MenuPage(driver, driver_Name, driver_Version, carrier, truckDriversList, text_CarrierType)

    print("********** END MASTER RESELLER TEST **********")
    return()
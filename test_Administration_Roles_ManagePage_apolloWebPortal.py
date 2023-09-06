#               Apollo Web Portal - ADMINISTRATION ROLES

def Administration_Roles_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList):

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

    #              ADMINISTRATION / ROLES Main

    #       Fields Address
    menuRegion_MainSideBar_ManagePageAdrAsideDiv = "/html/body/app-root/app-main/div/main-side-bar/aside/div"

    # Roles page
    button_Administration_ManagePageId = 'administration'
    button_Roles_Administration_ManagePageAdr = '//a[contains(@href,"/roles")]'
    #button_Roles_Administration_ManagePageAdr = "/html/body/app-root/app-main/div/main-side-bar/aside/div/div[4]/div/div/nav/ul/li[17]/ul/li[1]"
    button_User_Administration_ManagePageAdr = '//a[contains(@href,"/users")]'
    title_Roles_Administration_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/role-list/div/div/div[1]/h3"
    button_PlussNew_Roles_Administration_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/role-list/div/div/div[1]/div/button"
    input_Search_Roles_Administration_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/role-list/div/div/div[2]/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[1]/input"
    button_SearchClear_Roles_Administration_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/role-list/div/div/div[2]/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[2]/span"
    text_Name_Roles_Administration_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/role-list/div/div/div[2]/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[1]"
    text_Carrier_Roles_Administration_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/role-list/div/div/div[2]/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[2]/div"
    button_EditRole_Actions_Roles_Administration_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/role-list/div/div/div[2]/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[3]/div/button[1]"
    button_DeleteRole_Actions_Roles_Administration_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/role-list/div/div/div[2]/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[3]/div/button[2]"
    button_ConfirmationDeleteRole_Actions_Roles_Administration_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-confirmation-dialog/div[3]/button[1]"

    #Add Role page

    dropDown_CarrierWrite_AddRole_Roles_Administration_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-role-modal-form/div[2]/form/div/div[1]/div[1]/div/ng-select/div/div/div[3]/input"
    dropDown_CarrierRead_AddRole_Roles_Administration_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-role-modal-form/div[2]/form/div/div[1]/div[1]/div/ng-select/div"
    input_Name_AddRole_Roles_Administration_ManagePageId = "roleName"
    message_Name_AddRole_Roles_Administration_ManagePageId = "number-error"
    errorMessage_NameAdr = "/html/body/ngb-modal-window/div/div/app-role-modal-form/div[2]/form/div/div[1]/div[2]/div/span"
    checkBox_CarrierFull_Premission_AddRole_Roles_Administration_ManagePageId = "carrier-full"
    checkBox_CarrierView_Premission_AddRole_Roles_Administration_ManagePageId = "carrier-view"
    checkBox_HomeBaseFull_Premission_AddRole_Roles_Administration_ManagePageId = "home-base-full"
    checkBox_HomeBaseView_Premission_AddRole_Roles_Administration_ManagePageId = "home-base-view"
    checkBox_DriverFull_Premission_AddRole_Roles_Administration_ManagePageId = "driver-full"
    checkBox_DriverView_Premission_AddRole_Roles_Administration_ManagePageId = "driver-view"
    checkBox_AssetFull_Premission_AddRole_Roles_Administration_ManagePageId = "asset-full"
    checkBox_AssetView_Premission_AddRole_Roles_Administration_ManagePageId = "asset-view"
    checkBox_NotificationFull_Premission_AddRole_Roles_Administration_ManagePageId = "notification-full"
    checkBox_NotificationView_Premission_AddRole_Roles_Administration_ManagePageId = "notification-view"
    checkBox_LogbookAccess_Premission_AddRole_Roles_Administration_ManagePageId = "logbook-view"
    checkBox_LogbookEdit_Premission_AddRole_Roles_Administration_ManagePageId = "logbook-edit"
    checkBox_LogbookEditRemark_Premission_AddRole_Roles_Administration_ManagePageId = "logbook-edit-remark"
    checkBox_LogbookExport_Premission_AddRole_Roles_Administration_ManagePageId = "logbook-export"
    #Must include the other Role Permission options
    button_SAVE_AddRole_Roles_Administration_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-role-modal-form/div[2]/div/button[1]"
    button_CLOSE_AddRole_Roles_Administration_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-role-modal-form/div[2]/div/button[2]"
    title_Engine_Diagnostic_Access_AddRole_Roles_Administration_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-role-modal-form/div[2]/form/div/div[2]/permission-list/form/table/thead/tr[6]/td[1]/ul/li/ul/li/div/label"
    dropDown_Carrier_EditAddRole_Roles_Administration_ManagePageId = "select2-carrierSelector-container"
    button_DeleteRole_Confirm_Actions_Roles_Administration_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-confirmation-dialog/div[3]/button[1]"

    #   Global Variables

    workbookDB = test_Global_Variables_apolloWebPortal.workbookDB_Global
    worksheetDB = test_Global_Variables_apolloWebPortal.worksheetDB_Global
    text_Carrier_AddRole_Roles_Administration_ManagePageVar = test_Global_Variables_apolloWebPortal.text_CarrierFull_Var_Global

    #       Variables
    w = WebDriverWait(driver, 30)
    text_Name_AddRole_Roles_Administration_ManagePageVar = "QA_RoleTest_Delete"
    text_NameExist_Role_Administration_ManagePageVar = "QA Role"

    #   ################################################     DVIR Main functions    ###################################################
    #   ###############################################################################################################################

#   Page Title on TCReport
    function_Name = "Roles function- Administration page"
    tc_reports.function_Init_Page(function_Name, driver_Name)

#       Function Administration side bar button click

    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_Administration_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv,10).until(EC.element_to_be_clickable((By.ID, button_Administration_ManagePageId))).click()
    time.sleep(2)
    try:
        button_Roles_Administration_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv, 10).until(EC.element_to_be_clickable((By.XPATH, button_Roles_Administration_ManagePageAdr))).click()
    except:
        button_Administration_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv, 10).until(EC.element_to_be_clickable((By.ID, button_Administration_ManagePageId))).click()
        time.sleep(2)
        button_Roles_Administration_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv, 10).until(EC.element_to_be_clickable((By.XPATH, button_Roles_Administration_ManagePageAdr))).click()
    #       Screenshot

    #test_Name = "Roles"
    #tc_reports.screenshot(driver, driver_Name, test_Name)
    time.sleep(3)
    button_Roles_Administration_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv, 10).until(EC.element_to_be_clickable((By.XPATH, button_Roles_Administration_ManagePageAdr))).click()
#       Title of the right page
    title_Roles_Administration_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_Roles_Administration_ManagePageAdr))).text
    test_Name = "ROLES page open"
    condition1 = "Roles"
    condition2 = title_Roles_Administration_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Roles Page open:"
    print_Information_Var = title_Roles_Administration_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)
    print(f'Page: {title_Roles_Administration_ManagePage}')

    # Delete Test Role "QA_RoleTest_Delete"
    search = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Roles_Administration_ManagePageAdr)))
    search.send_keys(text_Name_AddRole_Roles_Administration_ManagePageVar)
    time.sleep(2)
    #       Screenshot
    test_Name = "Delete Role"
    tc_reports.screenshot(driver, driver_Name, test_Name)
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, button_DeleteRole_Actions_Roles_Administration_ManagePageAdr))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, button_ConfirmationDeleteRole_Actions_Roles_Administration_ManagePageAdr))).click()
    except:
        print('No Role QA_RoleTest_Delete')
    w.until(EC.element_to_be_clickable((By.XPATH, button_SearchClear_Roles_Administration_ManagePageAdr))).click()


    #*************************************************************************************************************
    # Create a NEW ROLE
    w.until(EC.element_to_be_clickable((By.XPATH, button_PlussNew_Roles_Administration_ManagePageAdr))).click()

    #*************************************************************************************************************
    # Negative Test
    # Empty Role Name
    input_Name_AddRole_Roles_Administration_ManagePage = w.until(EC.presence_of_element_located((By.ID, input_Name_AddRole_Roles_Administration_ManagePageId)))
    input_Name_AddRole_Roles_Administration_ManagePage.send_keys("")
    input_Name_AddRole_Roles_Administration_ManagePage.send_keys(Keys.TAB)
    try:
        errorMessage_Name = w.until(EC.presence_of_element_located((By.XPATH, errorMessage_NameAdr))).text
        #   Assert
        test_Name = "Name MUST have at least 1 caracteres - Add Role - Administration page"
        condition1 = "This field is required"
        condition2 = errorMessage_Name
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test - Name must have at least 1 caracteres - Add User - Administration page"
        print_Information_Var = errorMessage_Name
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #   Assert
        test_Name = "Message Username must have at least 1 caracteres - Add User - Administration page"
        condition1 = "This field is required"
        condition2 = errorMessage_Name
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Negative Test - Message Username must have at least 1 caracteres - Add User - Administration page"
        print_Information_Var = errorMessage_Name
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)



    #*************************************************************************************************************
    # Create a NEW ROLE


    # Select CARRIER:
    dropDown_Client = w.until(EC.presence_of_element_located((By.XPATH,     dropDown_CarrierWrite_AddRole_Roles_Administration_ManagePageAdr)))
    dropDown_Client.send_keys(text_Carrier_AddRole_Roles_Administration_ManagePageVar)
    time.sleep(2)
    dropDown_Client.send_keys(Keys.ENTER)


    # Role Name
    input_Name_AddRole_Roles_Administration_ManagePage = w.until(EC.presence_of_element_located((By.ID, input_Name_AddRole_Roles_Administration_ManagePageId)))
    input_Name_AddRole_Roles_Administration_ManagePage.send_keys(text_Name_AddRole_Roles_Administration_ManagePageVar)
    #Permissions set
    checkBox_HomeBaseView_AddRoleStatus = w.until(EC.element_to_be_clickable((By.ID, checkBox_HomeBaseView_Premission_AddRole_Roles_Administration_ManagePageId))).click()
    checkBox_AssetView_AddRoleStatus = w.until(EC.element_to_be_clickable((By.ID, checkBox_AssetView_Premission_AddRole_Roles_Administration_ManagePageId))).click()
    checkBox_LogbookAccess_AddRoleStatus = w.until(EC.element_to_be_clickable((By.ID, checkBox_LogbookAccess_Premission_AddRole_Roles_Administration_ManagePageId))).click()
    # Move down the page
    a = w.until(EC.presence_of_element_located((By.XPATH, title_Engine_Diagnostic_Access_AddRole_Roles_Administration_ManagePageAdr)))
    actions = ActionChains(driver)
    actions.move_to_element(a)
    actions.perform()
    w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_AddRole_Roles_Administration_ManagePageAdr))).click()
    #       Screenshot
    test_Name = "Create Role"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #*****************************************************************************************************************************
    # Verify the NEW ROLE
    search = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Roles_Administration_ManagePageAdr)))
    search.send_keys(text_Name_AddRole_Roles_Administration_ManagePageVar)
    time.sleep(2)
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, button_EditRole_Actions_Roles_Administration_ManagePageAdr))).click()
    except:
        print('New Role QA_RoleTest_Delete open')


    #Test Role Carrier saved
    dropDown_CarrierRead_AddRole_Roles_Administration_ManagePageRead = w.until(EC.presence_of_element_located((By.XPATH,     dropDown_CarrierRead_AddRole_Roles_Administration_ManagePageAdr))).text



    #   Assert
    test_Name = "New Carrier Saved  - Role - Administration page"
    condition1 = text_Carrier_AddRole_Roles_Administration_ManagePageVar
    condition2 = dropDown_CarrierRead_AddRole_Roles_Administration_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New Carrier Saved - Role - Administration page"
    print_Information_Var = dropDown_CarrierRead_AddRole_Roles_Administration_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #Test Role Name saved - ACTION EDIT ROLE
    input_Name_EditAddRole_Roles_Administration_ManagePage = w.until(EC.presence_of_element_located((By.ID, input_Name_AddRole_Roles_Administration_ManagePageId)))
    input_Name_EditAddRole_Roles_Administration_ManagePage = input_Name_EditAddRole_Roles_Administration_ManagePage.get_attribute('value')
    #   Assert
    test_Name = "New Name Saved - Role - Administration page"
    condition1 = text_Name_AddRole_Roles_Administration_ManagePageVar
    condition2 = input_Name_EditAddRole_Roles_Administration_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New Name Saved - Role - Administration page"
    print_Information_Var = input_Name_EditAddRole_Roles_Administration_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Verify new Role"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #Verify the 9 Permission Checked

    checkBox_HomeBaseView_AddRoleStatus = w.until(EC.element_to_be_clickable((By.ID, checkBox_HomeBaseView_Premission_AddRole_Roles_Administration_ManagePageId)))
    if checkBox_HomeBaseView_AddRoleStatus.is_selected():
        #       Print Assert OK
        print_Information_Fix = "Permission Home Base Full = Selected"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    else:
        #   Assert
        test_Name = "Permission Home Base Full = Selected"
        condition1 = "Permission Home Base Full = Selected"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    checkBox_AssetView_AddRoleStatus = w.until(EC.element_to_be_clickable((By.ID, checkBox_AssetView_Premission_AddRole_Roles_Administration_ManagePageId)))
    if checkBox_AssetView_AddRoleStatus.is_selected():
        #       Print Assert OK
        print_Information_Fix = "Permission Asset View = Selected"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    else:
        #   Assert
        test_Name = "Permission Asset View = Selected"
        condition1 = "Permission Asset View = Selected"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    checkBox_LogbookAccess_AddRoleStatus = w.until(EC.element_to_be_clickable((By.ID, checkBox_LogbookAccess_Premission_AddRole_Roles_Administration_ManagePageId)))
    if checkBox_LogbookAccess_AddRoleStatus.is_selected():
        #       Print Assert OK
        print_Information_Fix = "Permission LogBook Access = Selected"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    else:
        #   Assert
        test_Name = "Permission LogBook Access = Selected OK"
        condition1 = "Permission LogBook Access = Selected"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)


    # Edit Role CLOSE
    #   Move down the page

    w.until(EC.element_to_be_clickable((By.ID, checkBox_LogbookAccess_Premission_AddRole_Roles_Administration_ManagePageId))).click()
    a = w.until(EC.presence_of_element_located((By.XPATH, title_Engine_Diagnostic_Access_AddRole_Roles_Administration_ManagePageAdr)))
    actions = ActionChains(driver)
    actions.move_to_element(a)
    actions.perform()
    w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_AddRole_Roles_Administration_ManagePageAdr))).click()

    # Verify Actions available for a Role That was NOT assigned to any User - Edit and Delete MUST be available
    # Select the New Role created - Not assigned to anyone yet
    time.sleep(1)
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, button_SearchClear_Roles_Administration_ManagePageAdr))).click()
    except:
        print()
    search = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Roles_Administration_ManagePageAdr)))
    search.send_keys(text_Name_AddRole_Roles_Administration_ManagePageVar)
    time.sleep(2)
    #   EDIT ROLE
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, button_EditRole_Actions_Roles_Administration_ManagePageAdr))).click()
        #       Print Assert OK
        print_Information_Fix = "Edit Role Available"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        # Edit Role CLOSE
        #   Move down the page
        a = w.until(EC.presence_of_element_located((By.XPATH, title_Engine_Diagnostic_Access_AddRole_Roles_Administration_ManagePageAdr)))
        #a = w.until(EC.presence_of_element_located((By.XPATH, "/html/body/ngb-modal-window/div/div/app-role-modal-form/div[2]/div/button[2]")))
        actions = ActionChains(driver)
        actions.move_to_element(a)
        actions.perform()
        w.until(EC.element_to_be_clickable((By.XPATH, button_CLOSE_AddRole_Roles_Administration_ManagePageAdr))).click()
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)
    except:
        test_Name = "Action - Edit Role button NOT Available"
        condition1 = "Button NOT Available"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Action - Edit Role button NOT Available"
        print_Information_Var = "Button NOT Available"
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)

    #   DELETE ROLE
    try:
        #Test Delete button and delete Role
        w.until(EC.element_to_be_clickable((By.XPATH, button_DeleteRole_Actions_Roles_Administration_ManagePageAdr))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, button_DeleteRole_Confirm_Actions_Roles_Administration_ManagePageAdr))).click()
        #       Print Assert OK
        print_Information_Fix = "Action - Delete Role Available"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        test_Name = "Action - Delete Role button NOT Available"
        condition1 = "Delete Button NOT Available"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Action - Delete Role button NOT Available"
        print_Information_Var = "Delete Button NOT Available"
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)

    # Verify if "QA_RoleTest_Delete was delete properly"
    w.until(EC.element_to_be_clickable((By.XPATH, button_SearchClear_Roles_Administration_ManagePageAdr))).click()
    search = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Roles_Administration_ManagePageAdr)))
    search.send_keys(text_Name_AddRole_Roles_Administration_ManagePageVar)
    time.sleep(2)
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, button_DeleteRole_Actions_Roles_Administration_ManagePageAdr))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, button_ConfirmationDeleteRole_Actions_Roles_Administration_ManagePageAdr))).click()
        test_Name = "Role was NOT Deleted"
        condition1 = "Role Not deleted"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Action - Delete Role button Available"
        print_Information_Var = "Delete Button Available"
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)
    except:
        test_Name = "Role was Deleted"
        condition1 = "Role deleted"
        condition2 = "Role deleted"
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Role was Deleted"
        print_Information_Var = "Role was Deleted"
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    w.until(EC.element_to_be_clickable((By.XPATH, button_SearchClear_Roles_Administration_ManagePageAdr))).click()

    search = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Roles_Administration_ManagePageAdr)))
    search.send_keys(text_NameExist_Role_Administration_ManagePageVar)
    time.sleep(2)


    #   EDIT ROLE
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, button_EditRole_Actions_Roles_Administration_ManagePageAdr))).click()
        #       Print Assert OK
        print_Information_Fix = "Action - Edit Role Available"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        # Verify SAVE button is available
        try:
            # Verify SAVE button - must not be available
            #   Move down the page
            a = w.until(EC.presence_of_element_located((By.XPATH, title_Engine_Diagnostic_Access_AddRole_Roles_Administration_ManagePageAdr)))
            actions = ActionChains(driver)
            actions.move_to_element(a)
            actions.perform()
            w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_AddRole_Roles_Administration_ManagePageAdr))).click()
            test_Name = "Assigned Role SAVE button IS Available"
            condition1 = "Assigned Role SAVE Button IS Available"
            condition2 = ""
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "Assigned Role SAVE button IS Available"
            print_Information_Var = "Assigned Role SAVE Button IS Available"
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
            #       Screenshot
            tc_reports.screenshot(driver, driver_Name, test_Name)
        except:
            test_Name = "Assigned Role SAVE button NOT Available"
            condition1 = "Assigned Role SAVE Button NOT Available"
            condition2 = "Assigned Role SAVE Button NOT Available"
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "Assigned Role SAVE button NOT Available"
            print_Information_Var = "Assigned Role SAVE Button NOT Available"
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
            #       Screenshot
            tc_reports.screenshot(driver, driver_Name, test_Name)
    except:
        test_Name = "Edit button NOT Available"
        condition1 = "Edit Button NOT Available"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Edit button NOT Available"
        print_Information_Var = "Edit Button NOT Available"
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)
        print('IMPORTANT -> QA Role does not on the Role DB to be teste- Please create a on DB')

    # Edit Role CLOSE
    #   Move down the page
    a = w.until(EC.presence_of_element_located((By.XPATH, button_CLOSE_AddRole_Roles_Administration_ManagePageAdr)))
    actions = ActionChains(driver)
    actions.move_to_element(a)
    actions.perform()
    w.until(EC.element_to_be_clickable((By.XPATH, button_CLOSE_AddRole_Roles_Administration_ManagePageAdr))).click()
    

    #   DELETE Assigned ROLE
    w.until(EC.element_to_be_clickable((By.XPATH, button_DeleteRole_Actions_Roles_Administration_ManagePageAdr))).click()
    w.until(EC.element_to_be_clickable((By.XPATH, button_DeleteRole_Confirm_Actions_Roles_Administration_ManagePageAdr))).click()
    time.sleep(2)
    try:
        # Test Delete button 2nd time to assure Role was NOT deleted
        w.until(EC.element_to_be_clickable((By.XPATH, button_DeleteRole_Actions_Roles_Administration_ManagePageAdr))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, button_DeleteRole_Confirm_Actions_Roles_Administration_ManagePageAdr))).click()
        test_Name = "Assigned Role NOT Delete"
        condition1 = "Assigned Role NOT Delete"
        condition2 = "Assigned Role NOT Delete"
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        test_Name = "Assigned Role NOT Delete"
        print_Information_Fix = "Assigned Role NOT Delete"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)
    except:
        #       Print Assert OK
        test_Name = "Assigned Role Delete"
        condition1 = "Assigned Role Delete"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Assigned Role Delete"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)

    # Verify if "QA_RoleTest was NOT Delete"
    w.until(EC.element_to_be_clickable((By.XPATH, button_SearchClear_Roles_Administration_ManagePageAdr))).click()
    search = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Roles_Administration_ManagePageAdr)))
    search.send_keys(text_NameExist_Role_Administration_ManagePageVar)
    time.sleep(2)
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, button_EditRole_Actions_Roles_Administration_ManagePageAdr))).click()
        test_Name = "Assigned Role was NOT Deleted"
        condition1 = "Assigned Role was Not Deleted"
        condition2 = "Assigned Role was Not Deleted"
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Assigned Role was NOT Deleted"
        print_Information_Var = "Assigned Role was NOT Deleted"
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)
    except:
        test_Name = "Assigned Role was Deleted"
        condition1 = "Assigned Role deleted"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Assigned Role was Deleted"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Move down the page
    a = w.until(EC.presence_of_element_located((By.XPATH, button_CLOSE_AddRole_Roles_Administration_ManagePageAdr)))
    actions = ActionChains(driver)
    actions.move_to_element(a)
    actions.perform()
    w.until(EC.element_to_be_clickable((By.XPATH, button_CLOSE_AddRole_Roles_Administration_ManagePageAdr))).click()
    w.until(EC.element_to_be_clickable((By.XPATH, button_SearchClear_Roles_Administration_ManagePageAdr))).click()


    return ()







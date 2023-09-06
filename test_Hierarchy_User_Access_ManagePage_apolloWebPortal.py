#               Apollo Web Portal - HIERARCHY USERS

def Hierarchy_User_Access_MenuPage (driver, driver_Name, driver_Version, carrier, truckDriversList, text_CarrierType):

    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.select import Select
    import tc_reports
    import test_Global_Variables_apolloWebPortal
    import test_Global_Addresses_apolloWebPortal
    import time

    #       Carrier details Page Address & Variables
    #       Fields Address

    homeBase_Available_ListAdr = test_Global_Addresses_apolloWebPortal.homeBase_Available_ListAdr_Global
    button_Carrier_HomeBases_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[3]"
    title_ManagePageAdr = test_Global_Addresses_apolloWebPortal.title_ManagePageAdr_Global
    title_UserType_ManagePageAdr = test_Global_Addresses_apolloWebPortal.title_UserType_ManagePageAdr_Global
    dropDown_CarrierName_Manage_ManagePageAdr = test_Global_Addresses_apolloWebPortal.dropDown_CarrierName_Manage_ManagePageAdr_Global
    # Common Buttons - All Users type (14):
    button_Manage_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Manage_ManagePageAdr_Global
    button_LogBooks_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_LogBooks_ManagePageAdr_Global
    button_UnidentifiedLogs_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_UnidentifiedLogs_ManagePageAdr_Global
    button_LogEdits_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_LogEdits_ManagePageAdr_Global
    button_Dashboards_ManagePageId = test_Global_Addresses_apolloWebPortal.button_Dashboards_ManagePageId_Global
    button_Violations_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Violations_ManagePageAdr_Global
    button_DVIR_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_DVIR_ManagePageAdr_Global
    button_WorkOrder_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_WorkOrder_ManagePageAdr_Global
    button_EnhancedIFTA_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_EnhancedIFTA_ManagePageAdr_Global
    button_IFTA_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_IFTA_ManagePageAdr_Global
    button_DriverRecords_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_DriverRecords_ManagePageAdr_Global
    button_FMCSARecords_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_FMCSARecords_ManagePageAdr_Global
    button_Shipments_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Shipments_ManagePageAdr_Global
    button_EngineDiagnostic_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_EngineDiagnostic_ManagePageAdr_Global
    button_DriverDutyReport_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_DriverDutyReport_ManagePageAdr_Global
    dropDown_CarrierName_ManagePageId = test_Global_Addresses_apolloWebPortal.dropDown_CarrierName_ManagePageId_Global

    # Special Buttons for Reseller and Full Acces Client (1+2):
    button_Administration_ManagePageId = test_Global_Addresses_apolloWebPortal.button_Administration_ManagePageId_Global
    button_Administration_Roles_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Administration_Roles_ManagePageAdr_Global
    button_Administration_Users_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Administration_Users_ManagePageAdr_Global

    # Special Buttons for Master Reseller (2)
    button_Billing_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Billing_ManagePageAdr_Global
    button_BillingReport_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_BillingReport_ManagePageAdr_Global
    title_apollo_Portal_VersionAdr = test_Global_Addresses_apolloWebPortal.title_apollo_Portal_VersionAdr_Global

    # LIMITED CLIENT TEST
    button_Carrier_Assets_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Carrier_Assets_ManagePageAdr_Global
    button_Notifications_Carrier_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Notifications_Carrier_ManagePageAdr_Global
    dropDown_CarrierName_ManagePageAdr = test_Global_Addresses_apolloWebPortal.dropDown_CarrierName_ManagePageAdr_Global
    dropDown_CarrierName_ManagePageListAdr = test_Global_Addresses_apolloWebPortal.dropDown_CarrierName_ManagePageListAdr_Global


    #       Variables
    w = WebDriverWait(driver, 10)
    control_Reportfile = 0
    print_Information_Fix = ""
    print_Information_Var = ""
    global carriers_List_Global
    global homeBase_List_Global

    #       Main

    #       #######################################     Main Menu functions    ########################################################
    #   ###############################################################################################################################
    #   Page Title on TCReport
    function_Name = "Main Menu options based on Hierarchy User Function - open EDGE Browser"
    tc_reports.function_Init_Page(function_Name, driver_Name)
    function_Name = text_CarrierType
    tc_reports.function_Init_Page(function_Name, driver_Name)

    w.until(EC.element_to_be_clickable((By.XPATH, button_Manage_ManagePageAdr))).click()
    # Verify User Type
    title_UserType_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_UserType_ManagePageAdr))).text
    title_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_ManagePageAdr))).text
    #       Print User Type
    print_Information_Fix = "User Type:"
    print_Information_Var = title_UserType_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    if title_UserType_ManagePage == "QAFullAccessReseller" or title_UserType_ManagePage == "QAMasterReseller":
        button_Manage_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_Manage_ManagePageAdr))).click()
        dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDown_CarrierName_Manage_ManagePageAdr))))
        dropDown_CarrierName_Manage_ManagePage = dropDown.select_by_visible_text(text_CarrierType)

    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Hier" + title_UserType_ManagePage
    condition1 = "Manage"
    condition2 = title_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Manage page - Manage page open:"
    print_Information_Var = title_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)
    # **************** Test and report results at TCReports END  ************************************************************************************



    """
    #******************************************
    #Common Buttons - All Users type (14) Test:
    #******************************************
    print("Testing All Users Functions available")
    button_Manage_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_Manage_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: MANAGE"
    condition1 = "Manage"
    condition2 = button_Manage_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: MANAGE"
    print_Information_Var = button_Manage_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_LogBooks_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_LogBooks_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: LOG BOOKS"
    condition1 = "Log Books"
    condition2 = button_LogBooks_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: LOG BOOKS"
    print_Information_Var = button_LogBooks_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_UnidentifiedLogs_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_UnidentifiedLogs_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: UNIDENTIFIED LOGS"
    condition1 = "Unidentified Logs"
    condition2 = button_UnidentifiedLogs_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: UNIDENTIFIED LOGS"
    print_Information_Var = button_UnidentifiedLogs_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_LogEdits_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_LogEdits_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: LOG EDITS"
    condition1 = "Log Edits"
    condition2 = button_LogEdits_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: LOG EDITS"
    print_Information_Var = button_LogEdits_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_Dashboards_ManagePage = w.until(EC.presence_of_element_located((By.ID, button_Dashboards_ManagePageId))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: DASHBOARD"
    condition1 = "Dashboard"
    condition2 = button_Dashboards_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: DASHBOARD"
    print_Information_Var = button_Dashboards_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_Violations_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_Violations_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: VIOLATIONS"
    condition1 = "Violations"
    condition2 = button_Violations_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: VIOLATIONS"
    print_Information_Var = button_Violations_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_DVIR_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_DVIR_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: DVIR"
    condition1 = "DVIR"
    condition2 = button_DVIR_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: DVIR"
    print_Information_Var = button_DVIR_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #Based on Carrier setup
    try:
        button_WorkOrder_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_WorkOrder_ManagePageAdr))).text
        if text_CarrierType == "QA Carrier":
            #       Assert Test and print if assert is fail
            test_Name = "QA Carrier - Option: WORK ORDER"
            condition1 = "Work Order"
            condition2 = button_WorkOrder_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "QA Carrier - Option: WORK ORDER"
            print_Information_Var = button_WorkOrder_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

        else:
            #Error - Carrier not allowed
            #       Assert Test and print if assert is fail
            test_Name = "QA Carrier Limited has NOT Set to use Work Order"
            condition1 = ""
            condition2 = button_WorkOrder_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    except:
        if text_CarrierType == "QA Carrier":
            #       Assert Test and print if assert is fail
            test_Name = "QA Carrier MUST have Work Order function"
            condition1 = ""
            condition2 = "Work Order"
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "QA Carrier Limited have NO Work Order functionality"
            condition1 = "NO Work Order"
            condition2 = "NO Work Order"
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "QA Carrier Limited have NO Work Order functionality"
            print_Information_Var = "NO Work Order"
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #IFTA
    try:
        button_EnhancedIFTA_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_EnhancedIFTA_ManagePageAdr))).text
        assert button_EnhancedIFTA_ManagePage in "Enhanced IFTA"
        assert text_CarrierType in "QA Carrier"
        #       Assert Test and print if assert is fail
        test_Name = "QA Carrier has: Enhanced IFTA"
        condition1 = str("Enhanced IFTA")
        condition2 = str(button_EnhancedIFTA_ManagePage)
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "QA Carrier has: Enhanced IFTA"
        print_Information_Var = button_EnhancedIFTA_ManagePage
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #Screenshot
        test_Name = "CarrierFull"
        tc_reports.screenshot(driver, driver_Name, test_Name)
    except:
        try:
            button_IFTA_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_IFTA_ManagePageAdr))).text
            assert button_IFTA_ManagePage in "IFTA"
            assert text_CarrierType in "QA Carrier Limited"
            #       Assert Test and print if assert is fail
            test_Name = "QA Carrier Limited has: IFTA"
            condition1 = "IFTA"
            condition2 = button_IFTA_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "QA Carrier Limited has: IFTA"
            print_Information_Var = button_IFTA_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
            # Screenshot
            test_Name = "CarrierLimited"
            tc_reports.screenshot(driver, driver_Name, test_Name)
        except:
            if text_CarrierType == "QA Carrier":
                #       Assert Test and print if assert is fail
                test_Name = "Enhanced IFTA button ERROR"
                condition1 = "%"
                condition2 = ""
                tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            else:
                #       Assert Test and print if assert is fail
                test_Name = "IFTA button ERROR"
                condition1 = "%"
                condition2 = ""
                tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    button_DriverRecords_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_DriverRecords_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: DRIVER RECORDS"
    condition1 = "Driver Records"
    condition2 = button_DriverRecords_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: DRIVER RECORDS"
    print_Information_Var = button_DriverRecords_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_FMCSARecords_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_FMCSARecords_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: FMCSA Records"
    condition1 = "FMCSA Records"
    condition2 = button_FMCSARecords_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: FMCSA RECORDS"
    print_Information_Var = button_FMCSARecords_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    button_Shipments_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_Shipments_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: SHIPMENTS"
    condition1 = "Shipments"
    condition2 = button_Shipments_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: SHIPMENTS"
    print_Information_Var = button_Shipments_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_EngineDiagnostic_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_EngineDiagnostic_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: ENGINE DIAGNOSTIC"
    condition1 = "Engine Diagnostic"
    condition2 = button_EngineDiagnostic_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: ENGINE DIAGNOSTIC"
    print_Information_Var = button_EngineDiagnostic_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_DriverDutyReport_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_DriverDutyReport_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: DRIVER DUTY REPORT"
    condition1 = "Driver Duty Report"
    condition2 = button_DriverDutyReport_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: DRIVER DUTY REPORT"
    print_Information_Var = button_DriverDutyReport_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    # ******************************************
    # Administration Buttons - Resellers and Full Access Client Users type (3) Test:
    # ******************************************
    print("Testing Resellers and Full Access Client Users Functions available")
    try:
        button_Administration_ManagePage = w.until(EC.presence_of_element_located((By.ID, button_Administration_ManagePageId))).text
        if title_UserType_ManagePage == "QA_LimitedClient" or title_UserType_ManagePage == "QA_MasterReseller":
            #       Assert Test and print if assert is fail
            test_Name = "ADMINISTRATION Option MUST NOT allowed to user: "
            condition1 = ""
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "ADMINISTRATION Option MUST NOT allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "ADMINISTRATION Option is allowed to user: "
            condition1 = title_UserType_ManagePage
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "ADMINISTRATION Option is allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        test_Name = "ADMINISTRATION Option MUST NOT allowed to user: "
        condition1 = title_UserType_ManagePage
        condition2 = title_UserType_ManagePage
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "ADMINISTRATION Option MUST NOT allowed to user: "
        print_Information_Var = title_UserType_ManagePage
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    # Verify the Carriers

    if title_UserType_ManagePage == "QAFullAccessClient":
        dropDown_Carriers_Name_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[1]/div/select"
        dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDown_Carriers_Name_ManagePageAdr))))
        dropDown_dropDown_Carriers_Name_ManagePage_List = [x.text for x in dropDown.options]

        test_Name = "FullAccessClient > 2 Carriers test"
        condition1 = len(dropDown_dropDown_Carriers_Name_ManagePage_List)
        #Select a Client is include into the list
        condition2 = 3
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "FullAccessClient > 2 Carriers test"
        print_Information_Var = len(dropDown_dropDown_Carriers_Name_ManagePage_List)
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    else:
        print()


    #***************************************************
    # Exclusive Buttons - Master Reseller type (2) Test:
    #***************************************************+
    print("Testing Master Resellers Users Functions available")
    try:
        button_Billing_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_Billing_ManagePageAdr))).text
        if title_UserType_ManagePage == "MasterReseller":
            #       Assert Test and print if assert is fail
            test_Name = "Master Reseller Main Menu - Option: BILLING"
            condition1 = "Billing"
            condition2 = button_Billing_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "Master Reseller Main Menu - Option: BILLING"
            print_Information_Var = button_Billing_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "BILLING Option is allowed to user: "
            condition1 = "MasterReseller"
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "BILLING Option is allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #       Assert Test and print if assert is fail
        if "MasterReseller" == str(title_UserType_ManagePage):
            #       Assert Test and print if assert is fail
            test_Name = "BILLING Option MUST BE allowed to user: "
            condition1 = ""
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "BILLING Option is NOT allowed to user: "
            condition1 = title_UserType_ManagePage
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "BILLING Option is NOT allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    try:
        button_BillingReport_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_BillingReport_ManagePageAdr))).text
        if title_UserType_ManagePage == "MasterReseller":
            #       Assert Test and print if assert is fail
            test_Name = "Master Reseller Main Menu - Option: BILLING REPORT"
            condition1 = "Billing Report"
            condition2 = button_BillingReport_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "Master Reseller Main Menu - Option: BILLING REPORT"
            print_Information_Var = button_BillingReport_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "BILLING REPORTOption is allowed to user: "
            condition1 = "MasterReseller"
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "BILLING REPORT Option is allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #       Assert Test and print if assert is fail
        if "MasterReseller" == str(title_UserType_ManagePage):
            #       Assert Test and print if assert is fail
            test_Name = "BILLING REPORT Option MUST BE allowed to user: "
            condition1 = ""
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "BILLING REPORT Option is NOT allowed to user: "
            condition1 = title_UserType_ManagePage
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "BILLING REPORT Option is NOT allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #       Screenshot
    test_Name = title_UserType_ManagePage
    tc_reports.screenshot(driver, driver_Name, test_Name)

    """



    ###################################################################################################################################################
    # TEST CARRIER
    ###################################################################################################################################################

    #TEST CARRIER SELECTED FOR USER


    #TEST RULE & CARRIER FOR LIMITED USER
    if test_Global_Variables_apolloWebPortal.userTYPE_Global == 5:
        #TEST CARRIER LIST
        dropDown_CarrierName_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, dropDown_CarrierName_ManagePageAdr))).text
        #       Assert Test and print if assert is fail
        test_Name = "Carrier Selected - Manage Page Open"
        condition1 = test_Global_Variables_apolloWebPortal.carriers_List_Global
        condition2 = dropDown_CarrierName_ManagePage
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Carrier Selected - Manage Page Open"
        print_Information_Var = dropDown_CarrierName_ManagePage
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #TEST PERMISSION BASED ON THE RULE SELECTED
        try:
            w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_Assets_ManagePageAdr))).click()
            #       Assert Test and print if assert is fail
            test_Name = "ROLE Test FAILED - Based on the ROLE selected, ASSETS must be unavailable"
            condition1 = "Asset"
            condition2 = ""
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        except:
            print_Information_Fix = "ROLE Test PASSED - Based on the ROLE selected, ASSETS must be unavailable"
            print_Information_Var = "Assets"
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        try:
            w.until(EC.element_to_be_clickable((By.XPATH, button_Notifications_Carrier_ManagePageAdr))).click()
            #       Assert Test and print if assert is fail
            test_Name = "ROLE Test FAILED - Based on the ROLE selected, NOTIFICATIONS must be unavailable"
            condition1 = "Notification"
            condition2 = ""
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        except:
            #       Print Assert OK
            print_Information_Fix = "ROLE Test PASSED - Based on the ROLE selected, NOTIFICATION must be unavailable"
            print_Information_Var = "Notification"
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)
    else:
        print("It's not Limited Client")

    #TEST CARRIER FOR LIMITED RESELLER
    if test_Global_Variables_apolloWebPortal.userTYPE_Global == 3:
        # TEST CARRIER LIST
        test_Global_Variables_apolloWebPortal.carriers_List_Global = ''.join(test_Global_Variables_apolloWebPortal.carriers_List_Global)
        dropDown_CarrierName_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, dropDown_CarrierName_ManagePageAdr))).text
        #       Assert Test and print if assert is fail
        test_Name = "Carrier Selected - Manage Page Open"
        condition1 = test_Global_Variables_apolloWebPortal.carriers_List_Global
        condition2 = dropDown_CarrierName_ManagePage
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Carrier Selected - Manage Page Open"
        print_Information_Var = dropDown_CarrierName_ManagePage
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        # TEST PERMISSION BASED ON THE RULE SELECTED
        """
        try:
            w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_Assets_ManagePageAdr))).click()
            #       Assert Test and print if assert is fail
            test_Name = "ROLE Test FAILED - Based on the ROLE selected, ASSETS must be unavailable"
            condition1 = "Asset"
            condition2 = ""
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        except:
            print_Information_Fix = "ROLE Test PASSED - Based on the ROLE selected, ASSETS must be unavailable"
            print_Information_Var = "Assets"
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        try:
            w.until(EC.element_to_be_clickable((By.XPATH, button_Notifications_Carrier_ManagePageAdr))).click()
            #       Assert Test and print if assert is fail
            test_Name = "ROLE Test FAILED - Based on the ROLE selected, NOTIFICATIONS must be unavailable"
            condition1 = "Notification"
            condition2 = ""
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        except:
            #       Print Assert OK
            print_Information_Fix = "ROLE Test PASSED - Based on the ROLE selected, NOTIFICATION must be unavailable"
            print_Information_Var = "Notification"
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        """
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)
    else:
        print("It's not Limited Reseller")


    dropdown_Carrier_LimitedClient_Users_AdministrationPageAdr = "/html/body/app-root/app-main/div/div/app-manage/section/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[1]"
    #TEST HOME BASE SET FOR LIMITED RESELLER & LIMITED CLIENT
    if test_Global_Variables_apolloWebPortal.userTYPE_Global == 5 or 3:
        # Open HomeBases
        button_Carrier_HomeBases_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_HomeBases_ManagePageAdr)))
        time.sleep(0.5)
        button_Carrier_HomeBases_ManagePage.click()
        #homeBase_Available_List = w.until(EC.presence_of_element_located((By.XPATH,homeBase_Available_ListAdr))).text
        time.sleep(3)
        homeBase_Available_List = []


        n = 1
        while n <= len(test_Global_Variables_apolloWebPortal.homeBase_List_Global):
            n_str = str(n)
            a = "/html/body/app-root/app-main/div/div/app-manage/section/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[6]/div[2]/table/tbody/tr[" + n_str + "]/td[1]"
            homeBase_Available_List.append(w.until(EC.presence_of_element_located((By.XPATH, a))).text)
            n=n+1

        #       Assert Test and print if assert is fail
        test_Name = "Home Bases Available TEST for New User created"


        condition1 = ''.join(test_Global_Variables_apolloWebPortal.homeBase_List_Global)
        condition2 = ''.join(homeBase_Available_List)
        print(f'1                    {condition1}')
        print(f'2                    {condition2}')
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Home Bases Available"
        print_Information_Var = homeBase_Available_List
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)



    return ()

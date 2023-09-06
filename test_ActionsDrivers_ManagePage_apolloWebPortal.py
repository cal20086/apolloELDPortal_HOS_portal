#               Apollo Web Portal - Drivers - Details


def carrierDrivers_ChildMenu_ManagePage (driver, driver_Name, driver_Version):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from datetime import datetime
    import tc_reports
    import os
    import re
    import test_Global_Variables_apolloWebPortal
    from selenium.webdriver import ActionChains
    import test_Global_Variables_apolloWebPortal
    import openpyxl
    from pathlib import Path
    import random


    #       Carrier details Page Address
    button_Carrier_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[2]"
    title_Drivers_DriversChildPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-driver-list/div/div/div[1]/h3"
    button_DriversDetails_DriversChildPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[6]/div/button[1]"
    title_Driver_DriverChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[1]/h4"
    #Drivers page - New Driver on the Drivers list
    driverName_NewDriver_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[2]/table/tbody/tr[1]/td[1]/div"
    userName_NewDriver_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[2]"
    homeBase_NewDriver_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[3]/div"
    licenseNumber_NewDriver_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[4]"
    input_Search_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[1]/input"
    button_SearchClean_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[2]/span"

    #Driver child page
    button_NewDriver_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-driver-list/div/div/div[1]/div/button"
    input_DriverName_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div/div/div[1]/div[1]/div/input"
    input_DriverLastName_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div/div/div[1]/div[2]/div/input"
    #input_DriverUserName_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[3]/input"
    input_DriverUserName_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div/div/div[2]/div/div/input"
    input_DriverPassword_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div/div/div[3]/div[1]/div/input"
    input_DriverConfirmation_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div/div/div[3]/div[2]/div/input"
    dropdown_HomeBase_DriversChilPageId = "homebase"
    dropdown_Ruleset_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[6]/select"
    dropdown_Ruleset_DriversChilPageId = "ruleset"
    dropdown_24PeriodeStartingTime_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[7]/select"
    dropdown_24PeriodeStartingTime_DriversChilPageId = "startingTime"
    dropdown_RegistrationState_DriversChilPageId = "state"
    dropdown_Units_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[12]/select"
    dropdown_Units_DriversChilPageId = "fuelUnitCode"
    dropdown_LicenseState_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[13]/select"
    dropdown_LicenseState_DriversChilPageId = "state"
    input_LicenseNumber_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div/div/div[10]/div/div/input"
    button_Driver_SAVE_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[2]/button[1]"
    button_Driver_CLOSE_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[2]/button[3]"
    cardFooterpage_Driver_SAVE_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[2]"
    button_CanadaRuleSetCinfirmation_DriversChildPageAdr = "/html/body/ngb-modal-window[2]/div/div/app-confirmation-dialog/div[3]/button[1]"


    #   Carrier details Page Variables
    #   Global variables
    input_DriverName_DriversChildPageVar = test_Global_Variables_apolloWebPortal.input_DriverName_Global
    input_DriverLastName_DriversChildPageVar = test_Global_Variables_apolloWebPortal.input_DriverLastName_Global
    input_DriverUserName_DriversChildPageVar = test_Global_Variables_apolloWebPortal.input_DriverUserName_Global
    input_DriverPassword_DriversChildPageVar = test_Global_Variables_apolloWebPortal.input_DriverPassword_Global
    #Excel
    workbookMANAGEDB = test_Global_Variables_apolloWebPortal.workbookMANAGEDB_Global
    worksheetMANAGEDB = test_Global_Variables_apolloWebPortal.worksheetMANAGEDB_Global


    #   Read excel Variables
    excell_pointer = Path(workbookMANAGEDB)
    # Read excel value not formula
    workbookMANAGEDB_Read = openpyxl.load_workbook(excell_pointer, data_only=True)
    worksheetMANAGEDB_Read = workbookMANAGEDB_Read.active

    #   Local variables
    date = datetime.now()
    input_LicenseNumberFull_DriversChildPageVar = "Lic" + date.strftime(" %b%d%Y") + date.strftime("%H:%M:%S")
    input_LicenseNumber_DriversChildPageVar = re.sub('\W+','', input_LicenseNumberFull_DriversChildPageVar)
    text_UserNameFull_DriversChildPageVar = "QA" + date.strftime("%b%d%Y") + date.strftime("%H:%M:%S")
    text_UserName_DriversChildPageVar = re.sub('\W+', '', text_UserNameFull_DriversChildPageVar)

    w = WebDriverWait(driver, 30)

    # Excel DB
    excel_RuleSetTotal_cellValue = worksheetMANAGEDB_Read['A2'].value
    excel_24PeriodeTotal_cellValue = worksheetMANAGEDB_Read['C2'].value
    excel_StateTotal_cellValue = worksheetMANAGEDB_Read['E2'].value
    excel_DB_line = 4
    excel_DB_line_LogicTest = 2
    colum_Manage_RuleSetTotal = "A"
    colum_Manage_RuleSets = "B"


    #       #######################################     Carriers Main functions    ##########################################
    #   #####################################################################################################################

    #   Page Title on TCReport
    function_Name = "Drivers Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    button_Carrier_Drivers_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_Drivers_ManagePageAdr)))
    time.sleep(0.5)
    button_Carrier_Drivers_ManagePage.click()

    #   Drivers Page test:
    title_Drivers_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, title_Drivers_DriversChildPageAdr)))).text
    print(title_Drivers_DriversChildPage)
    #       Assert Test and print if assert is fail
    test_Name = "Drivers Child Page Open"
    condition1 = "Drivers"
    condition2 = title_Drivers_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Drivers Page Open"
    print_Information_Var = title_Drivers_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Drivers Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Page Title on TCReport
    function_Name = "Create New Driver"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    # Create a NEW DRIVER
    w.until(EC.element_to_be_clickable((By.XPATH, button_NewDriver_Drivers_ManagePageAdr))).click()
    input_DriverName_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, input_DriverName_DriversChildPageAdr)))
    a = "QAName" + date.strftime(" %b%d%Y") + date.strftime("%H:%M:%S")
    text_DriverName_DriversChildPageVar = re.sub('\W+','', a)
    input_DriverName_DriversChildPage.send_keys(text_DriverName_DriversChildPageVar)
    input_DriverLastName_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, input_DriverLastName_DriversChildPageAdr)))
    a = "QALName" + date.strftime(" %b%d%Y") + date.strftime("%H:%M:%S")
    text_DriverLastName_DriversChildPageVar = re.sub('\W+','', a)
    input_DriverLastName_DriversChildPage.send_keys(text_DriverLastName_DriversChildPageVar)
    input_DriverUserName_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, input_DriverUserName_DriversChildPageAdr)))
    input_DriverUserName_DriversChildPage.send_keys(text_UserName_DriversChildPageVar)
    input_DriverPassword_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, input_DriverPassword_DriversChildPageAdr)))
    input_DriverPassword_DriversChildPage.clear()
    input_DriverPassword_DriversChildPage.send_keys("NewQAdriver")
    input_DriverConfirmation_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, input_DriverConfirmation_DriversChildPageAdr)))
    input_DriverConfirmation_DriversChildPage.send_keys("NewQAdriver")
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropdown_RegistrationState_DriversChilPageId))))
    dropdown_RegistrationState_DriversChilPage_Selected = dropDown.select_by_visible_text("FL")





    input_LicenseNumber_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, input_LicenseNumber_DriversChildPageAdr)))
    a = "QALIC" + date.strftime(" %b%d%Y") + date.strftime("%H:%M:%S")
    a = re.sub('\W+','', a)
    input_LicenseNumber_DriversChildPage.send_keys(a)


    a = w.until(EC.presence_of_element_located((By.XPATH, cardFooterpage_Driver_SAVE_DriversChildPageAdr)))
    actions = ActionChains(driver)
    actions.move_to_element(a)
    actions.perform()




    #SAVE
    w.until(EC.element_to_be_clickable((By.XPATH, button_Driver_SAVE_DriversChildPageAdr))).click()
    time.sleep(2)
    #       Screenshot
    test_Name = "New Driver Created"
    tc_reports.screenshot(driver, driver_Name, test_Name)


    #################################################################
    # Verify New Driver information from the Drivers page by Username
    #   Page Title on TCReport
    function_Name = "Verify New Driver Information"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    input_Search_Drivers_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Drivers_ManagePageAdr)))
    input_Search_Drivers_ManagePage.send_keys(text_UserName_DriversChildPageVar)
    time.sleep(2)
    userName_NewDriver_Drivers_ManagePage = w.until(EC.presence_of_element_located((By.XPATH,userName_NewDriver_Drivers_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "New Driver Created"
    condition1 = text_UserName_DriversChildPageVar
    condition2 = userName_NewDriver_Drivers_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New Driver on Drivers List"
    print_Information_Var = userName_NewDriver_Drivers_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "New Driver on Drivers List"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Open DRIVERS page and open DRIVER PAGE FOR THE New Driver informations (eye button)
    input_driverName_Drivers_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, driverName_NewDriver_Drivers_ManagePageAdr))).text
    input_userNameName_Drivers_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, userName_NewDriver_Drivers_ManagePageAdr))).text
    input_licenseNumber_Drivers_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, licenseNumber_NewDriver_Drivers_ManagePageAdr))).text

    # Drivers details page
    button_DriversDetails_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, button_DriversDetails_DriversChildPageAdr)))
    #time.sleep(0.5)
    button_DriversDetails_DriversChildPage.click()

    #######################################################################################################################################
    #   Driver Child Page test:
    #######################################################################################################################################
    title_Driver_DriverChildPage = w.until((EC.presence_of_element_located((By.XPATH, title_Driver_DriverChildPageAdr)))).text
    #       Assert Test and print if assert is fail
    test_Name = "Driver Child Page Open"
    condition1 = "Driver"
    condition2 = title_Driver_DriverChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Child Page Open"
    print_Information_Var = title_Driver_DriverChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #   Driver child Page information page
    input_DriverName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH,input_DriverName_DriversChildPageAdr))).get_attribute('value')
    input_DriverUserName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverUserName_DriversChildPageAdr))).get_attribute('value')
    input_LicenseNumber_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_LicenseNumber_DriversChildPageAdr))).get_attribute('value')

    #   Compare New Drivers/Manage Page information with Driver/Child Page
    #       Assert Test and print if assert is fail
    test_Name = "Driver Name - Drivers page x Driver page"
    condition1 = input_DriverName_DriversChildPage
    condition2 = input_driverName_Drivers_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "NAME - Drivers page x Driver page"
    print_Information_Var = input_DriverName_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Assert Test and print if assert is fail
    test_Name = "Driver UserName - Drivers page x Driver page"
    condition1 = input_DriverUserName_DriversChildPage
    condition2 = input_userNameName_Drivers_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "USERNAME - Drivers page x Driver page"
    print_Information_Var = input_DriverUserName_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Assert Test and print if assert is fail
    test_Name = "Driver License - Drivers page x Driver page"
    condition1 = input_LicenseNumber_DriversChildPage
    condition2 = input_licenseNumber_Drivers_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "LICENSE - Drivers page x Driver page"
    print_Information_Var = input_LicenseNumber_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #############################################################################################################################################
    # UPDATE DRIVER & PAGE TEST FIELDS REQUIREMENTS
    #############################################################################################################################################
    #############################################################################################################################################
    #   Page Title on TCReport
    function_Name = "Update New Driver Information"
    tc_reports.function_Init_Page(function_Name, driver_Name)
    date = datetime.now()
    print(date)
    # TEST NAME FIELD RULES <2
    input_DriverName_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_DriverName_DriversChildPageAdr))))
    input_DriverName_DriversChildPage.clear()
    input_DriverName_DriversChildPage.send_keys("T")
    input_DriverName_DriversChildPageClass = w.until((EC.presence_of_element_located((By.XPATH, input_DriverName_DriversChildPageAdr)))).get_attribute('class')
    # Assert
    test_Name = "Name < 2 -> ERROR"
    condition1 = input_DriverName_DriversChildPageClass
    condition2 = "form-control is-invalid ng-invalid ng-touched ng-dirty"
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Page field NAME < 2 -> ! "
    print_Information_Var = input_DriverName_DriversChildPageClass
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    input_DriverName_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_DriverName_DriversChildPageAdr))))
    input_DriverName_DriversChildPage.clear()
    a = "QAName" + date.strftime(" %b%d%Y") + date.strftime("%H:%M:%S")
    a = re.sub('\W+', '', a)
    print(a)
    input_DriverName_DriversChildPage.send_keys(a)

    # TEST LAST NAME FIELD RULES <2
    input_DriverLastName_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_DriverLastName_DriversChildPageAdr))))
    input_DriverLastName_DriversChildPage.clear()
    input_DriverLastName_DriversChildPage.send_keys("T")
    input_DriverLastName_DriversChildPageClass = w.until((EC.presence_of_element_located((By.XPATH, input_DriverLastName_DriversChildPageAdr)))).get_attribute('class')
    # Assert
    test_Name = "Last Name < 2 -> ERROR"
    condition1 = input_DriverLastName_DriversChildPageClass
    condition2 = "form-control is-invalid ng-invalid ng-touched ng-dirty"
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Page field LAST NAME < 2 -> ! "
    print_Information_Var = input_DriverLastName_DriversChildPageClass
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    input_DriverLastName_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_DriverLastName_DriversChildPageAdr))))
    input_DriverLastName_DriversChildPage.clear()
    a = "QALName" + date.strftime(" %b%d%Y") + date.strftime("%H:%M:%S")
    a = re.sub('\W+', '', a)
    input_DriverLastName_DriversChildPage.send_keys(a)

    # TEST change USERNAME FIELD
    #   Page Title on TCReport
    function_Name = "Verify Update New Driver Information"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    input_DriverUserName_DriversChildPageRead = ""
    try:
        input_DriverUserName_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_DriverUserName_DriversChildPageAdr))))
        input_DriverUserName_DriversChildPage.clear()
        input_DriverUserName_DriversChildPage.send_keys("TEST")
        input_DriverUserName_DriversChildPageRead = w.until((EC.presence_of_element_located((By.XPATH, input_DriverUserName_DriversChildPageAdr)))).text
    except:
        print("Test Change UserName")
    # Assert
    if input_DriverUserName_DriversChildPageRead != "TEST":
        test_Name = "UserName can not change"
        condition1 = input_DriverUserName_DriversChildPageRead
        condition2 = input_DriverUserName_DriversChildPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
#       Print Assert OK
        print_Information_Fix = "UserName can not change"
        print_Information_Var = input_DriverUserName_DriversChildPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    else:
        test_Name = "UserName can not change"
        condition1 = ""
        condition2 = input_DriverUserName_DriversChildPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "UserName can not change"
        print_Information_Var = input_DriverUserName_DriversChildPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #Home Base options -> Select and Read
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropdown_HomeBase_DriversChilPageId))))
    dropdown_HomeBase_DriversChilPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_HomeBase_DriversChilPage_List):
        dropdown_HomeBase_DriversChilPage_Selected = dropDown.select_by_visible_text(dropdown_HomeBase_DriversChilPage_List[n])
        dropdown_HomeBase_DriversChilPage_Read = dropDown.first_selected_option.text
         # Assert
        test_Name = "Driver page Home Base -> Select x Read"
        condition1 = dropdown_HomeBase_DriversChilPage_List[n]
        condition2 = dropdown_HomeBase_DriversChilPage_Read
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        n = n + 1
    #       Print Assert OK
    print_Information_Fix = "Driver page Home Base -> Select x Read"
    print_Information_Var = ""
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #Rule Set options -> Select and Read
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropdown_Ruleset_DriversChilPageId))))
    dropdown_Ruleset_DriversChilPage_List = [x.text for x in dropDown.options]
    # Assert
    test_Name = "Rule Set Options quantities"
    condition1 = str(len(dropdown_Ruleset_DriversChilPage_List))
    condition2 = str(excel_RuleSetTotal_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Rule Set Options quantities: "
    print_Information_Var = str(len(dropdown_Ruleset_DriversChilPage_List))
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    n = 0
    while n < len(dropdown_Ruleset_DriversChilPage_List):
        dropdown_Ruleset_DriversChilPage = dropDown.select_by_visible_text(dropdown_Ruleset_DriversChilPage_List[n])
        dropdown_Ruleset_DriversChilPage_Read = dropDown.first_selected_option.text
        indice = "B" + str(n+2)
        ruleSet_Excel = worksheetMANAGEDB_Read[indice].value
        # Assert
        test_Name = "Rule Set Options -> Select x Read"
        condition1 = str(ruleSet_Excel)
        condition2 = str(dropdown_Ruleset_DriversChilPage_Read)
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        n = n + 1
    #       Print Assert OK
    print_Information_Fix = "Rule Set Options -> Select x Read"
    print_Information_Var = ""
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #24-Period Starting Time
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropdown_24PeriodeStartingTime_DriversChilPageId))))
    dropdown_24PeriodeStartingTime_DriversChilPage_List = [x.text for x in dropDown.options]
    n = 0
    # Assert
    test_Name = "24-Periode Starting Time Options quantities"
    condition1 = str(len(dropdown_24PeriodeStartingTime_DriversChilPage_List))
    condition2 = str(excel_24PeriodeTotal_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "24-Periode Starting Time quantities: "
    print_Information_Var = str(len(dropdown_24PeriodeStartingTime_DriversChilPage_List))
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #print(f'Celula C2 = {excel_RuleSetTotal_cellValue} x {len(dropdown_Ruleset_DriversChilPage_List)}')
    while n < len(dropdown_24PeriodeStartingTime_DriversChilPage_List):
        dropdown_24PeriodeStartingTime_DriversChilPage_Selected = dropDown.select_by_visible_text(dropdown_24PeriodeStartingTime_DriversChilPage_List[n])
        dropdown_24PeriodeStartingTime_DriversChilPage_Read = dropDown.first_selected_option.text
        # Assert
        test_Name = "24-Periode Starting Time -> Select x Read"
        condition1 = str(ruleSet_Excel)
        condition2 = str(dropdown_Ruleset_DriversChilPage_Read)
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        n = n + 1
    #       Print Assert OK
    print_Information_Fix = "24-Periode Starting Time -> Select x Read"
    print_Information_Var = ""
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    # Move page down to License field - page Scroll down
    input_LicenseNumber_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH,input_LicenseNumber_DriversChildPageAdr)))
    actions = ActionChains(driver)
    actions.move_to_element(input_LicenseNumber_DriversChildPage)
    actions.perform()
    #browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


    #Registration State
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropdown_RegistrationState_DriversChilPageId))))
    dropdown_RegistrationState_DriversChilPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_RegistrationState_DriversChilPage_List):
        dropdown_RegistrationState_DriversChilPage_Selected = dropDown.select_by_visible_text(dropdown_RegistrationState_DriversChilPage_List[n])
        dropdown_RegistrationState_DriversChilPage_Read = dropDown.first_selected_option.text
        # Assert
        test_Name = "Registration State -> Select x Read"
        condition1 = str(ruleSet_Excel)
        condition2 = str(dropdown_Ruleset_DriversChilPage_Read)
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        n = n + 1
    #       Print Assert OK
    print_Information_Fix = "Registration State -> Select x Read"
    print_Information_Var = ""
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    # TEST LICENSE NUMBER FIELD RULES
    input_LicenseNumber_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_LicenseNumber_DriversChildPageAdr))))
    input_LicenseNumber_DriversChildPage.clear()
    input_LicenseNumber_DriversChildPage.send_keys("T")
    input_LicenseNumber_DriversChildPageClassRead = w.until((EC.presence_of_element_located((By.XPATH, input_LicenseNumber_DriversChildPageAdr)))).get_attribute('class')
    # Assert
    test_Name = "License Number < 2 -> ERROR"
    condition1 = input_LicenseNumber_DriversChildPageClassRead
    condition2 = "form-control ng-touched is-invalid ng-dirty ng-invalid"
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Child Page field License Number < 2 -> ! "
    print_Information_Var = input_LicenseNumber_DriversChildPageClassRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    input_LicenseNumber_DriversChildPage.clear()
    input_LicenseNumber_DriversChildPage.send_keys(input_LicenseNumber_DriversChildPageVar)


    # Save Driver Child page
    w.until(EC.element_to_be_clickable((By.XPATH, button_Driver_SAVE_DriversChildPageAdr))).click()

    #*************************************************
    # Verify Changes on  Home Base and Rule Set and save
    #*************************************************
    w.until(EC.element_to_be_clickable((By.XPATH,button_SearchClean_Drivers_ManagePageAdr))).click()
    input_Search_Drivers_ManagePage = w.until(EC.presence_of_element_located((By.XPATH,input_Search_Drivers_ManagePageAdr)))
    input_Search_Drivers_ManagePage.send_keys(text_UserName_DriversChildPageVar)
    time.sleep(2)
    # Open the New Driver Child Page

    button_DriversDetails_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, button_DriversDetails_DriversChildPageAdr)))
    button_DriversDetails_DriversChildPage.click()

    # Home Base options -> Select and Read
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_HomeBase_DriversChilPageId))))
    dropdown_HomeBase_DriversChilPage_List = [x.text for x in dropDown.options]
    #Random Home Base
    n = len(dropdown_HomeBase_DriversChilPage_List)-1
    if n == 0:
        n = 0
    else:
        n = random.randrange(0,n,1)
    dropdown_HomeBase_DriversChilPage_Selected = dropDown.select_by_visible_text(dropdown_HomeBase_DriversChilPage_List[n])
    dropdown_HomeBase_DriversChilPage_Read = dropDown.first_selected_option.text

    # Rule Set options -> Select and Read
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_Ruleset_DriversChilPageId))))
    dropdown_Ruleset_DriversChilPage_List = [x.text for x in dropDown.options]
    n = len(dropdown_Ruleset_DriversChilPage_List)-1
    n = random.randrange(0,n,1)
    dropdown_Ruleset_DriversChilPage_Selected = dropDown.select_by_visible_text(dropdown_Ruleset_DriversChilPage_List[n])
    dropdown_Ruleset_DriversChilPage_Read = dropDown.first_selected_option.text

    #Scroll down Driver Child page to Save button TITLE
    footer_Driver_SAVE_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, cardFooterpage_Driver_SAVE_DriversChildPageAdr)))
    actions = ActionChains(driver)
    actions.move_to_element(footer_Driver_SAVE_DriversChildPage)
    actions.perform()
    w.until(EC.element_to_be_clickable((By.XPATH, button_Driver_SAVE_DriversChildPageAdr))).click()

    try:
        assert "Canada" in dropdown_Ruleset_DriversChilPage_Read
        w.until(EC.element_to_be_clickable((By.XPATH, button_CanadaRuleSetCinfirmation_DriversChildPageAdr))).click()
        time.sleep(1)
        w.until(EC.element_to_be_clickable((By.XPATH, button_Driver_SAVE_DriversChildPageAdr))).click()
    except:
        print("No Canada Rule Set")

    #*********************************************
    #Test saved information on Driver Child page
    #*********************************************
    #   Page Title on TCReport
    function_Name = "Verify saved information on Driver Child page"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    title_Drivers_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, title_Drivers_DriversChildPageAdr)))).text

    # HomeBase New Driver changed verification
    time.sleep(3)
    homeBase_NewDriver_Drivers_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, homeBase_NewDriver_Drivers_ManagePageAdr))))
    homeBase_NewDriver_Drivers_ManagePage = homeBase_NewDriver_Drivers_ManagePage.text
    # Assert
    test_Name = "HomeBase New Driver changed verification"
    condition1 = str(homeBase_NewDriver_Drivers_ManagePage)
    condition2 = str(dropdown_HomeBase_DriversChilPage_Read)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "HomeBase New Driver changed verification"
    print_Information_Var = homeBase_NewDriver_Drivers_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #*********************************************************
    # Verification - RuleSet New Driver changed on Child Page
    #*********************************************************
    button_DriversDetails_DriversChildPage = w.until((EC.element_to_be_clickable((By.XPATH, button_DriversDetails_DriversChildPageAdr))))
    time.sleep(1)
    button_DriversDetails_DriversChildPage.click()
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropdown_Ruleset_DriversChilPageId))))
    dropdown_Ruleset_DriversChilPage_Readagain = dropDown.first_selected_option.text
    # Assert
    test_Name = "RuleSet New Driver changed on Child Page - verification"
    condition1 = str(dropdown_Ruleset_DriversChilPage_Read)
    condition2 = str(dropdown_Ruleset_DriversChilPage_Readagain)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "RuleSet New Driver changed on Child Page - verification"
    print_Information_Var = dropdown_Ruleset_DriversChilPage_Readagain
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #Scroll down Driver Child page to Save button TITLE
    footer_Driver_SAVE_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, cardFooterpage_Driver_SAVE_DriversChildPageAdr)))
    actions = ActionChains(driver)
    actions.move_to_element(footer_Driver_SAVE_DriversChildPage)
    actions.perform()
    w.until(EC.element_to_be_clickable((By.XPATH, button_Driver_CLOSE_DriversChildPageAdr))).click()

    input_Search_Drivers_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Drivers_ManagePageAdr)))
    input_Search_Drivers_ManagePage.send_keys(text_UserName_DriversChildPageVar)

    #       Screenshot
    test_Name = "Driver Updated"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    w.until(EC.element_to_be_clickable((By.XPATH,button_SearchClean_Drivers_ManagePageAdr))).click()
    return ()

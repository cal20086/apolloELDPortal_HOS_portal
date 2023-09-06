#               Apollo Web Portal - Manage Page

def managePage (driver, driver_Name, driver_Version, client_Name_Var, siteAddressVar):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from datetime import datetime
    import tc_reports
    from selenium.webdriver import ActionChains
    import test_CreateCarrier_ManagePage_apolloWebPortal
    import test_Global_Addresses_apolloWebPortal

#       Carrier details Page Address & Variables
#       Fields Address

    title_ManagePageAdr = test_Global_Addresses_apolloWebPortal.title_ManagePageAdr_Global
    menu_3linesClass_ManagePageAdr = test_Global_Addresses_apolloWebPortal.menu_3linesClass_ManagePageAdr_Global
    title_apollo_Portal_VersionAdr = test_Global_Addresses_apolloWebPortal.title_apollo_Portal_VersionAdr_Global
    dropDown_CarrierName_ManagePageId = test_Global_Addresses_apolloWebPortal.dropDown_CarrierName_ManagePageId_Global
    button_PlusNew_1stCarrier_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_PlusNew_1stCarrier_ManagePageAdr_Global
    button_ActionsDetails_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_ActionsDetails_ManagePageAdr_Global
    button_X_Carrier_ActionsDetails_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_X_Carrier_ActionsDetails_ManagePageAdr_Global


    """    
    title_ManagePageAdr = "/html/body/app-root/app-main/div/div/breadcrumb/section/div/div/div/h1"
    menu_3linesClass_ManagePageAdr = "/html/body/app-root/app-main/div/main-header/nav/div[1]/ul/li"
    title_apollo_Portal_VersionAdr = "/html/body/app-root/app-main/div/main-header/nav/div[2]/small"
    dropDown_CarrierName_ManagePageId = "carrierSelector"
    button_PlusNew_1stCarrier_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[1]/div/carrier-list/div/div/div[1]/div/button"
    button_ActionsDetails_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[1]"
    button_X_Carrier_ActionsDetails_ManagePageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[1]/button"
    """

#       Variables
    w = WebDriverWait(driver,10)
    control_Reportfile = 0
    print_Information_Fix = ""
    print_Information_Var = ""

    # Report header:
    time.sleep(3)
    title_apollo_Portal_Version = w.until(EC.presence_of_element_located((By.XPATH, title_apollo_Portal_VersionAdr))).text
    contol_Reportfile = 0
    test_Case_Type = ""
    tc_reports.write_reportfile_Header(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version, title_apollo_Portal_Version)


    title_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_ManagePageAdr))).text

    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Manage Page Open"
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
    # **************** Test and report results at TCReports END  **************************************************************************************************************

#       menu 3 Lines - Close / Open buttons menu
#       Open "page" Menu region 3 Lines
    menu_3lines_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, menu_3linesClass_ManagePageAdr)))
    menu_3lines_ManagePage.click()
    time.sleep(1)
    menu_3lines_ManagePage.click()

    #Verify if there is a Carrier, if not Create the 1st Carrier:


    try:
        w.until(EC.element_to_be_clickable((By.XPATH, button_ActionsDetails_ManagePageAdr))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, button_X_Carrier_ActionsDetails_ManagePageAdr))).click()
    except:
        try:
            #Multi Carriers
            dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropDown_CarrierName_ManagePageId))))
            dropDown_ImportOption_CarrierCountry_CarrierChildPage_List = [x.text for x in dropDown.options]
            #a = len(dropDown_ImportOption_CarrierCountry_CarrierChildPage_List) - 1
            a = 1
            #dropDown_CarrierName_ManagePage = dropDown.select_by_visible_text(client_Name_Var)
            #dropDown_CarrierName_ManagePage = dropDown.select_by_index(a)
            dropDown_CarrierName_ManagePage = dropDown.select_by_visible_text("QA Carrier")
            dropDown_CarrierName_ManagePageRead = dropDown.first_selected_option.text
            #       Assert Test and print if assert is fail
            test_Name = "Carrier Selected - Manage Page Open"
            condition1 = "QA Carrier"
            condition2 = dropDown_CarrierName_ManagePageRead
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "Carrier Selected - Manage Page Open"
            print_Information_Var = dropDown_CarrierName_ManagePageRead
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
            #       Screenshot
            tc_reports.screenshot(driver, driver_Name, test_Name)

        except:
            #Create the 1st Carrier
            w.until(EC.element_to_be_clickable((By.XPATH, button_PlusNew_1stCarrier_ManagePageAdr))).click()
            test_CreateCarrier_ManagePage_apolloWebPortal.create1stCarrier_carrierDetail_ChildMenu_ManagePage(driver, driver_Name, driver_Version)
            driver.refresh()
    return ()



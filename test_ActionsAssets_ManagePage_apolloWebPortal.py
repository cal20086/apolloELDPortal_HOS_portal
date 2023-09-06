#               Apollo Web Portal - Manage - Assets


def carrierAssets_ChildMenu_ManagePage (driver, driver_Name, driver_Version):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from datetime import datetime
    import tc_reports
    import re
    from selenium.webdriver import ActionChains
    import test_Global_Variables_apolloWebPortal

#       Carrier details Page Address & Variables
#       Fields Address

    button_Carrier_Assets_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Carrier_Assets_ManagePageAdr_Global
    title_Assets_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-asset-list/div/div/div[1]/h3"
    button_PlussNew_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-asset-list/div/div/div[1]/div/button"
    input_Search_AssetsAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-asset-list/div/div/div[2]/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[1]/input"
    text_1stAssetNumber_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-asset-list/div/div/div[2]/dx-data-grid/div/div[6]/div[2]/table/tbody/tr[1]/td[2]/span"
    input_ClearSearch_AssetsAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section/div/div[2]/div/app-asset-list/div/div/div[2]/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[2]/span"
    dropBox_HomeBase_Asset_Assets_ManagePageId = 'homebase'
    title_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[1]/h4"
    button_PlussNew_Asset_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-asset-list/div/div/div[1]/div/button"
    dropBox_AssetType_Asset_Assets_ManagePageId = "assetType"
    text_Number_Asset_Assets_ManagePageId = "assetNumber"
    text_VIN_Asset_Assets_ManagePageId = "assetVIN"
    text_Plate_Asset_Assets_ManagePageId = "assetPlate"
    dropBox_RegistrationState_Asset_Assets_ManagePageId = "assetRegState"
    text_Description_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[1]/form/div/div/div/div[7]/textarea"
    text_ECMIdentifier_Asset_Assets_ManagePageId = "ecmidentified"
    text_AdditionalECMIdentifier_Asset_Assets_ManagePageId = "addecmidentified"
    checkBox_Active_Asset_Assets_ManagePageId = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[1]/form/div/div[9]/div/input"
    dropBox_FuelTypePrimary_Asset_Assets_ManagePageId = "FuelTypePrimary"
    text_Make_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[2]/form/div/div/div/div[2]/input"

    text_Model_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[2]/form/div/div/div/div[3]/input"
    text_Year_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[2]/form/div/div/div/div[4]/input"
    dropBox_Type_Asset_Assets_ManagePageId = "Type"
    text_BodyClass_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[2]/form/div/div/div/div[6]/input"
    dropBox_GVWR_Asset_Assets_ManagePageId = "GVWR"
    button_SAVE_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[2]/button[1]"
    button_CLOSE_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[2]/button[2]"
    label_FuelTypePrimary_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[2]/form/div/div/div/div[1]/div/div[1]/label"


    #       Variables:
    date = datetime.now()
    w = WebDriverWait(driver, 30)

    random = str(date)
    random = random[len(random) - 6:]
    random = str(random)

    """
    textTractor_Number_Asset_Assets_ManagePageVar = "QATru" + random[:-1]
    textTractor_VIN_Asset_Assets_ManagePageVar = "VNTRUCK0000" + random
    textTractor_Plate_Asset_Assets_ManagePageVar = "QA" + random
    textTractor_Description_Asset_Assets_ManagePageVar = "QA TRUCK" + random
    textTractor_ECMIdentifier_Asset_Assets_ManagePageVar = "AABBCCDDEEFF"
    dropBox_RegistrationState_Asset_Assets_ManagePageVar = "ID"
    textTractor_ECMIdentifier_Asset_Assets_ManagePageVar = "012345" + random
    textTractor_AdditionalECMIdentifier_Asset_Assets_ManagePageVar = random
    textTractor_FuelTypePrimary_Asset_Assets_ManagePageVar = "Biodiesel"
    textTractor_Make_Asset_Assets_ManagePageVar = "Peterbilt"
    textTractor_Model_Asset_Assets_ManagePageVar = "579"
    textTractor_Year_Asset_Assets_ManagePageVar = "2022"
    textTractor_Type_Asset_Assets_ManagePageVar = "TRUCK"
    textTractor_BodyClass_Asset_Assets_ManagePageVar = "Heavy-Duty"
    dropBox_Tractor_GVWR_Asset_Assets_ManagePageVar = "Class 8:33,001 lb and above (14,969 kg and above)"

    textTrailer_Number_Asset_Assets_ManagePageVar = "QATra" + random[:-1]
    textTrailer_VIN_Asset_Assets_ManagePageVar = "VNTrailer00" + random
    textTrailer_Plate_Asset_Assets_ManagePageVar = "TR" + random
    textTrailer_Description_Asset_Assets_ManagePageVar = "Description QATRAILER " + random
    """
    textTractor_Number_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_Number_AssetVar_Global
    textTractor_VIN_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_VIN_AssetVar_Global
    textTractor_Plate_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_Plate_AssetVar_Global
    textTractor_Description_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_Description_Asset_Var_Global
    textTractor_ECMIdentifier_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_ECMIdentifier_Asset_Var_Global
    dropBox_RegistrationState_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.dropBox_RegistrationState_Asset_Var_Global
    textTractor_ECMIdentifier_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_ECMIdentifier_Asset_Var_Global
    textTractor_AdditionalECMIdentifier_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_AdditionalECMIdentifier_Asset_Assets_ManagePageVar_Global
    textTractor_FuelTypePrimary_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_FuelTypePrimary_Asset_Assets_ManagePageVar_Global
    textTractor_Make_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_Make_Asset_Assets_ManagePageVar_Global
    textTractor_Model_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_Model_Asset_Assets_ManagePageVar_Global
    textTractor_Year_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_Year_Asset_Assets_ManagePageVar_Global
    textTractor_Type_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_Type_Asset_Assets_ManagePageVar_Global
    textTractor_BodyClass_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTractor_BodyClass_Asset_Assets_ManagePageVar_Global
    dropBox_Tractor_GVWR_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.dropBox_Tractor_GVWR_Asset_Assets_ManagePageVar_Global

    textTrailer_Number_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTrailer_Number_Asset_Assets_ManagePageVar_Global
    textTrailer_VIN_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTrailer_VIN_Asset_Assets_ManagePageVar_Global
    textTrailer_Plate_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTrailer_Plate_Asset_Assets_ManagePageVar_Global
    textTrailer_Description_Asset_Assets_ManagePageVar = test_Global_Variables_apolloWebPortal.textTrailer_Description_Asset_Assets_ManagePageVar_Global


    #####################################################################################################################################
    #                                                       ASSETS Main functions                                                       #
    #####################################################################################################################################

  #   Page Title on TCReport
    function_Name = "Carriers ASSETS Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    # Assets Page button
    button_Carrier_Assets_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_Assets_ManagePageAdr)))
    time.sleep(0.5)
    button_Carrier_Assets_ManagePage.click()

    time.sleep(3)
    #   Assets Page Open test:
    title_Assets_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, title_Assets_Assets_ManagePageAdr)))).text
    #       Assert Test and print if assert is fail
    test_Name = "Assets Page Open"
    condition1 = "Assets"
    condition2 = title_Assets_Assets_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Assets Page Open"
    print_Information_Var = title_Assets_Assets_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Assets Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Page Title on TCReport
    function_Name = "Test ASSET Child page fields"
    tc_reports.function_Init_Page(function_Name, driver_Name)
    #################
    #   + New button
    w.until(EC.element_to_be_clickable((By.XPATH, button_PlussNew_Assets_ManagePageAdr))).click()

    #   Page Title on TCReport
    #   Page Title on TCReport
    # Test Asset type: Tractor page
    #   Asset Page Open test:
    time.sleep(1)
    title_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, title_Asset_Assets_ManagePageAdr)))).text
    #print(title_Asset_Assets_ManagePageAdr)
    #       Assert Test and print if assert is fail
    test_Name = "Asset Child Page Open"
    condition1 = "Asset"
    condition2 = title_Asset_Assets_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset Page Open"
    print_Information_Var = title_Asset_Assets_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Asset Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #Test Asset Type
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_AssetType_Asset_Assets_ManagePageId))))
    dropBox_AssetType_Asset_Assets_ManagePage = dropDown
    dropBox_AssetType_Asset_Assets_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropBox_AssetType_Asset_Assets_ManagePage_List):
        dropBox_AssetType_Asset_Assets_ManagePage_Selected = dropDown.select_by_visible_text(dropBox_AssetType_Asset_Assets_ManagePage_List[n])
        dropBox_AssetType_Asset_Assets_ManagePage_Read = dropDown.first_selected_option.text

        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Asset Type"
        condition1 = dropBox_AssetType_Asset_Assets_ManagePage_List[n]
        condition2 = dropBox_AssetType_Asset_Assets_ManagePage_Read
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Asset Page - Asset Type element:"
        print_Information_Var = dropBox_AssetType_Asset_Assets_ManagePage_Read
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)
        n = n + 1
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #Select Asset Type = Tractor
    dropBox_AssetType_Asset_Assets_ManagePage = dropBox_AssetType_Asset_Assets_ManagePage.select_by_visible_text("Tractor")

    # Test Asset type: Tractor page
    #******************************
    text_Number_Asset_Assets_ManagePage = w.until(EC.presence_of_element_located((By.ID,text_Number_Asset_Assets_ManagePageId)))
    text_Number_Asset_Assets_ManagePage.send_keys(textTractor_Number_Asset_Assets_ManagePageVar)
    text_Number_Asset_Assets_ManagePageRead = text_Number_Asset_Assets_ManagePage.get_attribute('value')
    #       Assert Test and print if assert is fail
    test_Name = "Asset Number"
    condition1 = textTractor_Number_Asset_Assets_ManagePageVar
    condition2 = text_Number_Asset_Assets_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset Number"
    print_Information_Var = text_Number_Asset_Assets_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    text_VIN_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID,text_VIN_Asset_Assets_ManagePageId))))
    text_VIN_Asset_Assets_ManagePage.send_keys(textTractor_VIN_Asset_Assets_ManagePageVar)
    text_VIN_Asset_Assets_ManagePageRead = text_VIN_Asset_Assets_ManagePage.get_attribute('value')
    #       Assert Test and print if assert is fail
    test_Name = "Asset VIN Number"
    condition1 = textTractor_VIN_Asset_Assets_ManagePageVar
    condition2 = text_VIN_Asset_Assets_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset VIN Number"
    print_Information_Var = text_VIN_Asset_Assets_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    text_Plate_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID,text_Plate_Asset_Assets_ManagePageId))))
    text_Plate_Asset_Assets_ManagePage.send_keys(textTractor_Plate_Asset_Assets_ManagePageVar)
    text_Plate_Asset_Assets_ManagePageRead = text_Plate_Asset_Assets_ManagePage.get_attribute('value')
    #       Assert Test and print if assert is fail
    test_Name = "Asset PLATE Number"
    condition1 = textTractor_Plate_Asset_Assets_ManagePageVar
    condition2 = text_Plate_Asset_Assets_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset PLATE Number"
    print_Information_Var = text_Plate_Asset_Assets_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_RegistrationState_Asset_Assets_ManagePageId))))
    dropDown.select_by_visible_text(dropBox_RegistrationState_Asset_Assets_ManagePageVar)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_HomeBase_Asset_Assets_ManagePageId))))
    dropDown.select_by_index(0)

    text_Description_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,text_Description_Asset_Assets_ManagePageAdr))))
    text_Description_Asset_Assets_ManagePage.send_keys(textTractor_Description_Asset_Assets_ManagePageVar)
    text_Description_Asset_Assets_ManagePageRead = text_Description_Asset_Assets_ManagePage.get_attribute('value')
    #       Assert Test and print if assert is fail
    test_Name = "Asset Description Number"
    condition1 = textTractor_Description_Asset_Assets_ManagePageVar
    condition2 = text_Description_Asset_Assets_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset Description Number"
    print_Information_Var = text_Description_Asset_Assets_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    text_ECMIdentifier_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_ECMIdentifier_Asset_Assets_ManagePageId))))
    text_ECMIdentifier_Asset_Assets_ManagePage.send_keys(textTractor_ECMIdentifier_Asset_Assets_ManagePageVar)
    text_ECMIdentifier_Asset_Assets_ManagePageRead = text_ECMIdentifier_Asset_Assets_ManagePage.get_attribute('value')
    text_ECMIdentifier_Asset_Assets_ManagePageRead = re.sub(":","",text_ECMIdentifier_Asset_Assets_ManagePageRead)
    #       Assert Test and print if assert is fail
    test_Name = "Asset ECMIdentifier Number"
    condition1 = textTractor_ECMIdentifier_Asset_Assets_ManagePageVar
    condition2 = text_ECMIdentifier_Asset_Assets_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset ECMIdentifier Number"
    print_Information_Var = text_ECMIdentifier_Asset_Assets_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    text_AdditionalECMIdentifier_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_AdditionalECMIdentifier_Asset_Assets_ManagePageId))))
    text_AdditionalECMIdentifier_Asset_Assets_ManagePage.send_keys(textTractor_AdditionalECMIdentifier_Asset_Assets_ManagePageVar)
    text_AdditionalECMIdentifier_Asset_Assets_ManagePageRead = text_AdditionalECMIdentifier_Asset_Assets_ManagePage.get_attribute('value')
    #       Assert Test and print if assert is fail
    test_Name = "Asset AdditionalECMIdentifier Number"
    condition1 = textTractor_AdditionalECMIdentifier_Asset_Assets_ManagePageVar
    condition2 = text_AdditionalECMIdentifier_Asset_Assets_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset AdditionalECMIdentifier Number"
    print_Information_Var = text_AdditionalECMIdentifier_Asset_Assets_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    #   Scroll to action element - "Fuel Type Primary
    label_FuelTypePrimary_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,label_FuelTypePrimary_Asset_Assets_ManagePageAdr))))
    actions = ActionChains(driver)
    actions.move_to_element(label_FuelTypePrimary_Asset_Assets_ManagePage)
    actions.perform()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropBox_FuelTypePrimary_Asset_Assets_ManagePageId))))
    dropBox_FuelTypePrimary_Asset_Assets_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropBox_FuelTypePrimary_Asset_Assets_ManagePage_List):
        dropBox_FuelTypePrimary_Asset_Assets_ManagePage_Selected = dropDown.select_by_visible_text(dropBox_FuelTypePrimary_Asset_Assets_ManagePage_List[n])
        dropBox_FuelTypePrimary_Asset_Assets_ManagePage_Read = dropDown.first_selected_option.text
        n = n + 1

    text_Make_Asset_Assets_ManagePage = w.until(EC.presence_of_element_located((By.XPATH,text_Make_Asset_Assets_ManagePageAdr)))
    text_Make_Asset_Assets_ManagePage.send_keys(textTractor_Make_Asset_Assets_ManagePageVar)
    text_Make_Asset_Assets_ManagePageRead = text_Make_Asset_Assets_ManagePage.get_attribute('value')
    #       Assert Test and print if assert is fail
    test_Name = "Asset Asset Number"
    condition1 = textTractor_Make_Asset_Assets_ManagePageVar
    condition2 = text_Make_Asset_Assets_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset Asset Number"
    print_Information_Var = text_Make_Asset_Assets_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    text_Model_Asset_Assets_ManagePage = w.until(EC.presence_of_element_located((By.XPATH,text_Model_Asset_Assets_ManagePageAdr)))
    text_Model_Asset_Assets_ManagePage.send_keys(textTractor_Model_Asset_Assets_ManagePageVar)
    text_Model_Asset_Assets_ManagePageRead = text_Model_Asset_Assets_ManagePage.get_attribute('value')
    #       Assert Test and print if assert is fail
    test_Name = "Asset Model Number"
    condition1 = textTractor_Model_Asset_Assets_ManagePageVar
    condition2 = text_Model_Asset_Assets_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset Model Number"
    print_Information_Var = text_Model_Asset_Assets_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    text_Year_Asset_Assets_ManagePage = w.until(EC.presence_of_element_located((By.XPATH,text_Year_Asset_Assets_ManagePageAdr)))
    text_Year_Asset_Assets_ManagePage.send_keys(textTractor_Year_Asset_Assets_ManagePageVar)
    text_Year_Asset_Assets_ManagePageRead = text_Year_Asset_Assets_ManagePage.get_attribute('value')
    #       Assert Test and print if assert is fail
    test_Name = "Asset Year Number"
    condition1 = textTractor_Year_Asset_Assets_ManagePageVar
    condition2 = text_Year_Asset_Assets_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset Year Number"
    print_Information_Var = text_Year_Asset_Assets_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropBox_Type_Asset_Assets_ManagePageId))))
    dropBox_Type_Asset_Assets_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropBox_Type_Asset_Assets_ManagePage_List):
        dropBox_Type_Asset_Assets_ManagePage_Selected = dropDown.select_by_visible_text(dropBox_Type_Asset_Assets_ManagePage_List[n])
        dropBox_Type_Asset_Assets_ManagePage_Read = dropDown.first_selected_option.text
        n = n + 1

    text_BodyClass_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,text_BodyClass_Asset_Assets_ManagePageAdr))))
    text_BodyClass_Asset_Assets_ManagePage.send_keys(textTractor_BodyClass_Asset_Assets_ManagePageVar)
    text_BodyClass_Asset_Assets_ManagePageRead = text_BodyClass_Asset_Assets_ManagePage.get_attribute('value')
    #       Assert Test and print if assert is fail
    test_Name = "Asset BodyClass Number"
    condition1 = textTractor_BodyClass_Asset_Assets_ManagePageVar
    condition2 = text_BodyClass_Asset_Assets_ManagePageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset BodyClass Number"
    print_Information_Var = text_BodyClass_Asset_Assets_ManagePageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropBox_GVWR_Asset_Assets_ManagePageId))))
    dropBox_GVWR_Asset_Assets_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropBox_GVWR_Asset_Assets_ManagePage_List):
        dropBox_GVWR_Asset_Assets_ManagePage_Selected = dropDown.select_by_visible_text(dropBox_GVWR_Asset_Assets_ManagePage_List[n])
        dropBox_GVR_Asset_Assets_ManagePage_Read = dropDown.first_selected_option.text
        n = n + 1
    #dropDown.send_keys(textTractor_GVWR_Asset_Assets_ManagePageVar)

    button_CLOSE_Asset_Assets_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH,button_CLOSE_Asset_Assets_ManagePageAdr)))
    button_CLOSE_Asset_Assets_ManagePage.click()


    # Create Asset page -> Truck Asset
    #*********************************
    #   + New button
    #   Page Title on TCReport
    function_Name = "Create NEW TRACTOR Asset"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    w.until(EC.element_to_be_clickable((By.XPATH, button_PlussNew_Assets_ManagePageAdr))).click()
    dropBox_AssetType_Asset_Assets_ManagePage = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_AssetType_Asset_Assets_ManagePageId))))
    dropBox_AssetType_Asset_Assets_ManagePage.select_by_visible_text("Tractor")

    text_Number_Asset_Assets_ManagePage = w.until(EC.presence_of_element_located((By.ID, text_Number_Asset_Assets_ManagePageId)))
    text_Number_Asset_Assets_ManagePage.send_keys(textTractor_Number_Asset_Assets_ManagePageVar)
    text_VIN_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_VIN_Asset_Assets_ManagePageId))))
    text_VIN_Asset_Assets_ManagePage.send_keys(textTractor_VIN_Asset_Assets_ManagePageVar)


    text_Plate_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_Plate_Asset_Assets_ManagePageId))))
    text_Plate_Asset_Assets_ManagePage.send_keys(textTractor_Plate_Asset_Assets_ManagePageVar)
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_RegistrationState_Asset_Assets_ManagePageId))))
    dropDown.select_by_visible_text("ID")
    text_Description_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, text_Description_Asset_Assets_ManagePageAdr))))
    text_Description_Asset_Assets_ManagePage.send_keys(textTractor_Description_Asset_Assets_ManagePageVar)

    text_ECMIdentifier_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_ECMIdentifier_Asset_Assets_ManagePageId))))
    text_ECMIdentifier_Asset_Assets_ManagePage.send_keys(textTractor_ECMIdentifier_Asset_Assets_ManagePageVar)

    dropBox_FuelTypePrimary_Asset_Assets_ManagePage = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_FuelTypePrimary_Asset_Assets_ManagePageId))))
    dropBox_FuelTypePrimary_Asset_Assets_ManagePage.select_by_visible_text("Biodiesel")

    text_Make_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, text_Make_Asset_Assets_ManagePageAdr))))
    text_Make_Asset_Assets_ManagePage.send_keys(textTractor_Make_Asset_Assets_ManagePageVar)

    text_Model_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, text_Model_Asset_Assets_ManagePageAdr))))
    text_Model_Asset_Assets_ManagePage.send_keys(textTractor_Model_Asset_Assets_ManagePageVar)

    text_Year_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, text_Year_Asset_Assets_ManagePageAdr))))
    text_Year_Asset_Assets_ManagePage.send_keys(textTractor_Year_Asset_Assets_ManagePageVar)

    dropBox_Type_Asset_Assets_ManagePage = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Type_Asset_Assets_ManagePageId))))
    dropBox_Type_Asset_Assets_ManagePage.select_by_visible_text("TRUCK")

    text_BodyClass_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, text_BodyClass_Asset_Assets_ManagePageAdr))))
    text_BodyClass_Asset_Assets_ManagePage.send_keys(textTractor_BodyClass_Asset_Assets_ManagePageVar)

    dropBox_GVWR_Asset_Assets_ManagePage = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_GVWR_Asset_Assets_ManagePageId))))
    dropBox_GVWR_Asset_Assets_ManagePage.select_by_visible_text("Class 8: 33,001 lb and above (14,969 kg and above)")

    button_SAVE_Asset_Assets_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_Asset_Assets_ManagePageAdr))).click()

    # Create Asset -> Trailer Asset
    #*********************************
    #   + New button
    w.until(EC.element_to_be_clickable((By.XPATH, button_PlussNew_Assets_ManagePageAdr))).click()
    #   Page Title on TCReport
    function_Name = "Create NEW TRAILER Asset"

    dropBox_AssetType_Asset_Assets_ManagePage = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_AssetType_Asset_Assets_ManagePageId))))
    dropBox_AssetType_Asset_Assets_ManagePage.select_by_visible_text("Trailer")

    text_Number_Asset_Assets_ManagePage = w.until(EC.presence_of_element_located((By.ID, text_Number_Asset_Assets_ManagePageId)))
    text_Number_Asset_Assets_ManagePage.send_keys(textTrailer_Number_Asset_Assets_ManagePageVar)
    text_VIN_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_VIN_Asset_Assets_ManagePageId))))
    text_VIN_Asset_Assets_ManagePage.send_keys(textTrailer_VIN_Asset_Assets_ManagePageVar)
    text_Plate_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_Plate_Asset_Assets_ManagePageId))))
    text_Plate_Asset_Assets_ManagePage.send_keys(textTrailer_Plate_Asset_Assets_ManagePageVar)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_RegistrationState_Asset_Assets_ManagePageId))))
    dropDown.select_by_visible_text("ID")

    text_Description_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, text_Description_Asset_Assets_ManagePageAdr))))
    text_Description_Asset_Assets_ManagePage.send_keys(textTrailer_Description_Asset_Assets_ManagePageVar)

    button_SAVE_Asset_Assets_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH,button_SAVE_Asset_Assets_ManagePageAdr))).click()
    #button_CLOSE_Asset_Assets_ManagePage.click()

    #########################################################################################################################################################################
    #****************************************************************************************
    # Verify Truck created
    #****************************************************************************************
    #   Page Title on TCReport
    function_Name = "Verify NEW TRACTOR created"

    print(textTractor_Number_Asset_Assets_ManagePageVar)
    input_Search_AssetsVar = w.until(EC.presence_of_element_located((By.XPATH, input_Search_AssetsAdr)))
    input_Search_AssetsVar.send_keys(textTractor_Number_Asset_Assets_ManagePageVar)
    time.sleep(2)
    text_1stAssetNumber_Assets_ManagePageVar = w.until(EC.presence_of_element_located((By.XPATH, text_1stAssetNumber_Assets_ManagePageAdr))).text
#       Assert Test and print if assert is fail
    test_Name = "New Truck created - checked"
    condition1 = text_1stAssetNumber_Assets_ManagePageVar
    condition2 = textTractor_Number_Asset_Assets_ManagePageVar
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New Truck created - checked"
    print_Information_Var = text_1stAssetNumber_Assets_ManagePageVar
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    w.until(EC.element_to_be_clickable((By.XPATH, input_ClearSearch_AssetsAdr))).click()

    # ****************************************************************************************
    # Verify Trailer created
    # ****************************************************************************************
    #   Page Title on TCReport
    function_Name = "Verify NEW TRAILER created"

    input_Search_AssetsVar = w.until((EC.presence_of_element_located(((By.XPATH, input_Search_AssetsAdr)))))
    input_Search_AssetsVar.send_keys(textTrailer_Number_Asset_Assets_ManagePageVar)
    time.sleep(1)
    text_1stAssetNumber_Assets_ManagePageVar = w.until((EC.presence_of_element_located(((By.XPATH, text_1stAssetNumber_Assets_ManagePageAdr))))).text
    #       Assert Test and print if assert is fail
    test_Name = "New Trailer created - checked"
    condition1 = text_1stAssetNumber_Assets_ManagePageVar
    condition2 = textTrailer_Number_Asset_Assets_ManagePageVar
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New Trailer created - checked"
    print_Information_Var = text_1stAssetNumber_Assets_ManagePageVar
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Assets created - SAVED"
    tc_reports.screenshot(driver, driver_Name, test_Name)
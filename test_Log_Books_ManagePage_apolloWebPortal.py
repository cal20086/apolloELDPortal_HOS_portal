#               Apollo Web Portal - LOG BOOKS

def Log_Books_ManagePage (driver, driver_Name, driver_Version, carrier):

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
    import test_Global_Addresses_apolloWebPortal

    #               DVIR Main

    #       Fields Address
    menuRegion_MainSideBar_ManagePageAdrAsideDiv = test_Global_Addresses_apolloWebPortal.menuRegion_MainSideBar_ManagePageAdrAsideDiv_Global
    button_Log_Books_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_Log_Books_ManagePageAdr_Global
    title_Log_Books_Log_BooksPageAdr = test_Global_Addresses_apolloWebPortal.title_Log_Books_Log_BooksPageAdr_Global

    button_DVIR_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_DVIR_ManagePageAdr_Global
    title_DVIR_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.title_DVIR_DVIRPageAdr_Global
    dropBox_Carrier_DVIRPageAdrID = test_Global_Addresses_apolloWebPortal.dropBox_Carrier_DVIRPageAdrID_Global
    dropBox_Carrier_DVIRPageReadAdr = test_Global_Addresses_apolloWebPortal.dropBox_Carrier_DVIRPageReadAdr_Global
    dropBox_Status_DVIRPageAdrID = test_Global_Addresses_apolloWebPortal.dropBox_Status_DVIRPageAdrID_Global
    dropBox_Status_DVIRPageReadAdr = test_Global_Addresses_apolloWebPortal.dropBox_Status_DVIRPageReadAdr_Global
    dropBox_Drivers_DVIRPageID = test_Global_Addresses_apolloWebPortal.dropBox_Drivers_DVIRPageID_Global
    dropBox_Drivers_DVIRPageReadAdr = test_Global_Addresses_apolloWebPortal.dropBox_Drivers_DVIRPageReadAdr_Global
    date_SatrtEndDate_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.date_SatrtEndDate_DVIRPageAdr_Global
    button_Execute_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.button_Execute_DVIRPageAdr_Global
    sliderSwitch_MoreFilters_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.sliderSwitch_MoreFilters_DVIRPageAdr_Global
    title_TractorNumber_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.title_TractorNumber_DVIRPageAdr_Global
    text_TractorNumber_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.text_TractorNumber_DVIRPageAdr_Global
    text_TrailerNumber_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.text_TrailerNumber_DVIRPageAdr_Global
    dropBox_VehicleCondition_DVIRPageID = test_Global_Addresses_apolloWebPortal.dropBox_VehicleCondition_DVIRPageID_Global
    dropBox_VehicleCondition_DVIRPageReadAdr = test_Global_Addresses_apolloWebPortal.dropBox_VehicleCondition_DVIRPageReadAdr_Global
    dropBox_Report_DVIRPageID = test_Global_Addresses_apolloWebPortal.dropBox_Report_DVIRPageID_Global
    dropBox_Categories_DVIRPageID = test_Global_Addresses_apolloWebPortal.dropBox_Categories_DVIRPageID_Global
    dropBox_Defects_DVIRPageID = test_Global_Addresses_apolloWebPortal.dropBox_Defects_DVIRPageID_Global
    input_Defects_DVIRPageAdr =  test_Global_Addresses_apolloWebPortal.input_Defects_DVIRPageAdr_Global
    read_Defects_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.read_Defects_DVIRPageAdr_Global
    input_Defects_RemoveAllItems_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.input_Defects_RemoveAllItems_DVIRPageAdr_Global
    # Clock
    button_Manage_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.button_Manage_DVIRPageAdr_Global
    button_calendar_StartEndDate_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.button_calendar_StartEndDate_DVIRPageAdr_Global
    calendar_Month_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.calendar_Month_DVIRPageAdr_Global
    calendar_Year_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.calendar_Year_DVIRPageAdr_Global
    calendar_DayStart_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.calendar_DayStart_DVIRPageAdr_Global
    calendar_DayEnd_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.calendar_DayEnd_DVIRPageAdr_Global
    header_Driver_DVIRReport_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.header_Driver_DVIRReport_DVIRPageAdr_Global
    title_ManagePageAdr = test_Global_Addresses_apolloWebPortal.title_ManagePageAdr_Global
    download_ReportBigDVIR_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.download_ReportBigDVIR_DVIRPageAdr_Global
    download_ReportBigDVIR_zip_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.download_ReportBigDVIR_zip_DVIRPageAdr_Global
    title_TractorNumber_DVIRPageAdr = test_Global_Addresses_apolloWebPortal.title_TractorNumber_DVIRPageAdr_Global

    #   Global Variables

    workbookDB = test_Global_Variables_apolloWebPortal.workbookDB_Global
    worksheetDB = test_Global_Variables_apolloWebPortal.worksheetDB_Global

    #       Variables
    text_CarrierInTestVar = "QA Carrier"
    Ref_DVIR_DVIRPage = "DVIR"
    tractorNumber_DVIRPageVar = "112233445566778"
    trailerNumber_DVIRPageVar = "101010101010101"

    month_AbreviationList = ["Jan", "Feb", "Mar", "Apr", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    download_ReportBigDVIR_DVIRPagePath = "C:/Users/Carlos/Downloads/report_big_dvir.pdf"
    download_Delete_Report_DVIR_DVIRPagePath = "C:/Users/Carlos/Downloads/report_*.pdf"
    download_Delete_Report_DVIR_zip_DVIRPagePath = "C:/Users/Carlos/Downloads/BulkELDExportDVIR*.zip"
    startday_Position_Calendar_DVIRPageRowVar = 2
    day_Position_Calendar_DVIRPageStrInit = "/html/body/app-root/app-main/div/div[1]/app-dvir/section/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div["
    day_Position_Calendar_DVIRPageStrMid = "]/div["
    startday_Position_Calendar_DVIRPageColVar = 1
    day_Position_Calendar_DVIRPageStrEnd = "]"
    day_1st7ColumPosition_Calendar_DVIRPage = "/html/body/app-root/app-main/div/div[1]/app-dvir/section/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[7]/div[1]"
    lastday_Position_Calendar_DVIRPageRow6Var = 6
    lastday_Position_Calendar_DVIRPageRow7Var = 7
    lastday_Position_Calendar_DVIRPageColVar = 7
    w = WebDriverWait(driver, 30)



    #       #######################################     DVIR Main functions    ########################################################
    #   ###############################################################################################################################
#   Page Title on TCReport
    function_Name = "Log Books"
    tc_reports.function_Init_Page(function_Name, driver_Name)



#       Function Log Books side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_DVIR_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv,10).until(EC.element_to_be_clickable((By.XPATH, button_Log_Books_ManagePageAdr))).click()
    time.sleep(3)

#       Title of the right page
    title_Log_Books_Log_BooksPage = w.until(EC.presence_of_element_located((By.XPATH, title_Log_Books_Log_BooksPageAdr))).text
    test_Name = "Log Books page open"
    condition1 = "Log Books"
    condition2 = title_Log_Books_Log_BooksPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Log Books Page - Log Books page open:"
    print_Information_Var = title_Log_Books_Log_BooksPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)
    print(title_Log_Books_Log_BooksPage)

    return()


#       Carrier - Select    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Carrier_DVIRPageAdrID))))
    dropdown_Import_Carrier_DVIR_DVIRPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Carrier_DVIR_DVIRPage_List):
        dropBox_Carrier_DVIRPageSelected = dropDown.select_by_visible_text(dropdown_Import_Carrier_DVIR_DVIRPage_List[n])
        time.sleep(0)
        dropBox_Carrier_DVIRPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Status element DVIR page"
        condition1 = dropdown_Import_Carrier_DVIR_DVIRPage_List[n]
        condition2 = dropBox_Carrier_DVIRPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "DVIR Page - Carrier element:"
        print_Information_Var = dropBox_Carrier_DVIRPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)
        n = n + 1

    dropDown.select_by_visible_text(text_CarrierInTestVar)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)


#       Status - Select %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Status_DVIRPageAdrID))))
    dropdown_Import_Status_DVIR_DVIRPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Status_DVIR_DVIRPage_List):
        dropBox_Status_DVIRPageSelected = dropDown.select_by_visible_text(dropdown_Import_Status_DVIR_DVIRPage_List[n])
        dropBox_Status_DVIRPageRead = dropDown.first_selected_option.text
    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
        test_Name = "Status element DVIR page"
        condition1 = dropdown_Import_Status_DVIR_DVIRPage_List[n]
        condition2 = dropBox_Status_DVIRPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
        print_Information_Fix = "DVIR Page - Status element:"
        print_Information_Var = dropBox_Status_DVIRPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
        dropDown.select_by_visible_text("All")
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)

#       Driver - Select
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Drivers_DVIRPageID))))
    dropdown_Import_Driver_DVIR_DVIRPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Driver_DVIR_DVIRPage_List):
        dropBox_Drivers_DVIRPageSelected = dropDown.select_by_visible_text(dropdown_Import_Driver_DVIR_DVIRPage_List[n])
        dropBox_Drivers_DVIRPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Drivers element DVIR page"
        condition1 = dropdown_Import_Driver_DVIR_DVIRPage_List[n]
        condition2 = dropBox_Drivers_DVIRPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "DVIR Page - Drivers element"
        print_Information_Var = dropBox_Drivers_DVIRPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
        #dropDown.select_by_visible_text("Active")
        dropDown_Status = dropDown
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Drivers_DVIRPageID))))
    dropDown.select_by_visible_text("All")

#   Calendar Start-End date
    date_now = datetime.now()
    td = timedelta(30)
    date_now = date_now
    date_ActualMonth = str(date_now)
    year_ActualMonth = date_ActualMonth[:4]
    month_ActualMonth = date_ActualMonth[5:-19]
    month_ActualMonth = int(month_ActualMonth) + 1
    month_Abreviation_ActualMonth = month_AbreviationList[month_ActualMonth]
    calendar_Month_DVIRPageVar = month_Abreviation_ActualMonth
    calendar_Year_DVIRPageVar = year_ActualMonth
    button_calendar_StartEndDate_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, button_calendar_StartEndDate_DVIRPageAdr)))
    button_calendar_StartEndDate_DVIRPage.click()
    calendar_Month_DVIRPage = Select(w.until(EC.element_to_be_clickable((By.XPATH, calendar_Month_DVIRPageAdr))))
    calendar_Month_DVIRPage.select_by_visible_text(calendar_Month_DVIRPageVar)
    calendar_Year_DVIRPage = Select(w.until(EC.element_to_be_clickable((By.XPATH, calendar_Year_DVIRPageAdr))))
    calendar_Year_DVIRPage.select_by_visible_text(calendar_Year_DVIRPageVar)
    #       Try if the last weekday is in the 7th Row of the calendar
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, day_1st7ColumPosition_Calendar_DVIRPage))).click()
        lastday_Position_Calendar_DVIRPageRowVar = str(lastday_Position_Calendar_DVIRPageRow7Var)
    except:
        lastday_Position_Calendar_DVIRPageRowVar = str(lastday_Position_Calendar_DVIRPageRow6Var)

    # Find the 1st weekday of the month
    col = 1
    while col < 8:
        try:
            calendar_StartDay_DVIRPageAdr = day_Position_Calendar_DVIRPageStrInit + str(startday_Position_Calendar_DVIRPageRowVar) + day_Position_Calendar_DVIRPageStrMid + str(startday_Position_Calendar_DVIRPageColVar) + day_Position_Calendar_DVIRPageStrEnd
            calendar_StartDay_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, calendar_StartDay_DVIRPageAdr))).click()
            col = 8
        except:
            startday_Position_Calendar_DVIRPageColVar += 1
            col += 1
    # Find the Last weekday of the month
    col = 7

    while col > 0:
        try:
            calendar_LastDay_DVIRPageAdr = day_Position_Calendar_DVIRPageStrInit + str(lastday_Position_Calendar_DVIRPageRowVar) + day_Position_Calendar_DVIRPageStrMid + str(lastday_Position_Calendar_DVIRPageColVar) + day_Position_Calendar_DVIRPageStrEnd
            calendar_LasttDay_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, calendar_LastDay_DVIRPageAdr))).click()
            col = 0
        except:
            lastday_Position_Calendar_DVIRPageColVar -= 1
            col -= 1
    w.until(EC.element_to_be_clickable((By.XPATH, button_calendar_StartEndDate_DVIRPageAdr))).click()

    # Delete all old report_big_dvir.pdf files created by the DVIR page on c: drive
    files = glob.glob(download_Delete_Report_DVIR_DVIRPagePath)
    for f in files:
        os.remove(f)

    # Delete all old BulkELDExportDVIR*.zip files created by the DVIR page on c: drive
    files = glob.glob(download_Delete_Report_DVIR_zip_DVIRPagePath)
    for f in files:
        os.remove(f)

    #       Execute button
    time.sleep(3)

    #dropDown_Status.select_by_visible_text("All")
    time.sleep(3)
    button_Execute_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, button_Execute_DVIRPageAdr))).click()
    #webdriver.ActionChains(driver).move_to_element(button_Execute_DVIRPage).click().perform()
    #button_Execute_DVIRPage.click()

    #               DVIR Report Available?
    try:
        a = w.until(EC.presence_of_element_located((By.XPATH, header_Driver_DVIRReport_DVIRPageAdr)))
        # print('DVIR report is available')
        #       There is DVIR Data - verify is a DVIR file is in the download directory
        # Download report_big_dvir.pdf file
        test_Name = "DVIR Data Available"
        print_Information_Fix = "DVIR Page - Execute button"
        print_Information_Var = "There is DVIR available"
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                    driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)

        # VERIFY DVIR.PDF
        w.until(EC.element_to_be_clickable((By.XPATH, download_ReportBigDVIR_DVIRPageAdr))).click()
        time.sleep(3)
        if os.path.exists(download_ReportBigDVIR_DVIRPagePath):
            #       PASSED - The report_big_dvir.pdf file was saved.
            test_Name = "report_big_dvir.pdf - DVIR Reports download"
            print_Information_Fix = "report_big_dvir.pdf was downloaded"
            print_Information_Var = ""
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
            n = n + 1
            #       Screenshot
            tc_reports.screenshot(driver, driver_Name, test_Name)
        else:
            #       ERROR - The report_big_dvir.pdf file was not saved.
            print("Error file not downloaded")
            test_Name = "report_big_dvir.pdf - DVIR Reports download"
            condition1 = 1
            condition2 = 2
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Screenshot
            tc_reports.screenshot(driver, driver_Name, test_Name)

        # VERIFY DVIR.ZIP

        w.until(EC.element_to_be_clickable((By.XPATH, download_ReportBigDVIR_zip_DVIRPageAdr))).click()
        time.sleep(3)
        if os.path.exists(download_ReportBigDVIR_DVIRPagePath):
            #       PASSED - The report_big_dvir.pdf file was saved.
            test_Name = "report_big_dvir.zip - DVIR Reports download"
            print_Information_Fix = "report_big_dvir.zip was downloaded"
            print_Information_Var = ""
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
            n = n + 1
            #       Screenshot
            tc_reports.screenshot(driver, driver_Name, test_Name)
        else:
            #       ERROR - The report_big_dvir.zip file was not saved.
            print("Error file not downloaded")
            test_Name = "report_big_dvir.zip - DVIR Reports download"
            condition1 = 1
            condition2 = 2
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Screenshot
            tc_reports.screenshot(driver, driver_Name, test_Name)
    except:
        print('DVIR Data is NOT available')
        # There is NO DVIR Data
        #       Print Assert OK
        test_Name = "No DVIR Data Available"
        print_Information_Fix = "DVIR Page - Execute button -> PopUp toast message"
        print_Information_Var = "There is no data"
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)

    #       More Filter:
    sliderSwitch_MoreFilters_DVIRPage = w.until(EC.presence_of_element_located((By.XPATH, sliderSwitch_MoreFilters_DVIRPageAdr)))
    webdriver.ActionChains(driver).move_to_element(sliderSwitch_MoreFilters_DVIRPage).click(sliderSwitch_MoreFilters_DVIRPage).perform()
    time.sleep(2)

    #       Verify More filters works
    title_TractorNumber_DVIRPage = w.until((EC.presence_of_element_located((By.XPATH, title_TractorNumber_DVIRPageAdr)))).text
    test_Name = "More Filtes CheckBox"
    condition1 = "Tractor Number"
    condition2 = title_TractorNumber_DVIRPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DVIR Page - More Filtes CheckBox:"
    print_Information_Var = title_TractorNumber_DVIRPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)

    # TEST MORE FILTERS
    #       Tractor Number:
    text_TractorNumber_DVIRPage = w.until(EC.presence_of_element_located((By.XPATH, text_TractorNumber_DVIRPageAdr)))
    text_TractorNumber_DVIRPage.send_keys(tractorNumber_DVIRPageVar)
    tractorNumber_DVIRPageRead = text_TractorNumber_DVIRPage.get_property('value')
    test_Name = "Tractor Number element"
    condition1 = tractorNumber_DVIRPageVar
    condition2 = tractorNumber_DVIRPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DVIR Page - Tractor Number element:"
    print_Information_Var = tractorNumber_DVIRPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)


    #       Trailer Number:
    text_TrailerNumber_DVIRPage = w.until(EC.presence_of_element_located((By.XPATH, text_TrailerNumber_DVIRPageAdr)))
    text_TrailerNumber_DVIRPage.send_keys(trailerNumber_DVIRPageVar)

    trailerNumber_DVIRPageRead = text_TrailerNumber_DVIRPage.get_property('value')
    test_Name = "Trailer Number element"
    condition1 = trailerNumber_DVIRPageVar
    condition2 = trailerNumber_DVIRPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DVIR Page - Trailer Number element:"
    print_Information_Var = trailerNumber_DVIRPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)


    #       Vehicle Condition - Select
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_VehicleCondition_DVIRPageID))))
    dropdown_Import_VehicleCondition_DVIR_DVIRPageMoreFilters_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_VehicleCondition_DVIR_DVIRPageMoreFilters_List):
        dropBox_VehicleCondition_DVIRPageSelected = dropDown.select_by_visible_text(dropdown_Import_VehicleCondition_DVIR_DVIRPageMoreFilters_List[n])
        dropBox_VehicleCondition_DVIRPageRead = dropDown.first_selected_option.text
        #       Assert Test and print if assert is fail
        test_Name = "Vehicle Condition element DVIR page"
        condition1 = dropdown_Import_VehicleCondition_DVIR_DVIRPageMoreFilters_List[n]
        condition2 = dropBox_VehicleCondition_DVIRPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "DVIR page - Vehicle Condition element:"
        print_Information_Var = dropBox_VehicleCondition_DVIRPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
        dropDown.select_by_visible_text("All")
    #       Screenshot
    test_Name = "DVIR Page Fille up"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Clear Tractor & Trailler fields
    text_TractorNumber_DVIRPage.clear()
    text_TrailerNumber_DVIRPage.clear()

    # ############################################################################
    # Call Function to test Report, Categories and Defects and Interchanges logic:
    # ############################################################################
    dropBox_Report_PageID = dropBox_Report_DVIRPageID
    dropBox_Categories_PageID = dropBox_Categories_DVIRPageID
    dropBox_Defects_PageID = dropBox_Defects_DVIRPageID
    input_Defects_PageAdr = input_Defects_DVIRPageAdr
    read_Defects_PageAdr = read_Defects_DVIRPageAdr
    input_Defects_RemoveAllItems_PageAdr = input_Defects_RemoveAllItems_DVIRPageAdr
    source_Function = "DVIR"
    test_Report_Categories_Defects_FIELDSInterchanges_apolloWebPortal.Report_Categories_Defects_Interchanges(driver, driver_Name, driver_Version, dropBox_Report_PageID, dropBox_Categories_PageID, dropBox_Defects_PageID, read_Defects_PageAdr, input_Defects_PageAdr, input_Defects_RemoveAllItems_PageAdr, source_Function)

    #   Page Title on TCReport
    function_Name = "Return from Test REPORT, CATEGORIES and DEFECTS fields from " + source_Function
    tc_reports.function_Init_Page(function_Name, driver_Name)

    # ###################################################################################
    # Return from Function to test Report, Categories and Defects and Interchanges logic:
    # ###################################################################################

    #       Manage button
    button_Manage_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, button_Manage_DVIRPageAdr))).click()
    try:
        test_Name = "back to Manage page from DVIR page"
        title_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_ManagePageAdr))).text
        print_Information_Fix = "Manage page - Back to Manage page from DVIR page:"
        print_Information_Var = title_ManagePage
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:

    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
        test_Name = "back to Manage page from DVIR page"
        condition1 = "Manage"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)


    return ()
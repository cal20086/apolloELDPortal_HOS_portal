#               Apollo Web Portal - ENGINE DIAGNOSTIC

def Engine_Diagnostic_ManagePage (driver, driver_Name, driver_Version, carrier):

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
    button_EngineDiagnostic_ManagePageAdr = test_Global_Addresses_apolloWebPortal.button_EngineDiagnostic_ManagePageAdr_Global
    title_Engine_Diagnostic_Engine_Diagnostic_PageAdr = test_Global_Addresses_apolloWebPortal.title_Engine_Diagnostic_Engine_DiagnosticPageAdr_Global

    #   Global Variables

    workbookDB = test_Global_Variables_apolloWebPortal.workbookDB_Global
    worksheetDB = test_Global_Variables_apolloWebPortal.worksheetDB_Global

    #       Variables

    w = WebDriverWait(driver, 30)



    #       #######################################     DVIR Main functions    ########################################################
    #   ###############################################################################################################################
#   Page Title on TCReport
    function_Name = "ENGINE DIAGNOSTIC page"
    tc_reports.function_Init_Page(function_Name, driver_Name)

#       Function Log Books side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_EngineDiagnostic_ManagePageAdr = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv, 10).until(EC.element_to_be_clickable((By.XPATH, button_EngineDiagnostic_ManagePageAdr))).click()
    time.sleep(3)

#       Title of the right page
    title_Engine_Diagnostic_Engine_Diagnostic_Page = w.until(EC.presence_of_element_located((By.XPATH, title_Engine_Diagnostic_Engine_Diagnostic_PageAdr))).text
    test_Name = "Engine Diagnostic page open"
    condition1 = "Engine Diagnostic"
    condition2 = title_Engine_Diagnostic_Engine_Diagnostic_Page
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Engine Diagnostic Page - Engine Diagnostic page open:"
    print_Information_Var = title_Engine_Diagnostic_Engine_Diagnostic_Page
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)
    print(print_Information_Var)

    return()
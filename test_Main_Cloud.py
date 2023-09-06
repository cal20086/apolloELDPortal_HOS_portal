#               apollo Web Portal - Test Control page


from selenium import webdriver
import os

import time
from datetime import datetime

import test_Global_Variables_apolloWebPortal
import test_LoginPage_apolloWebPortal
import test_HomePage_apolloWebPortal
import test_ManagePage_apolloWebPortal
import test_ActionsCarrierDetails_ManagePage_apolloWebPortal
import test_ActionsDrivers_ManagePage_apolloWebPortal
import test_ActionsHomeBases_ManagePage_apolloWebPortal
import test_ActionsNotifications_ManagePage_apolloWebPortal
import test_ActionsAssets_ManagePage_apolloWebPortal
import test_DVIR_ManagePage_apolloWebPortal
import test_DVIR_WorkOrder_ManagePage_apolloWebPortal
import test_WorkOrder_ManagePage_apolloWebPortal
import test_WorkOrder_Flow_apolloWebPortal
import test_Report_Categories_Defects_FIELDSInterchanges_apolloWebPortal
import test_Enhanced_IFTAPage_apolloWebPortal
import test_Administration_Roles_ManagePage_apolloWebPortal
import test_Hierarchy_User_Access_ManagePage_apolloWebPortal
import test_Administration_Users_FullAccessReseller_ManagePage_apolloWebPortal
import test_Administration_Users_LimitedReseller_ManagePage_apolloWebPortal
import test_Administration_Users_FullAccessClient_ManagePage_apolloWebPortal
import test_Administration_Users_LimitedClient_ManagePage_apolloWebportal
import test_Administration_Roles_ManagePage_apolloWebPortal
import test_Administration_Users_MasterReseller_ManagePage_apolloWebPortal
import tc_reports
import test_Global_Variables_apolloWebPortal

#from selenium.webdriver.edge.service import Service
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.safari.service import Service



#               Open driver & Explicit:

#               Global Variables
global testCaseCounter_Global
#testCaseCounter_Global = 0


#               Variables
driverModelTestControl = 0

contol_Reportfile = 0
test_Case_Type = "Regression"

################################################
carrier = ["QA Carrier"]
# En Vivo
#carrier = ["LANDSTART INWAY INC"]
################################################

truckDriversList = ["All",
                    "QADriver1 (qadriver1)",
                    "QADriver2 (qadriver2)",
                    "QADriver3 (qadriver3)"]

# Site Development - HOS Direct
#siteAddressVar = "http://10.1.10.33:4202"
#siteAddressVar = "http://96.69.16.10/"
siteAddressVar = "https://cloud.apolloeld.com/userlogin"


driverListName = ["Chrome",
                  "Firefox",
                  "Edge",
                  "Opera"
                  ]

driverListVersion = ["103.0.5060.134 (Official Build) (64-bit)", "83.0.4254.27 (64-bit)",
                     "104.0.1293.47 (Official build) (64-bit)", "89.0.4447.83"
                     ]

driverDriverListVar = ["C:\\tools\chromedriver.exe",
                       "C:\\tools\geckodriver.exe",
                       "C:\\tools\msedgedriver.exe",
                       "C:\\tools\operadriver.exe"]

#####################################################################################
"""
user_ApolloWebPortalListVar = ["QA_MasterReseller",
                               "QA_MasterReseller",
                               "QA_MasterReseller",
                               "QA_MasterReseller",
                               "qauser5"]

password_ApolloWebPortalListVar = ["@MReseller1",
                                   "@MReseller1",
                                   "@MReseller1",
                                   "@MReseller1",
                                   "qauser5"]
"""
####################################################################################
user_ApolloWebPortalListVar = ["apollo.reseller",
                               "QA_MasterReseller",
                               "QA_MasterReseller",
                               "QA_MasterReseller",
                               "qauser5"]

password_ApolloWebPortalListVar = ["Apollo@2022",
                                   "@MReseller1",
                                   "@MReseller1",
                                   "@MReseller1",
                                   "qauser5"]
############################################################################################


truckDriversList = ["QADriver1 (qadriver1)",
                    "QADriver2 (qadriver2)",
                    "QADriver3 (qadriver3)",
                    "All"]
reportFolder_Path_QAReports = "C:/apollo QA Reports/apollo Web Portal/"
"""
driver_UserName_Var = test_Global_Variables_apolloWebPortal.input_DriverUserName_Global
client_Name_Var = test_Global_Variables_apolloWebPortal.client_Name_Var_Global
client_Address_Var = test_Global_Variables_apolloWebPortal.client_Address_Var_Global
client_Latitude_Var = test_Global_Variables_apolloWebPortal.input_Latitude_HomeBase_Global
client_Longitude_Var = test_Global_Variables_apolloWebPortal.input_Longitude_HomeBase_Global
#defect_Vehicle_List_Var = ("Refrigeration Unit", "Part 1. Air Brake System", "(b) air loss rate exceeds prescribed limit", "Part 19. Steering", "(b) steering wheel lash(free - play) exceeds prescribed limited")
defect_Vehicle_List_Var = test_Global_Variables_apolloWebPortal.defect_Vehicle_List_Var_Global
workOrder_CreatedBy_Var = test_Global_Variables_apolloWebPortal.workOrder_CreatedBy_Var_Global
workOrder_Contacts_Var = test_Global_Variables_apolloWebPortal.workOrder_Contacts_Var_Global
"""


driver_UserName_Var = "Test (sdsd1)"
client_Name_Var = "QA Carrier"
client_Address_Var = "1180 Seven Seas Dr, Walt Disney World, Orlando, FL 32830"
client_Latitude_Var = "28.4179"
client_Longitude_Var = "-81.5814"
#defect_Vehicle_List_Var = test_Global_Variables_apolloWebPortal.defect_Vehicle_List_Var_Global
defect_Vehicle_List_Var = ("Refrigeration Unit", "Part 1. Air Brake System", "(b) air loss rate exceeds prescribed limit", "Part 19. Steering", "(b) steering wheel lash(free - play) exceeds prescribed limit")
workOrder_CreatedBy_Var = "carlos.liguori@assuredtechmatics.com"
workOrder_Contacts_Var = ("vendor@vendor.com")




#####################################################################################################################################
#                                                        Main functions                                                             #
#####################################################################################################################################

dateInit = datetime.now()
# Delete all previous reports files
for f in os.listdir(reportFolder_Path_QAReports):
    os.remove(os.path.join(reportFolder_Path_QAReports, f))


while driverModelTestControl < 1:

    if driverModelTestControl == 0:
        from selenium.webdriver.chrome.service import Service
        driver = webdriver.Chrome(service=Service(driverDriverListVar[driverModelTestControl]))
    if driverModelTestControl == 1:
        from selenium.webdriver.firefox.service import Service
        driver = webdriver.Firefox(service=Service(driverDriverListVar[driverModelTestControl]))
    if driverModelTestControl == 2:
        from selenium.webdriver.edge.service import Service
        driver = webdriver.Edge(service=Service(driverDriverListVar[driverModelTestControl]))
    if driverModelTestControl == 3:
        from selenium.webdriver.Opera.service import Service
        driver = webdriver.Opera(service=Service(driverDriverListVar[driverModelTestControl]))
    if driverModelTestControl > 3:
        breack(1)

    dateInitbyDriver = datetime.now()
    driver_Name = driverListName[driverModelTestControl]
    driver_Version = driverListVersion[driverModelTestControl]
    user_ApolloWebPortalVar = user_ApolloWebPortalListVar[driverModelTestControl]
    password_ApolloWebPortalVar = password_ApolloWebPortalListVar[driverModelTestControl]

    print(driverModelTestControl)
    print(driver_Name)

# Call Functions:


    test_Global_Variables_apolloWebPortal.global_Variables()
    test_LoginPage_apolloWebPortal.login_apolloWebPortal(contol_Reportfile, driver, driver_Name, driver_Version, user_ApolloWebPortalVar, password_ApolloWebPortalVar, siteAddressVar, test_Case_Type)
    test_ManagePage_apolloWebPortal.managePage(driver, driver_Name, driver_Version, client_Name_Var,siteAddressVar)


    test_ActionsCarrierDetails_ManagePage_apolloWebPortal.carrierDetail_ChildMenu_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Address_Var)
#    test_ActionsDrivers_ManagePage_apolloWebPortal.carrierDrivers_ChildMenu_ManagePage(driver, driver_Name, driver_Version)
#!!!    test_ActionsHomeBases_ManagePage_apolloWebPortal.carrierHomeBases_ChildMenu_ManagePage(driver, driver_Name, driver_Version, client_Latitude_Var, client_Longitude_Var)
#    test_ActionsAssets_ManagePage_apolloWebPortal.carrierAssets_ChildMenu_ManagePage(driver, driver_Name, driver_Version)
#    test_ActionsNotifications_ManagePage_apolloWebPortal.carrierNotifications_ChildMenu_ManagePage (driver, driver_Name, driver_Version)
#!!!    test_DVIR_ManagePage_apolloWebPortal.DVIR_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList)
#    test_DVIR_WorkOrder_ManagePage_apolloWebPortal.DVIR_WorkOrder_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Address_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_WorkOrder_ManagePage_apolloWebPortal.WorkOrder_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Address_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_WorkOrder_Flow_apolloWebPortal.WorkOrder_Flow_ManagePage (driverModelTestControl, driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Address_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_Administration_Roles_ManagePage_apolloWebPortal.Administration_Roles_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList)
#    test_Administration_Users_MasterReseller_ManagePage_apolloWebPortal.Administration_Users_MasterReseller_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList)
#    test_Administration_Users_FullAccessReseller_ManagePage_apolloWebPortal.Administration_Users_FullAccessReseller_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList,siteAddressVar)
#    test_Administration_Users_LimitedReseller_ManagePage_apolloWebPortal.Administration_Users_LimitedReseller_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList,siteAddressVar)
#    test_Administration_Users_FullAccessClient_ManagePage_apolloWebPortal.Administration_Users_FullAccessClient_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList,siteAddressVar)
#    test_Administration_Users_LimitedClient_ManagePage_apolloWebportal.Administration_Users_LimitedClient_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList,siteAddressVar)
#    ##############test_Enhanced_IFTAPage_apolloWebPortal.EnhancedIFTA_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList)

    #driver.close()

    #def datebyDriver_Calc():
    #    dateEnd = datetime.now()
    #    datebyDriver = dateEnd - dateInitbyDriver
    #    return datebyDriver

    dateEnd = datetime.now()
    datebyDriver = dateEnd - dateInitbyDriver
    test_Execution_Time_By_Driver_Global = datebyDriver

    print()
    print(f"{driver_Name} - Test executing time TOTAL = {datebyDriver}")


    tc_reports.summaryPerformance_by_Driver(driver, driver_Name, datebyDriver)


    #       Print Preformance Summary
    #tc_reports.summaryPerformance_by_Driver(driver, driver_Name)


    driverModelTestControl = driverModelTestControl + 1

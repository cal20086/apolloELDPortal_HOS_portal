#               apollo Web Portal - Test Control page

def NewUser_Check_Hierarchy_User_Access_MenuPage (driver, driver_Name, driver_Version, carrier, truckDriversList, var_UsernameVar, var_PasswordVar, text_CarrierType, siteAddressVar):
    print("new user stop ***************************************************************************************************")
    import test_LoginPage_2_apolloWebPortal
    import tc_reports

    #               Global Variables
    global testCaseCounter_Global

    print("TEST NEW USER CHECK HIERARCHY")

    #               Variables
    driverModelTestControl = 0
    test_Case_Type = "Regression"
    client_Name_Var = "Apollo Copy"
    driverOriginal = driver

    #   Page Title on TCReport
    function_Name = "********** TEST NEW USER PRIVILEGE ON THE MAIN MENU **********"
    tc_reports.function_Init_Page(function_Name, driver_Name)
    function_Name = "************ LOGIN THE NEW USER ON A NEW BROWSER  ************"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    driverListName = "Edge"

    driverDriverListVar = "C:\\tools\msedgedriver.exe"
    carrier = ["QATest1"]



    #####################################################################################################################################
    #                                                        Main functions                                                             #
    #####################################################################################################################################
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    from selenium.webdriver.edge.service import Service


    driver_Name = driverListName
    #driver_Version = driverListVersion
    user_ApolloWebPortalVar = var_UsernameVar
    password_ApolloWebPortalVar = var_PasswordVar
    contol_Reportfile = 1



    # Call Functions:

    print(f' New user = {siteAddressVar}')
    #test_Global_Variables_apolloWebPortal.global_Variables()
    test_LoginPage_2_apolloWebPortal.login_2_apolloWebPortal(contol_Reportfile, driver, driver_Name, driver_Version, user_ApolloWebPortalVar, password_ApolloWebPortalVar, test_Case_Type, siteAddressVar, carrier, truckDriversList)


    driver = driverOriginal

    #   Page Title on TCReport
    function_Name = "******** NEW USER PRIVILEGE ON THE MAIN MENU END ********"
    tc_reports.function_Init_Page(function_Name, driver_Name)
    function_Name = "********* LOGOUT AND CLOSE THE NEW BROWSER  *************"

    return()
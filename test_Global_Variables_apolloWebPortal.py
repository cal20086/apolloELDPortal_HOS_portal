#   Global Variables

from datetime import datetime
import re

def global_Variables():

    date = datetime.now()
    random = str(date)
    random = random[len(random) - 6:]
    random = str(random)
    global carriers_List_Global
    global homeBase_List_Global
    global UserROLE
    global USERType

    userROLE_Global = int()
    userTYPE_Global = int()

    carrier_list_Global = list()
    homebase_List_Global = list()

    global menuRegion_MainSideBar_ManagePageAdrAsideDiv_Global
    menuRegion_MainSideBar_ManagePageAdrAsideDiv_Global = "/html/body/app-root/app-main/div/main-side-bar/aside/div"

    ###########################################################################
    # excel Data Base access INFORMATION
    # Module -
    ###########################################################################
    global workbookDB_Global
    global worksheetDB_Global
    global testCaseCounter_Global
    global test_Execution_Time_By_Driver_Global
    global workbookMANAGEDB_Global
    global worksheetMANAGEDB_Global
    workbookDB_Global = "C:/apollo QA Reports/Support test DB/apolloPortalDVIRReportDB.xlsx"
    worksheetDB_Global = "PortalDVIRReports"
    workbookMANAGEDB_Global = "C:/apollo QA Reports/Support test DB/apolloPortalMANAGEReportDB.xlsx"
    worksheetMANAGEDB_Global = "PortalMANAGEReportsDB"
    test_Execution_Time_By_Driver_Global = str()
    ###########################################################################


    ###########################################################################
    # DVIR & WORK ORDER INFORMATION
    # Module that Call those variables: test_Main_QATest1.py
    #                                   test_ActionsCarrierDetails_ManagePage_apolloWebPortal.py
    ###########################################################################

    global client_Name_Var_Global
    global client_Address_Var_Global
    global defect_Vehicle_List_Var_Global
    global workOrder_CreatedBy_Var_Global
    global workOrder_Contacts_Var_Global
    client_Name_Var_Global = "Carrier Test"
    client_Address_Var_Global = "11111 NE 11st Doral 33150"
    defect_Vehicle_List_Var_Global = ("Refrigeration Unit", "Part 1. Air Brake System", "(b) air loss rate exceeds prescribed limit", "Part 19. Steering", "(b) steering wheel lash(free - play) exceeds prescribed limit")
    workOrder_CreatedBy_Var_Global = "carlos.liguori@assuredtechmatics.com"
    workOrder_Contacts_Var_Global = "carlos.liguori@assuredtechmatics.com"


    ###########################################################################
    # CARRIER INFORMATION
    # Module that Call those variables: - test_ActionsCarrierDetails_ManagePage_apolloWebPortal.py
    ###########################################################################
    global var_DOT_Number_Original_Global
    global var_DOT_Number_Global
    global var_DOT_Number_Global
    global var_CarrierName_Global
    global var_CarrierAddress_Global
    global var_SupportUsername_Global
    global var_SupportUsername_Global
    global var_SupportPassword_Global
    var_DOT_Number_Original_Global = "111111108"
    var_DOT_Number_Global = date.strftime("%S %f")
    var_DOT_Number_Global = re.sub('\W+', '', var_DOT_Number_Global)
    var_CarrierName_Global = client_Name_Var_Global + date.strftime(" %b%d%Y %f")
    var_CarrierAddress_Global = "1180 Seven Seas Dr, Walt Disney World, Orlando, FL 32830"
    var_SupportUsername_Global = "QA" + date.strftime("%b%d%Y") + date.strftime("%H:%M:%S")
    var_SupportUsername_Global = re.sub('\W+', '', var_SupportUsername_Global)
    var_SupportPassword_Global = "QAuser"


    ###########################################################################
    # HOME BASE INFORMATION
    # Module that Call those variables: - test_ActionsCarrierDetails_ManagePage_apolloWebPortal.py
    ###########################################################################
    global input_LocationName_HomeBase_Global
    global input_Address_HomeBase_Global
    global input_Latitude_HomeBase_Global
    global input_Longitude_HomeBase_Global
    input_LocationName_HomeBase_Global = "Magic Kingdom Park " + random
    input_Address_HomeBase_Global = "1180 Seven Seas Dr, Walt Disney World, Orlando, FL 32830"
    input_Latitude_HomeBase_Global = "28.4179"
    input_Longitude_HomeBase_Global = "-81.5814"


    ###########################################################################
    # DRIVER INFORMATION
    # Module that Call those variables:- test_ActionsCarrierDetails_ManagePage_apolloWebPortal.py
    ###########################################################################
    global input_DriverName_Global
    global input_DriverLastName_Global
    global input_DriverUserName_Global
    global input_DriverPassword_Global
    input_DriverName_Global = "QADriver1" + random
    input_DriverLastName_Global = "QADriver1Last" + random
    input_DriverUserName_Global = "qadriver1"
    input_DriverPassword_Global = "qadriver1"




    ###########################################################################
    # ASSETS INFORMATION
    # Module that Call those variables: - test_ActionsAssets_ManagePage_apolloWebPortal.py
    ###########################################################################
    global textTractor_Number_AssetVar_Global
    global textTractor_VIN_AssetVar_Global
    global textTractor_Plate_AssetVar_Global
    global textTractor_Description_Asset_Var_Global
    global textTractor_ECMIdentifier_Asset_Var_Global
    global dropBox_RegistrationState_Asset_Var_Global
    global textTractor_ECMIdentifier_Asset_Var_Global
    global textTractor_AdditionalECMIdentifier_Asset_Assets_ManagePageVar_Global
    global textTractor_FuelTypePrimary_Asset_Assets_ManagePageVar_Global
    global textTractor_Make_Asset_Assets_ManagePageVar_Global
    global textTractor_Model_Asset_Assets_ManagePageVar_Global
    global textTractor_Year_Asset_Assets_ManagePageVar_Global
    global textTractor_Type_Asset_Assets_ManagePageVar_Global
    global textTractor_BodyClass_Asset_Assets_ManagePageVar_Global
    global dropBox_Tractor_GVWR_Asset_Assets_ManagePageVar_Global
    global textTrailer_Number_Asset_Assets_ManagePageVar_Global
    global textTrailer_VIN_Asset_Assets_ManagePageVar_Global
    global textTrailer_Plate_Asset_Assets_ManagePageVar_Global
    global textTrailer_Description_Asset_Assets_ManagePageVar_Global
    textTractor_Number_AssetVar_Global = "QATru" + random[:-1]
    textTractor_VIN_AssetVar_Global = "VNTRUCK0000" + random
    textTractor_Plate_AssetVar_Global = "QA" + random
    textTractor_Description_Asset_Var_Global = "QA TRUCK" + random
    textTractor_ECMIdentifier_Asset_Var_Global = "AABBCCDDEEFF"
    dropBox_RegistrationState_Asset_Var_Global = "ID"
    textTractor_ECMIdentifier_Asset_Var_Global = "012345" + random
    textTractor_AdditionalECMIdentifier_Asset_Assets_ManagePageVar_Global = random
    textTractor_FuelTypePrimary_Asset_Assets_ManagePageVar_Global = "Biodiesel"
    textTractor_Make_Asset_Assets_ManagePageVar_Global = "Peterbilt"
    textTractor_Model_Asset_Assets_ManagePageVar_Global = "579"
    textTractor_Year_Asset_Assets_ManagePageVar_Global = "2022"
    textTractor_Type_Asset_Assets_ManagePageVar_Global = "TRUCK"
    textTractor_BodyClass_Asset_Assets_ManagePageVar_Global = "Heavy-Duty"
    dropBox_Tractor_GVWR_Asset_Assets_ManagePageVar_Global = "Class 8:33,001 lb and above (14,969 kg and above)"
    textTrailer_Number_Asset_Assets_ManagePageVar_Global = "QATra" + random[:-1]
    textTrailer_VIN_Asset_Assets_ManagePageVar_Global = "VNTrailer00" + random
    textTrailer_Plate_Asset_Assets_ManagePageVar_Global = "TR" + random
    textTrailer_Description_Asset_Assets_ManagePageVar_Global = "Description QATRAILER " + random
    ###########################################################################





    #################################################################################################################
    # USER HIERARCHY
    # ADMINISTRATION USER INFORMATION
    # Module that Call those variables: - test_Administration_User_MasterReseller_ManagePage_apolloWebPortal.py
    #                                   - test_Administration_User_FullAccessReseller_ManagePage_apolloWebPortal.py
    #                                   - test_Administration_User_LimitedReseller_ManagePage_apolloWebPortal.py
    #                                   - test_Administration_User_FullAccessClient_ManagePage_apolloWebPortal.py
    #                                   - test_Administration_User_LimitedClient_ManagePage_apolloWebPortal.py
    #################################################################################################################
    # COMMON
    global var_CarrierFull_Var_Global
    var_CarrierFull_Var_Global = "QA Carrier"
    global text_CarrierLimited_Var_Global
    text_CarrierLimited_Var_Global = "QA Carrier Limited"
    global var_Username_ExistVar_Global
    var_Username_ExistVar_Global = "MasterReseller"

    # MASTER RESSELER
    global var_MasterReseller_UsernameVar_Global
    global var_MasterReseller_EmailVar_Global
    global var_MasterReseller_PasswordVar_Global
    global var_MasterReseller_ConfirmationPasswordVar_Global
    global var_MasterReseller_TypeOfUserVar_Global
    var_MasterReseller_UsernameVar_Global = "QA_MasterReseller"
    var_MasterReseller_EmailVar_Global = "carlos.liguori@assuredtechmatics.com"
    var_MasterReseller_PasswordVar_Global = "@MReseller1"
    var_MasterReseller_ConfirmationPasswordVar_Global = "@MReseller1"
    var_MasterReseller_TypeOfUserVar_Global = "Full Access Client"

    # FULL ACCESS RESELLER
    global var_FullAccessReseller_UsernameVar_Global
    global var_FullAccessReseller_EmailVar_Global
    global var_FullAccessReseller_PasswordVar_Global
    global var_FullAccessReseller_ConfirmationPasswordVar_Global
    var_FullAccessReseller_UsernameVar_Global = "QA_FullAccessReseller"
    var_FullAccessReseller_EmailVar_Global = "carlos.liguori@at.com"
    var_FullAccessReseller_PasswordVar_Global = "@FAReseller1"
    var_FullAccessReseller_ConfirmationPasswordVar_Global = "@FAReseller1"

    # LIMITED RESELLER
    global var_LimitedReseller_UsernameVar_Global
    global var_LimitedReseller_EmailVar_Global
    global var_LimitedReseller_PasswordVar_Global
    global var_LimitedReseller_ConfirmationPasswordVar_Global
    var_LimitedReseller_UsernameVar_Global = "QA_LimitedReseller"
    var_LimitedReseller_EmailVar_Global = "carlos.liguori@at.com"
    var_LimitedReseller_PasswordVar_Global = "@LReseller1"
    var_LimitedReseller_ConfirmationPasswordVar_Global = "@LReseller1"

    # FULL ACCESS CLIENT
    global var_FullAccessClient_UsernameVar_Global
    global var_FullAccessClient_EmailVar_Global
    global var_FullAccessClient_PasswordVar_Global
    global var_FullAccessClient_ConfirmationPasswordVar_Global
    global var_FullAccessClient_TypeOfUserVar_Global
    var_FullAccessClient_UsernameVar_Global = "QA_AUTOTEST_FullAccessClient"
    var_FullAccessClient_EmailVar_Global = "carlos.liguori@assuredtechmatics.com"
    var_FullAccessClient_PasswordVar_Global = "@FAClient1"
    var_FullAccessClient_ConfirmationPasswordVar_Global = "@FAClient1"
    var_FullAccessClient_TypeOfUserVar_Global = "Full Access Client"

    # LIMITED CLIENT
    global var_LimitedClient_TypeOfUserVar_Global
    global var_LimitedClient_RoleVar_Global
    global var_LimitedClient_UsernameVar_Global
    global var_LimitedClient_EmailVar_Global
    global var_LimitedClient_PasswordVar_Global
    global var_LimitedClient_ConfirmationPasswordVar_Global
    global text_CarrierFull_Var_Global

    var_LimitedClient_TypeOfUserVar_Global = "Limited Client"
    var_LimitedClient_RoleVar_Global = "QA Role"
    var_LimitedClient_UsernameVar_Global = "QA_AUTOTEST_LimitedClient"
    var_LimitedClient_EmailVar_Global = "carlos.liguori@assuredtechmatics.com"
    var_LimitedClient_PasswordVar_Global = "@LClient1"
    var_LimitedClient_ConfirmationPasswordVar_Global = "@LClient1"

    text_CarrierFull_Var_Global = "QA Carrier"
    var_Username_ExistVar = "MasterReseller"

    #################################################################################################################
    # ERROS MESSAGES Text
    #################################################################################################################
    global errorMessage_UserNamelength_Portal_Global
    errorMessage_UserNamelength_Portal_Global = "Username must be between 4 and 50 characters.Username has to be alphanumeric (-, _ or .) or email format."
    global errorMessage_InvalidEmail_Portal_Global
    errorMessage_InvalidEmail_Portal_Global = "Invalid email format"
    global errorMessage_InvalidPassword_Portal_Global
    errorMessage_InvalidPassword_Portal_Global = "This field is required."
    global errorMessage_InvalidConfirmationPassword_Portal_Global
    errorMessage_InvalidConfirmationPassword_Portal_Global = "Password and Confirmation do not match."
    global errorMessage_UsernameExist_Portal_Global
    errorMessage_UsernameExist_Portal_Global = "Username already exist."


    #################################################################################################################


    return()

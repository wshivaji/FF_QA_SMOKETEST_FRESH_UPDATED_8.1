import sys
import colorsys
import subprocess
from pathlib import Path
import datetime
import pytest


if __name__ == "__main__":
    # ------------------------------------------ regression and p1 - p5 Report Path ---------------------------------
    # ************* Report Path *********************
    Regression_suit = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Regression_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p1_re-test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p2_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p2_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p3_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p3_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p4_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p4_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p5_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p5_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------ Individual Module Report path  ---------------------------------
    # ************* Module Wise Report Path **********
    report_path_pl = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\portal_login_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_pm = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\portal_menu_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_stl = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\system_level_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_ur = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\user_roles_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_users = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\users_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_ng = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Notification_Groups_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_eg = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Enrollment_Groups_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_events = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Events_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_enrollments = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Enrollments_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_detect_faces = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Detect_Faces_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_tags = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Tags_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_ie = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\I&E_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_vs = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\_7_Visitor_Search_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_vsj = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\_8_Visitor_Search_Jobs_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_notes = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\_14_Notes_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_alr = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\ALR_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_notifier = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\_17_Notifier_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_accounts = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Accounts_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_reporting = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Reporting_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_notes_search_filter = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Notes_search_filter_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"

    system2_test_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\System2_Test_Report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    system1_test_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\System1_Test_Report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    sspr_test_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\SSPR_Test_Report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    dm_core_test_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\DM_Core_Test_Report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    dm_edge_test_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\DM_Edge_Test_Report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"

    # -----------------------------------------------------------------------------------------------------------
    # --------------------------------- regression and p1 - p5 Test suite path  ---------------------------------
    # ************* test suite path ******************
    # Regression_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\"
    system2_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\Portal Smoke Cases\\test_portal_smoke_test_cases.py"
    system1_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\Portal Smoke Cases\\test_portal_smoke_test_cases.py"
    sspr_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\Portal Smoke Cases\\test_portal_smoke_test_cases.py"
    dm_core_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_00_Deployment_Manager\\test_deployment_manager_page_test_cases.py"
    dm_edge_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_00_Deployment_Manager\\test_deployment_manager_edge_page_test_cases.py"

    # -----------------------------------------------------------------------------------------------------------
    # --------------------------------- Individual Module Test suite path  ---------------------------------
    test_suite_path_pl = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_1_Portal_Login_Module\\"
    test_suite_path_pm = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_2_Portal_Menu_Module\\"
    test_suite_path_stl = f"{Path(__file__).parent}\\All_Test_Cases_Package\\System_Level_Test\\"
    test_suite_path_IE = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_12_Idntify_and_Enroll_Module"
    test_suite_path_ur = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_3_User_Roles_Module\\"
    test_suite_path_users = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_4_Users_Module\\"
    test_suite_path_ng = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_6_Notification_Groups_Module\\"
    test_suite_path_eg = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_5_Enrollment_Groups_Module\\"
    test_suite_path_events = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_10_Events_Module"
    test_suite_path_enrollments = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_9_Enrollment_Module"
    test_suite_path_vs = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_7_Visitor_Search_Module\\"
    test_suite_path_vsj = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_8_Visitor_Search_Jobs_Module"
    test_suite_path_acc = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_19_Account_Module\\"
    test_suite_path_detect_faces = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_11_Detect_Faces_Module"
    test_suite_path_tags = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_13_tags_Module"
    test_suite_path_notes = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_14_Notes_Module"
    test_suite_path_notes_search_filter = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_14_Notes_search_filter"
    test_suite_path_alr = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_16_Audit_Log_Report_Module"
    test_suite_path_notifier = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_17_Notifier_Module"
    test_suite_path_reporting = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_18_Reporting_Module"

    # -----------------------------------------------------------------------------------------------------------
    # --------------------------------- Regression and p1 - p5  Test suite run commands  ------------------------

    # ************************ Commands to Run Test Suite *****************************
    # **************************  Priority Test Run *********************************
    # pytest.main(['-v', '-m', 'core', f'{dm_core_test_suite_path}', '--html', f'{dm_core_test_report_path}'])
    # pytest.main(['-v', '-m', 'edge', f'{dm_edge_test_suite_path}', '--html', f'{dm_edge_test_report_path}'])
    # pytest.main(['-v', '-m', 'system1', f'{system1_test_suite_path}', '--html', f'{system1_test_report_path}'])
    pytest.main(['-v', '-m', 'system', f'{system2_test_suite_path}', '--html', f'{system2_test_report_path}'])
    # pytest.main(['-v', '-m', 'sspr', f'{sspr_test_suite_path}', '--html', f'{sspr_test_report_path}'])

    # ************************** P2 Priority Test Run *********************************
    # pytest.main(['-v', '-m', 'p2', f'{Regression_test_suite_path}', '--html', f'{p2_report_path}'])

    # ************************** P3 Priority Test Run *********************************
    # pytest.main(['-v', '-m', 'p3', f'{Regression_test_suite_path}', '--html', f'{p3_report_path}'])

    # ************************** P4 Priority Test Run *********************************
    # pytest.main(['-s', '-q', '-m', 'p4', f'{test_suite_path}', '--html', f'{p4_report_path}'])

    # ************************** P5 Priority Test Run *********************************
    # pytest.main(['-s', '-q', '-m', 'p5', f'{test_suite_path}', '--html', f'{p5_report_path}'])

    # ************************** Regression Suite Test Run *********************************
    # pytest.main(['-s', '-q', f'{test_suite_path}', '--html', f'{Regression_suit}'])

    # -----------------------------------------------------------------------------------------------------------
    # --------------------------------- Module wise  Test suite run commands  ------------------------
    # ************************** Module Wise Test Run *********************************
    # pytest.main(['-v', f'{test_suite_path_pl}', '--html', f'{report_path_pl}'])
    # pytest.main(['-v', f'{test_suite_path_pm}', '--html', f'{report_path_pm}'])
    # pytest.main(['-v', f'{test_suite_path_stl}', '--html', f'{report_path_stl}'])
    # pytest.main(['-v', f'{test_suite_path_tags}', '--html', f'{report_path_tags}'])
    # pytest.main(['-v', f'{test_suite_path_notes}', '--html', f'{report_path_notes}'])
    # pytest.main(['-v', f'{test_suite_path_ur}', '--html', f'{report_path_ur}'])
    # pytest.main(['-v', f'{test_suite_path_users}', '--html', f'{report_path_users}'])
    # pytest.main(['-v', f'{test_suite_path_ng}', '--html', f'{report_path_ng}'])
    # pytest.main(['-v', f'{test_suite_path_eg}', '--html', f'{report_path_eg}'])
    # pytest.main(['-v', f'{test_suite_path_IE}', '--html', f'{report_path_ie}'])
    # pytest.main(['-v', f'{test_suite_path_enrollments}', '--html', f'{report_path_enrollments}'])
    # pytest.main(['-v', f'{test_suite_path_events}', '--html', f'{report_path_events}'])
    #
    # pytest.main(['-v', f'{test_suite_path_vs}', '--html', f'{report_path_vs}'])
    # pytest.main(['-v', f'{test_suite_path_vsj}', '--html', f'{report_path_vsj}'])
    # pytest.main(['-v', f'{test_suite_path_detect_faces}', '--html', f'{report_path_detect_faces}'])
    # pytest.main(['-v', f'{test_suite_path_reporting}', '--html', f'{report_path_reporting}'])
    #
    # pytest.main(['-v', f'{test_suite_path_notes_search_filter}', '--html', f'{report_path_notes_search_filter}'])
    # pytest.main(['-v', f'{test_suite_path_notifier}', '--html', f'{report_path_notifier}'])
    # pytest.main(['-v', f'{test_suite_path_alr}', '--html', f'{report_path_alr}'])
    # pytest.main(['-v', f'{test_suite_path_acc}', '--html', f'{report_path_accounts}'])
    #

    # ------------------------------------------------------------------------------------------------------------

    # ************* First Run Command p1 written above then re-verify failed tests by running commands below *****
    # *************************** Commands to run only failed test cases second time *****************************
    # ******************* commands below should only run after first execution is completed **********************

    # ***********Re-run Failed p1 tests across all modules *******************
    # pytest.main(['-v', '--lf', '-m', 'p1', f'{dm_test_suite_path}', '--html', f'{dm_test_report_path}'])

    # ***********Re-run Failed p2 tests across all modules *******************
    # pytest.main(['-v', '--lf', '-m', 'p2', f'{Regression_test_suite_path}', '--html', f'{p2_report_path}'])

    # ***********Re-run Failed p3 tests across all modules *******************
    # pytest.main(['-v', '--lf', '-m', 'p3', f'{Regression_test_suite_path}', '--html', f'{p3_report_path}'])

    # ***********Re-run Failed p4 tests across all modules *******************
    # pytest.main(['-s', '-q', '--lf', '-m', 'p4', f'{test_suite_path}', '--html', f'{p1_report_path}'])

    # ***********Re-run Failed p5 tests across all modules *******************
    # pytest.main(['-s', '-q', '--lf', '-m', 'p5', f'{test_suite_path}', '--html', f'{p1_report_path}'])

# ******************************************************************************************************************

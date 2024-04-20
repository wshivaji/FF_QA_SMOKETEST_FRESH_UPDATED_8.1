import pytest
from All_POM_Packages.Portal_Login_Module_POM.Portal_Login_Page_POM import Portal_Login_Page_Pom
from All_POM_Packages.Portal_Menu_Module_POM.Portal_Menu_Module_POM import Portal_Menu_Module_pom
from All_POM_Packages.Users_Module_POM.Users_Module_POM import Users_Module_pom
from All_POM_Packages.Enrollment_Groups_Module_POM.Enrollment_Groups_Module_POM import Enrollments_Groups_Module_pom
from All_POM_Packages.Notification_Groups_Module.notification_groups_module_POM import Notification_Groups_Module_pom
from All_POM_Packages.Visitor_Search_Module_POM.Visitor_Search_Module_POM import Visitor_Search_Module_pom
from All_POM_Packages.Visitor_Seach_Jobs_Module_POM.Visitor_Search_Jobs_Module_POM import Visitor_Search_Jobs_Module_pom
from All_POM_Packages.tags_module_POM.Tags_Module_POM import Tags_Module_pom
from All_POM_Packages.Enrollment_POM.Enrollment_module_POM import enrollments_POM
from All_POM_Packages.Insight_Dashboard_Module_POM.Insight_Dashboard_POM import insight_dashboard_pom
from All_POM_Packages.Identify_and_Enroll_Module_POM.Identify_and_Enroll_Module_POM import Identify_And_Enroll_POM
from All_POM_Packages.Audit_Log_Report_Module_POM.Audit_Log_Report_Module_POM import Audit_log_report_pom
from All_POM_Packages.Reporting_Module.Reporting_POM import Reporting_pom
from All_POM_Packages.Reporting_Module.Reporting_Events_POM import Reporting_Events_pom
from All_POM_Packages.SSPR_Module_POM.Sspr_POM import SSPR_pom

from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=1)
class Test_Portal_Smoke_Test_Cases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Portal_Smoke_Test_Cases Begin ********")

    # ------------------------------------------------- Portal Login Cases ---------------------------------------- #
    '''''
        These test cases will verify FF logo & Page title, logging with valid core credentials, validating WebAPI & 
        Server version numbers and verifying error message when logging with invalid credentials.
    '''
    @pytest.mark.system
    def test_SM_TC001(self):
        if (Portal_Login_Page_Pom().
                open_portal_url_and_verify_expected_url_is_visible_verify_expected_page_title_is_visible_and_verify_face_first_logo_is_visible()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC002(self):
        if (Portal_Login_Page_Pom().
                verify_user_login_with_valid_credentials_and_click_on_cloud_login_and_verify_it_is_navigating_to_cloud_menu_panel()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC003(self):
        if Portal_Login_Page_Pom().verify_face_first_copy_rights_is_visible_and_clickable_click_on_copyrights_and_verify_versions_of_webapi_and_server_both_are_visible_verify_latest_version_of_webapi_and_server_is_appeared():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC004(self):
        if Portal_Login_Page_Pom().Verify_user_login_to_webportal_should_fail_with_invalid_credentials():
            assert True
        else:
            assert False

    # ----------------------------------------------- Account Cases ------------------------------------------------- #
    '''''
        After login to portal url, this test case will verify all counts on Accounts panel as 0 before creating Users, 
        Enrollments, EG and NG and perform VS.
     '''

    # ------------------------------------------------ Zones Cases -------------------------------------------------- #
    '''''
        This test case will verify zone names and their cameras 
    '''
    # ----------------------------------------------- User Role Cases ----------------------------------------------- #
    '''''
        These cases will validate default and 5 newly added user roles (persona) and its total count.
    '''

    # ------------------------------------------------  Users Cases  ------------------------------------------------ #
    '''''
        These cases will create 5 new users using above user roles, validate their region assignment & total count of 
        users.
        '''
    @pytest.mark.system
    def test_SM_TC009(self):
        self.logger.info("Users module = test_TC_US_09 execution started..")
        if (Users_Module_pom().
                Create_5_users_standard_operator_responder_approver_executive_and_it_admin_with_all_required_field()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC010(self):
        self.logger.info("Users module = test_TC_US_10 execution started..")
        if Users_Module_pom().Verify_for_above_5_users_region_edges_are_properly_assigned():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC011(self):
        self.logger.info("user module = test_Tc_US_11_execution started....")
        if Users_Module_pom().Verify_total_users_are_n_including_default_user():
            assert True
        else:
            assert False

    # ----------------------------------------------  Portal Menu Cases  -------------------------------------------- #
    '''''
        Below cases will perform, logging with different users and verify & validate different cloud menus appears or 
        not. 
    '''
    @pytest.mark.system
    def test_SM_TC012(self):
        if Portal_Menu_Module_pom().Verify_all_submenus_are_visible_and_clickable_on_Cloud_Menu():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC013(self):
        if (Portal_Menu_Module_pom().
                Verify_for_Operator_user_PME_Tags_IE_DF_Enrollments_EG_VS_VSJ_Notes_Loc_Zones_Reporting_IDB_Notifier_these_menus_are_visible_on_the_cloud_menu_items()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC014(self):
        if (Portal_Menu_Module_pom().
                Verify_for_Responder_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC015(self):
        if (Portal_Menu_Module_pom().
                Verify_for_Approver_or_supervisor_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC016(self):
        if (Portal_Menu_Module_pom().
                Verify_for_Executive_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Account_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC017(self):
        if (Portal_Menu_Module_pom().
                Verify_for_IT_Admin_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Account_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items()):
            assert True
        else:
            assert False

    # ------------------------------------------  Notification Groups Cases  ----------------------------------------- #
    '''''
        Below cases will perform, creating new alert groups and linking them to Users.
    '''

    @pytest.mark.system
    def test_SM_TC018(self):
        if Notification_Groups_Module_pom().Create_5_Notification_groups_fill_the_details_and_link_the_particular_user_to_particular_NG_based_on_naming_convention():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC019(self):
        if Notification_Groups_Module_pom().Verify_total_count_of_NGs_is_6_including_default_NG():
            assert True
        else:
            assert False

    # ------------------------------------------  Enrollment Groups Cases  ----------------------------------------- #
    '''''
        Below cases will perform, creating new case groups and linking them to alert groups.
    '''

    @pytest.mark.system
    def test_SM_TC020(self):
        if (Enrollments_Groups_Module_pom().
                Create_5_Enrollment_groups_fill_the_details_and_link_the_particular_NG_to_particular_EG_based_on_naming_convention()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC021(self):
        if Enrollments_Groups_Module_pom().Verify_total_count_of_EGs_is_6_including_default_EG():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC022(self):
        if Enrollments_Groups_Module_pom().Verify_for_above_all_5_EG_face_and_mask_threshold_value_should_be_point_83_and_suppress_duplicate_events_value_should_be_0_minute():
            assert True
        else:
            assert False

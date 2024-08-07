import pytest

from All_POM_Packages.Detect_Faces_Module_POM.Detect_Faces_pom import detect_faces_pom
from All_POM_Packages.Portal_Login_Module_POM.Portal_Login_Page_POM import Portal_Login_Page_Pom
from All_POM_Packages.Portal_Menu_Module_POM.Portal_Menu_Module_POM import Portal_Menu_Module_pom
from All_POM_Packages.Users_Module_POM.Users_Module_POM import Users_Module_pom
from All_POM_Packages.Enrollment_Groups_Module_POM.Enrollment_Groups_Module_POM import Enrollments_Groups_Module_pom
from All_POM_Packages.Notification_Groups_Module.notification_groups_module_POM import Notification_Groups_Module_pom
from All_POM_Packages.Visitor_Search_Module_POM.Visitor_Search_Module_POM import Visitor_Search_Module_pom
from All_POM_Packages.Visitor_Seach_Jobs_Module_POM.Visitor_Search_Jobs_Module_POM import Visitor_Search_Jobs_Module_pom
from All_POM_Packages.Account_module_POM.Account_pom import account_pom
from All_POM_Packages.Notifier_Module_POM.Notifier_POM import Notifier_pom
from All_POM_Packages.Zones_Module_POM.Zones_Module_POM import Zones_pom
from All_POM_Packages.User_Roles_Module_POM.User_Roles_Module_POM import user_roles_module_pom
from All_POM_Packages._10_Events_Module_POM.Events_Pom import events_pom
from All_POM_Packages._6_Notes_Module_POM.Notes_pom import notes_pom
from All_POM_Packages.Store_Groups_Module_POM.Store_Groups_Module_POM import Store_Groups_Module_pom
from All_POM_Packages.tags_module_POM.Tags_Module_POM import Tags_Module_pom
from All_POM_Packages.Enrollment_POM.Enrollment_module_POM import enrollments_POM
from All_POM_Packages.Insight_Dashboard_Module_POM.Insight_Dashboard_POM import insight_dashboard_pom
from All_POM_Packages.Identify_and_Enroll_Module_POM.Identify_and_Enroll_Module_POM import Identify_And_Enroll_POM
from All_POM_Packages.Audit_Log_Report_Module_POM.Audit_Log_Report_Module_POM import Audit_log_report_pom
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
    @pytest.mark.system1
    def test_SM_TC001(self):
        if Portal_Login_Page_Pom().open_portal_url_and_verify_expected_url_is_visible_verify_expected_page_title_is_visible_and_verify_face_first_logo_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC002(self):
        if Portal_Login_Page_Pom().verify_user_login_with_valid_credentials_and_click_on_cloud_login_and_verify_it_is_navigating_to_cloud_menu_panel():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC003(self):
        if Portal_Login_Page_Pom().verify_face_first_copy_rights_is_visible_and_clickable_click_on_copyrights_and_verify_versions_of_webapi_and_server_both_are_visible_verify_latest_version_of_webapi_and_server_is_appeared():
            assert True
        else:
            assert False

    @pytest.mark.system1
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
    @pytest.mark.system1
    def test_SM_TC005(self):
        if account_pom().Verify_account_panel_details_before_execution():
            assert True
        else:
            assert False
    # ----------------------------------------------- User Role Cases ----------------------------------------------- #
    '''''
        These cases will validate default and 5 newly added user roles (persona) and its total count.
    '''
    @pytest.mark.system1
    def test_SM_TC006(self):
        if user_roles_module_pom().Verify_new_user_roles_operator_responder_approver_executive_and_it_admin_are_visible():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC007(self):
        if user_roles_module_pom().Verify_total_user_roles_are_6_including_default_user_role():
            assert True
        else:
            assert False

    # ------------------------------------------------  Users Cases  ------------------------------------------------ #
    '''''
        These cases will create 5 new users using above user roles, validate their region assignment & total count of
        users.
        '''

    @pytest.mark.system1
    def test_SM_TC008(self):
        self.logger.info("Users module = test_TC_US_09 execution started..")
        if Users_Module_pom().create_it_admin_user():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC009(self):
        self.logger.info("Users module = test_TC_SG_01 execution started..")
        if Store_Groups_Module_pom().create_three_store_groups_for_different_stores():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC010(self):
        self.logger.info("Users module = test_TC_US_09 execution started..")
        if Users_Module_pom().Create_5_users_standard_operator_responder_approver_executive_with_all_required_field():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC011(self):
        self.logger.info("Users module = test_TC_US_10 execution started..")
        if Users_Module_pom().Verify_for_above_5_users_region_edges_are_properly_assigned():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC012(self):
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
    @pytest.mark.system1
    def test_SM_TC013(self):
        if Portal_Menu_Module_pom().Verify_all_submenus_are_visible_and_clickable_on_Cloud_Menu():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC014(self):
        if Portal_Menu_Module_pom().Verify_for_Operator_user_PME_Tags_IE_DF_Enrollments_EG_VS_VSJ_Notes_Loc_Zones_Reporting_IDB_Notifier_these_menus_are_visible_on_the_cloud_menu_items():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC015(self):
        if Portal_Menu_Module_pom().Verify_for_Responder_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC016(self):
        if Portal_Menu_Module_pom().Verify_for_Approver_or_supervisor_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC017(self):
        if Portal_Menu_Module_pom().Verify_for_Executive_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Account_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC018(self):
        if Portal_Menu_Module_pom().Verify_for_IT_Admin_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_SG_Zones_Account_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items():
            assert True
        else:
            assert False

    # ------------------------------------------  Notification Groups Cases  ----------------------------------------- #
    '''''
        Below cases will perform, creating new alert groups and linking them to Users.
    '''
    @pytest.mark.system1
    def test_SM_TC019(self):
        if Notification_Groups_Module_pom().Create_5_Notification_groups_fill_the_details_and_link_the_particular_user_to_particular_NG_based_on_naming_convention():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC020(self):
        if Notification_Groups_Module_pom().Verify_total_count_of_NGs_is_6_including_default_NG():
            assert True
        else:
            assert False

    # ------------------------------------------  Enrollment Groups Cases  ----------------------------------------- #
    '''''
        Below cases will perform, creating new case groups and linking them to alert groups.
    '''
    @pytest.mark.system1
    def test_SM_TC021(self):
        if Enrollments_Groups_Module_pom().Create_5_Enrollment_groups_fill_the_details_and_link_the_particular_NG_to_particular_EG_based_on_naming_convention():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC022(self):
        if Enrollments_Groups_Module_pom().Verify_total_count_of_EGs_is_6_including_default_EG():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC023(self):
        if Enrollments_Groups_Module_pom().Verify_for_above_all_5_EG_face_and_mask_threshold_value_should_be_point_83_and_suppress_duplicate_events_value_should_be_0_minute():
            assert True
        else:
            assert False

    # ---------------------------------------------------  Tags Cases  ---------------------------------------------- #
    '''''
        Below cases will perform, creating 3 serious and 1 non-serious tags.
    '''
    @pytest.mark.system1
    def test_SM_TC024(self):
        if Tags_Module_pom().Create_3_serious_tags_assault_threat_and_push_cart():
            assert True
        else:
            self.logger.info("test_TC_TAG_01 fail")
            assert False

    @pytest.mark.system1
    def test_SM_TC025(self):
        if Tags_Module_pom().Create_2_non_serious_tags_fraud_and_vip():
            assert True
        else:
            self.logger.info("test_TC_TAG_02 fail")
            assert False

    @pytest.mark.system1
    def test_SM_TC026(self):
        if Tags_Module_pom().Verify_total_tags_are_n_including_default_Deterred_tag():
            assert True
        else:
            assert False

    # --------------------------------------------  Identify & Enroll Cases  ----------------------------------------- #
    '''''
        Below cases will perform, enrolling 25 subjects (5 for each EG) by "operator" user and approve them by 
        "approver" user.    '''

    @pytest.mark.system1
    def test_SM_TC027(self):
        if Identify_And_Enroll_POM().Identify_and_enroll_25_subjects_and_fill_the_required_fields_5_per_Enrollment_groups():
            assert True
        else:
            assert False

    @pytest.mark.system1
    def test_SM_TC028(self):
        if Identify_And_Enroll_POM().verify_user_able_approve_enrollment():
            assert True
        else:
            assert False

    # --------------------------------------------  Visitor Search Cases  ----------------------------------------- #
    @pytest.mark.system1
    def test_SM_TC029(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_metadata_Date_and_Org_Hierarchy_Selection_should_yield_visitor_results_within_selected_search_criteria():
            assert True
        else:
            self.logger.info("test_TC_VS_01 execution failed..")
            assert False

    @pytest.mark.system1
    def test_SM_TC030(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_image_only_should_list_the_matching_visitors_with_image():
            assert True
        else:
            self.logger.info("test_TC_VS_02 execution failed..")
            assert False

    @pytest.mark.system1
    def test_SM_TC031(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_Image_and_metadata_should_list_the_matched_visitors_with_search_image_from_selected_Org_Hierarchy_Selection_within_date_range():
            assert True
        else:
            self.logger.info("test_TC_VS_03 execution failed..")
            assert False

    # -------------------------------------------  Visitor Search Jobs Cases  --------------------------------------- #
    @pytest.mark.system1
    def test_SM_TC032(self):
        self.logger.info("Visitor search jobs module = test_VSJ_01 execution started..")
        if Visitor_Search_Jobs_Module_pom().verify_the_visitor_search_job_contains_user_performs_visitor_search_with_date_and_org_selection():
            assert True
        else:
            self.logger.info("test_VSJ_01 execution failed..")
            assert False

    @pytest.mark.system1
    def test_SM_TC033(self):
        self.logger.info("Visitor search jobs module = test_VSJ_04 execution started..")
        if Visitor_Search_Jobs_Module_pom().Verify_the_visitor_search_job_contains_the_selected_threshold_visitors_in_date_range_and_belongs_to_search_Org_Hierarchy_Selection_when_user_performs_a_visitor_search_with_Date_Org():
            assert True
        else:
            self.logger.info("test_VSJ_04 execution failed..")
            assert False

    @pytest.mark.system1
    def test_SM_TC034(self):
        self.logger.info("Visitor search jobs module = test_VSJ_06 execution started..")
        if Visitor_Search_Jobs_Module_pom().Verify_VSJ_filtering_with_date_range_selection_should_list_VSJ_in_the_selected_date_range_only():
            assert True
        else:
            self.logger.info("test_VSJ_06 execution failed..")
            assert False

    # ------------------------------------------  Probable Match Events Cases  --------------------------------------- #
    @pytest.mark.system
    def test_SM_TC035(self):
        if events_pom().Verify_25_events_are_generated_for_25_enrolled_subjects():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC036(self):
        if events_pom().Verify_5_events_for_each_group_soe_abe_pte_fraude_and_vipe_using_enrollment_group_selection_in_search_dropdown():
            assert True
        else:
            self.logger.info("test_events_TC_002 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC037(self):
        if events_pom().Verify_25_events_using_Org_hierarchy_selection_in_search_dropdown():
            assert True
        else:
            self.logger.info("test_events_TC_003 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC038(self):
        if events_pom().Verify_5_events_for_each_group_soe_abe_pte_fraude_and_vipe_using_enrollment_group_and_org_hierarchy_selection_in_search_dropdown():
            assert True
        else:
            self.logger.info("test_SM_TC036 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC039(self):
        if events_pom().Add_the_tags_with_respective_enrollment_groups_and_org_hierarchy_selection_example_soe_deterred_and_assualt_abe_deterred_and_threat_pte_deterred_and_push_cart_fraude_and_vipe_deterred_and_fraud():
            assert True
        else:
            self.logger.info("test_events_TC_005 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC040(self):
        if events_pom().Verify_5_events_are_visible_by_enrollment_group_org_hierarchy_and_Tag_selection():
            assert True
        else:
            self.logger.info("test_events_TC_006 fail")
            assert False

    # ------------------------------------------  Insights Dashboard Cases  ----------------------------------------- #
    @pytest.mark.system
    def test_SM_TC041(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_counts_on_overview_dashboard_as_total_loss_prevented_5500_active_enrollment_25_total_match_events_25_visito_searches_0_investgation_saving_time_0_repeat_people_of_interest_0():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC042(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_loss_prevented_by_enrollment_group_counts():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC043(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_Possible_Match_Events_by_enrollment_action_counts():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC044(self):
        if (insight_dashboard_pom().
                Verify_user_is_able_to_see_counts_on_overview_dashboard_organisation_and_individual_groups()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC045(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_loss_prevented_by_enrollment_group_counts_organisation_and_individual_groups():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC046(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_Possible_Match_Events_by_enrollment_action_counts_organisation_and_individual_groups():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC047(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC048(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_cumulative_Probable_Match_Events_by_date_todays_date_and_25_count():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC049(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_tagged_vs_untagged_Probable_Match_Events_count_as_tagged_and_untagged():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC050(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_Probable_Match_Events_by_enrollment_groups_counts():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC051(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_tagged_Probable_Match_Events_by_tag_type():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC052(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_counts_on_Probable_Match_Events_dashboard_organisation_and_individual_groups():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC053(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_cumulative_Probable_Match_Events_by_date_organisation_and_individual_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC054(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_tagged_vs_untagged_Probable_Match_Events_count_organisation_and_individual_groups():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC055(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_Probable_Match_Events_by_enrollment_groups_counts_organisation_and_individual_groups():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC056(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_tagged_Probable_Match_Events_by_tag_type_organisation_and_individual_groups():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC057(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_on_enrollment_dashboard_as_enrollment_overview_and_cumulative_enrollments_by_date_as_mention_is_link():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC058(self):
        if insight_dashboard_pom().Verify_enrollment_by_date_counts_on_enrollment_dashboard():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC059(self):
        if insight_dashboard_pom().Verify_enrollments_by_enrollment_group_counts_as_mention_in_link():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC060(self):
        if insight_dashboard_pom().Verify_enrollments_by_week_org_counts_as_mention_in_link():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC061(self):
        if insight_dashboard_pom().Verify_Enrollments_by_status_count():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC062(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_on_enrollment_dashboard_as_enrollment_overview_and_cumulative_enrollments_by_date():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC063(self):
        if insight_dashboard_pom().Verify_enrollment_by_date_counts_as_mention_in_link_organisation_and_individual_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC064(self):
        if insight_dashboard_pom().Verify_enrollments_by_enrollment_group_counts_as_mention_in_link_organisation_and_individual_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC065(self):
        if insight_dashboard_pom().Verify_enrollments_by_week_counts_as_mention_in_link_organisation_and_individual_groups():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC066(self):
        if insight_dashboard_pom().Verify_Enrollments_by_Status_counts_organisation_and_individual_groups():
            assert True
        else:
            assert False

    # ------------------------------------------ Reporting cases ------------------------------------ #
    @pytest.mark.system
    def test_SM_TC067(self):
        if (Reporting_Events_pom().
                Verify_report_for_number_of_probable_match_events_by_zone_with_default_dates_and_optional_filters()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC068(self):
        if (Reporting_Events_pom().
                Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_and_optional_filters()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC069(self):
        if (Reporting_Events_pom().
                Verify_report_for_number_of_enrollment_by_zones_with_default_dates_and_optional_filters()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC070(self):
        if Reporting_Events_pom().Verify_report_for_number_of_zones_by_enrollment_with_default_dates_and_optional_filters():
            assert True
        else:
            assert False

    # ------------------------------------------  Enrollments Cases  ----------------------------------------- #
    @pytest.mark.system
    def test_SM_TC071(self):
        if enrollments_POM().Verify_user_is_able_to_see_total_enrollment_count_as_25():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC072(self):
        if enrollments_POM().Verify_user_is_able_to_perform_enable_mask_enrollment_which_is_in_disable_state():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC073(self):
        if enrollments_POM().Verify_user_is_able_to_add_single_face_for_enabled_mask_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC074(self):
        if enrollments_POM().Verify_user_is_able_to_add_single_note_for_enabled_mask_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC075(self):
        if enrollments_POM().Verify_user_is_able_to_see_5_subjects_for_pending_review_condition_using_VIP_user_enroll_5_subjects_for_pending_review():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC076(self):
        if enrollments_POM().Verify_approver_user_is_able_to_reject_pending_subjects():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC077(self):
        if enrollments_POM().Verify_approver_user_is_able_to_approve_pending_subjects():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC078(self):
        if enrollments_POM().Verify_core_or_itadmin_user_is_able_to_delete_pending_subjects():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC079(self):
        if enrollments_POM().Verify_user_is_able_to_enable_the_reject_subject_user_with_all_permissions():
            assert True
        else:
            assert False

    # ------------------------------------------  ALR Cases  ----------------------------------------- #

    @pytest.mark.system
    def test_SM_TC080(self):
        if Audit_log_report_pom().Verify_user_with_all_permissions_enrolled_mask_subject_should_be_in_Disable_status_for_user_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC081(self):
        if Audit_log_report_pom().Verify_core_should_be_able_to_enable_above_mask_subject_and_verify_Enabled_status_and_action_by_core_for_user_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC082(self):
        if Audit_log_report_pom().Verify_for_above_enable_mask_subject_status_is_Enabled_in_Approver_Enrollments_too():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC083(self):
        if Audit_log_report_pom().Verify_user_with_2FA_enrolled_subject_should_be_able_to_see_Pending_status_for_user_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC084(self):
        if Audit_log_report_pom().Verify_user_with_2FA_enrolled_subject_approved_by_core_admin_should_be_able_to_see_Accepted_status_and_action_by_core_for_user_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC085(self):
        if Audit_log_report_pom().Verify_user_with_2FA_enrolled_subject_approved_by_core_admin_should_be_able_to_see_Accepted_status_for_approver_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC086(self):
        if Audit_log_report_pom().Verify_Threshold_changes_report_with_user_modified_enrolment_group_details_should_be_displayed_on_the_report_with_ip_address():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC087(self):
        if Audit_log_report_pom().Verify_Login_Logout_report_with_one_of_the_user_login_and_user_logout_with_minimum_delay_of_1_min():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC088(self):
        self.logger.info("Audit Log Report = test_TC_ALR_001 execution started..")
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_Approver_enrollments_and_download_excel_file():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC089(self):
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_user_enrollments_and_download_excel_file():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC090(self):
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_log_in_log_out_and_download_excel_file():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC091(self):
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_Threshold_changes_and_download_excel_file():
            assert True
        else:
            assert False

    # ------------------------------------------ Detect Faces Cases  ----------------------------------------- #
    @pytest.mark.system
    def test_SM_TC092(self):
        if detect_faces_pom().on_Detect_faces_page_upload_a_image_having_more_no_of_faces_verify_banner_showing_number_of_faces_on_a_image():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC093(self):
        if detect_faces_pom().on_image_quality_page_verify_download_image_button_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC094(self):
        if detect_faces_pom().on_image_qualty_page_in_action_dropdown_click_on_identify_within_enrollments_Identify_and_enroll_page_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC095(self):
        if detect_faces_pom().on_image_quality_page_In_action_dropdown_click_on_identify_within_visitors_visitor_search_page_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC096(self):
        if detect_faces_pom().on_Detect_faces_page_upload_a_image_having_more_no_of_faces_verify_banner_showing_number_of_faces_on_a_image():
            assert True
        else:
            assert False

    # ------------------------------------------ User Roles (CERD) Cases  ----------------------------------------- #
    @pytest.mark.system
    def test_SM_TC097(self):
        self.logger.info("***************** test_TC_UR_03 *****************")
        if user_roles_module_pom().Verify_user_able_to_create_a_new_users_role_by_filling_all_the_fields():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC098(self):
        self.logger.info("***************** test_TC_UR_04 *****************")
        if user_roles_module_pom().verify_user_able_to_edit_user_roles_detaild_description_with_disabled_enrollment_review_permissions():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC099(self):
        self.logger.info("***************** test_TC_UR_05 *****************")
        if user_roles_module_pom().Verify_details_and_all_permission_of_default_it_admin():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC100(self):
        self.logger.info("***************** test_TC_UR_06 *****************")
        if user_roles_module_pom().Verify_User_role_deletion_functionality_by_deleting_one_user_role():
            assert True
        else:
            assert False

    # ------------------------------------------ Users Cases (CURD) cases----------------------------------------- #
    @pytest.mark.system
    def test_SM_TC101(self):
        if Users_Module_pom().verify_if_user_creates_a_new_users_marked_as_enabled_it_should_reflect_as_enabled():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC102(self):
        if Users_Module_pom().verify_if_user_creates_a_new_users_marked_as_disabled_it_should_reflect_as_disabled():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC103(self):
        if Users_Module_pom().verify_user_able_to_edit_the_details_for_the_newly_created_user_details():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC104(self):
        if Users_Module_pom().verify_user_able_to_delete_the_newly_created_user():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC105(self):
        if Users_Module_pom() \
                .verify_login_with_newly_created_user_and_validate_login_successful():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC106(self):
        if Users_Module_pom() \
                .verify_user_should_not_be_able_to_create_user_which_already_exist():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC107(self):
        if Users_Module_pom() \
                .on_alert_schedule_edit_user_alert_schedule_and_verify_the_panel_should_be_editable():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC108(self):
        if Users_Module_pom() \
                .verify_send_sms_send_mms_send_email_send_in_app_notifications_enable_disable_alerts_Yes_No_button():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC109(self):
        if Users_Module_pom() \
                .Verify_reassigning_user_to_diferrent_region():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC110(self):
        if Users_Module_pom().verify_user_able_to_link_unlink_the_newly_created_user_to_a_notification_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC111(self):
        if Users_Module_pom().Verify_org_hierarchy_selection_root_name_should_be_able_to_match_with_DM_core_name():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC112(self):
        if Users_Module_pom().verify_details_of_core_user():
            assert True
        else:
            assert False

    # ------------------------------------------ Enrollment Groups (CERD) cases -------------------------------------- #
    @pytest.mark.system
    def test_SM_TC113(self):
        if Enrollments_Groups_Module_pom().Verify_user_able_to_create_a_new_Enrollment_Group_by_filling_all_the_fields_and_verify_present_3_buttons_below_are_activated():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC114(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_edit_enrollment_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC115(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_link_a_notification_group_from_enrollments_groups_panel():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC116(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_unlink_a_notification_group_from_enrollments_groups_panel():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC117(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_see_enrollments_from_associated_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC118(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_see_possible_match_events_associated_to_enrollements_group_and_possible_match_events_associated_to_details_of_enrollment_group_for_both_event_count_should_be_match():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC119(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_link_the_enrollments_from_enrollments_groups_panel():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC120(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_unlink_the_enrollments_from_enrollments_groups_panel():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC121(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_delete_newly_created_enrollment_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC122(self):
        if Enrollments_Groups_Module_pom().Verify_details_of_default_enrollment_group():
            assert True
        else:
            assert False

    # ------------------------------------------ Notification Groups (CURD) cases ------------------------------------ #
    @pytest.mark.system
    def test_SM_TC123(self):
        if Notification_Groups_Module_pom().Verify_user_able_to_create_a_new_Notification_Group_by_filling_all_the_fields_and_verify_present_3_buttons_below_are_activated():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC124(self):
        if Notification_Groups_Module_pom().verify_user_able_to_edit_notification_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC125(self):
        if Notification_Groups_Module_pom().verify_user_able_to_link_an_enrollments_groups_to_notification_groups():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC126(self):
        if Notification_Groups_Module_pom().verify_user_able_to_unlink_an_enrollments_groups_from_notification_groups():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC127(self):
        if Notification_Groups_Module_pom().verify_user_able_to_see_events_associated_to_Notification_group_and_events_associated_to_details_of_Notification_group_for_both_event_count_should_be_match():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC128(self):
        if Notification_Groups_Module_pom().verify_user_able_to_link_a_user_to_notification_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC129(self):
        if Notification_Groups_Module_pom().verify_user_able_to_unlink_a_user_to_notification_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC130(self):
        if Notification_Groups_Module_pom().Verify_user_able_to_delete_the_newly_created_notification_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC131(self):
        if Notification_Groups_Module_pom().Verify_details_of_default_notification_group():
            assert True
        else:
            assert False

    # ------------------------------------------ Enrollments (CURD) cases ------------------------------------ #

    @pytest.mark.system
    def test_SM_TC132(self):
        if enrollments_POM().Verify_if_user_is_enrolled_the_person_with_expiry_date_validate_expired_date_is_visible_on_Enrollment_module_panel():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC133(self):
        if enrollments_POM().enrollments_search_with_filter_dropdown_option_result_should_be_dropdown_options():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC134(self):
        if enrollments_POM().verify_user_enroller_of_an_enrollment_able_to_link_a_enrollment_group_and_add_the_person_to_the_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC135(self):
        if enrollments_POM().verify_user_enroller_of_an_enrollment_able_to_unlink_same_enrollment_group_and_remove_the_person_from_selected_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC136(self):
        if enrollments_POM().verify_user_able_to_add_more_faces_to_an_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC137(self):
        if enrollments_POM().verify_user_enroller_of_an_enrollment_able_to_see_events_for_a_enrolled_person_on_enrrollments_panel():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC138(self):
        if enrollments_POM().verify_user_enroller_of_an_enrollment_able_to_edit_the_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC139(self):
        if enrollments_POM().verify_user_able_to_see_disabled_status_for_masked_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC140(self):
        if enrollments_POM().verify_user_able_to_add_notes_for_a_enrolled_person_on_enrollments_panel():
            assert True
        else:
            assert False

    # ------------------------------------------ PME (CURD) cases ------------------------------------ #

    @pytest.mark.system
    def test_SM_TC141(self):
        if events_pom().Verify_user_should_be_able_to_add_the_tags_and_see_that_same_tags_are_visible_when_user_clicks_on_display_tags_option_in_view_dropdown():
            assert True
        else:
            self.logger.info("test_events_TC_007 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC142(self):
        if events_pom().Verify_user_able_to_delete_probable_match_events():
            assert True
        else:
            self.logger.info("test_events_TC_008 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC143(self):
        if events_pom().Probable_Match_Event_search_with_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tag_filter_combination_result_should_be_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tagged_event():
            assert True
        else:
            self.logger.info("test_events_TC_009 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC144(self):
        if events_pom().on_Event_view_panel_click_on_Action_dropdown_followed_by_Identify_within_enrollments_option_in_dropdown_and_verify_Identify_enroll_and_identify_results_panel_are_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC145(self):
        if events_pom().Verify_user_is_able_to_perform_identify_within_visitors_from_Probable_Match_Enrollment_View_panel_when_event_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC146(self):
        if events_pom().Verify_user_is_able_to_edit_the_Enrollment_details_on_Enrollment_View_panel_when_ProbableMatch_Event_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC147(self):
        if events_pom().Verify_user_is_able_to_add_face_on_Enrollment_view_panel_when_event_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC148(self):
        if events_pom().Verify_user_is_able_to_see_probable_match_events_associated_to_same_person_on_Enrollment_View_panel_when_probable_match_event_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC149(self):
        if events_pom().Verify_user_able_to_link_a_enrollment_group_and_add_the_person_to_the_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC150(self):
        if events_pom().Verify_user_able_to_unlink_same_enrollment_group_and_remove_the_person_from_selected_group():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC151(self):
        if events_pom().Verify_user_is_able_to_add_note_on_Enrollment_view_panel_when_Probable_Match_Event_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_SM_TC152(self):
        if events_pom().Verify_event_should_not_generate_for_opt_out_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_SM_TC153(self):
        if events_pom().Verify_event_should_not_generate_for_pending_review_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_SM_TC154(self):
        if events_pom().Verify_event_should_not_generate_for_disable_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_SM_TC155(self):
        if events_pom().Verify_event_should_not_generate_for_rejected_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC156(self):
        if events_pom().Verify_user_is_able_to_link_the_tag_and_add_tag_to_probable_match_events_when_tag_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC157(self):
        if events_pom().Verify_user_is_able_to_unlink_the_tag_and_remove_tag_from_probable_match_events_when_tag_icon_is_click():
            assert True
        else:
            assert False

    # ------------------------------------------ Identify Enroll (CURD) cases ------------------------------------ #
    @pytest.mark.system
    def test_SM_TC158(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_and_adding_the_required_details_for_the_same():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC159(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_to_see_the_possible_ranked_match_index_when_uploading_the_above_same_image_with_or_without_crop():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC160(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_and_adding_the_required_details_for_the_same_along_with_expiry_date_and_time_range():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC161(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_cropping_the_same_and_adding_the_required_details_for_the_same():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC162(self):
        if Identify_And_Enroll_POM().verify_three_buttons_faces_person_view_and_purge_Replace_are_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC163(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_enroll_the_person_which_is_delete_one_delete_and_enrolling_again_person_should_be_same():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC164(self):
        if Identify_And_Enroll_POM().Verify_for_above_25_enrolled_subject_region_edges_are_properly_assigned():
            assert True
        else:
            assert False

    # ------------------------------------------ Notifier (CURD) cases ------------------------------------ #
    @pytest.mark.system
    def test_SM_TC165(self):
        if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC166(self):
        if Notifier_pom().Verify_events_appears_with_live_and_probable_match_image_upon_event_generation_with_sound():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC167(self):
        if Notifier_pom().Verify_org_hierarchy_selection_features_collapse_all_expand_all_select_all_and_unselect_all():
            assert True
        else:
            assert False

    # ------------------------------------------ Account cases ------------------------------------ #

    @pytest.mark.system
    def test_SM_TC168(self):
        if account_pom().click_on_image_sources_and_check_theplanel_heading_of_Account_Image_sources_is_displayed():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC169(self):
        if account_pom().click_on_location_on_View_dropdown_map_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC170(self):
        if account_pom().click_on_regions_button_verify_panel_heading():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC171(self):
        if account_pom().click_on_detailsbutton_verify_imagesource_panel_heading_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC172(self):
        if account_pom().click_on_viewlocation_button_on_imagesource_verify_location():
            assert True
        else:
            assert False

    # ------------------------------------------------ Zones Cases -------------------------------------------------- #
        '''''
            This test case will verify zone names and their cameras
        '''
    @pytest.mark.system
    def test_SM_TC173(self):
        if Zones_pom().verify_zone_list_enlisted_and_zone_names_displayed_as_expected():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC174(self):
        if Zones_pom().verify_zone_list_enlisted_and_zone_details_btn_displayed_as_expected():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC175(self):
        if Zones_pom().verify_zone_list_enlisted_and_zone_select_checkbox_displayed_as_expected():
            assert True
        else:
            assert False

    # ---------------------------------------- Portal Login User Blocking test case ---------------------------------- #
    @pytest.mark.system
    def test_SM_TC176(self):
        if Portal_Login_Page_Pom(). \
                verify_user_account_blocked_for_30_min_if_user_enter_wrong_password_for_6_times_verify_message_warning():
            assert True
        else:
            assert False

    # ---------------------------------------- Visitor Search test case ---------------------------------- #
    @pytest.mark.system
    def test_SM_TC177(self):
        if Visitor_Search_Module_pom().Verify_org_hierarchy_selection_root_name_should_be_able_to_match_with_DM_core_name():
            assert True
        else:
            self.logger.info("test_TC_VS_04 execution failed..")
            assert False

    @pytest.mark.system
    def test_SM_TC178(self):
        if Visitor_Search_Module_pom().Verify_warning_message_when_user_is_dropping_the_image_which_is_clicked_on_live_or_file_image_on_events_panel_able_to_perform_image_with_meta_data_idealy_it_should_not_with_larger_image_able_to_perform():
            assert True
        else:
            self.logger.info("test_TC_VS_05 execution failed..")
            assert False

    # ---------------------------------------- Visitor Search Jobs test case ---------------------------------- #

    @pytest.mark.system
    def test_SM_TC179(self):
        if Visitor_Search_Jobs_Module_pom().Verify_visitor_search_status_banner_is_visible_visitor_search_jobs_on_VSJ_panel():
            assert True
        else:
            self.logger.info("test_VSJ_02 execution failed..")
            assert False

    @pytest.mark.system
    def test_SM_TC180(self):
        if Visitor_Search_Jobs_Module_pom().verify_when_user_click_on_View_Results_button_of_VSJ_should_display_visitor_search_results_panel():
            assert True
        else:
            self.logger.info("test_VSJ_03 execution failed..")
            assert False

    @pytest.mark.system
    def test_SM_TC181(self):
        if Visitor_Search_Jobs_Module_pom().verify_user_able_to_delete_VS_jobs():
            assert True
        else:
            self.logger.info("test_VSJ_05 execution failed..")
            assert False

    # ------------------------------------------ Tags CURD case ------------------------------------ #
    @pytest.mark.system
    def test_SM_TC182(self):
        self.logger.info("test_TC_TAG_04 execution started..")
        if Tags_Module_pom().tags_search_functionality():
            assert True
        else:
            self.logger.info("test_TC_TAG_04 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC183(self):
        self.logger.info("test_TC_TAG_08 execution started..")
        if Tags_Module_pom().Verify_filter_dropdown():
            assert True
        else:
            self.logger.info("test_TC_TAG_08 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC184(self):
        self.logger.info("test_TC_TAG_08 execution started..")
        if Tags_Module_pom().edit_serious_event_tag_name():
            assert True
        else:
            self.logger.info("test_TC_TAG_08 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC185(self):
        self.logger.info("test_TC_TAG_08 execution started..")
        if Tags_Module_pom().verify_user_able_to_delete_a_tag():
            assert True
        else:
            self.logger.info("test_TC_TAG_08 fail")
            assert False

    @pytest.mark.system
    def test_SM_TC186(self):
        self.logger.info("test_TC_TAG_07 execution started..")
        if Tags_Module_pom().duplicate_tags_not_create_validation():
            assert True
        else:
            self.logger.info("test_TC_TAG_07 fail")
            assert False

    # ------------------------------------------ Notes cases ------------------------------------ #
    @pytest.mark.system
    def test_SM_TC187(self):
        if notes_pom().verify_user_able_create_notes_successfully():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC188(self):
        if notes_pom().verify_user_able_to_edit_details_by_selecting_details_icon():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC189(self):
        if notes_pom().verify_user_is_able_to_select_any_one_note_and_click_on_location_in_view_dropdown():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC190(self):
        if notes_pom().verify_user_is_able_to_select_any_one_note_and_click_on_location_icon():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC191(self):
        if notes_pom().verify_user_is_able_to_see_the_enrollment_associated_to_particular_note():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC192(self):
        if notes_pom().Verify_user_is_able_to_add_photo_when_image_icon_is_clicked():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_SM_TC193(self):
        if notes_pom().verify_user_able_to_delete_notes_successfully():
            assert True
        else:
            assert False

    # ------------------------------------------ Enrollment Delete case ------------------------------------ #
    @pytest.mark.system
    def test_SM_TC194(self):
        if enrollments_POM().verify_executive_it_admin_enroller_of_an_enrollment_able_to_delete_enrollment():
            assert True
        else:
            assert False

    # ------------------------------------------ Account details After case ------------------------------------ #
    @pytest.mark.system
    def test_SM_TC195(self):
        if account_pom().Verify_account_panel_details_after_execution():
            assert True
        else:
            assert False

    # ------------------------------------------ SSPR cases ------------------------------------ #
    @pytest.mark.sspr
    def test_TC_SSPR_001(self):
        if SSPR_pom().open_portal_login_page_enter_username_password_and_click_on_login_btn_verify_password_reset_pop_up_displayed():
            assert True
        else:
            assert False

    @pytest.mark.sspr
    def test_TC_SSPR_002(self):
        if SSPR_pom().verify_password_length_should_not_accept_less_than_8():
            assert True
        else:
            assert False

    @pytest.mark.sspr
    def test_TC_SSPR_003(self):
        if SSPR_pom().verify_password_combination_alphabets_capital_small_digits_and_symbol_accepted_successfully():
            assert True
        else:
            assert False

import pytest
from All_POM_Packages._00_Deployment_Manager_POM.Deployment_Manager_Page_POM import Deployment_Manager_Page_Pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


class Test_Deployment_Manager_Page_Test_Cases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Deployment Manager Page (Order - 0) Begin ********")
    print("******** Deployment Manager Page (Order - 0) Begin ********")

    @pytest.mark.core
    def test_dm_tc01(self):
        if Deployment_Manager_Page_Pom().verify_user_directs_to_user_register_page_and_create_a_user_by_providing_details():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc02(self):
        if Deployment_Manager_Page_Pom().verify_user_login_to_deployment_manager_using_create_user_credentials():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc03(self):
        if Deployment_Manager_Page_Pom().enter_license_under_license_status_in_deployment_manager_settings():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc04(self):
        if Deployment_Manager_Page_Pom().verify_configuring_the_domain_url_using_recommended_letsencrypt_or_ssl_certificate():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc05(self):
        if Deployment_Manager_Page_Pom().verify_the_deployment_options_of_core_edges_from_deployment_wizard():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc06(self):
        if Deployment_Manager_Page_Pom().verify_deployment_of_core_by_providing_required_details_for_core_deployment():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc07(self):
        if Deployment_Manager_Page_Pom().verify_web_portal_url_and_login_to_web_portal_with_core_credentials_and_verify_login_successful():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc08(self):
        if Deployment_Manager_Page_Pom().verify_enable_disable_dashboard_enabled_should_make_appear_and_disappear_the_dashboard_on_web_portal():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc09(self):
        if Deployment_Manager_Page_Pom().verify_notification_email_configuration_by_proving_host_and_sender_credentials():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc10(self):
        if Deployment_Manager_Page_Pom().verify_visitor_log_retention_set_to_maximum_clustering_time_under_platform_settings():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc11(self):
        if Deployment_Manager_Page_Pom().verify_enrollment_quality_guard_is_enable_with_proper_settings():
            assert True
        else:
            assert False

    @pytest.mark.core
    def test_dm_tc12(self):
        if Deployment_Manager_Page_Pom().verify_session_time_is_set_to_maximum_value_under_platform_settings():
            assert True
        else:
            assert False

    def test_dm_tc_13(self):
        if Deployment_Manager_Page_Pom().verify_user_able_click_on_manage_user_menu_add_user_screen_should_appears():
            assert True
        else:
            assert False

    def test_dm_tc_14(self):
        if Deployment_Manager_Page_Pom().on_add_user_screen_verify_add_user_button_is_visible_verify_text_on_the_button():
            assert True
        else:
            assert False

    def test_dm_tc_15(self):
        if Deployment_Manager_Page_Pom().create_a_user_by_filling_all_fields():
            assert True
        else:
            assert False

    def test_dm_tc_16(self):
        if Deployment_Manager_Page_Pom().verify_created_user_should_be_visible_on_add_user_screen():
            assert True
        else:
            assert False

    def test_dm_tc_17(self):
        if Deployment_Manager_Page_Pom().verify_after_filling_all_valid_inputs_create_user_button_is_enabled():
            assert True
        else:
            assert False

    def test_dm_tc_18(self):
        if Deployment_Manager_Page_Pom().verify_login_to_deployment_maanger_using_newely_created_dm_users():
            assert True
        else:
            assert False

    def test_dm_training_01(self):
        if Deployment_Manager_Page_Pom().verify_on_deployment_manger_under_platform_settings_a_new_setting_training_system_settings_is_visible():
            assert True
        else:
            assert False

    def test_dm_training_02(self):
        if Deployment_Manager_Page_Pom().verify_beside_training_system_settings_pencil_icon_is_visible_and_clickable():
            assert True
        else:
            assert False

    def test_dm_training_03(self):
        if Deployment_Manager_Page_Pom().click_on_pencil_icon_annual_training_system_access_window_should_appear():
            assert True
        else:
            assert False

    def test_dm_training_04(self):
        if Deployment_Manager_Page_Pom().verify_training_acknowledgement_required_label_and_its_toggle_button_is_visible_and_clickable():
            assert True
        else:
            assert False

    def test_dm_ispring_tc_01(self):
        if Deployment_Manager_Page_Pom().verify_user_able_to_receive_account_login_id_password_setting_link_credentials_to_registed_email_to_sign_in_on_ispring_portal():
            assert True
        else:
            assert False

    def test_dm_ispring_tc_04(self):
        if Deployment_Manager_Page_Pom().login_to_facefirst_ispring_portal_with_valid_credentials():
            assert True
        else:
            assert False

    def test_dm_ispring_tc_05(self):
        if Deployment_Manager_Page_Pom().verify_and_complete_the_courses_are_enlisted_on_facefirst_ispring_portal():
            assert True
        else:
            assert False

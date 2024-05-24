import pytest
from All_POM_Packages.Users_Module_POM.Users_Module_POM import Users_Module_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=2)
class Test_Users_Module(web_driver, web_logger):
    logger = web_logger.logger_obj()
    d = web_driver.d()
    logger.info(" ******** Users_Module (Order - 2) Begin ********")
    print("******** Users_Module (Order - 2) Begin ********")

    @pytest.mark.system
    def test_TC_US(self):
        self.logger.info("Users module = test_TC_US_01 execution started..")
        if Users_Module_pom().create_it_admin_user():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_US_1(self):
        self.logger.info("Users module = test_TC_US_110 execution started..")
        if Users_Module_pom().Create_5_users_standard_operator_responder_approver_executive_with_all_required_field():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_US_2(self):
        if Users_Module_pom().Verify_for_above_5_users_region_edges_are_properly_assigned():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_US_3(self):
        self.logger.info("user module = test_Tc_US_3_execution stsrted....")
        if Users_Module_pom().Verify_total_users_are_n_including_default_user():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_04(self):
        self.logger.info("Users module = test_TC_US_04 execution started..")
        if Users_Module_pom().verify_if_user_creates_a_new_users_marked_as_enabled_it_should_reflect_as_enabled():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_05(self):
        self.logger.info("Users module = test_TC_US_05 execution started..")
        if Users_Module_pom().verify_if_user_creates_a_new_users_marked_as_disabled_it_should_reflect_as_disabled():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_06(self):
        self.logger.info("Users module = test_TC_US_06 execution started..")
        if Users_Module_pom() \
                .verify_user_able_to_edit_the_details_for_the_newly_created_user_details():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_07(self):
        self.logger.info("Users module = test_TC_US_07 execution started..")
        if Users_Module_pom() \
                .verify_user_able_to_delete_the_newly_created_user():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_08(self):
        self.logger.info("Users module = test_TC_US_08 execution started..")
        if Users_Module_pom() \
                .verify_login_with_newly_created_user_and_validate_login_successful():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_9(self):
        self.logger.info("Users module = test_TC_US_9 execution started..")
        if Users_Module_pom() \
                .verify_user_should_not_be_able_to_create_user_which_already_exist():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_10(self):
        self.logger.info("Users module = test_TC_US_10 execution started..")
        if Users_Module_pom() \
                .on_alert_schedule_edit_user_alert_schedule_and_verify_the_panel_should_be_editable():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_11(self):
        self.logger.info("Users module = test_TC_US_11 execution started..")
        if Users_Module_pom() \
                .verify_send_sms_send_mms_send_email_send_in_app_notifications_enable_disable_alerts_Yes_No_button():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_12(self):
        self.logger.info("Users module = test_TC_US_12 execution started..")
        if Users_Module_pom() \
                .Verify_reassigning_user_to_diferrent_region():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_13(self):
        self.logger.info("Users module = test_TC_US_13 execution started..")
        if Users_Module_pom().verify_user_able_to_link_unlink_the_newly_created_user_to_a_notification_group():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_US_14(self):
        self.logger.info("Users module = test_TC_US_14 execution started..")
        if Users_Module_pom().verify_details_of_core_user():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_15(self):
        self.logger.info("Users module = test_TC_US_14 execution started..")
        if Users_Module_pom().Verify_org_hierarchy_selection_root_name_should_be_able_to_match_with_DM_core_name():
            assert True
        else:
            assert False

import pytest
from All_POM_Packages._4_Users_Module_POM.Users_Module_POM import Users_Module_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=5)
class Test_Users_Module(web_driver, web_logger):
    logger = web_logger.logger_obj()
    d = web_driver.d()
    logger.info(" ******** Users_Module (Order - 4) Begin ********")
    print("******** Users_Module (Order - 4) Begin ********")
    #
    # # delete user is skipped for now
    # @pytest.mark.skip
    # def test_TC_US_006(self):
    #     self.logger.info("Users module = test_TC_US_006 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_delete_selected_user():
    #         assert True
    #     else:
    #         assert False


    # @pytest.mark.p2
    # def test_TC_US_022(self):
    #     self.logger.info("Users module = test_TC_US_022 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_able_to_see_user_role_dropdown_is_present_and_choose_the_user_roles():
    #         assert True
    #     else:
    #         assert False



    @pytest.mark.p1
    def test_TC_US_1(self):
        self.logger.info("Users module = test_TC_US_110 execution started..")
        if Users_Module_pom().Create_5_users_standard_operator_responder_approver_executive_and_it_admin_with_all_required_field():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_06(self):
        self.logger.info("Users module = test_TC_US_06 execution started..")
        if Users_Module_pom()\
                .verify_login_with_newly_created_user_and_validate_login_successful():
            assert True
        else:
            assert False

    # @pytest.mark.p1
    # def test_TC_US_113(self):
    #     self.logger.info("Users module = test_TC_US_113 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_all_the_details_filled_for_the_newly_created_user():
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.p2
    def test_TC_US_02(self):
        self.logger.info("Users module = test_TC_US_02 execution started..")
        if Users_Module_pom()\
                .verify_if_user_creates_a_new_users_marked_as_enabled_it_should_reflect_as_enabled():
            assert True
        else:
            assert False

    @pytest.mark.p2a
    def test_TC_US_03(self):
        self.logger.info("Users module = test_TC_US_03 execution started..")
        if Users_Module_pom()\
                .verify_if_user_creates_a_new_users_marked_as_disabled_it_should_reflect_as_disabled():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_121(self):
        self.logger.info("Users module = test_TC_US_121 execution started..")
        if Users_Module_pom() \
                .verify_user_able_to_see_if_the_enabled_is_displayed_for_users_marked_as_enabled_under_users_panel():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_TC_US_122(self):
        self.logger.info("Users module = test_TC_US_122 execution started..")
        if Users_Module_pom() \
                .verify_user_able_to_see_if_the_disabled_is_displayed_for_users_marked_as_disabled_under_users_panel():
            assert True
        else:
            assert False

    #
    # @pytest.mark.p2
    # def test_TC_US_128(self):
    #     self.logger.info("Users module = test_TC_US_128 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_able_to_open_the_details_for_the_newly_created_user_under_users_panel():
    #         assert True
    #     else:
    #         assert False


    @pytest.mark.p1
    def test_TC_US_04(self):
        self.logger.info("Users module = test_TC_US_04 execution started..")
        if Users_Module_pom() \
                .verify_user_able_to_edit_the_details_for_the_newly_created_user_details():
            assert True
        else:
            assert False

    # delete user is skipped for now
    @pytest.mark.skip
    def test_TC_US_06(self):
        self.logger.info("Users module = test_TC_US_06 execution started..")
        if Users_Module_pom() \
                .verify_user_able_to_delete_the_newly_created_user():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_TC_US_07(self):
        self.logger.info("Users module = test_TC_US_07 execution started..")
        if Users_Module_pom() \
                .verify_user_should_not_be_able_to_create_user_which_already_exist():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_TC_US_11(self):
        self.logger.info("Users module = test_TC_US_143 execution started..")
        if Users_Module_pom().verify_user_able_to_assign_the_newly_created_user_to_a_notification_group():
            assert True
        else:
            assert False
    @pytest.mark.p2
    def test_TC_US_08(self):
        self.logger.info("Users module = test_TC_US_08 execution started..")
        if Users_Module_pom() \
                .on_alert_schedule_edit_user_alert_schedule_and_verify_the_panel_should_be_editable():
            assert True
        else:
            assert False


    @pytest.mark.p1
    def test_TC_US_178(self):
        self.logger.info("Users module = test_TC_US_10 execution started..")
        if Users_Module_pom() \
                 .Verify_reassigning_user_to_diferrent_region():
             assert True
        else:
             assert False

    @pytest.mark.p3
    def test_TC_US_09(self):
        self.logger.info("Users module = test_TC_US_09 execution started..")
        if Users_Module_pom() \
                .verify_send_sms_send_mms_send_email_send_in_app_notifications_enable_disable_alerts_Yes_No_button():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_13(self):
        self.logger.info("user module = test_Tc_US_13_execution stsrted....")
        if Users_Module_pom().Verify_total_users_are_n_including_default_user():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_14(self):
        self.logger.info("user module = test_Tc_US_13_execution stsrted....")
        if Users_Module_pom().Create_5_users_with_all_required_field():
            assert True
        else:
            assert False



from pathlib import Path
import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.Notification_Groups_Module.notification_groups_module_POM import Notification_Groups_Module_pom


@pytest.mark.run(order=3)
class Test_Notification_Groups_Module(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Notification_Groups_Module (Order - 3) Begin ********")
    print("******** Notification_Groups_Module (Order - 3) Begin ********")

    @pytest.mark.system
    def test_TC_NG_01(self):
        if Notification_Groups_Module_pom().Create_5_Notification_groups_fill_the_details_and_link_the_particular_user_to_particular_NG_based_on_naming_convention():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_NG_02(self):
        if Notification_Groups_Module_pom().Verify_total_count_of_NGs_is_6_including_default_NG():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_NG_03(self):
        if Notification_Groups_Module_pom().Verify_user_able_to_create_a_new_Notification_Group_by_filling_all_the_fields_and_verify_present_3_buttons_below_are_activated():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_NG_04(self):
        if Notification_Groups_Module_pom().verify_user_able_to_edit_notification_group():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_NG_05(self):
        if Notification_Groups_Module_pom().verify_user_able_to_link_an_enrollments_groups_to_notification_groups():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_NG_06(self):
        if Notification_Groups_Module_pom().verify_user_able_to_unlink_an_enrollments_groups_from_notification_groups():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_NG_07(self):
        if Notification_Groups_Module_pom().verify_user_able_to_see_events_associated_to_Notification_group_and_events_associated_to_details_of_Notification_group_for_both_event_count_should_be_match():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_NG_08(self):
        if Notification_Groups_Module_pom().verify_user_able_to_link_a_user_to_notification_group():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_NG_09(self):
        if Notification_Groups_Module_pom().verify_user_able_to_unlink_a_user_to_notification_group():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_NG_10(self):
        if Notification_Groups_Module_pom().Verify_user_able_to_delete_the_newly_created_notification_group():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_NG_11(self):
        if Notification_Groups_Module_pom().Verify_details_of_default_notification_group():
            assert True
        else:
            assert False

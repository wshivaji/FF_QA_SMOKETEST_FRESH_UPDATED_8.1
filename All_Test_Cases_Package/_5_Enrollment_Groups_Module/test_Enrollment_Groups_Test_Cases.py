import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.Enrollment_Groups_Module_POM.Enrollment_Groups_Module_POM import Enrollments_Groups_Module_pom


@pytest.mark.run(order=4)
class Test_Enrollment_Groups_Module(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Enrollment_Groups_Module (Order - 4) Begin ********")
    print("******** Enrollment_Groups_Module (Order - 4) Begin ********")

    @pytest.mark.system
    def test_TC_EG_01(self):
        if Enrollments_Groups_Module_pom().Create_5_Enrollment_groups_fill_the_details_and_link_the_particular_NG_to_particular_EG_based_on_naming_convention():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_EG_02(self):
        if Enrollments_Groups_Module_pom().Verify_total_count_of_EGs_is_6_including_default_EG():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_EG_03(self):
        if Enrollments_Groups_Module_pom().Verify_for_above_all_5_EG_face_and_mask_threshold_value_should_be_point_83_and_suppress_duplicate_events_value_should_be_0_minute():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_EG_04(self):
        if Enrollments_Groups_Module_pom().Verify_user_able_to_create_a_new_Enrollment_Group_by_filling_all_the_fields_and_verify_present_3_buttons_below_are_activated():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_EG_05(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_edit_enrollment_group():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_EG_06(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_link_a_notification_group_from_enrollments_groups_panel():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_EG_07(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_unlink_a_notification_group_from_enrollments_groups_panel():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_EG_08(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_see_enrollments_from_associated_group():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_EG_09(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_see_possible_match_events_associated_to_enrollements_group_and_possible_match_events_associated_to_details_of_enrollment_group_for_both_event_count_should_be_match():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_EG_010(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_link_the_enrollments_from_enrollments_groups_panel():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_EG_011(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_unlink_the_enrollments_from_enrollments_groups_panel():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_EG_012(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_delete_newly_created_enrollment_group():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_EG_013(self):
        if Enrollments_Groups_Module_pom().Verify_details_of_default_enrollment_group():
            assert True
        else:
            assert False

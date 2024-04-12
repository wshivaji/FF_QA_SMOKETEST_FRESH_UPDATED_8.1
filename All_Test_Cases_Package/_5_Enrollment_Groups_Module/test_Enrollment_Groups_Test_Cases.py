import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._5_Enrollment_Groups_Module_POM.Enrollment_Groups_Module_POM import Enrollments_Groups_Module_pom


@pytest.mark.run(order=6)
class Test_Enrollment_Groups_Module(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Enrollment_Groups_Module (Order - 5) Begin ********")
    print("******** Enrollment_Groups_Module (Order - 5) Begin ********")

    @pytest.mark.p1
    def test_TC_EG_01(self):
        if Enrollments_Groups_Module_pom().Create_5_Enrollment_groups_fill_the_details_and_link_the_particular_NG_to_particular_EG_based_on_naming_convention():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_02(self):
        if Enrollments_Groups_Module_pom().Verify_total_count_of_EGs_is_6_including_default_EG():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_03(self):
        if Enrollments_Groups_Module_pom().Verify_for_above_all_5_EG_face_and_mask_threshold_value_should_be_point_83_and_suppress_duplicate_events_value_should_be_0_minute():
            assert True
        else:
            assert False

    def test_TC_EG_04(self):
        if Enrollments_Groups_Module_pom().Verify_user_able_to_create_a_new_Enrollment_Group_by_filling_all_the_fields_and_verify_present_3_buttons_below_are_activated():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_05(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_edit_enrollment_group():
            assert True
        else:
            assert False

    def test_TC_EG_06(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_link_a_notification_group_from_enrollments_groups_panel():
            assert True
        else:
            assert False

    def test_TC_EG_07(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_unlink_a_notification_group_from_enrollments_groups_panel():
            assert True
        else:
            assert False

    def test_TC_EG_08(self):
        if Enrollments_Groups_Module_pom().verify_user_able_to_see_enrollments_from_associated_group():
            assert True
        else:
            assert False




    # @pytest.mark.p2
    # def test_TC_EG_018(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_018 execution started..")
    #     if Enrollments_Groups_Module_pom().verify_suppress_duplicate_events_dropdown_is_visible_user_able_to_select_from_the_dropdown():
    #         assert True
    #     else:
    #         assert False

    #
    # @pytest.mark.p1
    # def test_TC_EG_021(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_021 execution started..")
    #     if Enrollments_Groups_Module_pom().verify_user_click_on_delete_groups_from_system_option_unselecting_check_box_a_popup_msg_is_appeared():
    #         assert True
    #     else:
    #         assert False
    #

    #
    # @pytest.mark.p2
    # def test_TC_EG_031(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_031 execution started..")
    #     if Enrollments_Groups_Module_pom().verify_user_click_on_enrollments_then_linked_enrollments_should_open():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EG_032(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_032 execution started..")
    #     if Enrollments_Groups_Module_pom().verify_user_click_on_notification_groups_then_linked_notification_groups_should_open():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EG_033(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_033 execution started..")
    #     if Enrollments_Groups_Module_pom().verify_user_click_on_events_then_linked_events_should_open():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EG_034(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_034 execution started..")
    #     if Enrollments_Groups_Module_pom().verify_enrollment_group_details_action_dropdown_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_EG_035(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_035 execution started..")
    #     if Enrollments_Groups_Module_pom().verify_enrollment_group_details_action_dropdown_has_edit_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # # delete enrollment group is skipped for now
    # @pytest.mark.p1
    # def test_TC_EG_036(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_036 execution started..")
    #     if Enrollments_Groups_Module_pom().verify_user_can_delete_any_enrollment_groups():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_070(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_070 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_data_it_should_displayed_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_071(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_071 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_suppress_duplicate_events_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_072(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_072 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_serious_offender_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_073(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_073 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_serious_offender_suppress_duplicate_events_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_074(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_074 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_masked_face_threshold_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_075(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_075 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_masked_face_threshold_suppress_duplicate_events_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_076(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_076 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_masked_face_threshold_serious_offender_success_message():
    #
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_077(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_077 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_masked_face_threshold_serious_offender_suppress_duplicate_events_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_078(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_078 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_serious_offender_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_079(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_079 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_face_threshold_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_080(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_080 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_face_threshold_serious_offender_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_081(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_081 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_face_threshold_serious_offender_suppress_duplicate_events_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_082(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_082 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_face_threshold_masked_face_threshold_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_083(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_083 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_face_threshold_masked_face_threshold_suppress_duplicate_events_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_084(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_084 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_face_threshold_masked_face_threshold_serious_offender_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_085(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_085 execution started..")
    #     if Enrollments_Groups_Module_pom().fill_name_face_masked_face_threshold_serious_offender_suppress_duplicate_events_data_success_msg():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_086(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_086 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_description_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_087(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_087 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_description_suppress_duplicate_events_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_088(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_088 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_description_serious_offender_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_089(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_089 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_description_serious_offender_suppress_duplicate_events_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_090(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_090 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_description_masked_face_threshold_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_091(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_091 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_description_masked_face_threshold_suppress_duplicate_events_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_092(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_092 execution started..")
    #     if Enrollments_Groups_Module_pom().fill_name_description_masked_face_threshold_serious_offender_events_data_success_msg():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_093(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_093 execution started..")
    #     if Enrollments_Groups_Module_pom().name_description_masked_face_threshold_serious_offender_suppress_duplicate_events_data_success_msg():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_094(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_094 execution started..")
    #     if Enrollments_Groups_Module_pom() .filling_name_description_face_threshold_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_095(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_095 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_description_face_threshold_suppress_duplicate_events_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_096(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_096 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_description_face_threshold_serious_offender_events_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_097(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_097 execution started..")
    #     if Enrollments_Groups_Module_pom().name_description_face_threshold_serious_offender_events_suppress_duplicate_events_data_success_msg():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_098(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_098 execution started..")
    #     if Enrollments_Groups_Module_pom().filling_name_description_face_threshold_masked_face_threshold_data_success_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_099(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_099 execution started..")
    #     if Enrollments_Groups_Module_pom().name_description_face_threshold_masked_face_threshold_suppress_duplicate_events_data_success_msg():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EG_0100(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_0100 execution started..")
    #     if Enrollments_Groups_Module_pom().name_description_face_masked_face_threshold_serious_offender_data_success():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_EG_0101(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_0101 execution started..")
    #     if Enrollments_Groups_Module_pom().name_description_face_masked_face_threshold_serious_offender_suppress_duplicate_events_data_success():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EG_0102(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_0102 execution started..")
    #     self.logger.info("Note: at least one enrollment is required to run this test successful...")
    #     if Enrollments_Groups_Module_pom().verify_that_enrollment_should_be_add_from_enrollment_group_module_end_to_end():
    #         assert True
    #     else:
    #
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_EG_0103(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_0103 execution started..")
    #     if Enrollments_Groups_Module_pom().verify_that_notification_group_should_be_created_from_enrollment_group_module_end_to_end():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_EG_0104(self):
    #     self.logger.info("Enrollment Groups module = test_TC_EG_0104 execution started..")
    #     if Enrollments_Groups_Module_pom().verify_that_events_should_be_created_from_enrollment_group_module_end_to_end():
    #         assert True
    #     else:
    #         assert False


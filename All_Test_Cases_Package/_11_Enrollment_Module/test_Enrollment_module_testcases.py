import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._11_Enrollment_POM.Enrollment_module_POM import enrollments_POM


@pytest.mark.run(order=10)
class Test_Enrollments_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Enrollment (Order - 10) Begin ********")
    print("******** Enrollment (Order - 10) Begin ********")

    @pytest.mark.system
    def test_TC_En_001(self):
        if enrollments_POM().Verify_user_is_able_to_see_total_enrollment_count_as_25():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_En_002(self):
        if enrollments_POM().Verify_user_is_able_to_perform_enable_mask_enrollment_which_is_in_disable_state():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_Tc_En_003(self):
        if enrollments_POM().Verify_user_is_able_to_add_single_face_for_enabled_mask_enrollment():
            assert True
        else:
            assert False

    def test_Tc_En_system(self):
        if enrollments_POM().Verify_user_is_able_to_add_single_note_for_enabled_mask_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_Tc_En_05(self):
        if enrollments_POM().Verify_user_is_able_to_see_5_subjects_for_pending_review_condition_using_VIP_user_enroll_5_subjects_for_pending_review():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_Tc_en_06(self):
        if enrollments_POM().Verify_core_user_is_able_to_approve_pending_subjects():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_Tc_en_08(self):
        if enrollments_POM().Verify_core_user_is_able_to_delete_pending_subjects():
            assert True
        else:
            assert  False

    @pytest.mark.system
    def test_Tc_en_09(self):
        if enrollments_POM().Verify_user_is_able_to_enable_the_reject_subject_user_with_all_permissions():
            assert  True
        else:
            assert False

    @pytest.mark.portal
    def test_Tc_en_11(self):
        if enrollments_POM().Verify_if_user_is_enrolled_the_person_with_expiry_date_validate_expired_date_is_visible_on_Enrollment_module_panel():
            assert  True
        else:
            assert False

    @pytest.mark.portal
    def test_Tc_en_12(self):
        if enrollments_POM().verify_user_enroller_of_an_enrollment_able_to_link_a_enrollment_group_and_add_the_person_to_the_group():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_Tc_en_13(self):
        if enrollments_POM().verify_user_enroller_of_an_enrollment_able_to_unlink_same_enrollment_group_and_remove_the_person_from_selected_group():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_en_14(self):
        if enrollments_POM().verify_user_able_to_add_more_faces_to_an_enrollment():
            assert  True
        else:
            assert False

    @pytest.mark.portal
    def test_Tc_en_15(self):
        if enrollments_POM().verify_user_enroller_of_an_enrollment_able_to_see_events_for_a_enrolled_person_on_enrrollments_panel():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_Tc_en_16(self):
        if enrollments_POM().verify_user_enroller_of_an_enrollment_able_to_edit_the_enrollment():
            assert  True
        else:
            assert False

    @pytest.mark.portal
    def test_tc_en_17(self):
        if enrollments_POM().verify_user_enroller_of_an_enrollment_able_to_delete_enrollment():
            assert True
        else:
            assert False


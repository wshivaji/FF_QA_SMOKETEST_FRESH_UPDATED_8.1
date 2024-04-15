import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._11_Enrollment_POM.Enrollment_module_POM import enrollments_POM



class Test_Identify_and_Enroll_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Enrollment (Order - 12) Begin ********")
    print("******** Enrollment (Order - 12) Begin ********")


    @pytest.mark.p1
    def test_TC_En_001(self):
        if enrollments_POM().Verify_user_is_able_to_see_total_enrollment_count_as_25():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_En_002(self):
        if enrollments_POM().Verify_user_is_able_to_perform_enable_mask_enrollment_which_is_in_disable_state():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_Tc_En_003(self):
        if enrollments_POM().Verify_user_is_able_to_add_single_face_for_enabled_mask_enrollment():
            assert  True
        else:
            assert False

    def test_Tc_En_04(self):
        if enrollments_POM().Verify_user_is_able_to_add_single_note_for_enabled_mask_enrollment():
            assert True
        else:
            assert False

    def test_Tc_En_05(self):
        if enrollments_POM().Verify_user_is_able_to_see_5_subjects_for_pending_review_condition_using_VIP_user_enroll_5_subjects_for_pending_review():
            assert True
        else:
            assert False


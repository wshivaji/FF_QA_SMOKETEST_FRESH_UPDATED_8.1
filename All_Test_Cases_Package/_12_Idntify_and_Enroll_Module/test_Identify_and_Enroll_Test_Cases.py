
import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.Identify_and_Enroll_Module_POM.Identify_and_Enroll_Module_POM import Identify_And_Enroll_POM


@pytest.mark.run(order=8)
class Test_Identify_and_Enroll_Test_Cases(web_driver, web_logger):
    # d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Identify & Enroll (Order - 8) Begin ********")
    print("******** Identify & Enroll (Order - 8) Begin ********")

    @pytest.mark.system
    def test_TC_IE_01(self):
        if Identify_And_Enroll_POM().Identify_and_enroll_25_subjects_and_fill_the_required_fields_5_per_Enrollment_groups():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_IE_02(self):
        if Identify_And_Enroll_POM().verify_user_able_approve_enrollment():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_IE_03(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_cropping_the_same_and_adding_the_required_details_for_the_same():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_IE_04(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_and_adding_the_required_details_for_the_same_along_with_expiry_date_and_time_range():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_IE_05(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_and_adding_the_required_details_for_the_same():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_IE_06(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_to_see_the_possible_ranked_match_index_when_uploading_the_above_same_image_with_or_without_crop():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_IE_07(self):
        if Identify_And_Enroll_POM().verify_three_buttons_faces_person_view_and_purge_Replace_are_visible():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_IE_08(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_enroll_the_person_which_is_delete_one_delete_and_enrolling_again_person_should_be_same():
            assert True
        else:
            assert False


    # @pytest.mark.portal
    # def test_TC_IE_09(self):
    #     if Identify_And_Enroll_POM().Verify_for_above_25_enrolled_subject_region_edges_are_properly_assigned():
    #         assert True
    #     else:
    #         assert False













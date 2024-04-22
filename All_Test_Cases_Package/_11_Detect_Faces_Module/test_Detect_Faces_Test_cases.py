import pytest
from All_POM_Packages.Detect_Faces_Module_POM.Detect_Faces_pom import detect_faces_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login, logout


@pytest.mark.run(order=11)
class Test_detect_faces_testcases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** detect_faces (Order - 11) Begin ********")
    print("******** detect_faces (Order - 11) Begin ********")

    @pytest.mark.system
    def test_Detect_Faces_TC_01(self):
        if detect_faces_pom().on_Detect_faces_page_upload_a_image_having_more_no_of_faces_verify_banner_showing_number_of_faces_on_a_image():
            assert True
        else:
            assert False

    @pytest.mark.p3
    def test_Detect_faces_Tc_017(self):
        if detect_faces_pom().on_image_quality_page_verify_download_image_button_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_Detect_faces_Tc_023(self):
        if detect_faces_pom().on_image_qualty_page_in_action_dropdown_click_on_identify_within_enrollments_Identify_and_enroll_page_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_Detect_faces_Tc_032(self):
        if detect_faces_pom().on_image_quality_page_In_action_dropdown_click_on_identify_within_visitors_visitor_search_page_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_Detect_Faces_TC_01(self):
        if detect_faces_pom().on_Detect_faces_page_upload_a_image_having_more_no_of_faces_verify_banner_showing_number_of_faces_on_a_image():
            assert True
        else:
            assert False

    # @pytest.mark.p3
    # def test_Detect_Faces_TC_005(self):
    #     if detect_faces_pom().After_clicking_detect_faces_on_cloudmenu_items_check_panel_heading_of_DETECT_FACES():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_Faces_TC_006(self):
    #     if detect_faces_pom().on_Detect_faces_page_check_a_banner_containing_no_faces_detected_before_uploading_a_image_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_Faces_TC_007(self):
    #     if detect_faces_pom().on_Detect_faces_page_verify_a_image_box_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_Detect_Faces_TC_008(self):
    #     if detect_faces_pom().on_Detect_faces_page_upload_a_image_into_image_box():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.system
    # def test_Detect_Faces_TC_01(self):
    #     if detect_faces_pom().on_Detect_faces_page_upload_a_image_having_more_no_of_faces_verify_banner_showing_number_of_faces_on_a_image():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_Detect_Faces_Tc_010(self):
    #     if detect_faces_pom().On_Detect_faces_page_upload_a_image_having_face_with_mask():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_Faces_Tc_011(self):
    #     if detect_faces_pom().verify_reselect_button_is_visible_in_detect_faces():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_Detect_Faces_Tc_012(self):
    #     if detect_faces_pom().on_Detect_faces_click_on_reselect_button_again_upload_a_image_verify_if_image_is_uploaded():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_Faces_Tc_013(self):
    #     if detect_faces_pom().on_Detect_faces_verify_cross_symbol_is_visible_after_uploding_a_image():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_Detect_Faces_Tc_014(self):
    #     if detect_faces_pom().on_Detect_faces_click_on_cross_symbol_verify_cross_symbol_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_faces_Tc_015(self):
    #     if detect_faces_pom().on_Detect_faces_After_a_selecting_a_image_question_mark_symbol_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_Detect_faces_Tc_016(self):
    #     if detect_faces_pom().After_uploading_a_image_into_imagebox_on_detect_faces_click_on_question_mark_IMAGE_QUALITY_page_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_faces_Tc_017(self):
    #     if detect_faces_pom().on_image_quality_page_verify_download_image_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_faces_Tc_018(self):
    #     if detect_faces_pom().on_image_quality_page_verify_view_file_info_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_Detect_faces_Tc_019(self):
    #     if detect_faces_pom().click_on_view_file_info_button_on_image_quality_page_verify_information_of_image_click_on_ok_on_alert():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_Detect_faces_Tc_020(self):
    #     if detect_faces_pom().on_image_quality_page_verify_and_scroll_image_information_is_visible():
    #         assert  True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_faces_Tc_021(self):
    #     if detect_faces_pom().verify_action_dropdown_is_visible_on_image_quality_page():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_faces_Tc_022(self):
    #     if detect_faces_pom().click_on_ACTION_DROPDOWN_dropdown_on_image_quality_page_verify_list_of_options_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_Detect_faces_Tc_023(self):
    #     if detect_faces_pom().on_image_qualty_page_in_action_dropdown_click_on_identify_within_enrollments_Identify_and_enroll_page_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_Detect_faces_Tc_024(self):
    #     if detect_faces_pom().In_identify_and_enroll_page_if_person_is_already_enrolled_identify_results_page_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_Detect_faces_Tc_025(self):
    #     if detect_faces_pom().In_identify_results_page_verify_faces_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_Detect_faces_Tc_026(self):
    #     if detect_faces_pom().On_identify_results_page_click_faces_button_enrollment_faces_page_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_faces_Tc_027(self):
    #     if detect_faces_pom().verify_person_view_button_is_visible_in_identify_results_page():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_Detect_faces_Tc_028(self):
    #     if detect_faces_pom().on_identify_results_page_click_on_person_view_button_enrollment_view_page_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_faces_Tc_029(self):
    #     if detect_faces_pom().verify_purge_and_replace_button_is_visible_on_identify_results():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_Detect_faces_Tc_030(self):
    #     if detect_faces_pom().on_identify_results_page_click_on_purge_and_replace_an_alert_is_visible_click_ok_button_on_alert_enrollment_faces_page_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_Detect_faces_Tc_031(self):
    #     if detect_faces_pom().on_identify_and_enroll_page_if_person_is_not_enrolled_add_details_are_page_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_Detect_faces_Tc_032(self):
    #     if detect_faces_pom().on_image_quality_page_In_action_dropdown_click_on_identify_within_visitors_visitor_search_page_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Detect_faces_Tc_033(self):
    #     if detect_faces_pom().on_image_quality_page_In_action_dropdown_verify_download_image_option_is_visible():
    #         assert True
    #     else:
    #         assert False
    #


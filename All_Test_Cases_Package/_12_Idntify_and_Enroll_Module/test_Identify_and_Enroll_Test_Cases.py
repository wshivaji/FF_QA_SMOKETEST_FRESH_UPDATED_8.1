
import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._12_Identify_and_Enroll_Module_POM.Identify_and_Enroll_Module_POM import Identify_And_Enroll_POM


@pytest.mark.run(order=5)
class Test_Identify_and_Enroll_Test_Cases(web_driver, web_logger):
    # d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Identify & Enroll (Order - 12) Begin ********")
    print("******** Identify & Enroll (Order - 12) Begin ********")

    @pytest.mark.system
    def test_TC_IE_01(self):
        if Identify_And_Enroll_POM().Identify_and_enroll_25_subjects_and_fill_the_required_fields_5_per_Enrollment_groups():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_02(self):
        if Identify_And_Enroll_POM().verify_user_able_approve_enrollment():
            assert  True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_03(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_cropping_the_same_and_adding_the_required_details_for_the_same():
            assert  True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_04(self):
        if Identify_And_Enroll_POM().Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_and_adding_the_required_details_for_the_same_along_with_expiry_date_and_time_range():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_05(self):
        if Identify_And_Enroll_POM().verify_three_buttons_faces_person_view_and_purge_Replace_are_visible():
            assert True
        else:
            # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_20.png")
            assert False

    @pytest.mark.p1
    def test_TC_IE_06(self):
        if Identify_And_Enroll_POM().Enter_user_able_delete_again_enrolling_same():
            assert  True
        else:
            assert False




    # @pytest.mark.p2
    # def test_TC_IE_06(self):
    #     if Identify_And_Enroll_POM().verify_images_are_visible_enlisted_inside_identify_result_panel():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_18.png")
    #         assert False


    # @pytest.mark.p1
    # def test_TC_IE_01(self):
    #     if Identify_And_Enroll_POM().verify_Cloud_Menu_Local_Menu():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_01.png")
    #         assert False

    # @pytest.mark.p1
    # def test_TC_IE_02(self):
    #     if Identify_And_Enroll_POM().verify_if_Identify_and_Enroll_Menu_Option_is_displayed_and_clickable():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_02.png")
    #         assert False

#     @pytest.mark.p1
#     def test_TC_IE_03(self):
#         if Identify_And_Enroll_POM().verify_a_new_panel_is_displayed_with_title_as_Identify_and_Enroll():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_03.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_04(self):
#         if Identify_And_Enroll_POM(). \
#                 verify_Select_A_Photo_test_is_displayed_at_the_top_inside_Identity_and_Enroll_Panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_04.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_05(self):
#         if Identify_And_Enroll_POM(). \
#                 verify_a_square_box_blank_image_icon_is_displayed_below_select_a_photo_and_it_is_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_05.png")
#             assert False
#
#     @pytest.mark.p5
#     def test_TC_IE_06(self):
#         if Identify_And_Enroll_POM().verify_text_below_image_icon_is_displayed_and_expected_text():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_06.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_07(self):
#         if Identify_And_Enroll_POM().verify_if_a_new_dialog_box_is_appeared_to_choose_image_file():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_07.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_08(self):
#         if Identify_And_Enroll_POM().click_on_image_icon_upload_image_and_verify_if_same_image_displayed_inside_image_box():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_08.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_09(self):
#         if Identify_And_Enroll_POM().verify_Image_Properties_text_below_image_and_its_dimensions_are_visible():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_09.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_10(self):
#         if Identify_And_Enroll_POM().verify_re_Select_Photo_button_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_10.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_11(self):
#         if Identify_And_Enroll_POM().verify_identify_enroll_button_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_11.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_12(self):
#         if Identify_And_Enroll_POM().verify_crop_photo_button_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_12.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_13(self):
#         if Identify_And_Enroll_POM().verify_text_below_three_buttons_is_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_13.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_14(self):
#         if Identify_And_Enroll_POM().verify_if_current_image_is_removed_from_image_box():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_14.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_15(self):
#         if Identify_And_Enroll_POM().verify_new_panel_is_displayed_with_title_as_Identify_Results():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_15.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_16(self):
#         if Identify_And_Enroll_POM().verify_matches_are_found_and_displayed_inside_Identify_Results_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_16.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_17(self):
#         if Identify_And_Enroll_POM().verify_ranked_match_index_title_along_with_symbol_visible_on_identify_results_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_17.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_18(self):
#         if Identify_And_Enroll_POM().verify_images_are_visible_enlisted_inside_identify_result_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_18.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_19(self):
#         if Identify_And_Enroll_POM().verify_location_Case_information_and_index_score_displayed_inside_indentify_result_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_19.png")
#             assert False
#
#
#
#     @pytest.mark.p3
#     def test_TC_IE_21(self):
#         if Identify_And_Enroll_POM().verify_faces_button_is_visible_with_its_label_popping_up_and_clickable_on_identify_results_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_21.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_22(self):
#         if Identify_And_Enroll_POM().verify_person_view_button_is_visible_with_its_label_popping_up_and_clickable_on_identify_results_panel(
#         ):
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_22.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_23(self):
#         if Identify_And_Enroll_POM().verify_purge_replace_button_is_visible_with_its_label_popping_up_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_23.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_24(self):
#         if Identify_And_Enroll_POM().click_on_faces_button_and_verify_a_new_panel_with_title_enrollment_faces_is_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_24.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_25(self):
#         if Identify_And_Enroll_POM().verify_action_dropdown_is_displayed_and_clickable_in_top_right_corner_of_enrollment_faces_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_25.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_26(self):
#         if Identify_And_Enroll_POM().click_on_action_dropdown_and_verify_menu_items_displayed_are_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_26.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_27(self):
#         if Identify_And_Enroll_POM().verify_location_and_case_information_is_displayed_as_a_heading_inside_enrollment_faces_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_27.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_28(self):
#         if Identify_And_Enroll_POM().verify_sample_image_icon_is_visible_below_location_and_it_is_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_28.png")
#             assert False
#
#     @pytest.mark.p5
#     def test_TC_IE_29(self):
#         if Identify_And_Enroll_POM().verify_if_draggable_photo_text_is_visible_above_image_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_29.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_30(self):
#         if Identify_And_Enroll_POM().verify_visitor_image_is_displayed_as_expected_below_sample_image_icon():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_30.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_31(self):
#         if Identify_And_Enroll_POM().verify_a_check_box_is_displayed_and_it_is_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_31.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_32(self):
#         if Identify_And_Enroll_POM().verify_download_image_button_with_its_label_poping_up_and_it_is_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_32.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_33(self):
#         if Identify_And_Enroll_POM().click_on_download_image_image_verify_visitor_image_is_downloaded_successfully():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_33.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_34(self):
#         if Identify_And_Enroll_POM().verify_view_image_info_button_is_visible_along_with_its_label():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_34.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_35(self):
#         if Identify_And_Enroll_POM().click_on_view_image_info_button_verify_a_pop_up_is_appeared_with_image_information(
#         ):
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_35.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_36(self):
#         if Identify_And_Enroll_POM(). \
#                 click_on_close_panel_button_displayed_beside_panel_title_verify_panel_is_closed_successfully():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_36.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_37(self):
#         if Identify_And_Enroll_POM(). \
#                 click_on_Person_View_button_and_verify_a_new_panel_with_title_Enrollment_View_is_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_37.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_38(self):
#         if Identify_And_Enroll_POM(). \
#                 verify_action_dropdown_is_displayed_and_clickable_in_top_right_corner_of_Enrollment_View_is_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_38.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_39(self):
#         if Identify_And_Enroll_POM().click_on_action_dropdown_and_verify_menu_items():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_39.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_40(self):
#         if Identify_And_Enroll_POM().click_on_close_button_of_Identify_Results_panel_and_verify_closed_successfully():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_40.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_41(self):
#         if Identify_And_Enroll_POM().verify_location_and_case_information_is_displayed_as_a_heading_inside_enrollment_view_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_41.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_42(self):
#         if Identify_And_Enroll_POM().verify_visitor_image_is_displayed_as_expected_below_heading_on_enrollment_view_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_42.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_43(self):
#         if Identify_And_Enroll_POM().verify_visitors_lOCATION_STORE_CASE_SUBJECT_information_is_displayed_on_enrollment_view_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_43.png")
#             assert False
#
#     # @pytest.mark.p3
#     # def test_TC_IE_44(self):
#     #     if Identify_And_Enroll_POM() \
#     #             .verify_visitors_ACTION_information_is_displayed_below_its_image_on_Enrollment_View_panel():
#     #         assert True
#     #     else:
# #     #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_44.png")
#     #         assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_45(self):
#         if Identify_And_Enroll_POM().verify_Enrolled_On_text_and_its_information_is_visible_as_expected_on_enrollment_view_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_45.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_46(self):
#         if Identify_And_Enroll_POM().verify_enabled_disabled_information_is_visible_on_enrollment_view_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_46.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_47(self):
#         if Identify_And_Enroll_POM().verify_enrollment_details_button_is_visible_and_clickable_as_expected_on_enrollment_view_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_47.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_48(self):
#         if Identify_And_Enroll_POM().verify_faces_button_is_visible_along_with_count_and_it_is_clickable_on_enrollment_view_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_48.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_49(self):
#         if Identify_And_Enroll_POM().verify_events_button_is_visible_along_with_count_and_it_is_clickable_on_enrollment_view_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_49.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_50(self):
#         if Identify_And_Enroll_POM().verify_enrollment_groups_button_is_visible_along_with_its_count_and_is_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_50.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_51(self):
#         if Identify_And_Enroll_POM().verify_notes_button_is_visible_along_with_its_count_and_is_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_51.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_52(self):
#         if Identify_And_Enroll_POM().click_on_close_panel_button_displayed_beside_panel_title_and_verify_panel_is_closed_successfully():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_52.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_53(self):
#         if Identify_And_Enroll_POM().click_on_purge_and_replace_button_and_pop_up_is_appeared_along_with_expected_message():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_53.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_54(self):
#         if Identify_And_Enroll_POM().click_on_close_panel_button_displayed_beside_panel_title_verify_panel_closed_successfully():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_54.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_55(self):
#         if Identify_And_Enroll_POM().click_on_Crop_Image_button_and_verify_a_pop_up_is_visible_with_expected_message():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_55.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_56(self):
#         if Identify_And_Enroll_POM().click_on_close_panel_button_displayed_beside_panel_title_verify_panel_successfully_closed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_56.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_57(self):
#         if Identify_And_Enroll_POM().verify_two_new_panel_appeared_with_title_as_Enrollment_Steps_and_Add_Details():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_57.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_58(self):
#         if Identify_And_Enroll_POM().verify_first_panel_title_Enrollment_Steps_and_below_it_image_selected_is_visible():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_58.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_59(self):
#         if Identify_And_Enroll_POM().verify_image_properties_text_below_image_along_with_details_is_displayed_as_expected():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_59.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_60(self):
#         if Identify_And_Enroll_POM().verify_warning_text_is_displayed_below_image_on_Enrollment_Steps_panel_as_expected():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_60.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_61(self):
#         if Identify_And_Enroll_POM().verify_No_match_found_text_below_warning_is_visible_as_expected_on_Enrollment_Steps_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_61.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_62(self):
#         if Identify_And_Enroll_POM().verify_exposure_sharpness_resolution_images_parameters_their_data_green_tick_symbol_is_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_62.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_63(self):
#         if Identify_And_Enroll_POM().verify_second_panel_titled_as_Add_Details_and_panel_is_active_enabled():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_63.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_64(self):
#         if Identify_And_Enroll_POM().verify_cancel_button_below_title_Add_Details_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_64.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_65(self):
#         if Identify_And_Enroll_POM().verify_save_button_below_title_Add_Details_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_65.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_66(self):
#         if Identify_And_Enroll_POM().verify_two_option_Expire_Date_and_Do_Not_Expire_are_visible_and_clickable_below_Add_Details_title():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_66.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_67(self):
#         if Identify_And_Enroll_POM().verify_date_entry_textbox_beside_Expire_Date_is_visible_and_clickable_and_current_date_is_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_67.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_68(self):
#         if Identify_And_Enroll_POM().verify_opt_out_label_text_and_check_box_besides_is_visible_and_clickable_on_Add_Details_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_68.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_69(self):
#         if Identify_And_Enroll_POM().verify_Enrollment_Group_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_69.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_70(self):
#         if Identify_And_Enroll_POM().click_on_Enrollment_Group_dropdown_and_verify_options_inside_it_are_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_70.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_71(self):
#         if Identify_And_Enroll_POM().verify_Field_Incomplete_text_below_enrollment_group_dropdown_is_visible_as_expected():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_71.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_72(self):
#         if (Identify_And_Enroll_POM().
#                 verify_REQUIRED_FIELDS_heading_below_enrollment_group_dropdown_is_displayed()):
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_72.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_73(self):
#         if Identify_And_Enroll_POM().verify_LOCATION_STORE_label_text_and_text_box_besides_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_73.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_74(self):
#         if Identify_And_Enroll_POM().verify_Field_Incomplete_text_below_location_store_textbox_is_visible_as_expected():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_74.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_75(self):
#         if Identify_And_Enroll_POM().verify_CASE_SUBJECT_label_text_and_text_box_besides_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_75.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_76(self):
#         if Identify_And_Enroll_POM().verify_Field_Incomplete_text_below_case_subject_textbox_is_visible_as_expected():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_76.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_77(self):
#         if Identify_And_Enroll_POM().verify_REPORTED_LOSS_label_text_and_text_box_besides_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_77.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_78(self):
#         if Identify_And_Enroll_POM().verify_Field_Incomplete_text_below_REPORTED_LOSS_textbox_is_visible_as_expected():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_78.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_79(self):
#         if Identify_And_Enroll_POM().verify_DATE_INCIDENT_label_text_and_text_box_besides_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_79.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_80(self):
#         if Identify_And_Enroll_POM().verify_Field_Incomplete_text_below_DATE_INCIDENT_textbox_is_visible_as_expected():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_80.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_83(self):
#         if Identify_And_Enroll_POM().verify_ACTION_label_text_and_text_box_besides_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_83.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_84(self):
#         if Identify_And_Enroll_POM().verify_Field_Incomplete_text_below_ACTION_textbox_is_visible_as_expected():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_84.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_85(self):
#         if Identify_And_Enroll_POM().verify_OPTIONAL_FIELDS_heading_below_action_textbox_is_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_85.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_86(self):
#         if Identify_And_Enroll_POM().verify_CASE_EVENT_TYPE_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_86.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_87(self):
#         if Identify_And_Enroll_POM().click_on_CASE_EVENT_TYPE_dropdown_and_verify_options_inside_it_are_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_87.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_88(self):
#         if Identify_And_Enroll_POM().verify_ACTIVITY_TYPE_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_88.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_89(self):
#         if Identify_And_Enroll_POM().click_on_ACTIVITY_TYPE_dropdown_and_verify_options_inside_it_are_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_89.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_90(self):
#         if Identify_And_Enroll_POM().verify_METHOD_OF_OFFENSE_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_90.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_91(self):
#         if Identify_And_Enroll_POM().click_on_METHOD_OF_OFFENSE_dropdown_and_verify_options_inside_it_are_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_91.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_92(self):
#         if Identify_And_Enroll_POM().verify_REPORTED_BY_label_text_and_text_box_besides_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_92.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_93(self):
#         if Identify_And_Enroll_POM().verify_Build_label_text_and_text_box_besides_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_93.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_94(self):
#         if Identify_And_Enroll_POM().verify_Body_Markings_label_text_and_text_box_besides_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_94.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_95(self):
#         if Identify_And_Enroll_POM().verify_GENDER_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_95.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_96(self):
#         if Identify_And_Enroll_POM().click_on_GENDER_dropdown_and_verify_options_inside_it_are_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_96.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_97(self):
#         if Identify_And_Enroll_POM().verify_HEIGHT_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_97.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_98(self):
#         if Identify_And_Enroll_POM().click_on_HEIGHT_dropdown_and_verify_options_inside_it_are_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_98.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_99(self):
#         if Identify_And_Enroll_POM().verify_NARRATIVES_label_text_and_text_box_besides_it_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_99.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_100(self):
#         if Identify_And_Enroll_POM().Enter_Data_into_fields_displayed_on_Add_Details_panel_and_verify_enrollment_successfully_created():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_100.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_101(self):
#         if Identify_And_Enroll_POM().verify_Success_message_is_displayed_below_warning_on_Identify_and_enroll_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_101.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_102(self):
#         if Identify_And_Enroll_POM().verify_three_buttons_below_success_message_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_102.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_103(self):
#         if Identify_And_Enroll_POM().click_on_Review_Enrollment_Details_button_and_verify_if_Enrollment_Details_panel_is_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_103.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_104(self):
#         if Identify_And_Enroll_POM().verify_Action_button_visible_and_clickable_on_Enrollment_Details_Panel_below_its_title():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_104.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_105(self):
#         if Identify_And_Enroll_POM().click_and_verify_Edit_Identify_Within_Enrollment_and_Identify_within_visitors_option_are_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_105.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_106(self):
#         if Identify_And_Enroll_POM().verify_location_and_case_name_is_displayed_as_heading_on_Enrollment_Details_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_106.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_107(self):
#         if Identify_And_Enroll_POM().verify_visitor_image_is_visible_besides_it_Enrolled_on_date_and_time_is_displayed_as_expected():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_107.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_108(self):
#         if Identify_And_Enroll_POM().verify_Enabled_Disabled_status_with_its_symbol_is_visible_besides_visitor_image():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_108.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_109(self):
#         if Identify_And_Enroll_POM().verify_Opt_out_status_is_displayed_as_expected_on_Enrollment_Details_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_109.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_110(self):
#         if Identify_And_Enroll_POM().verify_REQUIRED_FIELDS_heading_is_displayed_along_with_its_data_on_Enrollment_Details_Panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_110.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_111(self):
#         if Identify_And_Enroll_POM().verify_OPTIONAL_FIELDS_heading_below_required_field_is_displayed_as_expected():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_111.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_112(self):
#         if Identify_And_Enroll_POM().click_on_close_enrollment_details_panel_and_verify_panel_is_closed_successfully():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_112.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_113(self):
#         if Identify_And_Enroll_POM().click_on_Review_Added_Groups_Button_and_verify_if_enrollment_groups_panel_is_visible():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_113.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_114(self):
#         if Identify_And_Enroll_POM().verify_Filter_dropdown_is_visible_and_clickable_on_Enrollment_Groups_Panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_114.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_115(self):
#         if Identify_And_Enroll_POM().click_on_Filter_dropdown_and_verify_its_options_are_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_115.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_116(self):
#         if Identify_And_Enroll_POM().verify_Action_dropdown_is_visible_and_clickable_on_Enrollment_Groups_Panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_116.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_117(self):
#         if Identify_And_Enroll_POM().click_on_Action_dropdown_and_verify_its_options_are_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_117.png")
#             assert False
#
#     @pytest.mark.skip
#     def test_TC_IE_118(self):
#         if Identify_And_Enroll_POM().verify_select_all_check_box_along_with_its_label_is_visible_and_clickable():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_118.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_119(self):
#         if Identify_And_Enroll_POM().verify_enrollment_groups_associated_with_enrollment_is_enlisted_inside_Enrollment_Groups_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_119.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_120(self):
#         if Identify_And_Enroll_POM().click_on_close_enrollment_group_panel_and_verify_panel_is_closed_successfully():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_120.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_121(self):
#         if Identify_And_Enroll_POM().click_on_add_more_faces_button_and_verify_if_Enrollment_Faces_panel_is_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_121.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_122(self):
#         if Identify_And_Enroll_POM().verify_Action_button_is_visible_and_clickable_on_Enrollment_Faces_Panel_below_its_title():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_122.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_123(self):
#         if Identify_And_Enroll_POM().click_on_Action_dropdown_and_verify_its_options_are_visible_and_clickable_enroll_face_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_123.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_124(self):
#         if Identify_And_Enroll_POM().verify_location_and_case_name_is_displayed_as_heading_on_Enrollment_Faces_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_124.png")
#             assert False
#
#     @pytest.mark.p2
#     def test_TC_IE_125(self):
#         if Identify_And_Enroll_POM().verify_sample_image_box_is_visible_and_clickable_below_location_information():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_125.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_126(self):
#         if Identify_And_Enroll_POM().click_on_sample_image_box_and_verify_if_file_open_dialog_box_is_displayed():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_126.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_127(self):
#         if Identify_And_Enroll_POM().verify_Dragable_Photo_Text_be_displayed_on_enrolled_visitor_image_below_sample_image():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_127.png")
#             assert False
#
#     @pytest.mark.p3
#     def test_TC_IE_128(self):
#         if Identify_And_Enroll_POM().verify_check_box_is_visible_and_clickable_besides_visitor_image_on_the_panel():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_128.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_129(self):
#         if Identify_And_Enroll_POM().verify_download_image_button_is_visible_and_clickable_besides_visitor_image():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_129.png")
#             assert False
#
#     @pytest.mark.p4
#     def test_TC_IE_130(self):
#         if Identify_And_Enroll_POM().verify_image_file_info_button_is_visible_and_clickable_besides_visitor_image():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_130.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_131(self):
#         if Identify_And_Enroll_POM().click_on_download_image_button_and_verify_image_is_downloaded_successfully():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_131.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_132(self):
#         if Identify_And_Enroll_POM().click_on_image_file_info_button_and_verify_a_pop_up_is_displayed_with_image_information():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_132.png")
#             assert False
#
#     @pytest.mark.p1
#     def test_TC_IE_133(self):
#         if Identify_And_Enroll_POM().click_on_close_panel_button_and_verify_enrollment_faces_panel_is_closed_successfully():
#             assert True
#         else:
#             # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_133.png")
#             assert False





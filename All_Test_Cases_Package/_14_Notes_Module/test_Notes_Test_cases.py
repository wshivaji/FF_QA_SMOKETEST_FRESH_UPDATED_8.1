import pytest
from All_POM_Packages._6_Notes_Module_POM.Notes_pom import notes_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=15)
class Test_notes_page_testcases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Notes_Module (Order - 14) Begin ********")
    print("******** Notes_Module (Order - 14) Begin ********")

    @pytest.mark.p1
    def test_NOTES_TC_82(self):
        if notes_pom().create_note_by_filling_all_details_on_create_note():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_NOTES_TC_88(self):
        if notes_pom().click_on_Edit_note_on_notes_details_panel_and_verify_notes_is_edited():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_NOTES_TC_99(self):
        if notes_pom().on_notes_panel_click_on_location_symbol_map_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_NOTES_TC_107(self):
        if notes_pom().on_notes_panel_selecting_a_checkbox_and_click_on_delete_selected_notes_a_WARNING_message_window_is_displayed_click_on_yes_button():
            assert True
        else:
            assert False

    def test_NOTES_TC_04(self):
        if notes_pom().verif_use_is_able_to_select_any_one_note_and_click_on_location_in_view_dropdown():
            assert True
        else:
            assert False

    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_01(self):
    #     if notes_pom().click_on_NOTES_and_check_heading_of_the_notes_page():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_02(self):
    #     if notes_pom().on_notes_panel_verify_searchdropdown_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_03(self):
    #     if notes_pom().On_notes_panel_click_on_Search_dropdown_the_List_of_elements_are_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_NOTES_Tc_04(self):
    #     if notes_pom().click_on_search_dropdown_on_notes_panel_verify_Location_store_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_Tc_05(self):
    #     if notes_pom().on_notes_panel_Inside_search_dropdown_Enter_a_text_on_Location_store_click_in_search_notes_is_displayed_as_expected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_06(self):
    #     if notes_pom().on_notes_panel_inside_search_dropdown_Enter_a_text_on_Location_store_click_on_clear_text_is_cleared_on_textbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_NOTES_Tc_07(self):
    #     if notes_pom().on_notes_panel_inside_search_dropdown_verify_case_Subject_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_08(self):
    #     if notes_pom().on_notes_panel_inside_action_dropdown_Enter_a_text_on_case_Subject_and_click_on_search_notes_is_displayed_as_expected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_09(self):
    #     if notes_pom().on_notes_panel_inside_search_dropdown_Enter_a_case_Subject_and_click_on_clear_text_is_cleared_on_textbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTESTc_010(self):
    #     if notes_pom().on_notes_panel_inside_search_dropdown_verify_and_click_either_sort_by_A_Z_or_sort_by_Z_A_radio_button_is_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_Tc_011(self):
    #     if notes_pom().on_notes_panel_inside_search_dropdown_click_on_sort_by_AtoZ_radio_button_followed_by_Location_store_in_sort_by_dropdown_click_on_search_notes_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_012(self):
    #     if notes_pom().on_notes_panel_inside_search_dropdown_click_on_sort_by_AtoZ_radio_button_followed_by_Location_store_in_sort_by_dropdown_click_on_clear_Location_store_is_cleared_on_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_Tc_013(self):
    #     if notes_pom().on_notes_panel_inside_search_dropdown_click_on_sort_by_Z_A_radio_button_followed_by_case_subject_in_sort_by_dropdown_click_on_search_notes_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_014(self):
    #     if notes_pom().on_notes_panel_inside_search_dropdown_click_on_sort_by_ZtoA_radio_button_followed_by_case_subject_in_sort_by_dropdown_click_on_clear_case_subject_is_cleared_on_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_Tc_015(self):
    #     if notes_pom().on_notes_panel_inside_search_dropdown_verify_and_enter_a_text_on_both_Location_store_and_Case_subject_and_click_on_search_notes_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_16(self):
    #     if notes_pom().on_notes_panel_inside_searchdropdown_verify_and_enter_a_text_on_both_Location_store_and_Case_subject_and_click_on_clear_text_is_cleared():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_17(self):
    #     if notes_pom().on_notes_panel_inside_searchdropdown_Enter_a_text_on_location_store_textbox_click_on_search_on_note_page_in_search_criteria_location_store_details_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_018(self):
    #     if notes_pom().on_notes_panel_inside_searchdropdown_Enter_a_text_on_case_subject_textbox_click_on_search_on_notes_page_search_criteria_case_subject_details_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_19(self):
    #     if notes_pom().on_notes_panel_inside_search_dropdown_Enter_both_location_store_and_case_subject_both_details_are_displayed_on_search_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_020(self):
    #     if notes_pom().on_notes_panel_inside_searchdropdown_Enter_both_location_store_and_case_subject_and_click_on_cross_symbol_on_search_criteria_details_on_search_criteria_are_removed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_21(self):
    #     if notes_pom().on_notes_panel_Click_on_location_inside_Search_Drop_down_map_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_022(self):
    #     if notes_pom().verify_the_heading_of_map_Notes_Location_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_023(self):
    #     if notes_pom().verify_Find_location_textbox_is_visible_on_Notes_Location_page():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_024(self):
    #     if notes_pom().on_notes_location_panel_Enter_a_location_in_Find_location_textbox_verify_dropdown_list_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_025(self):
    #     if notes_pom().on_notes_location_panel_verify_Draw_circle_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_NOTES_Tc_26(self):
    #     if notes_pom().on_notes_loaction_panel_Click_on_toggle_symbol_full_screen_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_NOTES_Tc_027(self):
    #     if notes_pom().on_notes_location_panel_Click_on_ESC_button_on_keyboard_Full_Screen_view_is_minimized():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_028(self):
    #     if notes_pom().on_notes_location_panel_verify_and_click_on_plus_symbol_on_Notes_location_page_map_is_maximized():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_029(self):
    #     if notes_pom().on_notes_location_panel_click_on_minus_symbol_on_Notes_location_page_map_is_minimized():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_030(self):
    #     if notes_pom().on_notes__location_panel_Click_on_three_horizantal_lines_on_right_side_of_map_Select_a_Search_Target_Window_is_dispayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_Tc_031(self):
    #     if notes_pom().on_notes_location_panel_In_Select_a_search_Target_Drop_down_and_click_on_Events_location_map_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_notes_TC_032(self):
    #     if notes_pom().on_notes_location_panel_in_Select_a_search_Target_Drop_down_and_click_on_Notes_Notes_location_map_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_033(self):
    #     if notes_pom().on_notes_location_panel_click_on_three_horizantal_lines_followed_by_click_on_cancel_button_on_Select_Search_Target_window_is_closed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_034(self):
    #     if notes_pom().click_on_cross_symbol_on_Notes_location_page_is_closed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_notes_Tc_035(self):
    #     if notes_pom().click_on_cross_symbol_on_Event_page_is_closed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_036(self):
    #     if notes_pom().verify_Action_Drop_down_is_visible_on_Notes():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_37(self):
    #     if notes_pom().click_on_Action_Drop_down_list_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_38(self):
    #     if notes_pom().click_on_Create_User_in_Action_Dropdown_check_Create_Note_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_39(self):
    #     if notes_pom().verify_0n_Create_Note_imagebox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_40(self):
    #     if notes_pom().click_on_imagebox_and_select_a_image_from_desktop_location():
    #         assert True
    #     else:
    #         assert False
    #
    #
    # @pytest.mark.p2
    # def test_notes_Tc_41(self):
    #     if notes_pom().on_note_add_image_panel__after_image_selected_from_desktop_crop_image_skip_cropping_and_cancel_buttons_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_notes_TC_42(self):
    #     if notes_pom().on_note_add_image_panel_Click_cancel_button_on_Note_Add_Image_page_is_closed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_43(self):
    #     if notes_pom().on_note_add_image_panel_click_on_skip_cropping_Re_Crop_photo_select_photo_buttons_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_Tc_44(self):
    #     if notes_pom().on_note_add_image_panel_click_on_select_photo_button_photo_is_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_Notes_TC_45(self):
    #     if notes_pom().on_note_add_image_panel_click_on_Re_Crop_button_cancel_Skip_cropping_crop_image_buttons_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_46(self):
    #     if notes_pom().on_note_add_image_panel_click_on_crop_image_alert_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_47(self):
    #     if notes_pom().on_create_note_panel_LOCATION_STORE_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_48(self):
    #     if notes_pom().on_create_note_panel_Enter_a_text_on_LOCATION_STORE_textbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_49(self):
    #     if notes_pom().verify_CASE_SUBJECT_textbox_is_visible_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_50(self):
    #     if notes_pom().on_crate_note_panel_Enter_a_text_on_CASE_SUBJECT_textbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_51(self):
    #     if notes_pom().verify_REPORTED_LOSS_textbox_is_visible_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_52(self):
    #     if notes_pom().enter_a_text_on_REPORTED_LOSS_on_create_note_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_53(self):
    #     if notes_pom().verify_on_create_note_claender_is_visible_in_date_of_incident():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_54(self):
    #     if notes_pom().on_create_notes_panel_click_date_of_incident_calender_symbol_calender_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_55(self):
    #     if notes_pom().on_create_note_panel_verify_CASE_EVENT_TYPE_drop_down_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_56(self):
    #     if notes_pom().on_create_note_panel_click_on_CASE_EVENT_TYPE_dropdown_list_is_visible_select_any_element_present_in_dropdown_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_57(self):
    #     if notes_pom().verify_ACTIVITY_TYPE_drop_down_list_visible_on_create_note_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_58(self):
    #     if notes_pom().on_create_note_panel_select_any_option_on_ACTIVITY_TYPE_drop_down_option_and_verify_option_is_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_59(self):
    #     if notes_pom().on_create_note_panel__click_on_METHOD_OF_OFFENCE_drop_down_list_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_60(self):
    #     if notes_pom().on_create_note_panel_verify_and_select_element_on_METHOD_OF_OFFENCE_drop_down_is_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_61(self):
    #     if notes_pom().verify_REPORTED_BY_textbox_is_visible_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_62(self):
    #     if notes_pom().on_create_note_panel_Enter_a_text_on_REPORTED_BY_textbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_63(self):
    #     if notes_pom().verify_on_BUILD_textbox_is_visible_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_64(self):
    #     if notes_pom().on_create_note_Enter_a_text_on_BUILD_textbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_65(self):
    #     if notes_pom().verify_BODY_MARKINGS_textbox_is_visible_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_66(self):
    #     if notes_pom().on_create_note_enter_a_text_on_BODY_MARKINGS_textbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_67(self):
    #     if notes_pom().verify_GENDER_drop_down_is_displayed_on_create_note_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_68(self):
    #     if notes_pom().on_create_note_panel_verify_and_select_a_options_on_GENDER_drop_down_option_is_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_69(self):
    #     if notes_pom().verify_HEIGHT_drop_down_is_displayed_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_70(self):
    #     if notes_pom().on_create_note_panel_select_a_element_on_HEIGHT_drop_down_verify_option_is_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_71(self):
    #     if notes_pom().verify_NARRATIVES_text_box_is_visible_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_72(self):
    #     if notes_pom().on_create_notes_panel_enter_a_text_on_NARRATIVES_textbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_73(self):
    #     if notes_pom().verify_action_textbox_is_visible_in_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_74(self):
    #     if notes_pom().on_create_note_panel_Enter_a_text_in_action_textbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_75(self):
    #     if notes_pom().verify_ADD_LOCATION_button_is_visible_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_76(self):
    #     if notes_pom().click_on_ADD_LOCATION_on_create_note_notes_location_page_is_visible_followed_by_click_on_any_location_facefirst_logo_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_Tc_77(self):
    #     if notes_pom().verify_save_button_is_visible_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_Tc_78(self):
    #     if notes_pom().on_create_note_panel_click_on_save_button():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_79(self):
    #     if notes_pom().verify_cancel_button_is_visible_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_80(self):
    #     if notes_pom().click_on_cancel_button_in_createnote_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_81(self):
    #     if notes_pom().on_notes_panel_verify_refresh_in_action_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_NOTES_TC_82(self):
    #     if notes_pom().create_note_by_filling_all_details_on_create_note():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_NOTES_TC_83(self):
    #     if notes_pom().on_notes_panel_click_on_refresh_on_Action_Drop_down_the_page_gets_refreshed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_084(self):
    #     if notes_pom().on_notes_panel_verify_Delete_selected_notes_is_visible_on_Action_drop_down():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_085(self):
    #     if notes_pom().on_notes_panel_click_on_Delete_selected_notes_an_alert_window_is_displayed_click_ok_on_alert():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_86(self):
    #     if notes_pom().on_notes_panel_For_deleting_notes_select_check_box():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_87(self):
    #     if notes_pom().on_notes_panel_selecting_a_checkbox_and_click_on_delete_selected_notes_a_WARNING_message_window_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_NOTES_TC_88(self):
    #     if notes_pom().click_on_Edit_note_on_notes_details_panel_and_verify_notes_is_edited():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_89(self):
    #     if notes_pom().on_notes_panel_click_on_NO_cancel_button_on_warning_window_notes_is_not_deleted():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_90(self):
    #     if notes_pom().on_notes_panel_change_panel_refresh_rate_is_visible_in_Action_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_91(self):
    #     if notes_pom().on_notes_panel_click_on_change_panel_refresh_rate_change_panel_refresh_rate_window_is_opened():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_92(self):
    #     if notes_pom().click_on_change_refresh_option_inside_action_dropdown_and_verify_Auto_refresh_off_drop_down_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_93(self):
    #     if notes_pom().on_notes_panel_click_on_change_refresh_rate_panel_select_a_optioninside_Auto_refresh_off_drop_down_option_is_selected_and_displayed_on_Action_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_94(self):
    #     if notes_pom().verify_cancel_button_is_visible_in_change_refresh_rate_window():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_95(self):
    #     if notes_pom().click_on_cancel_button_in_change_refresh_rate_window():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_96(self):
    #     if notes_pom().on_notes_panel_verify_view_dropdown_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_97(self):
    #     if notes_pom().click_on_locations_inside_view_dropdown_notes_location_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_98(self):
    #     if notes_pom().verify_location_symbol_is_visible_on_notes_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_99(self):
    #     if notes_pom().on_notes_panel_click_on_location_symbol_map_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_100(self):
    #     if notes_pom().verify_notes_details_symbol_is_visible_on_notes_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_101(self):
    #     if notes_pom().on_notes_panel_click_on_view_details_symbol_notes_details_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_NOTES_TC_102(self):
    #     if notes_pom().verify_three_horizantal_lines_button_is_visible_in_notes_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_103(self):
    #     if notes_pom().click_on_three_horizantal_lines_button_and_verify_image_and_enrollments_buttons_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_104(self):
    #     if notes_pom().click_on_enrollment_button_on_three_horizantal_lines_button_enrollments_groups_are_visible_if_not_alert_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_NOTES_TC_105(self):
    #     if notes_pom().on_notes_panel_click_on_three_horizantal_lines_button_followed_by_images_button_notes_image_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_NOTES_TC_106(self):
    #     if notes_pom().close_notes_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_NOTES_TC_107(self):
    #     if notes_pom().on_notes_panel_selecting_a_checkbox_and_click_on_delete_selected_notes_a_WARNING_message_window_is_displayed_click_on_yes_button():
    #         assert True
    #     else:
    #         assert False

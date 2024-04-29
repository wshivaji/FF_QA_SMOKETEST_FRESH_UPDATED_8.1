import pytest
from All_POM_Packages._10_Events_Module_POM.Events_Pom import events_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
# from All_POM_Package.Events_Module.Events_Pom import events_pom
# from All_Test_Cases_Package.conftest import Base_Class


@pytest.mark.run(order=14)
class Test_eVents_testcases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Events (Order - 10) Begin ********")
    print("******** Events (Order - 10) Begin ********")

    @pytest.mark.p1
    def test_events_TC_001(self):
        if events_pom().Verify_25_events_are_generated_for_25_enrolled_subjects():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_events_TC_002(self):
        self.logger.info("Verify_5_events_for_each_group_soe_abe_pte_fraude_and_vipe_using_enrollment_group_selection_in_search_dropdown")
        if events_pom().Verify_5_events_for_each_group_soe_abe_pte_fraude_and_vipe_using_enrollment_group_selection_in_search_dropdown():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_002.png")
            self.logger.info("test_events_TC_002 fail")
            assert False

    @pytest.mark.p1
    def test_events_TC_003(self):
        self.logger.info("Verify 25 events using Org/hierarchy selection in search dropdown")
        if events_pom().Verify_25_events_using_Org_hierarchy_selection_in_search_dropdown():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_003.png")
            self.logger.info("test_events_TC_003 fail")
            assert False

    @pytest.mark.p1
    def test_events_TC_004(self):
        self.logger.info("Verify 5 events for each group (soe, abe, pte, fraude and vipe) using enrollment group and org/hierarchy selection in search dropdown")
        if events_pom().Verify_5_events_for_each_group_soe_abe_pte_fraude_and_vipe_using_enrollment_group_and_org_hierarchy_selection_in_search_dropdown():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_05.png")
            self.logger.info("test_TC_ESFC_05 fail")
            assert False

    @pytest.mark.p1
    def test_events_TC_005(self):
        self.logger.info("Add the tags with respective enrollment groups and org/hierarchy selection (example soe: deterred and assualt, abe: deterred and threat, pte: deterred and push cart, fraude and vipe: deterred and fraud) ")
        if events_pom().Add_the_tags_with_respective_enrollment_groups_and_org_hierarchy_selection_example_soe_deterred_and_assualt_abe_deterred_and_threat_pte_deterred_and_push_cart_fraude_and_vipe_deterred_and_fraud():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_005.png")
            self.logger.info("test_events_TC_005 fail")
            assert False

    @pytest.mark.p1
    def test_events_TC_006(self):
        self.logger.info("Verify 5 events are visible by enrollment group, org/hierarchy and Tag selection")
        if events_pom().Verify_5_events_are_visible_by_enrollment_group_org_hierarchy_and_Tag_selection():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_006.png")
            self.logger.info("test_events_TC_006 fail")
            assert False

    @pytest.mark.p1
    def test_events_TC_007(self):
        self.logger.info("Verify user should be able to add the tags and see that same tags are visible when user clicks on display tags option in view dropdown")
        if events_pom().Verify_user_should_be_able_to_add_the_tags_and_see_that_same_tags_are_visible_when_user_clicks_on_display_tags_option_in_view_dropdown():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_007.png")
            self.logger.info("test_events_TC_007 fail")
            assert False

    @pytest.mark.p1
    def test_events_TC_008(self):
        self.logger.info("Verify user able to delete probable match events")
        if events_pom().Verify_user_able_to_delete_probable_match_events():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_008.png")
            self.logger.info("test_events_TC_008 fail")
            assert False

    @pytest.mark.p1
    def test_events_TC_009(self):
        self.logger.info("Probable Match Event search with DateTimeRange, EnrollmentGroup, Org/Hierarchy and Tag filter combination result should be DateTimeRange, EnrollmentGroup, Org/Hierarchy and Tagged event.")
        if events_pom().Probable_Match_Event_search_with_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tag_filter_combination_result_should_be_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tagged_event():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_009.png")
            self.logger.info("test_events_TC_009 fail")
            assert False

    @pytest.mark.p3
    def test_events_TC_010(self):
        if events_pom().on_Event_view_panel_click_on_Action_dropdown_followed_by_Identify_within_enrollments_option_in_dropdown_and_verify_Identify_enroll_and_identify_results_panel_are_visible():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_events_TC_011(self):
        if events_pom().Verify_user_is_able_to_perform_identify_within_visitors_from_Probable_Match_Enrollment_View_panel_when_event_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_events_TC_012(self):
        if events_pom().Verify_user_is_able_to_edit_the_Enrollment_details_on_Enrollment_View_panel_when_ProbableMatch_Event_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_events_TC_013(self):
        if events_pom().Verify_user_is_able_to_add_face_on_Enrollment_view_panel_when_event_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_events_TC_014(self):
        if events_pom().Verify_user_is_able_to_see_probable_match_events_associated_to_same_person_on_Enrollment_View_panel_when_probable_match_event_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_events_TC_015(self):
        if events_pom().Verify_user_able_to_link_a_enrollment_group_and_add_the_person_to_the_group():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_events_TC_016(self):
        if events_pom().Verify_user_able_to_unlink_same_enrollment_group_and_remove_the_person_from_selected_group():
            assert True
        else:
            assert False

    # @pytest.mark.p1
    # def test_events_TC_001(self):
    #     if events_pom().Launching_login_page():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_events_TC_002(self):
    #     if events_pom().logo_username_texbox_password_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p1
    # def test_events_TC_003(self):
    #     if events_pom().verify_on_cloud_menu_after_login():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p1
    # def test_events_TC_004(self):
    #     if events_pom().verify_Events_are_displayed_in_dashboard_items():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p1
    # def test_events_TC_005(self):
    #     if events_pom().click_on_Events_and_verify_panel_heading_of_Events_is_visible():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_events_TC_006(self):
    #     if events_pom().verify_view_dropdown_is_visible():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_events_TC_007(self):
    #     if events_pom().on_Events_panel_heading_verify_cross_symbol_is_visible():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p1
    # def test_events_TC_008(self):
    #     if events_pom().on_Events_page_verify_filter_search_results_textbox_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
            
    @pytest.mark.p2
    def test_events_TC_009_1(self):
        if events_pom().on_Events_page_Enter_a_text_in_search_filter_by_action_textbox_and_verify_number_of_events_displayed():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_010_1(self):
        if events_pom().on_Events_page_verify_search_dropdown_is_visible_and_clickable_text_on_button_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_011_1(self):
        if events_pom().on_Events_page_verify_Action_dropdown_is_visible_and_clickable_text_on_button_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_012_1(self):
        if events_pom().on_Events_page_verify_SELECT_ALL_checkbox_is_visible_and_clickable_select_all_text_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_013_1(self):
        if events_pom().on_Events_page_verify_Event_real_time_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_014_1(self):
        if events_pom().on_Events_page_verify_location_store_along_with_case_subject_Index_score_Action_taken_region_this_event_info_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_015_1(self):
        if events_pom().on_Events_page_verify_Live_Image_text_and_Live_Image_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_016_1(self):
        if events_pom().on_Events_page_verify_File_Image_text_File_Image_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_017(self):
        if events_pom().on_Events_page_verify_Event_button_is_visible_and_symbol_on_button_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_018(self):
        if events_pom().on_Events_page_verify_tag_button_is_visible_and_symbol_on_button_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_019(self):
        if events_pom().on_Events_page_verify_extent_menu_button_and_symbol_on_button_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_020(self):
        if events_pom().on_Events_page_verify_Load_More_button_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_021(self):
        if events_pom().on_Events_page_verify_number_of_events_are_visible_below_Load_More_button():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_022(self):
        if events_pom().on_Events_page_click_on_load_more_button_and_verify_number_of_Events_count_is_40_displayed():
            assert True
        else:
            assert False
    #
    # @pytest.mark.skip
    # def test_events_TC_023(self):
    #     if events_pom().on_Events_page_click_on_load_more_button_and_verify_number_of_Events_count_is_40_displayed():
    #         assert True
    #     else:
    #         assert False
            
    @pytest.mark.p2
    def test_events_TC_024(self):
        if events_pom().click_on_view_dropdown_and_verify_location_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_025(self):
        if events_pom().In_view_dropdown_click_on_location_an_alert_is_opened_click_ok_an_alert_select_a_event_and_verify_panel_heading_of_Events_location_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_026(self):
        if events_pom().on_Events_location_page_verify_Find_textbox_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_027(self):
        if events_pom().on_Events_location_page_on_map_facefirst_logo_is_visible_click_on_logo_event_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_event_TC_028(self):
        if events_pom().on_Events_location_page_verify_Draw_circle_button_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_029(self):
        if events_pom().on_Events_Location_page_verify_serach_area_button_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_030(self):
        if events_pom().on_Events_location_page_verify_extent_menu_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_031(self):
        if events_pom().on_Events_location_page_click_on_extent_menu_verify_search_target_window_dialouge_box_is_displayed():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_032(self):
        if events_pom().on_Events_location_page_in_select_a_search_target_dialouge_box_a_dropdown_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_033(self):
        if events_pom().on_Events_location_page_In_select_a_search_target_dropdown_click_on_NOTES_option_Notes_location_page_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_034(self):
        if events_pom().on_Events_location_page_In_select_a_search_target_dropdown_click_on_Events_option_Events_location_page_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_035(self):
        if events_pom().on_Events_location_page_In_select_a_search_target_dialouge_box_verify_cancel_button_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_036(self):
        if events_pom().on_Events_location_page_In_select_search_target_dropdown_click_on_cancel_button_verify_Events_location_panel_heading_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_037(self):
        if events_pom().on_Events_location_page_Click_on_full_screen_toggle_symbol_full_screen_is_displayed():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_038(self):
        if events_pom().on_Events_location_page_Click_on_ESC_button_from_keyboard_Full_Screen_view_to_minimize_full_screen_view():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_039(self):
        if events_pom().on_Events_location_page_verify_and_click_on_plus_symbol_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_040(self):
        if events_pom().on_Events_location_page_verify_and_click_on_plus_symbol_on_Notes_location_page_map_performs_zoom_in():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_041(self):
        if events_pom().on_Events_location_page_verify_minus_symbol_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_042(self):
        if events_pom().on_Events_location_page_verify_and_click_on_minus_symbol_on_Notes_location_page_map_performs_zoom_out():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_043(self):
        if events_pom().on_Events_page_click_on_select_All_checkbox_click_on_location_in_view_dropdown_verify_number_of_events_on_that_location():
            assert True
        else:
            assert False

    @pytest.mark.p3
    def test_events_TC_044(self):
        if events_pom().on_Events_page_verify_in_view_dropdown_display_tags_option_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_045(self):
        if events_pom().on_Events_page_click_on_display_tags_and_verify_Tags_are_visible_inthe_formof_horizantal_line_below_the_events():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_046(self):
        if events_pom().on_Events_page_click_on_search_dropdown_and_verify_Date_time_range_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.skip
    def test_events_TC_047(self):
        if events_pom().on_Events_page_click_on_search_dropdown_and_verify_Date_time_range_to_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_048(self):
        if events_pom().on_Events_page_click_on_search_dropdown_and_verify_Enrollment_group_selection_button_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_049(self):
        if events_pom().on_Events_page_click_on_search_dropdown_and_verify_org_hierarchy_selection_button_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_050(self):
        if events_pom().on_Events_page_click_on_search_dropdown_and_verify_tag_selection_button_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_051(self):
        if events_pom().on_Events_page_click_on_search_dropdown_and_verify_sort_by_dropdown_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_052(self):
        if events_pom().on_Events_page_click_on_search_dropdow_and_verify_sort_by_AtoZ_radio_button_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_053(self):
        if events_pom().on_Events_page_click_on_search_dropdown_and_verify_sort_by_ZtoA_radio_button_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_054(self):
        if events_pom().on_Events_page_click_on_search_dropdown_verify_clear_button_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_055(self):
        if events_pom().on_Events_page_click_on_search_dropdown_andverify_location_search_button_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_056(self):
        if events_pom().verify_an_event_search_with_not_selected_any_button_in_search_dropdown_click_on_search():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_072(self):
        if events_pom().on_Events_page_click_on_Action_dropdown_and_verify_dropdown_options_are_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_073(self):
        if events_pom().on_Events_page_click_on_Action_dropdown_followed_by_Edit_tags_not_selecting_an_event_verify_an_alert_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_074(self):
        if events_pom().on_Events_page_In_Action_dropdown_click_on_Edit_tags_option_and_verify_Events_tags_panel_is_visible_and_verify_panel_heading():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_075(self):
        if events_pom().on_Events_tags_panel_verify_filter_dropdown_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_076(self):
        if events_pom().on_Events_tags_panel_click_on_filter_dropdown_and_verify_linked_tags_and_unlinked_tag_options_are_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_077(self):
        if events_pom().on_Events_tags_panel_click_on_linked_tags_in_filter_dropdown_and_verify_only_linked_tags_are_disiplayed():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_078(self):
        if events_pom().on_Events_tags_panelclick_on_unlinked_tags_in_filter_dropdown_and_verify_only_unlinked_tags_banner_and_unlinked_tags_are_displayed():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_079(self):
        if events_pom().on_Events_tags_panel_verify_filter_tag_name_text_box_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_080(self):
        if events_pom().on_Events_tags_panelEnter_a_tagname_in_filter_tag_name_text_and_verify_only_text_entered_tags_are_displayed():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_081(self):
        if events_pom().on_Events_tags_verify_Details_button_is_visible_in_each_tag():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_082(self):
        if events_pom().on_Events_tags_click_on_Details_button_and_verify_Tag_Details_panel_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_083(self):
        if events_pom().on_Events_tags_panel_verify_Action_dropdown_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_084(self):
        if events_pom().on_Events_tags_panel_click_on_Action_dropdrown_followed_by_Addtags_to_events_without_selecting_checkbox_an_alert_is_visible_verify_text_and_ok_on_alert():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_085(self):
        if events_pom().Verify_user_is_able_to_link_the_tag_and_add_tag_to_probable_match_events_when_tag_icon_is_click():
            assert True
        else:
            assert False
            

            
    @pytest.mark.p2
    def test_events_TC_087(self):
        if events_pom().Verify_user_is_able_to_unlink_the_tag_and_remove_tag_from_probable_match_events_when_tag_icon_is_click():
            assert True
        else:
            assert False
            

            
    @pytest.mark.p2
    def test_events_TC_089(self):
        if events_pom().In_Events_page_In_Action_dropdown_click_on_refresh_option_and_verify_page_is_refreshed_and_verify_updated_text():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_events_TC_090(self):
        if events_pom().In_Events_page_In_Action_dropdown_click_on_change_refresh_option_and_verify_change_refresh_rate_dialouge_box_is_opened():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_091(self):
        if events_pom().on_Events_page_In_change_refresh_rate_dialouge_box_verify_dropdown_options_are_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_092(self):
        if events_pom().on_Events_page_on_Inchange_refresh_rate_dialouge_box_dropdown_select_a_1_minute_dropdown_option_and_verify_in_Action_dropdown_showing_changerefresh_rate_1_minute_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_093(self):
        if events_pom().on_Events_page_In_change_refresh_rate_dialouge_box_verify_cancel_button_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_094(self):
        if events_pom().on_Events_page_click_on_cancel_button_on_change_refresh_rate_dialouge_box_dialouge_box_is_closed():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_095(self):
        if events_pom().In_Events_page_click_on_Action_dropdown_verify_print_option_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_096(self):
        if events_pom().In_Events_page_click_on_Action_dropdown_click_on_print_verify_print_and_cancel_buttons_are_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_097(self):
        if events_pom().on_Events_page_click_on_Events_symbol_and_verify_Event_view_and_Enrollment_view_panels_are_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_098(self):
        if events_pom().on_Event_view_panel_verify_Action_dropdown_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_099(self):
        if events_pom().on_Event_view_panel_click_on_Action_dropdown_followed_by_Identify_within_enrollments_option_in_dropdown_and_verify_Identify_enroll_and_identify_results_panel_are_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_100(self):
        if events_pom().on_Event_view_panel_click_on_Action_dropdown_followed_by_Identify_within_visitor_option_in_dropdown_and_verify_visitor_search_panel_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_101(self):
        if events_pom().on_Event_view_click_on_print_option_in_Action_dropdown_and_verify_print_page_is_visible_print_button_and_cancel_button_are_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_102(self):
        if events_pom().on_Event_view_panel_verify_video_button_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_103(self):
        if events_pom().on_Event_view_panel_click_on_video_button_and_verify_Event_video_panel_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_104(self):
        if events_pom().on_Event_view_panel_verify_tags_button_is_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_events_TC_105(self):
        if events_pom().on_Event_view_panel_click_on_tags_button_and_verify_Events_tags_panel_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_106(self):
        if events_pom().In_Enrollment_view_panel_verify_Action_dropdown_is_visible_and_clickable():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_107(self):
        if events_pom().Verify_user_is_able_to_perform_identify_within_enrollments_fromEnrollment_View_panel_when_event_icon_is_click():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_108(self):
        if events_pom().Verify_user_is_able_to_perform_identify_within_visitors_from_Probable_Match_Enrollment_View_panel_when_event_icon_is_click():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_109(self):
        if events_pom().on_Enrollment_view_click_on_view_Edits_details_in_Acton_dropdown_and_verify_Enrollment_details_panel_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_110(self):
        if events_pom().Verify_user_enroller_of_an_enrollment_is_able_to_enable_the_disable_enrolled_subject_on_Enrollment_View_modules():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_111(self):
        if events_pom().on_Enrollment_view_click_Permanently_DELETE_Enrollment_in_Action_dropdown_verify_warning_dialouge_box_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_112(self):
        if events_pom().on_Enrollment_view_click_on_Actiondropdown_followed_by_Permanently_DELETE_Enrollment_verify_warning_dialouge_box_is_visible_click_on_Nocancel_button_and_verify_warning_dialouge_box_is_closed():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_114(self):
        if events_pom().Verify_user_is_able_to_edit_the_Enrollment_details_on_Enrollment_View_panel_when_ProbableMatch_Event_icon_is_click():
            assert True
        else:
            assert False

            
    @pytest.mark.p2
    def test_events_TC_117(self):
        if events_pom().Verify_user_is_able_to_add_face_on_Enrollment_view_panel_when_event_icon_is_click():
            assert True
        else:
            assert False
            
    @pytest.mark.p3
    def test_events_TC_118(self):
        if events_pom().on_Enrollment_view_verify_Events_button_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_events_TC_119(self):
        if events_pom().Verify_user_is_able_to_see_probable_match_events_associated_to_same_person_on_Enrollment_View_panel_when_probable_match_event_icon_is_click():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_120(self):
        if events_pom().Verify_user_able_to_link_a_enrollment_group_and_add_the_person_to_the_group():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_121(self):
        if events_pom().Verify_user_able_to_unlink_same_enrollment_group_and_remove_the_person_from_selected_group():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_122(self):
        if events_pom().Verify_user_is_able_to_add_note_on_Enrollment_view_panel_when_Probable_Match_Event_icon_is_click():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_123(self):
        if events_pom().on_Enrollment_view_panel_click_on_Notes_button_and_verify_Enrollment_notes_panel_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_124(self):
        if events_pom().on_Event_page_click_on_tags_symbol_and_verify_Events_Tags_panel_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_125(self):
        if events_pom().on_Eventpage_click_on_extent_menu_button_and_verify_video_location_symbol_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_126(self):
        if events_pom().on_Event_page_click_on_extent_menu_followed_by_video_symbol_and_verify_Event_video_panel_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_127(self):
        if events_pom().on_Event_video_panel_verify_video_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_128(self):
        if events_pom().on_Event_page_click_on_extentmenu_followed_by_location_symbol_and_verify_Events_Location_is_panel_is_visible():
            assert True
        else:
            assert False

    # @pytest.mark.p1
    # def test_events_TC_129(self):
    #     if events_pom().Verify_25_events_are_generated_for_25_enrolled_subjects():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p1
    # def test_TC_ESFC_05(self):
    #     self.logger.info("Event Search Filter Combination = test_TC_ESFC_05 execution started..")
    #     if events_pom().Verify_5_events_for_each_group_soe_abe_pte_fraude_and_vipe_using_enrollment_group_selection_in_search_dropdown():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_05.png")
    #         self.logger.info("test_TC_ESFC_05 fail")
    #         assert False

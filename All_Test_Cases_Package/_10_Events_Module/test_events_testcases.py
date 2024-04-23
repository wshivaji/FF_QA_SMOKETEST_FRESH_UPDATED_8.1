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



    @pytest.mark.portal
    def test_events_TC_05(self):
        if events_pom().Verify_user_is_able_to_perform_identify_within_enrollments_fromEnrollment_View_panel_when_event_icon_is_click():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_06(self):
        if events_pom().Verify_user_is_able_to_perform_identify_within_visitors_from_Probable_Match_Enrollment_View_panel_when_event_icon_is_click():
            assert True
        else:
            assert False
            
    @pytest.mark.p2
    def test_events_TC_07(self):
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

    @pytest.mark.p2
    def test_events_TC_08(self):
        if events_pom().Verify_user_is_able_to_edit_the_Enrollment_details_on_Enrollment_View_panel_when_ProbableMatch_Event_icon_is_click():
            assert True
        else:
            assert False

            
    @pytest.mark.p2
    def test_events_TC_09(self):
        if events_pom().Verify_user_is_able_to_add_face_on_Enrollment_view_panel_when_event_icon_is_click():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_events_TC_10(self):
        if events_pom().Verify_user_is_able_to_see_probable_match_events_associated_to_same_person_on_Enrollment_View_panel_when_probable_match_event_icon_is_click:
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_11(self):
        if events_pom().Verify_user_able_to_link_a_enrollment_group_and_add_the_person_to_the_group():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_12(self):
        if events_pom().Verify_user_able_to_unlink_same_enrollment_group_and_remove_the_person_from_selected_group():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_13(self):
        if events_pom().on_Enrollment_view_panel_click_on_Notes_button_and_verify_Enrollment_notes_panel_is_visible():
            assert True
        else:
            assert False
            
    @pytest.mark.p1
    def test_events_TC_14(self):
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

    @pytest.mark.p1
    def test_events_TC_14(self):
        if events_pom().Verify_25_events_are_generated_for_25_enrolled_subjects():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_16(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_05 execution started..")
        if events_pom().Verify_5_events_for_each_group_soe_abe_pte_fraude_and_vipe_using_enrollment_group_selection_in_search_dropdown():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_05.png")
            self.logger.info("test_TC_ESFC_05 fail")
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

    @pytest.mark.p2
    def test_events_TC_045(self):
        if events_pom().on_Events_page_click_on_display_tags_and_verify_Tags_are_visible_inthe_formof_horizantal_line_below_the_events():
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

    @pytest.mark.p3
    def test_events_TC_055(self):
        if events_pom().on_Events_page_click_on_search_dropdown_andverify_location_search_button_is_visible_and_clickable():
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

    #
    # @pytest.mark.p1
    # def test_events_TC_002(self):
    #     if events_pom().logo_username_texbox_password_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_events_TC_009(self):
    #     if events_pom().on_Events_page_Enter_a_text_in_search_filter_by_action_textbox_and_verify_number_of_events_displayed():
    #         assert True
    #     else:
    #         assert False
    # @pytest.mark.p1
    # def test_events_TC_022(self):
    #     if events_pom().on_Events_page_click_on_load_more_button_and_verify_number_of_Events_count_is_40_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_events_TC_023(self):
    #     if events_pom().on_Events_page_click_on_load_more_button_and_verify_number_of_Events_count_is_40_displayed():
    #         assert True
    #     else:
    #         assert False


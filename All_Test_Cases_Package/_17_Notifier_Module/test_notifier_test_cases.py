from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._17_Notifier_Module_POM.Notifier_POM import Notifier_pom
import pytest


@pytest.mark.run(order=18)
class Test_Notifier_Module_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Notifier (Order - 17) Begin ********")
    print("******** Notifier (Order - 17) Begin ********")

    @pytest.mark.p2
    def test_TC_Notifier_069(self):
        if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_104(self):
        if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_10_sec_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_ON():
            assert True
        else:
            assert False

    @pytest.mark.p3
    def test_TC_Notifier_040(self):
        if Notifier_pom().On_Notifier_panel_click_on_COLLAPSE_button_and_verify_event_alert_info_collapsed_and_EXPAND_button_is_visible():
            assert True
        else:
            assert False

    # @pytest.mark.p1
    # def test_TC_Notifier_002(self):
    #     if Notifier_pom().Verify_Notifier_is_visible_and_clickable_in_dashboard_menu_items_click_on_Notifier_and_verify_it_is_navigating_to_notifier_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_003(self):
    #     if Notifier_pom().Click_on_Notifier_and_verify_title_is_visible_CLOUD_MENU_button_is_visible_and_clickable_user_name_is_visible_Logout_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_004(self):
    #     if Notifier_pom().Verify_Close_Notifier_button_in_dashboard_menu_is_visible_and_clickable_bullhorn_icon_and_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_005(self):
    #     if Notifier_pom().Click_on_Close_Notifier_button_on_dashboard_and_verify_notifier_panel_is_closed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_006(self):
    #     if Notifier_pom().Verify_Enrollment_Group_Selection_button_is_visible_and_clickable_text_and_group_icon_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_007(self):
    #     if Notifier_pom().Verify_Org_Hierarchy_Selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_008(self):
    #     if Notifier_pom().\
    #             Verify_Notifier_Setting_button_is_visible_and_clickable_text_and_setting_icon_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_009(self):
    #     if Notifier_pom().Verify_Close_Notifier_symbol_on_Notifier_panel_is_visible_and_clickable_close_symbol_is_visible_click_on_close_notifier_and_verify_Notifier_panel_is_closing():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Notifier_010(self):
    #     if Notifier_pom().Click_on_Enrollment_Group_Selection_button_and_verify_select_a_group_panel_is_visible_heading_on_panel_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_011(self):
    #     if Notifier_pom().In_Group_Selection_dialog_box_verify_filter_group_list_below_textbox_is_visible_and_clickable_group_list_below_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_012(self):
    #     if Notifier_pom().Verify_group_list_radio_buttons_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_013(self):
    #     if Notifier_pom().Verify_Clear_button_Close_button_and_Save_button_are_visible_and_clickable_texts_on_buttons_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Notifier_014(self):
    #     if Notifier_pom().\
    #             Select_one_group_and_click_on_Save_button_and_verify_that_group_name_is_visible_on_Notifier_panel_verify_Selected_group_s_text_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_015(self):
    #     if Notifier_pom().\
    #             Select_one_group_and_click_on_Clear_button_and_verify_the_selected_group_is_unselected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_016(self):
    #     if Notifier_pom().Click_on_Close_button_and_verify_group_selection_panel_is_closing():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Notifier_017(self):
    #     if Notifier_pom().Click_on_Org_Hierarchy_Selection_button_and_verify_new_panel_is_visible_verify_heading_on_Org_Hierarchy_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_018(self):
    #     if Notifier_pom().Verify_Collapse_all_Expand_all_Select_all_Unselect_all_buttons_are_visible_and_clickable_text_on_buttons_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_019(self):
    #     if Notifier_pom().Click_on_Collapse_all_button_and_verify_all_regions_are_collapsing():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_020(self):
    #     if Notifier_pom().Click_on_Expand_all_and_verify_all_regions_are_expanding():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_021(self):
    #     if Notifier_pom().Click_on_Select_all_and_verify_all_regions_are_selecting():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_022(self):
    #     if Notifier_pom().Click_on_Unselect_all_and_verify_all_regions_are_unselecting():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Notifier_023(self):
    #     if Notifier_pom().Verify_Search_textbox_is_visible_and_clickable_label_on_text_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_024(self):
    #     if Notifier_pom().Enter_one_region_name_in_Search_textbox_and_verify_only_given_region_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_025(self):
    #     if Notifier_pom().\
    #             Verify_Close_button_on_Org_Hierarchy_is_visible_and_clickable_text_on_Close_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_026(self):
    #     if Notifier_pom().click_on_Close_button_and_verify_Org_Hierarchy_Selection_panel_is_closing():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Notifier_027(self):
    #     if Notifier_pom().\
    #             Verify_Save_button_on_Org_Hierarchy_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_028(self):
    #     if Notifier_pom().On_Org_Hierarchy_Selection_panel_verify_all_regions_under_root_with_their_cameras_are_visible_and_checkbox_besides_them_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_029(self):
    #     if Notifier_pom().Select_one_region_from_list_click_on_Save_button_and_verify_only_selected_region_events_are_visible_verify_STATION_text_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_030(self):
    #     if Notifier_pom().\
    #             Click_on_Notifier_Settings_and_verify_dialog_box_is_visible_verify_heading_on_dialog_box_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_031(self):
    #     if Notifier_pom().On_Notifier_Settings_dialog_box_verify_CANCEL_and_SAVE_buttons_are_visible_and_clickable_text_on_buttons_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_032(self):
    #     if Notifier_pom().In_Notifier_Settings_verify_Refresh_Rate_text_and_dropdown_beside_it_is_visible_and_clickable_options_inside_dropdown_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_033(self):
    #     if Notifier_pom().In_Notifier_Settings_verify_Of_Events_Displayed_text_and_dropdown_beside_it_is_visible_and_clickable_options_inside_dropdown_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_034(self):
    #     if Notifier_pom().In_Notifier_Settings_verify_Photo_Size_text_and_dropdown_beside_it_is_visible_and_clickable_options_inside_dropdown_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_035(self):
    #     if Notifier_pom().In_Notifier_Settings_verify_Sound_Option_text_and_dropdown_beside_it_is_visible_and_clickable_options_inside_dropdown_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Notifier_036(self):
    #     if Notifier_pom().Verify_message_to_user_if_there_is_no_event_for_region_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Notifier_037(self):
    #     if Notifier_pom().Verify_message_to_user_if_there_is_no_event_for_group_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Notifier_038(self):
    #     if Notifier_pom().On_Notifier_panel_verify_COLLAPSE_button_on_event_notification_info_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Notifier_039(self):
    #     if Notifier_pom().On_Notifier_panel_verify_Close_Notifier_button_on_event_notification_info_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_040(self):
    #     if Notifier_pom().On_Notifier_panel_click_on_COLLAPSE_button_and_verify_event_alert_info_collapsed_and_EXPAND_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Notifier_041(self):
    #     if Notifier_pom().Verify_EXPAND_button_is_clickable_and_text_on_it_is_visible_click_on_EXPAND_button_and_verify_it_is_navigating_back_to_event_alert_info():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_042(self):
    #     if Notifier_pom().On_Notifier_panel_click_on_Close_Notifier_button_and_verify_notifier_is_closed_and_Events_panel_and_Enrollment_View_panel_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_044(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_5_min_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_045(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_4_min_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_046(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_3_min_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_047(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_2_min_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_048(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_1_min_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_049(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_30_sec_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_050(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_10_sec_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_051(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_5_sec_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_052(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_1_sec_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_053(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_054(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_1_photo_size_as_XX_Large_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_055(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_3_photo_size_as_X_Large_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_056(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_4_photo_size_as_Large_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_057(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_5_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_058(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_6_photo_size_as_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_059(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_7_photo_size_as_X_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_060(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_8_photo_size_as_X_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_061(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_9_photo_size_as_X_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_062(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_10_photo_size_as_X_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_063(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_11_photo_size_as_X_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_064(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_12_photo_size_as_X_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_065(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_13_photo_size_as_X_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_066(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_14_photo_size_as_X_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_067(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_15_photo_size_as_X_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_068(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_20_photo_size_as_X_Small_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_069(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_070(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_071(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_072(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_073(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_074(self):
    #     if Notifier_pom().Verify_Notifier_result_for_first_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_075(self):
    #     if Notifier_pom().Verify_Notifier_result_for_first_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_076(self):
    #     if Notifier_pom().Verify_Notifier_result_for_first_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_077(self):
    #     if Notifier_pom().Verify_Notifier_result_for_first_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_078(self):
    #     if Notifier_pom().Verify_Notifier_result_for_first_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_079(self):
    #     if Notifier_pom().Verify_Notifier_result_for_second_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_080(self):
    #     if Notifier_pom().Verify_Notifier_result_for_second_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_081(self):
    #     if Notifier_pom().Verify_Notifier_result_for_second_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_082(self):
    #     if Notifier_pom().Verify_Notifier_result_for_second_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_083(self):
    #     if Notifier_pom().Verify_Notifier_result_for_second_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_084(self):
    #     if Notifier_pom(
    #             ).Verify_Notifier_result_for_third_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_085(self):
    #     if Notifier_pom(
    #             ).Verify_Notifier_result_for_third_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_086(self):
    #     if Notifier_pom(
    #             ).Verify_Notifier_result_for_third_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_087(self):
    #     if Notifier_pom(
    #             ).Verify_Notifier_result_for_third_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Notifier_088(self):
    #     if Notifier_pom(
    #             ).Verify_Notifier_result_for_third_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # # @pytest.mark.p2
    # # def test_TC_Notifier_089(self):
    # #     if Notifier_pom(
    # #             ).Verify_Notifier_result_for_fourth_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    # #         assert True
    # #     else:
    # #         assert False
    # #
    # # @pytest.mark.p2
    # # def test_TC_Notifier_090(self):
    # #     if Notifier_pom(
    # #             ).Verify_Notifier_result_for_fourth_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    # #         assert True
    # #     else:
    # #         assert False
    # #
    # # @pytest.mark.p2
    # # def test_TC_Notifier_091(self):
    # #     if Notifier_pom(
    # #             ).Verify_Notifier_result_for_fourth_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    # #         assert True
    # #     else:
    # #         assert False
    # #
    # # @pytest.mark.p2
    # # def test_TC_Notifier_092(self):
    # #     if Notifier_pom(
    # #             ).Verify_Notifier_result_for_fourth_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    # #         assert True
    # #     else:
    # #         assert False
    # #
    # # @pytest.mark.p2
    # # def test_TC_Notifier_093(self):
    # #     if Notifier_pom(
    # #             ).Verify_Notifier_result_for_fourth_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    # #         assert True
    # #     else:
    # #         assert False
    # #
    # # @pytest.mark.p2
    # # def test_TC_Notifier_094(self):
    # #     if Notifier_pom(
    # #             ).Verify_Notifier_result_for_fifth_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    # #         assert True
    # #     else:
    # #         assert False
    # #
    # # @pytest.mark.p2
    # # def test_TC_Notifier_095(self):
    # #     if Notifier_pom(
    # #             ).Verify_Notifier_result_for_fifth_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    # #         assert True
    # #     else:
    # #         assert False
    # #
    # # @pytest.mark.p2
    # # def test_TC_Notifier_096(self):
    # #     if Notifier_pom(
    # #             ).Verify_Notifier_result_for_fifth_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    # #         assert True
    # #     else:
    # #         assert False
    # #
    # # @pytest.mark.p2
    # # def test_TC_Notifier_097(self):
    # #     if Notifier_pom(
    # #             ).Verify_Notifier_result_for_fifth_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    # #         assert True
    # #     else:
    # #         assert False
    # #
    # # @pytest.mark.p2
    # # def test_TC_Notifier_098(self):
    # #     if Notifier_pom(
    # #             ).Verify_Notifier_result_for_fifth_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    # #         assert True
    # #     else:
    # #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Notifier_099(self):
    #     if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Notifier_100(self):
    #     if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Notifier_101(self):
    #     if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Notifier_102(self):
    #     if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Notifier_103(self):
    #     if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Notifier_104(self):
    #     if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_10_sec_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_ON():
    #         assert True
    #     else:
    #         assert False
    #

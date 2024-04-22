from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.Reporting_Module.Reporting_Events_POM import Reporting_Events_pom
import pytest


@pytest.mark.run(order=16)
class Test_Reporting_Module_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Reporting_Module (Order - 16) Begin ********")
    print("******** Reporting_Module (Order - 16) Begin ********")

    @pytest.mark.portal
    def test_TC_Reporting_01(self):
        if (Reporting_Events_pom().
                Verify_report_for_number_of_probable_match_events_by_zone_with_default_dates_and_optional_filters()):
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_Reporting_02(self):
        if (Reporting_Events_pom().
                Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_and_optional_filters()):
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_Reporting_03(self):
        if (Reporting_Events_pom().
                Verify_report_for_number_of_enrollment_by_zones_with_default_dates_and_optional_filters()):
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_Reporting_04(self):
        if Reporting_Events_pom().Verify_report_for_number_of_zones_by_enrollment_with_default_dates_and_optional_filters():
            assert True
        else:
            assert False

    # *************************************************************************************************
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_002(self):
    #     if Reporting_pom().verify_reporting_is_visible_in_dashboard_items_click_on_reporting_and_verify_it_is_navigating_to_reporting_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_003(self):
    #     if Reporting_pom().\
    #             verify_reporting_panel_heading_is_visible_close_panel_button_on_panel_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_004(self):
    #     if Reporting_pom().verify_report_selection_text_chart_icon_select_report_criteria_text_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_005(self):
    #     if Reporting_pom().verify_report_the_text_and_dropdown_beside_it_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_006(self):
    #     if Reporting_pom().click_on_report_the_dropdown_and_verify_options_inside_dropdown_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_007(self):
    #     if Reporting_pom().click_on_dropdown_followed_by_report_the_and_select_number_of_events_option_verify_new_dropdown_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_008(self):
    #     if Reporting_pom().verify_by_text_is_visible_click_on_by_dropdown_and_verify_options_inside_dropdown_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_009(self):
    #     if Reporting_pom().Click_on_close_panel_button_and_verify_Reporting_panel_is_closing():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_018(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_number_of_visitors_from_report_field1_and_hour_of_day_from_report_field2_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_019(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_date_and_time_range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_020(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_021(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_022(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_023(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_024(self):
    #     if Reporting_pom().\
    #             for_number_of_visitors_by_hour_of_day_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_025(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_optional_filters_age_range_to_number_of_ages_to_group_totals_by_texts_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_026(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_start_age_dropdown_end_age_dropdown_and_number_of_ages_to_group_totals_by_dropdown_are_visible_and_clickable_click_on_dropdowns():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_027(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_gender_and_male_texts_are_visible_male_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_028(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_female_text_is_visible_female_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_029(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_unknown_text_is_visible_unknown_gender_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_030(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible_text_on_right_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_031(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_032(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_033(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_034(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_035(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_036(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_selected_zone_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_037(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_038(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_039(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_040(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_041(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_042(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_043(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_day_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_044(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_day_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_045(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_day_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_046(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_day_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_047(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_day_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_048(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_day_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_049(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_day_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_050(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_day_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_051(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_day_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_052(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_053(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_054(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_055(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_056(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_zone_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_all_zones_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_057(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_zone_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_all_zones_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_058(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_zone_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_all_zones_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_059(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_zone_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_all_zones_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_060(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_number_of_visitors_from_report_field1_and_day_of_week_from_report_field2_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_061(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_062(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_063(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_064(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_065(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_066(self):
    #     if Reporting_pom().\
    #             for_number_of_visitors_by_day_of_week_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_067(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_Optional_Filters_Age_Range_to_Number_of_ages_to_group_totals_by_text_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_068(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_start_age_dropdown_end_age_dropdown_and_number_to_age_group_totals_by_dropdown_are_visible_and_clickable_click_on_dropdowns():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_069(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_gender_and_male_texts_are_visible_male_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_070(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_female_text_is_visible_female_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_071(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_unknown_text_is_visible_unknown_gender_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_072(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible_text_on_right_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_073(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_074(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_075(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_076(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_077(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_078(self):
    #     if Reporting_pom().\
    #             for_number_of_visitors_by_day_of_week_verify_selected_zone_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_079(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_080(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_081(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_082(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_083(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_084(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_DW_085(self):
    #     if Reporting_pom().for_number_of_visitors_by_day_of_week_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_086(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_number_of_visitors_from_report_field1_and_hour_of_week_from_report_field2_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_087(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_088(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_089(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_090(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_091(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_092(self):
    #     if Reporting_pom().\
    #             for_number_of_visitors_by_hour_of_week_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_093(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_Optional_Filters_Age_Range_to_Number_of_ages_to_group_totals_by_text_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_094(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_start_age_dropdown_end_age_dropdown_and_number_to_age_group_totals_by_dropdown_are_visible_and_clickable_click_on_dropdowns():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_095(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_gender_and_male_texts_are_visible_male_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_096(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_female_text_is_visible_female_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_097(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_unknown_text_is_visible_unknown_gender_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_098(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible_text_on_right_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_099(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_100(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_101(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_102(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_103(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_104(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_selected_zone_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_105(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_106(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_107(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_108(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_109(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_110(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HW_111(self):
    #     if Reporting_pom().for_number_of_visitors_by_hour_of_week_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_112(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_number_of_visitors_from_report_field1_and_zone_from_report_field2_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_113(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_114(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_115(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_116(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_117(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_118(self):
    #     if Reporting_pom().\
    #             for_number_of_visitors_by_zone_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_119(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_Optional_Filters_Age_Range_to_Number_of_ages_to_group_totals_by_text_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_120(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_start_age_dropdown_end_age_dropdown_and_number_to_age_group_totals_by_dropdown_are_visible_and_clickable_click_on_dropdowns():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_121(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_gender_and_male_texts_are_visible_male_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_122(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_female_text_is_visible_female_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_123(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_unknown_text_is_visible_unknown_gender_checkbox_is_visible_and_clickable_and_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_ZN_124(self):
    #     if Reporting_pom().for_number_of_visitors_by_zone_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EN_ZN_125(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_number_of_enrollments_from_report_field1_and_zone_from_report_field2_texts_are_visible_on_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EN_ZN_126(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_127(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_128(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_129(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_130(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EN_ZN_131(self):
    #     if Reporting_pom().\
    #             for_number_of_enrollments_by_zone_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EN_ZN_132(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_133(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_134(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_Generate_Report_button_is_visible_and_clickable_text_and_chart_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EN_ZN_135(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_136(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_137(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_138(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EN_ZN_139(self):
    #     if Reporting_pom().\
    #             for_number_of_enrollments_by_zone_verify_selected_group_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_140(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_141(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_142(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_143(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_144(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EN_ZN_145(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EN_ZN_146(self):
    #     if Reporting_pom().for_number_of_enrollments_by_zone_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EN_ZN_147(self):
    #     if Reporting_pom().verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_and_with_group_selected_as_SOE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EN_ZN_148(self):
    #     if Reporting_pom().verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_and_with_group_selected_as_ABE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EN_ZN_149(self):
    #     if Reporting_pom().verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_and_with_group_selected_as_PTE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EN_ZN_150(self):
    #     if Reporting_pom().verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_and_with_group_selected_as_FRAUDE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EN_ZN_151(self):
    #     if Reporting_pom().verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_and_with_group_selected_as_VIPE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EN_ZN_152(self):
    #     if Reporting_pom().verify_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_SOE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EN_ZN_153(self):
    #     if Reporting_pom().verify_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_ABE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EN_ZN_154(self):
    #     if Reporting_pom().verify_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_PTE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EN_ZN_155(self):
    #     if Reporting_pom().verify_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_FRAUDE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EN_ZN_156(self):
    #     if Reporting_pom().verify_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_VIPE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Reporting_EN_ZN_157(self):
    #     if Reporting_pom().verify_individual_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_SOE_ABE_PTE_FRAUDE_and_VIPE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_ZN_EN_158(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_number_of_zones_from_report_field1_and_enrollment_from_report_field2_texts_are_visible_on_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_ZN_EN_159(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_160(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_161(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_162(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_163(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_ZN_EN_164(self):
    #     if Reporting_pom().\
    #             for_number_of_zones_by_enrollment_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_ZN_EN_165(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_and_that_of_Select_zone_filter_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_166(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_167(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_Select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_168(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_Generate_Report_button_is_visible_and_clickable_text_and_chart_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_ZN_EN_169(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_170(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_171(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_172(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_select_all_button_in_group_filter_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_ZN_EN_173(self):
    #     if Reporting_pom().\
    #             for_number_of_zones_by_enrollment_verify_selected_group_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_174(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_175(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_176(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_click_on_select_all_button_in_group_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_177(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_178(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_ZN_EN_179(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_ZN_EN_180(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_ZN_EN_181(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_ZN_EN_182(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_ZN_EN_183(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_ZN_EN_184(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_select_all_button_in_zone_filter_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_ZN_EN_185(self):
    #     if Reporting_pom().\
    #             for_number_of_zones_by_enrollment_verify_selected_zone_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_ZN_EN_186(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_ZN_EN_187(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_ZN_EN_188(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_click_on_select_all_button_in_zone_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_ZN_EN_189(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_ZN_EN_190(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_ZN_EN_191(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_ZN_EN_192(self):
    #     if Reporting_pom().for_number_of_zones_by_enrollment_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_ZN_EN_193(self):
    #     if Reporting_pom().verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_ZN_EN_194(self):
    #     if Reporting_pom().verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_ZN_EN_195(self):
    #     if Reporting_pom().verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_ZN_EN_196(self):
    #     if Reporting_pom().verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_ZN_EN_197(self):
    #     if Reporting_pom().verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_ZN_EN_198(self):
    #     if Reporting_pom().verify_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_ZN_EN_199(self):
    #     if Reporting_pom().verify_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_ZN_EN_200(self):
    #     if Reporting_pom().verify_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_ZN_EN_201(self):
    #     if Reporting_pom().verify_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_ZN_EN_202(self):
    #     if Reporting_pom().verify_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Reporting_ZN_EN_203(self):
    #     if Reporting_pom().verify_individual_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_204(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_day_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_205(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_day_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_206(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_day_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_207(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_day_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_208(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_day_of_week_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_209(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_day_of_week_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_210(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_day_of_week_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_211(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_day_of_week_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_212(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_week_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_213(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_week_with_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_214(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_week_with_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_215(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_hour_of_week_with_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_216(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_zone_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_all_zones_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_217(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_zone_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_all_zones_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_218(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_zone_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_all_zones_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.skip
    # def test_TC_Reporting_VS_HD_219(self):
    #     if Reporting_pom().verify_report_for_number_of_visitors_by_zone_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_all_zones_selected_by_default():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_EN_220(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_number_of_events_from_report_field1_and_enrollment_from_report_field2_texts_are_visible_on_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_EN_221(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_boxes_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_222(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_223(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_224(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_225(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_EN_226(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_EN_227(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_228(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_229(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_EN_230(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_231(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_232(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_233(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_EN_234(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_selected_group_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_235(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_236(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_237(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_238(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_239(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_EN_240(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_EN_241(self):
    #     if Reporting_Events_pom().For_number_of_events_by_enrollment_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HD_242(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_number_of_events_from_report_field1_and_hour_of_day_from_report_field2_texts_are_visible_on_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HD_243(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_boxes_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_244(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_245(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_246(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_247(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HD_248(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HD_249(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_and_that_of_Select_zone_filter_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_250(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_251(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_Select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_252(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_Generate_Report_button_is_visible_and_clickable_text_and_chart_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HD_253(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_254(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_255(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_256(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_select_all_button_in_group_filter_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HD_257(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_selected_group_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_258(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_259(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_260(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_click_on_select_all_button_in_group_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_261(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_262(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_263(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HD_264(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HD_265(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_266(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_267(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_268(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_select_all_button_in_zone_filter_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HD_269(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_selected_zone_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_270(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_271(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_272(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_click_on_select_all_button_in_zone_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_273(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_274(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HD_275(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HD_276(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_day_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_DW_277(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_number_of_events_from_report_field1_and_day_of_week_from_report_field2_texts_are_visible_on_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_DW_278(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_boxes_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_279(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_280(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_281(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_282(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_DW_283(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_DW_284(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_and_that_of_Select_zone_filter_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_285(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_286(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_Select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_287(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_Generate_Report_button_is_visible_and_clickable_text_and_chart_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_DW_288(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_289(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_290(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_291(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_select_all_button_in_group_filter_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_DW_292(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_selected_group_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_293(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_294(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_295(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_click_on_select_all_button_in_group_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_296(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_297(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_298(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_DW_299(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_DW_300(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_301(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_302(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_303(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_select_all_button_in_zone_filter_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_DW_304(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_selected_zone_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_305(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_306(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_307(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_click_on_select_all_button_in_zone_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_308(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_309(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_DW_310(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_DW_311(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_day_of_week_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HW_312(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_number_of_events_from_report_field1_and_hour_of_week_from_report_field2_texts_are_visible_on_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HW_313(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_boxes_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_314(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_315(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_316(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_317(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HW_318(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HW_319(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_and_that_of_Select_zone_filter_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_320(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_321(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_Select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_322(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_Generate_Report_button_is_visible_and_clickable_text_and_chart_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HW_323(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_324(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_325(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_326(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_select_all_button_in_group_filter_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HW_327(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_selected_group_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_328(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_329(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_330(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_click_on_select_all_button_in_group_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_331(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_332(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_333(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HW_334(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HW_335(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_336(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_337(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_338(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_select_all_button_in_zone_filter_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HW_339(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_selected_zone_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_340(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_341(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_342(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_click_on_select_all_button_in_zone_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_343(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_344(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_HW_345(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_HW_346(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_hour_of_week_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_ZN_347(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_number_of_events_from_report_field1_and_zone_from_report_field2_texts_are_visible_on_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_ZN_348(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_boxes_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_349(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_350(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_351(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_352(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_ZN_353(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_ZN_354(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_355(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_356(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_ZN_357(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_358(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_359(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_360(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_ZN_361(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_selected_group_list_title_and_default_text_below_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_362(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_363(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_364(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_365(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_366(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_Reporting_EV_ZN_367(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_Reporting_EV_ZN_368(self):
    #     if Reporting_Events_pom(
    #             ).For_number_of_events_by_zone_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_EN_369(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_enrollment_with_default_dates_1_month_and_with_group_selected_as_SOE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_EN_370(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_enrollment_with_default_dates_1_month_and_with_group_selected_as_ABE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_EN_371(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_enrollment_with_default_dates_1_month_and_with_group_selected_as_PTE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_EN_372(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_enrollment_with_default_dates_1_month_and_with_group_selected_as_FRAUDE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_EN_373(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_enrollment_with_default_dates_1_month_and_with_group_selected_as_VIPE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_EN_374(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_SOE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_EN_375(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_ABE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_EN_376(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_PTE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_EN_377(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_FRAUDE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_EN_378(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_VIPE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Reporting_EV_EN_379(self):
    #     if Reporting_Events_pom(
    #             ).verify_individual_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_SOE_ABE_PTE_FRAUDE_and_VIPE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HD_380(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_day_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HD_381(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_day_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HD_382(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_day_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HD_383(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_day_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HD_384(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_day_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HD_385(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HD_386(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HD_387(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HD_388(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HD_389(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Reporting_EV_HD_390(self):
    #     if Reporting_Events_pom(
    #             ).verify_individual_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_DW_391(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_day_of_week_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_DW_392(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_day_of_week_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_DW_393(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_day_of_week_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_DW_394(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_day_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_DW_395(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_day_of_week_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_DW_396(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_DW_397(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_DW_398(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_DW_399(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_DW_400(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Reporting_EV_DW_401(self):
    #     if Reporting_Events_pom(
    #             ).verify_individual_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HW_402(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HW_403(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HW_404(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HW_405(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HW_406(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HW_407(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HW_408(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HW_409(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HW_410(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_HW_411(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Reporting_EV_HW_412(self):
    #     if Reporting_Events_pom(
    #             ).verify_individual_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_ZN_413(self):
    #     if Reporting_Events_pom().verify_report_for_number_of_events_by_zone_with_default_dates_1_month_and_with_group_selected_as_SOE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_ZN_414(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_zone_with_default_dates_1_month_and_with_group_selected_as_ABE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_ZN_415(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_zone_with_default_dates_1_month_and_with_group_selected_as_PTE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_ZN_416(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_zone_with_default_dates_1_month_and_with_group_selected_as_FRAUDE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_ZN_417(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_zone_with_default_dates_1_month_and_with_group_selected_as_VIPE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_ZN_418(self):
    #     if Reporting_Events_pom(
    #             ).verify_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_SOE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_ZN_419(self):
    #     if Reporting_Events_pom().verify_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_ABE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_ZN_420(self):
    #     if Reporting_Events_pom().verify_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_PTE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_ZN_421(self):
    #     if Reporting_Events_pom().verify_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_FRAUDE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_Reporting_EV_ZN_422(self):
    #     if Reporting_Events_pom().verify_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_VIPE():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Reporting_EV_ZN_423(self):
    #     if Reporting_Events_pom().verify_individual_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_SOE_ABE_PTE_FRAUDE_and_VIPE():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_TC_Reporting_424(self):
    #     if Reporting_pom().\
    #             verify_Reporting_module_is_not_visible_in_dashboard_menu_without_having_permission_in_local():
    #         assert True
    #     else:
    #         assert False

import configparser
from pathlib import Path

filepath = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_INI\\Reporting.ini"
print("configure filepath: ", filepath)


class Reporting_read_ini:
    def __init__(self):
        try:
            self.config = configparser.RawConfigParser()
            self.config.read(filepath)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print(ex)

    def get_core_username(self):
        try:
            core_username = self.common_test_data_config.get("Login_Logout_Data", "username")
            print("core username:", core_username)
            return core_username
        except Exception as ex:
            print(ex)

    def get_core_password(self):
        try:
            core_password = self.common_test_data_config.get("Login_Logout_Data", "password")
            print("core password: ", core_password)
            return core_password
        except Exception as ex:
            print(ex)

    def get_dashboard_menu_items_by_xpath(self):
        try:
            dashboard_menu_items = self.config.get("Reporting", "dashboard_menu_items_by_xpath")
            print("dashboard items: ", dashboard_menu_items)
            return dashboard_menu_items
        except Exception as ex:
            print(ex)

    def get_total_events_count_on_events_panel_by_xpath(self):
        try:
            total_events_count_on_events_panel_by_xpath = (
                self.config.get("Reporting", "total_events_count_on_events_panel_by_xpath"))
            print("total_events_count_on_events_panel_by_xpath: ", total_events_count_on_events_panel_by_xpath)
            return total_events_count_on_events_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_reporting_module(self):
        try:
            reporting_module_name = self.common_test_data_config.get("Reporting_Data", "reporting_module")
            print("reporting module name: ", reporting_module_name)
            return reporting_module_name
        except Exception as ex:
            print(ex)

    def get_events_by_zone_counts(self):
        try:
            events_by_zone_counts = self.common_test_data_config.get("Reporting_Data", "events_by_zone_counts")
            print("events_by_zone_counts: ", events_by_zone_counts)
            return events_by_zone_counts
        except Exception as ex:
            print(ex)

    def events_by_enrollment_count(self):
        try:
            events_by_enrollment_count = self.common_test_data_config.get("Reporting_Data", "events_by_enrollment_count")
            print("events_by_enrollment_count: ", events_by_enrollment_count)
            return events_by_enrollment_count
        except Exception as ex:
            print(ex)

    def get_reporting_module_by_xpath(self):
        try:
            reporting_module = self.config.get("Reporting", "reporting_module_by_xpath")
            print("reporting module: ", reporting_module)
            return reporting_module
        except Exception as ex:
            print(ex)

    def get_total_enrollments_count_on_enrollments_panel_by_xpath(self):
        try:
            total_enrollments_count_on_enrollments_panel_by_xpath = (
                self.config.get("Reporting", "total_enrollments_count_on_enrollments_panel_by_xpath"))
            print("total_enrollments_count_on_enrollments_panel_by_xpath: ",
                  total_enrollments_count_on_enrollments_panel_by_xpath)
            return total_enrollments_count_on_enrollments_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_search_dropdown_on_events_panel_by_xpath(self):
        try:
            search_dropdown_on_events_panel_by_xpath = self.config.get("Reporting",
                                                                       "search_dropdown_on_events_panel_by_xpath")
            print("search_dropdown_on_events_panel_by_xpath: ", search_dropdown_on_events_panel_by_xpath)
            return search_dropdown_on_events_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_org_hierarchy_selection_btn_on_event_search_by_xpath(self):
        try:
            org_hierarchy_selection_btn_on_event_search_by_xpath = (
                self.config.get("Reporting", "org_hierarchy_selection_btn_on_event_search_by_xpath"))
            print("org_hierarchy_selection_btn_on_event_search_by_xpath: ",
                  org_hierarchy_selection_btn_on_event_search_by_xpath)
            return org_hierarchy_selection_btn_on_event_search_by_xpath
        except Exception as ex:
            print(ex)

    def get_regions_text_list_by_xpath(self):
        try:
            regions_text_list_by_xpath = (self.config.get("Reporting", "regions_text_list_by_xpath"))
            print("regions_text_list_by_xpath: ", regions_text_list_by_xpath)
            return regions_text_list_by_xpath
        except Exception as ex:
            print(ex)

    def get_region_checkboxes_by_xpath(self):
        try:
            region_checkboxes_by_xpath = (self.config.get("Reporting", "region_checkboxes_by_xpath"))
            print("region_checkboxes_by_xpath: ", region_checkboxes_by_xpath)
            return region_checkboxes_by_xpath
        except Exception as ex:
            print(ex)

    def get_save_button_on_org_hierarchy_by_xpath(self):
        try:
            save_button_on_org_hierarchy_by_xpath = (self.config.get("Reporting",
                                                                     "save_button_on_org_hierarchy_by_xpath"))
            print("save_button_on_org_hierarchy_by_xpath: ", save_button_on_org_hierarchy_by_xpath)
            return save_button_on_org_hierarchy_by_xpath
        except Exception as ex:
            print(ex)

    def get_events_by_enrollments_count_on_reporting_by_xpath(self):
        try:
            events_by_enrollments_count_on_reporting_by_xpath = (self.config.get("Reporting",
                                                                     "events_by_enrollments_count_on_reporting_by_xpath"))
            print("events_by_enrollments_count_on_reporting_by_xpath: ", events_by_enrollments_count_on_reporting_by_xpath)
            return events_by_enrollments_count_on_reporting_by_xpath
        except Exception as ex:
            print(ex)

    def get_search_btn_on_search_dropdown_on_events_panel_by_xpath(self):
        try:
            search_btn_on_search_dropdown_on_events_panel_by_xpath = \
                (self.config.get("Reporting", "search_btn_on_search_dropdown_on_events_panel_by_xpath"))
            print("search_btn_on_search_dropdown_on_events_panel_by_xpath: ",
                  search_btn_on_search_dropdown_on_events_panel_by_xpath)
            return search_btn_on_search_dropdown_on_events_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_search_btn_on_search_dropdown_on_enrollments_panel_by_xpath(self):
        try:
            search_btn_on_search_dropdown_on_enrollments_panel_by_xpath = \
                (self.config.get("Reporting", "search_btn_on_search_dropdown_on_enrollments_panel_by_xpath"))
            print("search_btn_on_search_dropdown_on_enrollments_panel_by_xpath: ",
                  search_btn_on_search_dropdown_on_enrollments_panel_by_xpath)
            return search_btn_on_search_dropdown_on_enrollments_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_enrollments_by_zone_count(self):
        try:
            enrollments_by_zone_count = self.common_test_data_config.get("Reporting_Data", "enrollments_by_zone_count")
            print("expected enrollments_by_zone_count: ", enrollments_by_zone_count)
            return enrollments_by_zone_count
        except Exception as ex:
            print(ex)

    def get_zones_by_enrollment_count(self):
        try:
            zones_by_enrollment_count = self.common_test_data_config.get("Reporting_Data", "zones_by_enrollment_count")
            print("expected zones_by_enrollment_count: ", zones_by_enrollment_count)
            return zones_by_enrollment_count
        except Exception as ex:
            print(ex)

    def get_reporting_panel_heading_by_xpath(self):
        try:
            reporting_panel_heading = self.config.get("Reporting", "reporting_panel_heading_by_xpath")
            print("reporting panel heading: ", reporting_panel_heading)
            return reporting_panel_heading
        except Exception as ex:
            print(ex)

    def get_search_dropdown_on_enrollments_panel_by_xpath(self):
        try:
            search_dropdown_on_enrollments_panel_by_xpath = (
                self.config.get("Reporting", "search_dropdown_on_enrollments_panel_by_xpath"))
            print("search_dropdown_on_enrollments_panel_by_xpath: ", search_dropdown_on_enrollments_panel_by_xpath)
            return search_dropdown_on_enrollments_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_close_panel_button_by_xpath(self):
        try:
            close_panel_button = self.config.get("Reporting", "close_panel_button_by_xpath")
            print("Close Panel button: ", close_panel_button)
            return close_panel_button
        except Exception as ex:
            print(ex)

    def get_report_selection_text_on_heading_by_xpath(self):
        try:
            report_selection_text_on_heading = self.config.get("Reporting", "report_selection_text_on_heading_by_xpath")
            print("REPORT SELECTION text: ", report_selection_text_on_heading)
            return report_selection_text_on_heading
        except Exception as ex:
            print(ex)

    def get_expected_report_selection_text(self):
        try:
            report_selection_text = self.common_test_data_config.get("Reporting_Data", "report_selection_text")
            print("expected REPORT SELECTION text: ", report_selection_text)
            return report_selection_text
        except Exception as ex:
            print(ex)

    def get_chart_icon_beside_report_selection_text_by_xpath(self):
        try:
            chart_icon_beside_report_selection_text = self.config.get("Reporting", "chart_icon_beside_report_selection_text_by_xpath")
            print("Chart icon: ", chart_icon_beside_report_selection_text)
            return chart_icon_beside_report_selection_text
        except Exception as ex:
            print(ex)

    def get_select_report_criteria_text_by_xpath(self):
        try:
            select_report_criteria_text_by_xpath = self.config.get("Reporting", "select_report_criteria_text_by_xpath")
            print("'Select report criteria:' text: ", select_report_criteria_text_by_xpath)
            return select_report_criteria_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_select_report_criteria_text(self):
        try:
            select_report_criteria_text = self.common_test_data_config.get("Reporting_Data", "select_report_criteria_text")
            print("expected Select report criteria: text: ", select_report_criteria_text)
            return select_report_criteria_text
        except Exception as ex:
            print(ex)

    def get_report_the_text_by_xpath(self):
        try:
            report_the_text_by_xpath = self.config.get("Reporting", "report_the_text_by_xpath")
            print("'Report the' text: ", report_the_text_by_xpath)
            return report_the_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_report_the_text(self):
        try:
            report_the_text = self.common_test_data_config.get("Reporting_Data", "report_the_text")
            print("expected Report the text: ", report_the_text)
            return report_the_text
        except Exception as ex:
            print(ex)

    def get_report_field1_dropdown_by_xpath(self):
        try:
            report_field1_dropdown = self.config.get("Reporting", "report_field1_dropdown_by_xpath")
            print("report field1 dropdown: ", report_field1_dropdown)
            return report_field1_dropdown
        except Exception as ex:
            print(ex)

    def get_report_field1_dropdown_items_by_xpath(self):
        try:
            report_field1_dropdown_items = self.config.get("Reporting", "report_field1_dropdown_items_by_xpath")
            print("report field1 dropdown items: ", report_field1_dropdown_items)
            return report_field1_dropdown_items
        except Exception as ex:
            print(ex)

    def get_expected_report_field_items(self):
        try:
            report_field_items = self.config.get("Reporting", "report_field_items")
            print("expected report field items: ", report_field_items)
            return report_field_items
        except Exception as ex:
            print(ex)

    def get_expected_first_text_from_field1(self):
        try:
            expected_first_text_from_field1 = self.common_test_data_config.get("Reporting_Data", "expected_first_text_from_field1")
            print("expected first text from field1: ", expected_first_text_from_field1)
            return expected_first_text_from_field1
        except Exception as ex:
            print(ex)

    def get_expected_second_text_from_field1(self):
        try:
            expected_second_text_from_field1 = self.common_test_data_config.get("Reporting_Data", "expected_second_text_from_field1")
            print("expected second text from field1: ", expected_second_text_from_field1)
            return expected_second_text_from_field1
        except Exception as ex:
            print(ex)

    def get_expected_third_text_from_field1(self):
        try:
            expected_third_text_from_field1 = self.common_test_data_config.get("Reporting_Data", "expected_third_text_from_field1")
            print("expected third text from field1: ", expected_third_text_from_field1)
            return expected_third_text_from_field1
        except Exception as ex:
            print(ex)

    def get_report_field2_dropdown_for_events_by_xpath(self):
        try:
            report_field2_dropdown = self.config.get("Reporting", "field2_dropdown_for_events_by_xpath")
            print("report field2 dropdown: ", report_field2_dropdown)
            return report_field2_dropdown
        except Exception as ex:
            print(ex)

    def get_report_field2_dropdown_items_for_events_by_xpath(self):
        try:
            report_field2_dropdown_items = self.config.get("Reporting", "field2_dropdown_items_for_events_by_xpath")
            print("expected report field2 items: ", report_field2_dropdown_items)
            return report_field2_dropdown_items
        except Exception as ex:
            print(ex)

    def get_by_text_xpath(self):
        try:
            by_text_xpath = self.config.get("Reporting", "by_text_xpath")
            print("'by' text:" , by_text_xpath)
            return by_text_xpath
        except Exception as ex:
            print(ex)

    def get_expected_by_text(self):
        try:
            expected_by_text = self.common_test_data_config.get("Reporting_Data", "expected_by_text")
            print("expected 'by' text: ", expected_by_text)
            return expected_by_text
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_for_visitors_by_xpath(self):
        try:
            field2_dropdown_for_visitors = self.config.get("Reporting", "field2_dropdown_for_visitors_by_xpath")
            print("field2 dropdown for visitors: ", field2_dropdown_for_visitors)
            return field2_dropdown_for_visitors
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_items_for_visitors_by_xpath(self):
        try:
            field2_dropdown_items_for_visitors = self.config.get("Reporting", "field2_dropdown_items_for_visitors_by_xpath")
            print("field2 dropdown items for visitors: ", field2_dropdown_items_for_visitors)
            return field2_dropdown_items_for_visitors
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_for_enrollments_by_xpath(self):
        try:
            field2_dropdown_for_enrollments = self.config.get("Reporting", "field2_dropdown_for_enrollments_by_xpath")
            print("field2 dropdown for enrollments: ", field2_dropdown_for_enrollments)
            return field2_dropdown_for_enrollments
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_items_for_enrollments_by_xpath(self):
        try:
            field2_dropdown_items_for_enrollments = self.config.get("Reporting", "field2_dropdown_items_for_enrollments_by_xpath")
            print("field2 dropdown items for enrollments: ", field2_dropdown_items_for_enrollments)
            return field2_dropdown_items_for_enrollments
        except Exception as ex:
            print(ex)

    def get_expected_enrollment_text_from_field2(self):
        try:
            expected_enrollment_text_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_enrollment_text_from_field2")
            print("expected enrollment text from field2: ", expected_enrollment_text_from_field2)
            return expected_enrollment_text_from_field2
        except Exception as ex:
            print(ex)

    def get_expected_first_text_from_field2(self):
        try:
            expected_first_text_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_first_text_from_field2")
            print("expected first text from field2: ", "expected_first_text_from_field2")
            return expected_first_text_from_field2
        except Exception as ex:
            print(ex)

    def get_expected_second_text_from_field2(self):
        try:
            expected_second_text_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_second_text_from_field2")
            print("expected second text from field2: ", expected_second_text_from_field2)
            return expected_second_text_from_field2
        except Exception as ex:
            print(ex)

    def get_expected_third_text_from_field2(self):
        try:
            expected_third_text_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_third_text_from_field2")
            print("expected third text from field2: ", expected_third_text_from_field2)
            return expected_third_text_from_field2
        except Exception as ex:
            print(ex)

    def get_expected_fourth_text_from_field2(self):
        try:
            expected_fourth_text_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_fourth_text_from_field2")
            print("expected fourth text from field2: ", expected_fourth_text_from_field2)
            return expected_fourth_text_from_field2
        except Exception as ex:
            print(ex)

    def get_date_range_text_by_xpath(self):
        try:
            date_range_text = self.config.get("Reporting", "date_range_text_by_xpath")
            print("date range text: ", date_range_text)
            return date_range_text
        except Exception as ex:
            print(ex)

    def get_expected_date_range_text(self):
        try:
            expected_date_range_text = self.common_test_data_config.get("Reporting_Data", "expected_date_range_text")
            print("expected date range text: ", expected_date_range_text)
            return expected_date_range_text
        except Exception as ex:
            print(ex)

    def get_date_and_time_range_text_by_xpath(self):
        try:
            date_and_time_range_text = self.config.get("Reporting", "date_and_time_range_text_by_xpath")
            print("date & time range text: ", date_and_time_range_text)
            return date_and_time_range_text
        except Exception as ex:
            print(ex)

    def get_expected_date_and_time_range_text(self):
        try:
            expected_date_and_time_range_text = self.common_test_data_config.get("Reporting_Data", "expected_date_and_time_range_text")
            print("expected date & time range text: ", expected_date_and_time_range_text)
            return expected_date_and_time_range_text
        except Exception as ex:
            print(ex)

    def get_between_text_by_xpath(self):
        try:
            between_text_by_xpath = self.config.get("Reporting", "between_text_by_xpath")
            print("between text: ", between_text_by_xpath)
            return between_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_between_text(self):
        try:
            expected_between_text = self.common_test_data_config.get("Reporting_Data", "expected_between_text")
            print("expected between text: ", expected_between_text)
            return expected_between_text
        except Exception as ex:
            print(ex)

    def get_to_text_by_xpath(self):
        try:
            to_text_by_xpath = self.config.get("Reporting", "to_text_by_xpath")
            print("to text: ", to_text_by_xpath)
            return to_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_to_text(self):
        try:
            expected_to_text = self.common_test_data_config.get("Reporting_Data", "expected_to_text")
            print("expected to text: ", expected_to_text)
            return expected_to_text
        except Exception as ex:
            print(ex)

    def get_horizontal_line_below_calenders_by_xpath(self):
        try:
            horizontal_line_below_calenders_by_xpath = self.config.get("Reporting", "horizontal_line_below_calenders_by_xpath")
            print("horizontal line below calenders: ", horizontal_line_below_calenders_by_xpath)
            return horizontal_line_below_calenders_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_horizontal_line_below_calenders(self):
        try:
            expected_horizontal_line_below_calenders = self.common_test_data_config.get("Reporting_Data", "expected_horizontal_line_below_calenders")
            print("expected horizontal line below calenders: ", expected_horizontal_line_below_calenders)
            return expected_horizontal_line_below_calenders
        except Exception as ex:
            print(ex)

    def get_start_date_calender_box_by_xpath(self):
        try:
            start_date_calender_box_by_xpath = self.config.get("Reporting", "start_date_calender_box_by_xpath")
            print("start date calender box: ", start_date_calender_box_by_xpath)
            return start_date_calender_box_by_xpath
        except Exception as ex:
            print(ex)

    def get_start_date_checkbox_by_xpath(self):
        try:
            start_date_checkbox_by_xpath = self.config.get("Reporting", "start_date_checkbox_by_xpath")
            print("start date checkbox: ", start_date_checkbox_by_xpath)
            return start_date_checkbox_by_xpath
        except Exception as ex:
            print(ex)

    def get_end_date_calender_box_by_xpath(self):
        try:
            end_date_calender_box_by_xpath = self.config.get("Reporting", "end_date_calender_box_by_xpath")
            print("end date calender box: ", end_date_calender_box_by_xpath)
            return end_date_calender_box_by_xpath
        except Exception as ex:
            print(ex)

    def get_end_date_checkbox_by_xpath(self):
        try:
            end_date_checkbox_by_xpath = self.config.get("Reporting", "end_date_checkbox_by_xpath")
            print("end date checkbox: ", end_date_checkbox_by_xpath)
            return end_date_checkbox_by_xpath
        except Exception as ex:
            print(ex)

    def get_generate_report_button_by_xpath(self):
        try:
            generate_report_button_by_xpath = self.config.get("Reporting", "generate_report_button_by_xpath")
            print("generate report button: ", generate_report_button_by_xpath)
            return generate_report_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_new_reporting_panel_heading(self):
        try:
            new_reporting_panel_heading_for_visitors_by_hour_of_day = self.config.get("Reporting", "new_reporting_panel_heading_for_visitors_by_hour_of_day")
            print("new reporting panel heading: ", new_reporting_panel_heading_for_visitors_by_hour_of_day)
            return new_reporting_panel_heading_for_visitors_by_hour_of_day
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_for_zones_by_xpath(self):
        try:
            field2_dropdown_for_zones_by_xpath = self.config.get("Reporting", "field2_dropdown_for_zones_by_xpath")
            print("field2 dropdown for zones: ", field2_dropdown_for_zones_by_xpath)
            return field2_dropdown_for_zones_by_xpath
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_items_for_zones_by_xpath(self):
        try:
            field2_dropdown_items_for_zones_by_xpath = self.config.get("Reporting", "field2_dropdown_items_for_zones_by_xpath")
            print("field2 dropdown items for zones: ", field2_dropdown_items_for_zones_by_xpath)
            return field2_dropdown_items_for_zones_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_fourth_text_from_field1(self):
        try:
            expected_fourth_text_from_field1 = self.common_test_data_config.get("Reporting_Data", "expected_fourth_text_from_field1")
            print("expected fourth text from field1: ", expected_fourth_text_from_field1)
            return expected_fourth_text_from_field1
        except Exception as ex:
            print(ex)

    def get_expected_value_for_zones_by_enrollment_from_field2(self):
        try:
            expected_value_for_zones_by_enrollment_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_value_for_zones_by_enrollment_from_field2")
            print("expected value for zones by enrollment from field2: ", expected_value_for_zones_by_enrollment_from_field2)
            return expected_value_for_zones_by_enrollment_from_field2
        except Exception as ex:
            print(ex)

    def get_body_by_xpath(self):
        try:
            body_by_xpath = self.config.get("Reporting", "body_by_xpath")
            print("body: ", body_by_xpath)
            return body_by_xpath
        except Exception as ex:
            print(ex)

    def get_close_all_panels_button_on_dashboard_by_xpath(self):
        try:
            close_all_panels_button_on_dashboard_by_xpath = self.config.get("Reporting",
                                                                            "close_all_panels_button_on_dashboard_by_xpath")
            print("Close all panels button on dashboard: ", close_all_panels_button_on_dashboard_by_xpath)
            return close_all_panels_button_on_dashboard_by_xpath
        except Exception as ex:
            print(ex)

    def get_abe_enrollment_group(self):
        try:
            get_abe_enrollment_group = self.common_test_data_config.get("Notifier_Data", "abe_enrollment_group")
            print("get_abe_enrollment_group: ", get_abe_enrollment_group)
            return get_abe_enrollment_group
        except Exception as ex:
            print(ex)

    def get_vipe_enrollment_group(self):
        try:
            get_vipe_enrollment_group = self.common_test_data_config.get("Notifier_Data", "vipe_enrollment_group")
            print("get_vipe_enrollment_group: ", get_vipe_enrollment_group)
            return get_vipe_enrollment_group
        except Exception as ex:
            print(ex)

    def get_soe_enrollment_group(self):
        try:
            get_soe_enrollment_group = self.common_test_data_config.get("Notifier_Data", "soe_enrollment_group")
            print("get_soe_enrollment_group: ", get_soe_enrollment_group)
            return get_soe_enrollment_group
        except Exception as ex:
            print(ex)

    def get_pte_enrollment_group(self):
        try:
            get_pte_enrollment_group = self.common_test_data_config.get("Notifier_Data", "pte_enrollment_group")
            print("get_pte_enrollment_group: ", get_pte_enrollment_group)
            return get_pte_enrollment_group
        except Exception as ex:
            print(ex)

    def get_fraude_enrollment_group(self):
        try:
            get_fraude_enrollment_group = self.common_test_data_config.get("Notifier_Data", "fraude_enrollment_group")
            print("get_fraude_enrollment_group: ", get_fraude_enrollment_group)
            return get_fraude_enrollment_group
        except Exception as ex:
            print(ex)

    def get_camera0(self):
        try:
            get_camera0 = self.common_test_data_config.get("Notifier_Data", "camera0")
            print("get_camera0: ", get_camera0)
            return get_camera0
        except Exception as ex:
            print(ex)

    def get_camera1(self):
        try:
            get_camera1 = self.common_test_data_config.get("Notifier_Data", "camera1")
            print("get_camera1: ", get_camera1)
            return get_camera1
        except Exception as ex:
            print(ex)

    def get_zones(self):
        try:
            zones = self.common_test_data_config.get("Notifier_Data", "zones")
            print("zones: ", zones)
            return zones
        except Exception as ex:
            print(ex)
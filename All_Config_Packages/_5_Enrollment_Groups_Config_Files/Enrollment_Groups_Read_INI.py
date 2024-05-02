import configparser
from pathlib import Path


class Read_Enrollment_Groups_Components:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.common_test_data_config = configparser.RawConfigParser()
        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\All_Test_Data\\5_Enrollment_Groups_Module\\Data_From_INI\\Enrollment_Groups.ini'
            self.config.read(portal_menu_ini_file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def close_all_panel_list_in_tags(self):
        try:
            close_all_panel_list = self.config.get("LOCATORS", "close_all_panel_list_in_tags")
            return close_all_panel_list
        except Exception as ex:
            print("close_all_panel_list : ", ex)

    def get_enrollment_group_name(self):
        try:
            enrollment_group_name = self.common_test_data_config.get("system_level_test_Data", "enrollment_group_name")
            return enrollment_group_name
        except Exception as ex:
            print(ex)

    def eg_extends_menu_btns_by_xpath(self):
        try:
            eg_extends_menu_btns_by_xpath = self.config.get("LOCATORS", "eg_extends_menu_btns_by_xpath")
            return eg_extends_menu_btns_by_xpath
        except Exception as ex:
            print(ex)

    def eg_details_btns_by_xpath(self):
        try:
            eg_details_btns_by_xpath = self.config.get("LOCATORS", "eg_details_btns_by_xpath")
            return eg_details_btns_by_xpath
        except Exception as ex:
            print(ex)

    def new_name_field_data(self):
        try:
            new_name_field_data = self.common_test_data_config.get("Enrollment_Groups_Data", "new_name")
            return new_name_field_data
        except Exception as ex:
            print(ex)

    def description_field_new_data(self):
        try:
            description_field_new_data = self.common_test_data_config.get("Enrollment_Groups_Data", "new_description")
            return description_field_new_data
        except Exception as ex:
            print(ex)

    def serious_offender_high(self):
        try:
            serious_offender_high = self.common_test_data_config.get("Enrollment_Groups_Data", "serious_offender_high")
            return serious_offender_high
        except Exception as ex:
            print(ex)

    def serious_offender_low(self):
        try:
            serious_offender_low = self.common_test_data_config.get("Enrollment_Groups_Data", "serious_offender_low")
            return serious_offender_low
        except Exception as ex:
            print(ex)

    def get_number_of_egs_by_xpath(self):
        try:
            number_of_egs_by_xpath = self.config.get("LOCATORS", "number_of_egs_by_xpath")
            return number_of_egs_by_xpath
        except Exception as ex:
            print(ex)

    def get_total_number_of_egs(self):
        try:
            total_number_of_egs = self.common_test_data_config.get("Enrollment_Groups_Data", "total_number_of_egs")
            return total_number_of_egs
        except Exception as ex:
            print(ex)

    def link_eg1_to_ng1(self):
        try:
            link_eg1_to_ng1 = self.common_test_data_config.get("system_level_test_Data", "link_eg1_to_ng1")
            return link_eg1_to_ng1
        except Exception as ex:
            print(ex)

    def link_ng1_to_eg1(self):
        try:
            link_ng1_to_eg1 = self.common_test_data_config.get("system_level_test_Data", "link_ng1_to_eg1")
            return link_ng1_to_eg1
        except Exception as ex:
            print(ex)

    def name_placeholder_on_ng_panel_by_xpath(self):
        try:
            name_placeholder_on_ng_panel_by_xpath = self.config.get("LOCATORS", "name_placeholder_on_ng_panel_by_xpath")
            return name_placeholder_on_ng_panel_by_xpath
        except Exception as ex:
            print(ex)

    def enrollment_icon_btn_to_view_linked_enrollments_by_xpath(self):
        try:
            enrollment_icon_btn_to_view_linked_enrollments_by_xpath = self.config.get("LOCATORS", "enrollment_icon_btn_to_view_linked_enrollments_by_xpath")
            return enrollment_icon_btn_to_view_linked_enrollments_by_xpath
        except Exception as ex:
            print(ex)

    def description_placeholder_on_ng_panel_by_xpath(self):
        try:
            description_placeholder_on_ng_panel_by_xpath = self.config.get("LOCATORS", "description_placeholder_on_ng_panel_by_xpath")
            return description_placeholder_on_ng_panel_by_xpath
        except Exception as ex:
            print(ex)

    def enrollment_groups_title_by_xpath(self):
        try:
            enrollment_groups_title_by_xpath = self.config.get("LOCATORS", "enrollment_groups_title_by_xpath")
            return enrollment_groups_title_by_xpath
        except Exception as ex:
            print("enrollment_groups_title_by_xpath : ", ex)

    def get_filter_btn_on_notification_groups_panel_by_xpath(self):
        try:
            filter_btn_on_notification_groups_panel_by_xpath = self.config.get("LOCATORS", "filter_btn_on_notification_groups_panel_by_xpath")
            return filter_btn_on_notification_groups_panel_by_xpath
        except Exception as ex:
            print(ex)

    def notification_icon_btns_on_eg_panel(self):
        try:
            notification_icon_btns_on_eg_panel = self.config.get("LOCATORS", "notification_icon_btns_on_eg_panel")
            return notification_icon_btns_on_eg_panel
        except Exception as ex:
            print(ex)

    def linked_notification_groups_list_by_xpath(self):
        try:
            linked_notification_groups_list_by_xpath = self.config.get("LOCATORS", "linked_notification_groups_list_by_xpath")
            return linked_notification_groups_list_by_xpath
        except Exception as ex:
            print(ex)

    def linked_ng_checkbox_by_xpath(self):
        try:
            linked_ng_checkbox_by_xpath = self.config.get("LOCATORS", "linked_ng_checkbox_by_xpath")
            return linked_ng_checkbox_by_xpath
        except Exception as ex:
            print(ex)

    def remove_from_eg_on_ng_panel_by_xpath(self):
        try:
            remove_from_eg_on_ng_panel_by_xpath = self.config.get("LOCATORS", "remove_from_eg_on_ng_panel_by_xpath")
            return remove_from_eg_on_ng_panel_by_xpath
        except Exception as ex:
            print(ex)
    def enrollment_groups_button_by_xpath(self):
        try:
            enrollment_groups_button_by_xpath = self.config.get("LOCATORS", "enrollment_groups_button_by_xpath")
            return enrollment_groups_button_by_xpath
        except Exception as ex:
            print("enrollment_groups_button_by_xpath : ", ex)

    def enrollment_group_title_validation_text(self):
        try:
            enrollment_group_title_validation_text = self.common_test_data_config.get("Enrollment_Groups_Data", "enrollment_group_title_validation_text")
            return enrollment_group_title_validation_text
        except Exception as ex:
            print("enrollment_group_title_validation_text : ", ex)

    def action_dropdown_button_by_xpath(self):
        try:
            action_dropdown_button_by_xpath = self.config.get("LOCATORS", "action_dropdown_button_by_xpath")
            return action_dropdown_button_by_xpath
        except Exception as ex:
            print("action_dropdown_menu_by_xpath : ", ex)

    def create_enrollment_group_button_by_xpath(self):
        try:
            create_enrollment_group_btn_by_xpath = self.config.get("LOCATORS", "create_enrollment_group_btn_by_xpath")
            return create_enrollment_group_btn_by_xpath
        except Exception as ex:
            print("create_enrollment_group_btn_by_xpath : ", ex)

    def delete_button_by_xpath(self):
        try:
            delete_button_by_xpath = self.config.get("LOCATORS", "delete_button_by_xpath")
            return delete_button_by_xpath
        except Exception as ex:
            print("delete_button_by_xpath : ", ex)

    def refresh_button_by_xpath(self):
        try:
            refresh_button_by_xpath = self.config.get("LOCATORS", "refresh_button_by_xpath")
            return refresh_button_by_xpath
        except Exception as ex:
            print("refresh_button_by_xpath : ", ex)

    def enrollment_groups_details_validation_text(self):
        try:
            enrollment_groups_details_validation_text = self.common_test_data_config.get("Enrollment_Groups_Data", "enrollment_groups_details_validation_text")
            return enrollment_groups_details_validation_text
        except Exception as ex:
            print("enrollment_groups_details_validation_text : ", ex)

    def enrollment_group_details_by_xpath(self):
        try:
            enrollment_group_details_by_xpath = self.config.get("LOCATORS", "enrollment_group_details_by_xpath")
            return enrollment_group_details_by_xpath
        except Exception as ex:
            print("enrollment_group_details_by_xpath : ", ex)

    def enrollment_group_details_sub_title_validation_text(self):
        try:
            enrollment_group_details_sub_title_validation_text = self.common_test_data_config.get("Enrollment_Groups_Data", "enrollment_group_details_sub_title_validation_text")
            return enrollment_group_details_sub_title_validation_text
        except Exception as ex:
            print("enrollment_group_details_sub_title_validation_text : ", ex)

    def enrollment_group_details_sub_title_by_xpath(self):
        try:
            enrollment_group_details_sub_title_by_xpath = self.config \
                .get("LOCATORS", "enrollment_group_details_sub_title_by_xpath")
            return enrollment_group_details_sub_title_by_xpath
        except Exception as ex:
            print("enrollment_group_details_sub_title_by_xpath : ", ex)

    def cancel_button_validation_text(self):
        try:
            cancel_button_validation_text = self.common_test_data_config.get("Enrollment_Groups_Data", "cancel_button_validation_text")
            return cancel_button_validation_text
        except Exception as ex:
            print("cancel_button_validation_text : ", ex)

    def cancel_button_by_xpath(self):
        try:
            cancel_button_by_xpath = self.config \
                .get("LOCATORS", "cancel_button_by_xpath")
            return cancel_button_by_xpath
        except Exception as ex:
            print("cancel_button_by_xpath : ", ex)

    def save_button_validation_text(self):
        try:
            save_button_validation_text = self.common_test_data_config.get("Enrollment_Groups_Data", "save_button_validation_text")
            return save_button_validation_text
        except Exception as ex:
            print("save_button_validation_text : ", ex)

    def save_button_by_xpath(self):
        try:
            save_button_by_xpath = self.config \
                .get("LOCATORS", "save_button_by_xpath")
            return save_button_by_xpath
        except Exception as ex:
            print("save_button_by_xpath : ", ex)

    def name_field_validation_text(self):
        try:
            name_field_validation_text = self.common_test_data_config.get("Enrollment_Groups_Data", "name_field_validation_text")
            return name_field_validation_text
        except Exception as ex:
            print("name_field_validation_text : ", ex)

    def name_field_by_xpath(self):
        try:
            name_field_by_xpath = self.config \
                .get("LOCATORS", "name_field_by_xpath")
            return name_field_by_xpath
        except Exception as ex:
            print("name_field_by_xpath : ", ex)

    def name_field_data(self):
        try:
            name_field_data = self.common_test_data_config.get("Enrollment_Groups_Data", "name")
            return name_field_data
        except Exception as ex:
            print("name_field_data : ", ex)

    def description_field_by_xpath(self):
        try:
            description_field_by_xpath = self.config.get("LOCATORS", "description_field_by_xpath")
            return description_field_by_xpath
        except Exception as ex:
            print("description_field_by_xpath : ", ex)

    def description_title_name_validation(self):
        try:
            description_field_by_xpath = self.config.get("VALIDATION", "description_title_name_validation")
            return description_field_by_xpath
        except Exception as ex:
            print("description_field_by_xpath : ", ex)

    def description_field_data(self):
        try:
            description_field_data = self.common_test_data_config \
                .get("Enrollment_Groups_Data", "description")
            return description_field_data
        except Exception as ex:
            print("description_field_data : ", ex)

    def face_threshold_field_by_xpath(self):
        try:
            face_threshold_field_by_xpath = self.config \
                .get("LOCATORS", "face_threshold_field_by_xpath")
            return face_threshold_field_by_xpath
        except Exception as ex:
            print("face_threshold_field_by_xpath : ", ex)

    def face_threshold_validation_text(self):
        try:
            face_threshold_validation_text = self.common_test_data_config \
                .get("Enrollment_Groups_Data", "face_threshold_validation_text")
            return face_threshold_validation_text
        except Exception as ex:
            print("face_threshold_validation_text : ", ex)

    def face_threshold_field_data(self):
        try:
            face_threshold_field_data = self.common_test_data_config \
                .get("Enrollment_Groups_Data", "face_threshold")
            return face_threshold_field_data
        except Exception as ex:
            print("face_threshold_field_data : ", ex)

    def masked_face_threshold_field_by_xpath(self):
        try:
            masked_face_threshold_field_by_xpath = self.config \
                .get("LOCATORS", "masked_face_threshold_field_by_xpath")
            return masked_face_threshold_field_by_xpath
        except Exception as ex:
            print("masked_face_threshold_field_by_xpath : ", ex)

    def masked_face_threshold_validation_text(self):
        try:
            masked_face_threshold_validation_text = self.common_test_data_config \
                .get("Enrollment_Groups_Data", "masked_face_threshold_validation_text")
            return masked_face_threshold_validation_text
        except Exception as ex:
            print("masked_face_threshold_validation_text : ", ex)

    def masked_face_threshold_data(self):
        try:
            masked_face_threshold_data = self.common_test_data_config \
                .get("Enrollment_Groups_Data", "masked_face_threshold")
            return masked_face_threshold_data
        except Exception as ex:
            print("masked_face_threshold_data : ", ex)

    def serious_offender_drop_down_by_xpath(self):
        try:
            serious_offender_drop_down_by_xpath = self.config.get("LOCATORS", "serious_offender_drop_down_by_xpath")
            return serious_offender_drop_down_by_xpath
        except Exception as ex:
            print("description_field_data : ", ex)

    def supress_duplicate_events_by_xpath(self):
        try:
            supress_duplicate_events_by_xpath = self.config.get("LOCATORS", "supress_duplicate_events_by_xpath")
            return supress_duplicate_events_by_xpath
        except Exception as ex:
            print("supress_duplicate_events_by_xpath : ", ex)

    def validation_error_message_by_xpath(self):
        try:
            validation_error_message_by_xpath = self.config \
                .get("LOCATORS", "validation_error_message_by_xpath")
            return validation_error_message_by_xpath
        except Exception as ex:
            print("validation_error_message_by_xpath : ", ex)

    def enrollment_button_by_xpath(self):
        try:
            enrollment_button_by_xpath = self.config \
                .get("LOCATORS", "enrollment_button_by_xpath")
            return enrollment_button_by_xpath
        except Exception as ex:
            print("enrollment_button_by_xpath : ", ex)

    def notification_groups_button_by_xpath(self):
        try:
            notification_groups_button_by_xpath = self.config \
                .get("LOCATORS", "notification_groups_button_by_xpath")
            return notification_groups_button_by_xpath
        except Exception as ex:
            print("notification_groups_button_by_xpath : ", ex)

    def events_button_by_xpath(self):
        try:
            events_button_by_xpath = self.config \
                .get("LOCATORS", "events_button_by_xpath")
            return events_button_by_xpath
        except Exception as ex:
            print("events_button_by_xpath : ", ex)

    def checkbox_text_by_xpath(self):
        try:
            checkbox_text_by_xpath = self.config \
                .get("LOCATORS", "checkbox_text_by_xpath")
            return checkbox_text_by_xpath
        except Exception as ex:
            print("select_checkbox_by_xpath : ", ex)

    def checkbox_validation_text(self):
        try:
            checkbox_validation_test = self.common_test_data_config \
                .get("Enrollment_Groups_Data", "checkbox_validation_text")
            return checkbox_validation_test
        except Exception as ex:
            print("checkbox_validation_text : ", ex)

    def select_checkbox_by_xpath(self):
        try:
            select_checkbox_by_xpath = self.config \
                .get("LOCATORS", "select_checkbox_by_xpath")
            return select_checkbox_by_xpath
        except Exception as ex:
            print("select_checkbox_by_xpath : ", ex)

    def check_box_list_by_xpath(self):
        try:
            check_box_list_by_xpath = self.config \
                .get("LOCATORS", "check_box_list_by_xpath")
            return check_box_list_by_xpath
        except Exception as ex:
            print("check_box_list_by_xpath : ", ex)

    def success_message_by_xpath(self):
        try:
            success_message_by_xpath = self.config \
                .get("LOCATORS", "success_message_by_xpath")
            return success_message_by_xpath
        except Exception as ex:
            print("success_message_by_xpath : ", ex)

    def success_message_validation_text(self):
        try:
            success_message_validation_text = self.common_test_data_config \
                .get("Enrollment_Groups_Data", "success_message_validation_text")
            return success_message_validation_text
        except Exception as ex:
            print("success_message_validation_text : ", ex)

    def enrollment_in_text_title_by_xpath(self):
        try:
            enrollment_in_text_title_by_xpath = self.config \
                .get("LOCATORS", "enrollment_in_text_title_by_xpath")
            return enrollment_in_text_title_by_xpath
        except Exception as ex:
            print("enrollment_in_text_title_by_xpath : ", ex)

    def linked_enrollments_count_on_icon_by_xpath(self):
        try:
            linked_enrollments_count_on_icon_by_xpath = self.config \
                .get("LOCATORS", "linked_enrollments_count_on_icon_by_xpath")
            return linked_enrollments_count_on_icon_by_xpath
        except Exception as ex:
            print("enrollment_in_text_title_by_xpath : ", ex)

    def list_of_linked_enrollments_by_xpath(self):
        try:
            list_of_linked_enrollments_by_xpath = self.config \
                .get("LOCATORS", "list_of_linked_enrollments_by_xpath")
            return list_of_linked_enrollments_by_xpath
        except Exception as ex:
            print("list_of_linked_enrollments_by_xpath : ", ex)

    def probable_match_events_icon_by_xpath(self):
        try:
            probable_match_events_icon_by_xpath = self.config \
                .get("LOCATORS", "probable_match_events_icon_by_xpath")
            return probable_match_events_icon_by_xpath
        except Exception as ex:
            print("probable_match_events_icon_by_xpath : ", ex)

    def events_list_by_xpath(self):
        try:
            events_list_by_xpath = self.config \
                .get("LOCATORS", "events_list_by_xpath")
            return events_list_by_xpath
        except Exception as ex:
            print("events_list_by_xpath : ", ex)

    def enrollment_in_text_title_validation_text(self):
        try:
            enrollment_in_text_title_validation_text = self.common_test_data_config \
                .get("Enrollment_Groups_Data", "enrollment_in_text_title_validation_text")
            return enrollment_in_text_title_validation_text
        except Exception as ex:
            print("enrollment_in_text_title_validation_text : ", ex)

    def notification_groups_title_by_xpath(self):
        try:
            notification_groups_title_by_xpath = self.config \
                .get("LOCATORS", "notification_groups_title_by_xpath")
            return notification_groups_title_by_xpath
        except Exception as ex:
            print("notification_groups_title_by_xpath : ", ex)

    def notification_groups_title_validation_text(self):
        try:
            notification_groups_title_validation_text = self.common_test_data_config \
                .get("Enrollment_Groups_Data", "enrollment_in_text_title_validation_text")
            return notification_groups_title_validation_text
        except Exception as ex:
            print("notification_groups_title_validation_text : ", ex)

    def events_title_by_xpath(self):
        try:
            events_title_by_xpath = self.config \
                .get("LOCATORS", "events_title_by_xpath")
            return events_title_by_xpath
        except Exception as ex:
            print("events_title_by_xpath : ", ex)

    def events_title_validation_text(self):
        try:
            events_title_validation_text = self.common_test_data_config \
                .get("Enrollment_Groups_Data", "events_title_validation_text")
            return events_title_validation_text
        except Exception as ex:
            print("events_title_validation_text : ", ex)

    def enrollment_groups_details_action_dropdown_button_by_xpath(self):
        try:
            enrollment_groups_details_action_dropdown_button_by_xpath = self.config \
                .get("LOCATORS", "enrollment_groups_details_action_dropdown_button_by_xpath")
            return enrollment_groups_details_action_dropdown_button_by_xpath
        except Exception as ex:
            print("enrollment_groups_details_action_dropdown_button_by_xpath : ", ex)

    def edit_button_by_xpath(self):
        try:
            edit_button_by_xpath = self.config \
                .get("LOCATORS", "edit_button_by_xpath")
            return edit_button_by_xpath
        except Exception as ex:
            print("edit_button_by_xpath : ", ex)

    def enrollment_group_name_delete(self, group_name):
        try:
            ele = self.config.get('DYNAMIC_XPATH', 'enrollment_group_name_delete')
            return ele.format(group_name)
        except Exception as ex:
            print(ex)

    def delete_popup_yes_btn_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'delete_popup_yes_btn_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_group_list_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'enrollment_group_list_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def face_threshold_for_eg_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'face_threshold_for_eg_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def default_face_threshold(self):
        try:
            ele = self.common_test_data_config.get('Enrollment_Groups_Data', 'default_face_threshold')
            return ele
        except Exception as ex:
            print(ex)

    def masked_face_threshold_for_eg_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'masked_face_threshold_for_eg_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def default_masked_face_threshold(self):
        try:
            ele = self.common_test_data_config.get('Enrollment_Groups_Data', 'default_masked_face_threshold')
            return ele
        except Exception as ex:
            print(ex)


    def serious_offender_input_data(self):
        try:
            ele = self.common_test_data_config.get('Enrollment_Groups_Data', 'serious_offender_input_data')
            return ele
        except Exception as ex:
            print(ex)

    def supress_duplicate_events_input_data(self):
        try:
            ele = self.common_test_data_config.get('Enrollment_Groups_Data', 'supress_duplicate_events_input_data')
            return ele
        except Exception as ex:
            print(ex)

    def validation_error_message_validation_text(self):
        try:
            ele = self.common_test_data_config.get('Enrollment_Groups_Data', 'validation_error_message_validation_text')
            return ele
        except Exception as ex:
            print(ex)

    def user_close_panel_and_discard_changes(self):
        try:
            ele = self.config.get('LOCATORS', 'user_close_panel_and_discard_Changes')
            return ele
        except Exception as ex:
            print(ex)

    def unlinked_enrollments_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'unlinked_enrollments_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def enroll_filter_button_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'enroll_filter_button_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def enroll_check_box(self):
        try:
            ele = self.config.get('LOCATORS', 'enroll_check_box')
            return ele
        except Exception as ex:
            print(ex)

    def third_action_dropdown_button_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'third_action_dropdown_button_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def add_enrollments_to_groups(self):
        try:
            ele = self.config.get('LOCATORS', 'add_enrollments_to_groups')
            return ele
        except Exception as ex:
            print(ex)

    def added_enrollment_to_enrollment_groups_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'added_enrollment_to_enrollment_groups_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def added_enrollment_to_enrollment_groups_text(self):
        try:
            ele = self.common_test_data_config.get('Enrollment_Groups_Data', 'added_enrollment_to_enrollment_groups_text')
            return ele
        except Exception as ex:
            print(ex)

    def remove_enrollments_from_group_by(self):
        try:
            ele = self.config.get('LOCATORS', 'remove_enrollments_from_group_by')
            return ele
        except Exception as ex:
            print(ex)

    def default_enrollment_group_details_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'default_enrollment_group_details_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def default_enrollment_group_details(self):
        try:
            ele = self.common_test_data_config.get('Enrollment_Groups_Data', 'default_enrollment_group_details')
            return ele
        except Exception as ex:
            print(ex)

    def create_notification_group_btn_by_xpath(self):
        try:
            create_notification_group_btn_by_xpath = self \
                .config.get("LOCATORS", "create_notification_group_btn_by_xpath")
            return create_notification_group_btn_by_xpath
        except Exception as ex:
            print("create_notification_group_btn_by_xpath : ", ex)

    def notification_group_in_enrollment_group(self):
        try:
            notification_group_in_enrollment_group = self \
                .config.get("LOCATORS", "notification_group_in_enrollment_group")
            return notification_group_in_enrollment_group
        except Exception as ex:
            print("notification_group_in_enrollment_group : ", ex)

    def get_action_dropdown_on_notification_groups_panel_by_xpath(self):
        try:
            action_dropdown_on_notification_groups_panel_by_xpath = self.config.get("LOCATORS",
                                                                                    "action_dropdown_on_notification_groups_panel_by_xpath")
            return action_dropdown_on_notification_groups_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_users_btn_on_notification_groups_panel_by_xpath(self):
        try:
            users_btn_on_notification_groups_panel_by_xpath = self.config.get("LOCATORS", "users_btn_on_notification_groups_panel_by_xpath")
            return users_btn_on_notification_groups_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_add_to_enrollment_groups_option_by_xpath(self):
        try:
            add_to_enrollment_groups_option_by_xpath = self.config.get("LOCATORS", "add_to_enrollment_groups_option_by_xpath")
            return add_to_enrollment_groups_option_by_xpath
        except Exception as ex:
            print(ex)

    def unlinked_notification_groups(self):
        try:
            unlinked_notification_groups = self \
                .config.get("LOCATORS", "unlinked_notification_groups")
            return unlinked_notification_groups
        except Exception as ex:
            print("unlinked_notification_groups : ", ex)

    def filter_notification_search_by_xpath(self):
        try:
            filter_notification_search_by_xpath = self \
                .config.get("LOCATORS", "filter_notification_search_by_xpath")
            return filter_notification_search_by_xpath
        except Exception as ex:
            print("filter_notification_search_by_xpath : ", ex)

    def ng_adding_eg_by_xpath(self):
        try:
            ng_adding_eg_by_xpath = self \
                .config.get("LOCATORS", "ng_adding_eg_by_xpath")
            return ng_adding_eg_by_xpath
        except Exception as ex:
            print("ng_adding_eg_by_xpath : ", ex)

    def eg_select_check_box_by_xpath(self):
        try:
            eg_select_check_box_by_xpath = self \
                .config.get("LOCATORS", "eg_select_check_box_by_xpath")
            return eg_select_check_box_by_xpath
        except Exception as ex:
            print("eg_select_check_box_by_xpath : ", ex)

    def second_name_by_xpath(self):
        try:
            second_name_by_xpath = self \
                .config.get("LOCATORS", "second_name_by_xpath")
            return second_name_by_xpath
        except Exception as ex:
            print("second_name_by_xpath : ", ex)

    def second_save_button_by_xpath(self):
        try:
            second_save_button_by_xpath = self \
                .config.get("LOCATORS", "second_save_button_by_xpath")
            return second_save_button_by_xpath
        except Exception as ex:
            print("second_save_button_by_xpath : ", ex)

    def event_button_by_xpath(self):
        try:
            event_button_by_xpath = self.config \
                .get("LOCATORS", "event_button_by_xpath")
            return event_button_by_xpath
        except Exception as ex:
            print("validation_error_message_by_xpath : ", ex)

    def events_action_dropdown_button_by_xpath(self):
        try:
            events_action_dropdown_button_by_xpath = self.config.get("LOCATORS",
                                                                     "events_action_dropdown_button_by_xpath")
            return events_action_dropdown_button_by_xpath
        except Exception as ex:
            print(ex)

    def events_refresh_button_by_xpath(self):
        try:
            events_refresh_button_by_xpath = self.config.get("LOCATORS", "events_refresh_button_by_xpath")
            return events_refresh_button_by_xpath
        except Exception as ex:
            print("events_refresh_button_by_xpath : ", ex)

    def created_ng_validation_text(self):
        try:
            created_ng_validation_text = self.common_test_data_config.get("Enrollment_Groups_Data", "created_ng_validation_text")
            return created_ng_validation_text
        except Exception as ex:
            print("created_ng_validation_text : ", ex)

    def created_ng_by_xpath(self):
        try:
            created_ng_by_xpath = self.config.get("LOCATORS", "created_ng_by_xpath")
            return created_ng_by_xpath
        except Exception as ex:
            print("created_ng_by_xpath : ", ex)

    def created_eg_by_xpath(self):
        try:
            created_eg_by_xpath = self.config.get("LOCATORS", "created_eg_by_xpath")
            return created_eg_by_xpath
        except Exception as ex:
            print("created_eg_by_xpath : ", ex)

    def enrollment_group_btn_by_xpath(self):
        try:
            enrollment_group_btn_by_xpath = self.config.get("LOCATORS", "enrollment_group_btn_by_xpath")
            return enrollment_group_btn_by_xpath
        except Exception as ex:
            print("enrollment_group_btn_by_xpath : ", ex)

    def close_all_panel_one_by_one(self):
        try:
            close_all_panel_one_by_one = self.config.get("LOCATORS", "close_panel_one_by_one_list")
            return close_all_panel_one_by_one
        except Exception as ex:
            print("close_all_panel_one_by_one : ", ex)

    def logout_btn_by_xpath(self):
        try:
            logout_btn_by_xpath = self.config.get("LOCATORS", "logout_btn_by_xpath")
            return logout_btn_by_xpath
        except Exception as ex:
            print("copyright_btn_by_xpath : ", ex)

    def cloud_menu_by_xpath(self):
        try:
            cloud_menu_by_xpath = self.config.get("LOCATORS", "cloud_menu_by_xpath")
            return cloud_menu_by_xpath
        except Exception as ex:
            print("cloud_menu_by_xpath : ", ex)

    def close_all_panels_btn_by_xpath(self):
        close_all_panels_btn_by_xpath = self.config.get("LOCATORS", "close_all_panels_btn_by_xpath")
        return close_all_panels_btn_by_xpath

    def close_panel_and_discard_changes(self):
        close_panel_and_discard_changes = self.config.get("LOCATORS", "close_panel_and_discard_changes")
        return close_panel_and_discard_changes
# print(Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath())

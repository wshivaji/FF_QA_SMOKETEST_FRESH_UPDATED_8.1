import configparser
from pathlib import Path
import datetime as dt


class read_enrollment_components:

    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            enrollments_ini_file_path = f'{Path(__file__).parent.parent.parent}\\All_Test_Data\\_11_Enrollment_Module\\Data_from_INI' \
                                        f'\\Enrollments.ini'
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(enrollments_ini_file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def default_enrollment_group_details(self):
        try:
            default_enrollment_group_details = self.common_test_data_config.get("Enrollment_Groups_Data", "default_enrollment_group_details")
            return default_enrollment_group_details
        except Exception as ex:
            print(ex.args)

    def Enrollment_link(self):
        try:
            enrollment_link = self.config.get("Locators", "Enrollment_link")
            return enrollment_link
        except Exception as ex:
            print(ex.args)

    def unlinked_eg_groups_checkbox_by_xpath(self):
        try:
            unlinked_eg_groups_checkbox_by_xpath = self.config.get("Locators","unlinked_eg_groups_checkbox_by_xpath")
            return unlinked_eg_groups_checkbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def Total_number_of_enrollments(self):
        try:
            enrollments_count = self.config.get("Locators", "count_of_Enrollments")
            return enrollments_count
        except  Exception as ex:
            print(ex.args)

    def disabled_text_xpath(self):
        try:
            disabled = self.config.get("Locators", "Disabled_text_xpath")
            return disabled
        except Exception as ex:
            print(ex.args)

    def get_disabled_text(self):
        try:
            read_disabled_text = self.config.get("data", "expected_disabled_text")
            return read_disabled_text
        except Exception as ex:
            print(ex.args)

    def faces_button_on_enrollment_panel(self):
        try:
            faces_button = self.config.get("Locators","Faces_button")
            return faces_button
        except Exception as ex:
            print(ex.args)

    def add_face_image_box_by_xpath(self):
        try:
            add_face = self.config.get("Locators","add_face_img_box")
            return add_face
        except  Exception as ex:
            print(ex)

    def skip_cropping_button_xpath(self):
        try:
            skip_cropping = self.config.get("Locators","skip_cropping_button_xpath")
            return skip_cropping
        except Exception as ex:
            print(ex)
    def add_photo_button_xpath(self):
        try:
            add_button = self.config.get("Locators","add_photo_button")
            return add_button
        except Exception as ex:
            print(ex)

    def add_face_button_xpath(self):
        try:
            add_button = self.config.get("Locators","add_face_button")
            return add_button
        except Exception as ex:
            print(ex)

    def success_message_of_add_photo(self):
        try:
            success = self.config.get("Locators", "success_message")
            return success
        except Exception as ex:
            print(ex.args)

    def extend_menu_icon_by_xpath(self):
        try:
            extend_menu = self.config.get("Locators","extend_menu_xpath")
            return extend_menu
        except Exception as ex:
            print(ex)

    def notes_icon_by_xpath(self):
        try:
            notes_icon = self.config.get("Locators","Notes_icon_by_xpath")
            return notes_icon
        except Exception as ex:
            print(ex)

    def action_button_in_enrollment_notes(self):
        try:
            action_button = self.config.get("Locators","Action_button_in_enrollment_notes")
            return action_button
        except Exception as ex:
            print(ex.args)

    def link_to_add_notes_to_an_enrollment_xpath(self):
        try:
            add_notes = self.config.get("Locators","add_notes_option_link")
            return add_notes
        except Exception as ex:
            print(ex)

    def image_box_to_add_notes(self):
        try:
            image_box = self.config.get("Locators","notes_image_box_to_add_notes")
            return image_box
        except Exception as ex:
            print(ex.args)

    def get_location_store_input_xpath(self):
        try:
            location_store = self.config.get("Locators", "notes_location_store_input_xpath")
            return location_store
        except Exception as ex:
            print(ex.args)

    def get_location_data(self):
        try:
            location_data = self.config.get("data","notes_location")
            return location_data
        except Exception as ex:
            print(ex.args)


    def get_case_subject_input_xpath(self):
        try:
            case_subject = self.config.get("Locators","notes_case_subject_input_xpath")
            return case_subject
        except Exception as ex:
            print(ex.args)

    def get_case_subject_data(self):
        try:
            case_subject = self.config.get("data","case_subject")
            return case_subject
        except Exception as ex:
            print(ex.args)

    def get_date_and_incident_by_xpath(self):
        try:
            date_of_incident = self.config.get("Locators","notes_date_of_incident")
            return date_of_incident
        except Exception as ex:
            print(ex)

    def save_button_xpath(self):
        try:
            save = self.config.get("Locators","save_button_xpath")
            return  save
        except Exception as ex:
            print(ex)

    def after_creating_notes_list(self):
        try:
            notes_list = self.config.get("Locators","after_creating_notes_list")
            return notes_list
        except Exception as ex:
            print(ex.args)

    def filter_dropdown_by_xpath(self):
        try:
            filter_dropdown = self.config.get("Locators","filter_dropdown_on_enrollment")
            return filter_dropdown
        except Exception as ex:
            print(ex)

    def pending_for_review_option(self):
        try:
            pending_for_review_option = self.config.get("Locators","pending_for_review")
            return pending_for_review_option
        except Exception as ex:
            print(ex.args)

    def select_checkbox_of_pending_for_review(self):
        try:
            checkbox = self.config.get("Locators","pending_for_review_checkbox")
            return checkbox
        except Exception as ex:
            print(ex)

    def Action_button_on_enrollment_panel(self):
        try:
            Action_button = self.config.get("Locators","Action_button_on_enrollment")
            return Action_button
        except Exception as ex:
            print(ex)

    def Approve_enrollment_option_xpath(self):
        try:
            approve_enrollment = self.config.get("Locators","approve_enrollment_option_xpath")
            return approve_enrollment
        except Exception as ex:
            print(ex)

    def enable_enrollment_option_by_xpath(self):
        try:
            enable_enrollment_option_by_xpath = self.config.get("Locators","enable_enrollment_option_by_xpath")
            return enable_enrollment_option_by_xpath
        except Exception as ex:
            print(ex)

    def accepted_enrollment_id(self):
        try:
            accepted_en_id = self.config.get("Locators","accepted_enrollment_id")
            return accepted_en_id
        except Exception as ex:
            print(ex.args)

    def enabled_option_xpath(self):
        try:
            enabled_option = self.config.get("Locators","enabled_option_xpath")
            return enabled_option
        except Exception as ex:
            print(ex.args)

    # def get_approver_id(self):
    #     try:
    #         approver_id = self.config.get("data","approver_enrollment_id")
    #         return approver_id
    #     except Exception as ex:
    #         print(ex.args)

    def reject_enrollment_option(self):
        try:
            reject = self.config.get("Locators","reject_enable_enrollment")
            return reject
        except Exception as ex:
            print(ex.args)

    def rejected_enrollment_option_in_filter(self):
        try:
            rejected = self.config.get("Locators","rejected_option_in_filter")
            return rejected
        except Exception as ex:
            print(ex.args)

    def get_rejected_buttton_in_dialouge_tooltip(self):
        try:
            rejected_button = self.config.get("Locators","reject_button_on_dialouge_tooltip")
            return rejected_button
        except Exception as ex:
            print(ex.args)

    def get_enrollment_rejected_id(self):
        try:
            rejected_id = self.config.get("Locators","enrollment_rejected_id")
            return  rejected_id
        except Exception as ex:
            print(ex.args)

    def rejected_enrollment_text(self):
        try:
           rejected_text = self.config.get("Locators","rejected_enrollment_text")
           return  rejected_text
        except Exception as ex:
            print(ex.args)

    def delete_option_in_action_dropdown(self):
        try:
            delete_option = self.config.get("Locators","deleted_option_in_Action")
            return delete_option
        except Exception as ex:
            print(ex.args)

    def yes_delete_button_xpath(self):
        try:
            delete_enrollment = self.config.get("Locators","yes_delete_button_xpath")
            return delete_enrollment
        except Exception as ex:
            print(ex.args)

    def delete_enrollment_successfully_message(self):
        try:
            message = self.config.get("Locators","enrollment_delte_message")
            return message
        except Exception as ex:
            print(ex.args)

    def expired_date_on_enrollment(self):
        try:
            expired_date_on_enrollment = self.config.get("Locators","expired_date_on_enrollment")
            return expired_date_on_enrollment
        except Exception as ex:
            print(ex.args)



    def get_approver_id(self):
        try:
            approver_id = self.config.get("data","approver_enrollment_id")
            return approver_id
        except Exception as ex:
            print(ex.args)



    def get_rejected_buttton_in_dialouge_tooltip(self):
        try:
            rejected_button = self.config.get("Locators","reject_button_on_dialouge_tooltip")
            return rejected_button
        except Exception as ex:
            print(ex.args)

    def get_enrollment_rejected_id(self):
        try:
            rejected_id = self.config.get("Locators","enrollment_rejected_id")
            return  rejected_id
        except Exception as ex:
            print(ex.args)

    def rejected_enrollment_text(self):
        try:
           rejected_text = self.config.get("Locators","rejected_enrollment_text")
           return  rejected_text
        except Exception as ex:
            print(ex.args)

    def delete_option_in_action_dropdown(self):
        try:
            delete_option = self.config.get("Locators","deleted_option_in_Action")
            return delete_option
        except Exception as ex:
            print(ex.args)

    def yes_delete_button_xpath(self):
        try:
            delete_enrollment = self.config.get("Locators","yes_delete_button_xpath")
            return delete_enrollment
        except Exception as ex:
            print(ex.args)

    def delete_enrollment_successfully_message(self):
        try:
            message = self.config.get("Locators","enrollment_delte_message")
            return message
        except Exception as ex:
            print(ex.args)

    def expired_date_on_enrollment(self):
        try:
            expired_date_on_enrollment = self.config.get("Locators","expired_date_on_enrollment")
            return expired_date_on_enrollment
        except Exception as ex:
            print(ex.args)



    # def get_approver_id(self):
    #     try:
    #         approver_id = self.config.get("data","approver_enrollment_id")
    #         return approver_id
    #     except Exception as ex:
    #         print(ex.args)

    def get_rejected_buttton_in_dialouge_tooltip(self):
        try:
            rejected_button = self.config.get("Locators","reject_button_on_dialouge_tooltip")
            return rejected_button
        except Exception as ex:
            print(ex.args)

    def get_enrollment_rejected_id(self):
        try:
            rejected_id = self.config.get("Locators","enrollment_rejected_id")
            return  rejected_id
        except Exception as ex:
            print(ex.args)

    def rejected_enrollment_text(self):
        try:
           rejected_text = self.config.get("Locators","rejected_enrollment_text")
           return  rejected_text
        except Exception as ex:
            print(ex.args)

    def delete_option_in_action_dropdown(self):
        try:
            delete_option = self.config.get("Locators","deleted_option_in_Action")
            return delete_option
        except Exception as ex:
            print(ex.args)

    def yes_delete_button_xpath(self):
        try:
            delete_enrollment = self.config.get("Locators","yes_delete_button_xpath")
            return delete_enrollment
        except Exception as ex:
            print(ex.args)

    def delete_enrollment_successfully_message(self):
        try:
            message = self.config.get("Locators","enrollment_delte_message")
            return message
        except Exception as ex:
            print(ex.args)

    def expired_date_on_enrollment(self):
        try:
            expired_date_on_enrollment = self.config.get("Locators","expired_date_on_enrollment")
            return expired_date_on_enrollment
        except Exception as ex:
            print(ex.args)

    def clicking_on_one_enrollment_group_button(self):
        try:
            enrollment_group = self.config.get("Locators","Enrollment_group_button")
            return enrollment_group
        except Exception as ex:
            print(ex.args)

    def get_enrollment_group_count(self):
        try:
            enrollment_group_count = self.config.get("Locators","Enrollment_group_count")
            return enrollment_group_count
        except Exception as ex:
            print(ex.args)

    def filter_dropdown_on_enrollment_group(self):
        try:
            filter_dropdown = self.config.get("Locators","filter_dropdown_on_enrollment_group")
            return filter_dropdown
        except Exception as ex:
            print(ex.args)


    def unlinked_eg_option_xpath(self):
        try:
            linked_eg = self.config.get("Locators","unlinked_eg__option_xpath")
            return linked_eg
        except Exception as ex:
            print(ex.args)

    def list_of_egs(self):
        try:
            egs = self.config.get("Locators","list_of_egs")
            return egs
        except Exception as ex:
            print(ex)

    def read_eg_data(self):
        try:
            eg_name = self.config.get("data","eg_name")
            return eg_name
        except Exception as ex:
            print(ex.args)

    def checkbox_xpath_1(self):
        try:
            checkbox_xpath_1 = self.config.get("Locators","checkbox_xpath_1")
            return checkbox_xpath_1
        except Exception as ex:
            print(ex.args)

    def checkbox_xpath_2(self):
        try:
            checkbox_xpath_2 = self.config.get("Locators","checkbox_xpath_2")
            return checkbox_xpath_2
        except Exception as ex:
            print(ex.args)

    def action_dropdown_on_eg(self):
        try:
            action_dropdown = self.config.get("Locators","action_dropdown_on_eg")
            return action_dropdown
        except Exception as ex:
            print(ex.args)

    def add_group_to_enrollment_option(self):
        try:
            add_eg_to_en = self.config.get("Locators","adding_group_option_xpath")
            return add_eg_to_en
        except Exception as ex:
            print(ex.args)

    def after_linking_eg_count(self):
        try:
            after_linking_eg_count = self.config.get("Locators","after_linking_enrollment_group_count")
            return after_linking_eg_count
        except Exception as ex:
            print(ex.args)

    def remove_enrollment_group_to_enrollment(self):
        try:
            remove_enrollment = self.config.get("Locators","remove_eg_to_enrollment_option")
            return remove_enrollment
        except Exception as ex:
            print(ex.args)

    def faces_button_by_xpath(self):
        try:
            faces_button = self.config.get("Locators","faces_button_by_xpath")
            return faces_button
        except Exception as ex:
            print(ex.args)

    def before_adding_faces_count(self):
        try:
            faces = self.config.get("Locators","faces_button_by_xpath")
            return faces
        except Exception as ex:
            print(ex.args)

    def image_box_xpath(self):
        try:
            image_box = self.config.get("Locators","image_box_xpath")
            return  image_box
        except Exception as ex:
            print(ex.args)

    def skip_cropping_button(self):
        try:
            skip_cropping = self.config.get("Locators","skip_cropping_button")
            return skip_cropping
        except Exception as ex:
            print(ex.args)

    def  select_photo_button(self):
        try:
            select_photo = self.config.get("Locators","select_photo_button")
            return  select_photo
        except Exception as ex:
            print(ex.args)
    def success_photo_added_message(self):
        try:
            success_msg = self.config.get("Locators","success_message_photo_added")
            return success_msg
        except Exception as ex:
            print(ex.args)

    def select_tribar_button_on_enrollment_panel(self):
        try:
            tribar = self.config.get("Locators","tribar_button")
            return tribar
        except Exception as ex:
            print(ex.args)

    def probable_match_events_button(self):
        try:
            events_button = self.config.get("Locators","events_button")
            return events_button
        except Exception as ex:
            print(ex.args)

    def list_of_events(self):
        try:
            list_of_events = self.config.get("Locators","list_of_events")
            return list_of_events
        except Exception as ex:
            print(ex.args)

    def no_events_msg(self):
        try:
            events = self.config.get("Locators","no_events_message")
            return events
        except Exception as ex:
            print(ex.args)

    def details_button(self):
        try:
            details_button = self.config.get("Locators","details_button_xpath")
            return details_button
        except Exception as ex:
            print(ex.args)

    def Action_dropdown_on_en_details_panel(self):
        try:
            action = self.config.get("Locators","Action_dropdown_on_en_details")
            return action
        except Exception as ex:
            print(ex.args)

    def edit_option_on_en_details_panel(self):
        try:
            edit = self.config.get("Locators","Edit_option_on_en_details")
            return edit
        except Exception as ex:
            print(ex.args)

    def case_event_type_dropdown(self):
        try:
            case_event_type = self.config.get("Locators","case_event_type_dropdown")
            return case_event_type
        except Exception as ex:
            print(ex.args)

    def save_button_on_en_details(self):
        try:
            save = self.config.get("Locators","save_button_on_en_details")
            return save
        except Exception as ex:
            print(ex.args)

    def get_edited_text(self):
        try:
            edit_text = self.config.get("Locators","get_edited_text")
            return edit_text
        except Exception as ex:
            print(ex.args)

    def read_case_event_type(self):
        try:
            read_case_event = self.config.get("data","case_event_type")
            return  read_case_event
        except Exception as ex:
            print(ex.args)

    def search_dropdown_xpath(self):
        try:
            search_dropdown = self.config.get("Locators","search_dropdown")
            return search_dropdown
        except Exception as ex:
            print(ex.args)

    def case_subject_xpath(self):
        try:
            case_subject = self.config.get("Locators","case_subject_xpath")
            return case_subject
        except Exception as ex:
            print(ex.args)

    def search_button(self):
        try:
            search_button = self.config.get("Locators","search_button")
            return search_button
        except Exception as ex:
            print(ex.args)

    def enabled_text(self):
        try:
            enabled_text = self.config.get("Locators","enabled_text")
            return enabled_text
        except Exception as ex:
            print(ex.args)

    def disabled_option_(self):
        try:
            disabled_option = self.config.get("Locators","disabled_option")
            return disabled_option
        except Exception as ex:
            print(ex.args)

    def list_of_filter_dropdown_option(self):
        try:
            filter_li = self.config.get("Locators","list_of_filter_dropdown_options")
            return filter_li
        except Exception as ex:
            print(ex.args)

    def enabled_en_list(self):
        try:
            filter_li = self.config.get("Locators","enabled_enrollments_list")
            return filter_li
        except Exception as ex:
            print(ex.args)

    def message_there_are_no_enrollment(self):
        try:
            msg = self.config.get("Locators","message_to_there_are_no_en")
            return msg
        except Exception as ex:
            print(ex.args)








    def close_single_panel(self):
        try:
            close_panel = self.config.get("Locators","close_single_panel")
            return  close_panel
        except Exception as ex:
            print(ex.args)




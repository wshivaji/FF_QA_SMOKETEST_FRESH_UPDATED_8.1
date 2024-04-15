import configparser
from pathlib import Path
import datetime as dt


class read_enrollment_components:

    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\All_Test_Data\\_11_Enrollment_Module\\Data_from_INI' \
                                        f'\\Enrollments.ini'
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(portal_menu_ini_file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def Enrollment_link(self):
        try:
            enrollment_link = self.config.get("Locators" ,"Enrollment_link")
            return enrollment_link
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
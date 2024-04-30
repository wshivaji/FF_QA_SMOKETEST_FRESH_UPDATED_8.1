import configparser
from pathlib import Path
import datetime as dt


class Read_Identify_and_Enroll_Components:

    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\All_Test_Data\\12_Identify_and_Enroll_Module\\Data_From_INI' \
                                        f'\\Identify_and_Enroll.ini'
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(portal_menu_ini_file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def get_eg(self):
        try:
            eg = self.common_test_data_config.get("system_level_test_Data", "enrollment_group_name")
            print(f"eg list: {eg}")
            return eg
        except Exception as ex:
            print("get_eg exception")

    def identifying_photo_wait_by_xpath(self):
        try:
            identifying_photo_wait_by_xpath = self.config.get("LOCATORS", "identifying_photo_wait_by_xpath")
            return identifying_photo_wait_by_xpath
        except Exception as ex:
            print("identifying_photo_wait_by_xpath : ", ex)

    def identifying_photo_wait_by_xpath_second_panel(self):
        try:
            identifying_photo_wait_second_panel_by_xpath = self.config.get("LOCATORS", "identifying_photo_wait_second_panel_by_xpath")
            return identifying_photo_wait_second_panel_by_xpath
        except Exception as ex:
            print("identifying_photo_wait_second_panel_by_xpath : ", ex)

    def identify_and_enroll_link_by_xpath(self):
        try:
            identify_and_enroll_link_by_xpath = self.config.get("LOCATORS", "identify_and_enroll_link_by_xpath")
            return identify_and_enroll_link_by_xpath
        except Exception as ex:
            print("identify_and_enroll_link_by_xpath : ", ex)

    def enrollment_steps_by_xpath(self):
        try:
            enrollment_steps_by_xpath = self.config.get("LOCATORS", "enrollment_steps_by_xpath")
            return enrollment_steps_by_xpath
        except Exception as ex:
            print("enrollment_steps_by_xpath : ", ex)

    def upload_image_by_xpath(self):
        try:
            upload_image_by_xpath = self.config.get("LOCATORS", "upload_image_by_xpath")
            return upload_image_by_xpath
        except Exception as ex:
            print("upload_image_by_xpath : ", ex)

    def new_enrollment_msg_by_xpath(self):
        try:
            new_enrollment_msg_by_xpath = self.config.get("LOCATORS", "new_enrollment_msg_by_xpath")
            return new_enrollment_msg_by_xpath
        except Exception as ex:
            print("new_enrollment_msg_by_xpath : ", ex)

    def add_details_panel_by_xpath(self):
        try:
            add_details_panel_by_xpath = self.config.get("LOCATORS", "add_details_panel_by_xpath")
            return add_details_panel_by_xpath
        except Exception as ex:
            print("add_details_panel_by_xpath : ", ex)

    def add_details_cancel_btn_by_xpath(self):
        try:
            add_details_cancel_btn_by_xpath = self.config.get("LOCATORS", "add_details_cancel_btn_by_xpath")
            return add_details_cancel_btn_by_xpath
        except Exception as ex:
            print("add_details_cancel_btn_by_xpath : ", ex)

    def cancel_msg_by_xpath(self):
        try:
            cancel_msg_by_xpath = self.config.get("LOCATORS", "cancel_msg_by_xpath")
            return cancel_msg_by_xpath
        except Exception as ex:
            print("cancel_msg_by_xpath : ", ex)

    def go_back_btn_by_xpath(self):
        try:
            go_back_btn_by_xpath = self.config.get("LOCATORS", "go_back_btn_by_xpath")
            return go_back_btn_by_xpath
        except Exception as ex:
            print("go_back_btn_by_xpath : ", ex)

    def cancel_enrollment_btn_by_xpath(self):
        try:
            cancel_enrollment_btn_by_xpath = self.config.get("LOCATORS", "cancel_enrollment_btn_by_xpath")
            return cancel_enrollment_btn_by_xpath
        except Exception as ex:
            print("cancel_enrollment_btn_by_xpath : ", ex)

    def add_details_save_btn_by_xpath(self):
        try:
            add_details_save_btn_by_xpath = self.config.get("LOCATORS", "add_details_save_btn_by_xpath")
            return add_details_save_btn_by_xpath
        except Exception as ex:
            print("add_details_save_btn_by_xpath : ", ex)

    def add_details_save_btn_by_xpath1(self):
        try:
            add_details_save_btn_by_xpath = self.config.get("LOCATORS", "add_details_submit_btn_by_Xpath")
            return add_details_save_btn_by_xpath
        except Exception as ex:
            print("add_details_save_btn_by_xpath : ", ex)

    def expire_date_radio_btn_by_xpath(self):
        try:
            expire_date_radio_btn_by_xpath = self.config.get("LOCATORS", "expire_date_radio_btn_by_xpath")
            return expire_date_radio_btn_by_xpath
        except Exception as ex:
            print("expire_date_radio_btn_by_xpath : ", ex)

    def do_not_expire_radio_btn_by_xpath(self):
        try:
            do_not_expire_radio_btn_by_xpath = self.config.get("LOCATORS", "do_not_expire_radio_btn_by_xpath")
            return do_not_expire_radio_btn_by_xpath
        except Exception as ex:
            print("do_not_expire_radio_btn_by_xpath : ", ex)

    def opt_out_chk_bx_by_xpath(self):
        try:
            opt_out_chk_bx_by_xpath = self.config.get("LOCATORS", "opt_out_chk_bx_by_xpath")
            return opt_out_chk_bx_by_xpath
        except Exception as ex:
            print("opt_out_chk_bx_by_xpath : ", ex)

    def enrollment_basis_by_xpath(self):
        try:
            enrollment_basis_by_xpath = self.config.get("LOCATORS", "enrollment_basis_by_xpath")
            return enrollment_basis_by_xpath
        except Exception as ex:
            print("enrollment_basis_by_xpath : ", ex)

    def enrollment_group_by_xpath(self):
        try:
            enrollment_group_by_xpath = self.config.get("LOCATORS", "enrollment_group_by_xpath")
            return enrollment_group_by_xpath
        except Exception as ex:
            print("enrollment_group_by_xpath : ", ex)

    def location_store_inpt_bx_by_xpath(self):
        try:
            location_store_inpt_bx_by_xpath = self.config.get("LOCATORS", "location_store_inpt_bx_by_xpath")
            return location_store_inpt_bx_by_xpath
        except Exception as ex:
            print("location_store_inpt_bx_by_xpath : ", ex)

    def case_subject_inpt_bx_by_xpath(self):
        try:
            case_subject_inpt_bx_by_xpath = self.config.get("LOCATORS", "case_subject_inpt_bx_by_xpath")
            return case_subject_inpt_bx_by_xpath
        except Exception as ex:
            print("case_subject_inpt_bx_by_xpath : ", ex)

    def reported_loss_inpt_bx_by_xpath(self):
        try:
            reported_loss_inpt_bx_by_xpath = self.config.get("LOCATORS", "reported_loss_inpt_bx_by_xpath")
            return reported_loss_inpt_bx_by_xpath
        except Exception as ex:
            print("reported_loss_inpt_bx_by_xpath : ", ex)

    def date_incident_inpt_bx_by_xpath(self):
        try:
            date_incident_inpt_bx_by_xpath = self.config.get("LOCATORS", "date_incident_inpt_bx_by_xpath")
            return date_incident_inpt_bx_by_xpath
        except Exception as ex:
            print("date_incident_inpt_bx_by_xpath : ", ex)

    def action_inpt_bx_by_xpath(self):
        try:
            action_inpt_bx_by_xpath = self.config.get("LOCATORS", "action_inpt_bx_by_xpath")
            return action_inpt_bx_by_xpath
        except Exception as ex:
            print("action_inpt_bx_by_xpath : ", ex)

    def case_event_type_by_xpath(self):
        try:
            case_event_type_by_xpath = self.config.get("LOCATORS", "case_event_type_by_xpath")
            return case_event_type_by_xpath
        except Exception as ex:
            print("case_event_type_by_xpath : ", ex)

    def activity_type_by_xpath(self):
        try:
            activity_type_by_xpath = self.config.get("LOCATORS", "activity_type_by_xpath")
            return activity_type_by_xpath
        except Exception as ex:
            print("activity_type_by_xpath : ", ex)

    def method_of_offence_by_xpath(self):
        try:
            method_of_offence_by_xpath = self.config.get("LOCATORS", "method_of_offence_by_xpath")
            return method_of_offence_by_xpath
        except Exception as ex:
            print("method_of_offence_by_xpath : ", ex)

    def reported_by_inpt_bx_by_xpath(self):
        try:
            reported_by_inpt_bx_by_xpath = self.config.get("LOCATORS", "reported_by_inpt_bx_by_xpath")
            return reported_by_inpt_bx_by_xpath
        except Exception as ex:
            print("reported_by_inpt_bx_by_xpath : ", ex)

    def build_inpt_bx_by_xpath(self):
        try:
            build_inpt_bx_by_xpath = self.config.get("LOCATORS", "build_inpt_bx_by_xpath")
            return build_inpt_bx_by_xpath
        except Exception as ex:
            print("build_inpt_bx_by_xpath : ", ex)

    def body_markings_inpt_bx_by_xpath(self):
        try:
            body_markings_inpt_bx_by_xpath = self.config.get("LOCATORS", "body_markings_inpt_bx_by_xpath")
            return body_markings_inpt_bx_by_xpath
        except Exception as ex:
            print("body_markings_inpt_bx_by_xpath : ", ex)

    def gender_by_xpath(self):
        try:
            gender_by_xpath = self.config.get("LOCATORS", "gender_by_xpath")
            return gender_by_xpath
        except Exception as ex:
            print("gender_by_xpath : ", ex)

    def height_by_xpath(self):
        try:
            height_by_xpath = self.config.get("LOCATORS", "height_by_xpath")
            return height_by_xpath
        except Exception as ex:
            print("height_by_xpath : ", ex)

    def narratives_txt_bx_by_xpath(self):
        try:
            narratives_txt_bx_by_xpath = self.config.get("LOCATORS", "narratives_txt_bx_by_xpath")
            return narratives_txt_bx_by_xpath
        except Exception as ex:
            print("narratives_txt_bx_by_xpath : ", ex)

    def identification_results_by_xpath(self):
        try:
            identification_results_by_xpath = self.config.get("LOCATORS", "identification_results_by_xpath")
            return identification_results_by_xpath
        except Exception as ex:
            print("identification_results_by_xpath : ", ex)

    def possible_match_found_msg_by_xpath(self):
        try:
            possible_match_found_msg_by_xpath = self.config.get("LOCATORS", "possible_match_found_msg_by_xpath")
            return possible_match_found_msg_by_xpath
        except Exception as ex:
            print("possible_match_found_msg_by_xpath : ", ex)

    def enroll_btn_by_xpath(self):
        try:
            enroll_btn_by_xpath = self.config.get("LOCATORS", "enroll_btn_by_xpath")
            return enroll_btn_by_xpath
        except Exception as ex:
            print("enroll_btn_by_xpath : ", ex)

    def identify_results_panel_by_xpath(self):
        try:
            identify_results_panel_by_xpath = self.config.get("LOCATORS", "identify_results_panel_by_xpath")
            return identify_results_panel_by_xpath
        except Exception as ex:
            print("identify_results_panel_by_xpath : ", ex)

    def no_face_error_msg_by_xpath(self):
        try:
            no_face_error_msg_by_xpath = self.config.get("LOCATORS", "no_face_error_msg_by_xpath")
            return no_face_error_msg_by_xpath
        except Exception as ex:
            print("no_face_error_msg_by_xpath : ", ex)

    ######################### Changes in config ini file ############################

    def cloud_menu_by_xpath(self):
        try:
            cloud_menu_by_xpath = self.config.get("LOCATORS", "cloud_menu_by_xpath")
            return cloud_menu_by_xpath
        except Exception as ex:
            print("cloud_menu_by_xpath : ", ex)

    def identify_and_enroll_panel_title_by_xpath(self):
        try:
            identify_and_enroll_panel_title_by_xpath = self.config.get("LOCATORS",
                                                                       "identify_and_enroll_panel_title_by_xpath")
            return identify_and_enroll_panel_title_by_xpath
        except Exception as ex:
            print("identify_and_enroll_panel_title_by_xpath : ", ex)

    def identify_and_enroll_panel_title(self):
        try:
            identify_and_enroll_panel_title = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_and_enroll_panel_title")
            return identify_and_enroll_panel_title
        except Exception as ex:
            print("identify_and_enroll_panel_title : ", ex)

    def select_a_photo_text_by_xpath(self):
        try:
            select_a_photo_text_by_xpath = self.config.get("LOCATORS",
                                                           "select_a_photo_text_by_xpath")
            return select_a_photo_text_by_xpath
        except Exception as ex:
            print("select_a_photo_text_by_xpath : ", ex)

    def identify_and_enroll_panel_select_photo_text(self):
        try:
            identify_and_enroll_panel_select_photo_text = self.common_test_data_config.get("Identify_and_Enroll_Data",
                                                                          "identify_and_enroll_panel_select_photo_text")
            return identify_and_enroll_panel_select_photo_text
        except Exception as ex:
            print("identify_and_enroll_panel_select_photo_text : ", ex)

    def select_Photo_Instructions_text_by_xpath(self):
        try:
            select_Photo_Instructions_text_by_xpath = self.config.get("LOCATORS",
                                                                      "select_Photo_Instructions_text_by_xpath")
            return select_Photo_Instructions_text_by_xpath
        except Exception as ex:
            print("select_Photo_Instructions_text_by_xpath : ", ex)

    def select_Photo_Instructions_text(self):
        try:
            select_Photo_Instructions_text = self.common_test_data_config.get("Identify_and_Enroll_Data",
                                                             "select_Photo_Instructions_text")
            return select_Photo_Instructions_text
        except Exception as ex:
            print("select_Photo_Instructions_text : ", ex)

    def uploaded_photo_validation_by_xpath(self):
        try:
            uploaded_photo = self.config.get("LOCATORS", "uploaded_photo_validation_by_xpath")
            return uploaded_photo
        except Exception as ex:
            print("uploaded_photo_validation_by_xpath : ", ex)

    def image_properties_text_by_xpath(self):
        try:
            image_properties_text_by_xpath = self.config.get("LOCATORS", "image_properties_text_by_xpath")
            return image_properties_text_by_xpath
        except Exception as ex:
            print("image_properties_text_by_xpath : ", ex)

    def image_dia_mentions_by_xpath(self):
        try:
            image_dia_mentions = self.config.get("LOCATORS", "image_dia_mentions")
            return image_dia_mentions
        except Exception as ex:
            print("image_dia_mentions : ", ex)

    def image_properties_text(self):
        try:
            image_properties_text = self.common_test_data_config.get("Identify_and_Enroll_Data", "image_properties_text")
            return image_properties_text
        except Exception as ex:
            print("image_properties_text : ", ex)

    def identify_enroll_panel_reselect_photo_btn_by_xpath(self):
        try:
            reselect_photo_btn = self.config.get("LOCATORS", "identify_enroll_panel_reselect_photo_btn_by_xpath")
            return reselect_photo_btn
        except Exception as ex:
            print("identify_enroll_panel_reselect_photo_btn_by_xpath : ", ex)

    def identify_enroll_panel_identify_enroll_btn_by_xpath(self):
        try:
            identify_enroll_btn = self.config.get("LOCATORS", "identify_enroll_panel_identify_enroll_btn_by_xpath")
            return identify_enroll_btn
        except Exception as ex:
            print("identify_enroll_panel_identify_enroll_btn_by_xpath : ", ex)

    def identify_enroll_panel_crop_photo_btn_by_xpath(self):
        try:
            crop_photo_btn = self.config.get("LOCATORS", "identify_enroll_panel_crop_photo_btn_by_xpath")
            return crop_photo_btn
        except Exception as ex:
            print("identify_enroll_panel_crop_photo_btn_by_xpath : ", ex)

    def identify_enroll_panel_text_by_xpath(self):
        try:
            identify_enroll_txt = self.config.get("LOCATORS", "identify_enroll_panel_text_by_xpath")
            return identify_enroll_txt
        except Exception as ex:
            print("identify_enroll_panel_text_by_xpath : ", ex)

    def identify_enroll_panel_text_validation(self):
        try:
            identify_enroll_txt = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_enroll_panel_text_validation")
            return identify_enroll_txt
        except Exception as ex:
            print("identify_enroll_panel_text_validation : ", ex)

    def select_photo_instructions_by_xpath(self):
        try:
            instruction = self.config.get("LOCATORS", "select_photo_instructions_by_xpath")
            return instruction
        except Exception as ex:
            print("select_photo_instructions_by_xpath : ", ex)

    def select_photo_instructions_text_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "select_photo_instructions_text_validation")
            return data
        except Exception as ex:
            print("select_photo_instructions_text_validation : ", ex)

    def identify_results_text_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_results_text_validation")
            return data
        except Exception as ex:
            print("identify_results_text_validation : ", ex)

    def identify_results_image_by_xpath(self):
        try:
            instruction = self.config.get("LOCATORS", "identify_results_image_by_xpath")
            return instruction
        except Exception as ex:
            print("identify_results_image_by_xpath : ", ex)

    def identify_results_faces_icon_by_xpath(self):
        try:
            faces_icon = self.config.get("LOCATORS", "identify_results_faces_icon_by_xpath")
            return faces_icon
        except Exception as ex:
            print("identify_results_faces_icon_by_xpath : ", ex)

    def visitor_image_on_enroll_face_panel(self):
        try:
            visitor_image_on_enroll_face_panel = self.config.get("LOCATORS", "visitor_image_on_enroll_face_panel")
            return visitor_image_on_enroll_face_panel
        except Exception as ex:
            print("visitor_image_on_enroll_face_panel : ", ex)

    def enrollment_faces_panel_checkbox_by_xpath(self):
        try:
            enrollment_faces_panel_checkbox_by_xpath = self.config.get("LOCATORS",
                                                                       "enrollment_faces_panel_checkbox_by_xpath")
            return enrollment_faces_panel_checkbox_by_xpath
        except Exception as ex:
            print("enrollment_faces_panel_checkbox_by_xpath : ", ex)

    def download_button_enroll_panel_by_xpath(self):
        try:
            download_button_enroll_panel_by_xpath = self.config.get("LOCATORS",
                                                                    "download_button_enroll_panel_by_xpath")
            return download_button_enroll_panel_by_xpath
        except Exception as ex:
            print("download_button_enroll_panel_by_xpath : ", ex)

    def download_button_validation_by_xpath(self):
        try:
            download_button_validation_by_xpath = self.config.get("LOCATORS",
                                                                  "download_button_validation_by_xpath")
            return download_button_validation_by_xpath
        except Exception as ex:
            print("download_button_validation_by_xpath : ", ex)

    def download_button_validation(self):
        try:
            download_button_validation = self.common_test_data_config.get("Identify_and_Enroll_Data", "download_button_validation")
            return download_button_validation
        except Exception as ex:
            print("download_button_validation : ", ex)

    def enrollment_faces_panel_checkbox_checked_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_panel_checkbox_checked_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_panel_checkbox_checked_by_xpath : ", ex)

    def identify_results_person_view_icon_hover_by_xpath(self):
        try:
            person_view_hover = self.config.get("LOCATORS", "identify_results_person_view_icon_hover_by_xpath")
            return person_view_hover
        except Exception as ex:
            print("identify_results_person_view_icon_hover_by_xpath : ", ex)

    def identify_results_person_view_icon_hover_text_validation(self):
        try:
            person_view_hover = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_results_person_view_icon_hover_text_validation")
            return person_view_hover
        except Exception as ex:
            print("identify_results_person_view_icon_hover_text_validation : ", ex)

    def identify_results_purge_replace_icon_hover_by_xpath(self):
        try:
            purge_hover = self.config.get("LOCATORS", "identify_results_purge_replace_icon_hover_by_xpath")
            return purge_hover
        except Exception as ex:
            print("identify_results_purge_replace_icon_hover_by_xpath : ", ex)

    def identify_results_purge_replace_icon_hover_text_validation(self):
        try:
            person_view_hover = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_results_purge_replace_icon_hover_text_validation")
            return person_view_hover
        except Exception as ex:
            print("identify_results_purge_replace_icon_hover_text_validation : ", ex)

    def enrollment_faces_panel_by_xpath(self):
        try:
            ele = self.config \
                .get("LOCATORS", "enrollment_faces_panel_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_panel_by_xpath : ", ex)

    def enrollment_faces_text_validation(self):
        try:
            txt = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_faces_text_validation")
            return txt
        except Exception as ex:
            print("enrollment_faces_text_validation : ", ex)

    def enrollment_faces_action_drop_down_by_xpath(self):
        try:
            txt = self.config.get("LOCATORS", "enrollment_faces_action_drop_down_by_xpath")
            return txt
        except Exception as ex:
            print("enrollment_faces_action_drop_down_by_xpath : ", ex)

    def enrollment_faces_drop_down_identify_within_enrollments_txt_validation(self):
        try:
            txt = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_faces_drop_down_identify_within_enrollments_txt_validation")
            return txt
        except Exception as ex:
            print("enrollment_faces_drop_down_identify_within_enrollments_txt_validation : ", ex)

    def enrollment_faces_drop_down_identify_within_visitors_txt_validation(self):
        try:
            txt = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_faces_drop_down_identify_within_visitors_txt_validation")
            return txt
        except Exception as ex:
            print("enrollment_faces_drop_down_identify_within_visitors_txt_validation : ", ex)

    def enrollment_faces_drop_down_add_photo_txt_validation(self):
        try:
            txt = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_faces_drop_down_add_photo_txt_validation")
            return txt
        except Exception as ex:
            print("enrollment_faces_drop_down_add_photo_txt_validation : ", ex)

    def enrollment_faces_drop_down_delete_selected_faces_txt_validation(self):
        try:
            txt = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_faces_drop_down_delete_selected_faces_txt_validation")
            return txt
        except Exception as ex:
            print("enrollment_faces_drop_down_delete_selected_faces_txt_validation : ", ex)

    def enrollment_faces_drop_down_identify_within_enrollments_ele_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_drop_down_identify_within_enrollments_ele_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_drop_down_identify_within_enrollments_ele_by_xpath : ", ex)

    def enrollment_faces_drop_down_identify_within_visitors_ele_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_drop_down_identify_within_visitors_ele_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_drop_down_identify_within_visitors_ele_by_xpath : ", ex)

    def enrollment_faces_drop_down_add_photo_ele_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_drop_down_add_photo_ele_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_drop_down_add_photo_ele_by_xpath : ", ex)

    def enrollment_faces_drop_down_delete_selected_faces_ele_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_drop_down_delete_selected_faces_ele_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_drop_down_delete_selected_faces_ele_by_xpath : ", ex)

    def enrollment_faces_location_case_heading_ele_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_location_case_heading_ele_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_location_case_heading_ele_by_xpath : ", ex)

    def enrollment_faces_sample_image_icon_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_sample_image_icon_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_sample_image_icon_by_xpath : ", ex)

    def enrollment_faces_draggable_photo_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_draggable_photo_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_draggable_photo_by_xpath : ", ex)

    def enrollment_faces_draggable_photo_txt_validation(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_faces_draggable_photo_txt_validation")
            return ele
        except Exception as ex:
            print("enrollment_faces_draggable_photo_txt_validation : ", ex)

    def enrollment_faces_visitor_img_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_visitor_img_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_visitor_img_by_xpath : ", ex)

    def enrollment_view_location_case_heading_ele_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_location_case_heading_ele_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_location_case_heading_ele_by_xpath : ", ex)

    def enrollment_view_visitor_img_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_visitor_img_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_visitor_img_by_xpath : ", ex)

    def enrollment_view_location_store_case_subject_ele_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_location_store_case_subject_ele_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_location_store_case_subject_ele_by_xpath : ", ex)

    def enrollment_view_location_store_case_subject_info_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_location_store_case_subject_info_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_location_store_case_subject_info_by_xpath : ", ex)

    def enrollment_view_action_ele_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_action_ele_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_action_ele_by_xpath : ", ex)

    def enrollment_view_action_info_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_action_info_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_action_info_by_xpath : ", ex)

    def enrollment_view_enrolled_on_ele_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_enrolled_on_ele_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_enrolled_on_ele_by_xpath : ", ex)


    def logout_btn_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'logout_btn_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_view_enrolled_on_info_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_enrolled_on_info_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_enrolled_on_info_by_xpath : ", ex)

    def identify_results_location_case_info(self):
        try:
            location_case = self.config.get("LOCATORS", "identify_results_location_case_info")
            return location_case
        except Exception as ex:
            print("identify_results_location_case_info : ", ex)

    def identify_results_index_score_by_xpath(self):
        try:
            index_score = self.config.get("LOCATORS", "identify_results_index_score_by_xpath")
            return index_score
        except Exception as ex:
            print("identify_results_index_score_by_xpath : ", ex)

    def identify_results_ranked_match_index_by_xpath(self):
        try:
            ranked_match = self.config.get("LOCATORS", "identify_results_ranked_match_index_by_xpath")
            return ranked_match
        except Exception as ex:
            print("identify_results_ranked_match_index_by_xpath : ", ex)

    def identify_results_exclamation_symbol_by_xpath(self):
        try:
            symbol = self.config.get("LOCATORS", "identify_results_exclamation_symbol_by_xpath")
            return symbol
        except Exception as ex:
            print("identify_results_exclamation_symbol_by_xpath : ", ex)

    def identify_results_ranked_match_index_text_validation(self):
        try:
            txt = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_results_ranked_match_index_text_validation")
            return txt
        except Exception as ex:
            print("identify_results_ranked_match_index_text_validation : ", ex)

    def identify_results_person_view_icon_by_xpath(self):
        try:
            person_view = self.config.get("LOCATORS", "identify_results_person_view_icon_by_xpath")
            return person_view
        except Exception as ex:
            print("identify_results_person_view_icon_by_xpath : ", ex)

    def identify_results_purge_replace_icon_by_xpath(self):
        try:
            purge = self.config.get("LOCATORS", "identify_results_purge_replace_icon_by_xpath")
            return purge
        except Exception as ex:
            print("identify_results_purge_replace_icon_by_xpath : ", ex)

    def identify_results_faces_icon_hover_by_xpath(self):
        try:
            face_icon_hover = self.config.get("LOCATORS", "identify_results_faces_icon_hover_by_xpath")
            return face_icon_hover
        except Exception as ex:
            print("identify_results_faces_icon_hover_by_xpath : ", ex)

    def identify_results_face_icon_hover_text_validation(self):
        try:
            face_icon_hover_txt = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_results_face_icon_hover_text_validation")
            return face_icon_hover_txt
        except Exception as ex:
            print("identify_results_face_icon_hover_text_validation : ", ex)

    def view_image_file_info_validation(self):
        try:
            view_image_file_info_validation = self.config.get("LOCATORS", "view_image_file_info_validation")
            return view_image_file_info_validation
        except Exception as ex:
            print("view_image_file_info_validation : ", ex)

    def view_image_file_info_button(self):
        try:
            view_image_file_info_button = self.config.get("LOCATORS", "view_image_file_info_button")
            return view_image_file_info_button
        except Exception as ex:
            print("view_image_file_info_button : ", ex)

    def view_image_file_info(self):
        try:
            view_image_file_info = self.common_test_data_config.get("Identify_and_Enroll_Data", "view_image_file_info")
            return view_image_file_info
        except Exception as ex:
            print("view_image_file_info : ", ex)

    def view_image_pop_up_text_1(self):
        try:
            view_image_pop_up_text_1 = self.common_test_data_config.get("Identify_and_Enroll_Data", "view_image_pop_up_text_1")
            return view_image_pop_up_text_1
        except Exception as ex:
            print("view_image_pop_up_text_1 : ", ex)

    def view_image_pop_up_text_2(self):
        try:
            view_image_pop_up_text_2 = self.common_test_data_config.get("Identify_and_Enroll_Data", "view_image_pop_up_text_2")
            return view_image_pop_up_text_2
        except Exception as ex:
            print("view_image_pop_up_text_2 : ", ex)

    def view_image_pop_up_text_3(self):
        try:
            view_image_pop_up_text_3 = self.common_test_data_config.get("Identify_and_Enroll_Data", "view_image_pop_up_text_3")
            return view_image_pop_up_text_3
        except Exception as ex:
            print("view_image_pop_up_text_3 : ", ex)

    def view_image_pop_up_text_4(self):
        try:
            view_image_pop_up_text_4 = self.common_test_data_config.get("Identify_and_Enroll_Data", "view_image_pop_up_text_4")
            return view_image_pop_up_text_4
        except Exception as ex:
            print("view_image_pop_up_text_4 : ", ex)

    def close_enrollment_faces_panel(self):
        try:
            close_enrollment_faces_panel = self.config.get("LOCATORS", "close_enrollment_faces_panel")
            return close_enrollment_faces_panel
        except Exception as ex:
            print("close_enrollment_faces_panel : ", ex)

    def enrollment_face_panel_title(self):
        try:
            enrollment_face_panel_title = self.config.get("LOCATORS", "enrollment_face_panel_title")
            return enrollment_face_panel_title
        except Exception as ex:
            print("enrollment_face_panel_title : ", ex)

    def close_panel_enroll_faces_validation(self):
        try:
            close_panel_enroll_faces_validation = self.config.get("LOCATORS", "close_panel_enroll_faces_validation")
            return close_panel_enroll_faces_validation
        except Exception as ex:
            print("close_panel_enroll_faces_validation : ", ex)

    def enrollment_view_panel_validation(self):
        try:
            enrollment_view_panel_validation = self.config.get("LOCATORS", "enrollment_view_panel_validation")
            return enrollment_view_panel_validation
        except Exception as ex:
            print("enrollment_view_panel_validation : ", ex)

    def enrollment_view_panel_action_button(self):
        try:
            enrollment_view_panel_action_button = self.config.get("LOCATORS", "enrollment_view_panel_action_button")
            return enrollment_view_panel_action_button
        except Exception as ex:
            print("enrollment_view_panel_action_button : ", ex)

    def enrollment_view_panel_action_button_validation(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_panel_action_button_validation")
            return ele
        except Exception as ex:
            print("enrollment_view_panel_action_button_validation : ", ex)

    def disable_enrollment_option_validation(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "disable_enrollment_option")
            return ele
        except Exception as ex:
            print("disable_enrollment_option_validation : ", ex)

    def identify_within_enrollments_option_validation(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_within_enrollments_option")
            return ele
        except Exception as ex:
            print("identify_within_enrollments_option_validation : ", ex)

    def identify_within_visitors_option_validation(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_within_visitors_option")
            return ele
        except Exception as ex:
            print("identify_within_visitors_option_validation : ", ex)

    def view_edit_details_option_validation(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "view_edit_details_option")
            return ele
        except Exception as ex:
            print("view_edit_details_option_validation : ", ex)

    def delete_enrollment_option_validation(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "delete_enrollment_option")
            return ele
        except Exception as ex:
            print("delete_enrollment_option_validation : ", ex)

    def identify_within_enrollments_option(self):
        try:
            ele = self.config.get("LOCATORS", "identify_within_enrollments_option_by_xpath")
            return ele
        except Exception as ex:
            print("identify_within_enrollments_option : ", ex)

    def identify_within_visitors_option(self):
        try:
            ele = self.config.get("LOCATORS", "identify_within_visitors_option")
            return ele
        except Exception as ex:
            print("identify_within_visitors_option : ", ex)

    def view_edit_details_option(self):
        try:
            ele = self.config.get("LOCATORS", "view_edit_details_option")
            return ele
        except Exception as ex:
            print("view_edit_details_option : ", ex)

    def delete_enrollment_option(self):
        try:
            ele = self.config.get("LOCATORS", "delete_enrollment_option")
            return ele
        except Exception as ex:
            print("delete_enrollment_option : ", ex)

    def disable_enrollment_option_click_validation(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "disable_enrollment_option_click_validation")
            return ele
        except Exception as ex:
            print("disable_enrollment_option_click_validation : ", ex)

    def identify_and_enroll_panel_close(self):
        try:
            ele = self.config.get("LOCATORS", "identify_and_enroll_panel_close")
            return ele
        except Exception as ex:
            print("identify_and_enroll_panel_close : ", ex)

    def identify_result_panel_close(self):
        try:
            ele = self.config.get("LOCATORS", "identify_result_panel_close")
            return ele
        except Exception as ex:
            print("identify_result_panel_close : ", ex)

    def identify_enroll_panel_validation(self):
        try:
            ele = self.config.get("LOCATORS", "identify_enroll_panel_validation")
            return ele
        except Exception as ex:
            print("identify_enroll_panel_validation : ", ex)

    def visitor_search_panel_validation(self):
        try:
            ele = self.config.get("LOCATORS", "visitor_search_panel_validation")
            return ele
        except Exception as ex:
            print("visitor_search_panel_validation : ", ex)

    def visitor_search_panel_close(self):
        try:
            ele = self.config.get("LOCATORS", "visitor_search_panel_close")
            return ele
        except Exception as ex:
            print("visitor_search_panel_close : ", ex)

    def enrollment_details_panel_validation(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_details_panel_validation")
            return ele
        except Exception as ex:
            print("enrollment_details_panel_validation : ", ex)

    def enrollment_details_panel_close(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_details_panel_close")
            return ele
        except Exception as ex:
            print("enrollment_details_panel_close : ", ex)

    def delete_enrollment_validation(self):
        try:
            ele = self.config.get("LOCATORS", "delete_enrollment_validation")
            return ele
        except Exception as ex:
            print("delete_enrollment_validation : ", ex)

    def delete_enrollment_cancel_button(self):
        try:
            ele = self.config.get("LOCATORS", "delete_enrollment_cancel_button")
            return ele
        except Exception as ex:
            print("delete_enrollment_cancel_button : ", ex)

    def identify_results_panel_close(self):
        try:
            ele = self.config.get("LOCATORS", "identify_results_panel_close")
            return ele
        except Exception as ex:
            print("identify_results_panel_close : ", ex)

    def identify_result_text_validation(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_result_text_validation")
            return ele
        except Exception as ex:
            print("identify_result_text_validation : ", ex)

    def enrollment_view_enrolled_status_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_enrolled_status_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_enrolled_status_by_xpath : ", ex)

    def enrollment_view_disabled_status_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_disabled_status_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_disabled_status_by_xpath : ", ex)

    def enrollment_view_enrollment_details_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_enrollment_details_btn_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_enrollment_details_btn_by_xpath : ", ex)

    def enrollment_view_faces_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_faces_btn_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_faces_btn_by_xpath : ", ex)

    def enrollment_view_events_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_events_btn_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_events_btn_by_xpath : ", ex)

    def enrollment_view_enrollment_groups_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_enrollment_groups_btn_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_enrollment_groups_btn_by_xpath : ", ex)

    def enrollment_view_notes_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_view_notes_btn_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_view_notes_btn_by_xpath : ", ex)

    def enrollment_view_enrollment_details_txt_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_view_enrollment_details_txt_validation")
            return data
        except Exception as ex:
            print("enrollment_view_enrollment_details_txt_validation : ", ex)

    def enrollment_view_faces_txt_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_view_faces_txt_validation")
            return data
        except Exception as ex:
            print("enrollment_view_faces_txt_validation : ", ex)

    def enrollment_view_events_txt_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_view_events_txt_validation")
            return data
        except Exception as ex:
            print("enrollment_view_events_txt_validation : ", ex)

    def enrollment_view_enrollment_groups_txt_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_view_enrollment_groups_txt_validation")
            return data
        except Exception as ex:
            print("enrollment_view_enrollment_groups_txt_validation : ", ex)

    def enrollment_view_notes_txt_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_view_notes_txt_validation")
            return data
        except Exception as ex:
            print("enrollment_view_notes_txt_validation : ", ex)

    def enrollment_view_faces_count_by_xpath(self):
        try:
            data = self.config.get("LOCATORS", "enrollment_view_faces_count_by_xpath")
            return data
        except Exception as ex:
            print("enrollment_view_faces_count_by_xpath : ", ex)

    def enrollment_view_enrollment_groups_count_by_xpath(self):
        try:
            data = self.config.get("LOCATORS", "enrollment_view_enrollment_groups_count_by_xpath")
            return data
        except Exception as ex:
            print("enrollment_view_enrollment_groups_count_by_xpath : ", ex)

    def enrollment_view_notes_count_by_xpath(self):
        try:
            data = self.config.get("LOCATORS", "enrollment_view_notes_count_by_xpath")
            return data
        except Exception as ex:
            print("enrollment_view_notes_count_by_xpath : ", ex)

    def enrollment_view_panel_close(self):
        try:
            data = self.config.get("LOCATORS", "enrollment_view_panel_close")
            return data
        except Exception as ex:
            print("enrollment_view_panel_close : ", ex)

    def enrollment_view_panel_title_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_view_panel_title_validation")
            return data
        except Exception as ex:
            print("enrollment_view_panel_title_validation : ", ex)

    def purge_and_replace_validation_text(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "purge_and_replace_validation_text")
            return data
        except Exception as ex:
            print("purge_and_replace_validation_text : ", ex)

    def purge_and_replace_pop_up_validation(self):
        try:
            data = self.config.get("LOCATORS", "purge_and_replace_pop_up_validation")
            return data
        except Exception as ex:
            print("purge_and_replace_pop_up_validation : ", ex)

    def crop_photo_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "crop_photo_validation")
            return data
        except Exception as ex:
            print("crop_photo_validation : ", ex)

    def crop_photo_button(self):
        try:
            data = self.config.get("LOCATORS", "crop_photo_button")
            return data
        except Exception as ex:
            print("crop_photo_button : ", ex)

    def uploaded_image_validation(self):
        try:
            data = self.config.get("LOCATORS", "uploaded_image_validation")
            return data
        except Exception as ex:
            print("uploaded_image_validation : ", ex)

    def enrollment_steps_title_txt_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_steps_title_txt_validation")
            return data
        except Exception as ex:
            print("enrollment_steps_title_txt_validation : ", ex)

    def add_details_panel_title_txt_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "add_details_panel_title_txt_validation")
            return data
        except Exception as ex:
            print("add_details_panel_title_txt_validation : ", ex)

    def enrollment_steps_selected_img_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_steps_selected_img_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_steps_selected_img_by_xpath : ", ex)

    def enrollment_steps_image_properties_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_steps_image_properties_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_steps_image_properties_by_xpath : ", ex)

    def enrollment_steps_image_properties_info_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_steps_image_properties_info_by_xpath")
            return ele
        except Exception as ex:
            print("enrollment_steps_image_properties_info_by_xpath : ", ex)

    def enrollment_steps_image_properties_txt_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_steps_image_properties_txt_validation")
            return data
        except Exception as ex:
            print("enrollment_steps_image_properties_txt_validation : ", ex)

    def enrollment_steps_warning_by_xpath(self):
        try:
            data = self.config.get("LOCATORS", "enrollment_steps_warning_by_xpath")
            return data
        except Exception as ex:
            print("enrollment_steps_warning_by_xpath : ", ex)

    def enrollment_steps_warning_txt_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_steps_warning_txt_validation")
            return data
        except Exception as ex:
            print("enrollment_steps_warning_txt_validation : ", ex)

    def enrollment_steps_no_match_found_txt_validation(self):
        try:
            data = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_steps_no_match_found_txt_validation")
            return data
        except Exception as ex:
            print("enrollment_steps_no_match_found_txt_validation : ", ex)

    def enrollments_steps_no_match_found_by_xpath(self):
        try:
            enrollments_steps_no_match_found_by_xpath = self.config \
                .get("LOCATORS", "enrollments_steps_no_match_found_by_xpath")
            return enrollments_steps_no_match_found_by_xpath
        except Exception as ex:
            print("enrollments_steps_no_match_found_by_xpath : ", ex)

    def enrollment_steps_green_ticks_list_by_xpath(self):
        try:
            enrollment_steps_green_ticks_list_by_xpath = self.config \
                .get("LOCATORS", "enrollment_steps_green_ticks_list_by_xpath")
            return enrollment_steps_green_ticks_list_by_xpath
        except Exception as ex:
            print("enrollment_steps_green_ticks_list_by_xpath : ", ex)

    def enrollment_steps_image_datas_list_by_xpath(self):
        try:
            enrollment_steps_image_datas_list_by_xpath = self.config \
                .get("LOCATORS", "enrollment_steps_image_datas_list_by_xpath")
            return enrollment_steps_image_datas_list_by_xpath
        except Exception as ex:
            print("enrollment_steps_image_datas_list_by_xpath : ", ex)

    def enrollment_steps_image_info_list_by_xpath(self):
        try:
            enrollment_steps_image_info_list_by_xpath = self.config \
                .get("LOCATORS", "enrollment_steps_image_info_list_by_xpath")
            return enrollment_steps_image_info_list_by_xpath
        except Exception as ex:
            print("enrollment_steps_image_info_list_by_xpath : ", ex)

    def add_details_cancel_msg_txt_validation(self):
        try:
            add_details_cancel_msg_txt_validation = self.common_test_data_config \
                .get("Identify_and_Enroll_Data", "add_details_cancel_msg_txt_validation")
            return add_details_cancel_msg_txt_validation
        except Exception as ex:
            print("add_details_cancel_msg_txt_validation : ", ex)

    def location_store_data(self):
        try:
            location_store_data = self.common_test_data_config.get("Enrollments_Data", "location_store_data_input")
            return location_store_data
        except Exception as ex:
            print("location_store_data : ", ex)

    def case_subject_data(self):
        try:
            case_subject_data = self.common_test_data_config.get("Enrollments_Data", "case_subject_data")
            return case_subject_data
        except Exception as ex:
            print("case_subject_data : ", ex)

    def reported_loss_data(self):
        try:
            reported_loss_data = self.common_test_data_config \
                .get("Enrollments_Data", "reported_loss_data")
            return reported_loss_data
        except Exception as ex:
            print("reported_loss_data : ", ex)

    def date_incident_data(self):
        try:
            date_incident_data = self.common_test_data_config.get("Enrollments_Data", "date_incident_data")
            day = date_incident_data[0:2]
            month = date_incident_data[3:5]
            year = date_incident_data[6:]
            print(f"day: {day}, month: {month}, year: {year}, type day: {type(day)}, month: {type(month)}, year: {type(year)}")
            day = int(day)
            month = int(month)
            year = int(year)
            datetime = dt.datetime.now()
            if day < 31:
                print("day is valid")
                if datetime.month == 2:
                    if month == datetime.month:
                        if day > 29:
                            day = datetime.day
                        else:
                            print(f" valid day: {day}")

            else:
                print(f"day: {datetime.day}")
                day = datetime.day

            if month > 12:
                print("invalid month provided")
            elif month > datetime.month:
                month = datetime.month
                print(f"month: {month}")
            else:
                month = datetime.month
                print(f"month: {month}")
            if year > datetime.year:
                print("invalid year provided")
            else:
                year = datetime.year
                print(f"year: {year}")
            if day<10:
                day = "0" + str(day)
            if month < 10:
                month = "0" + str(month)
            print(f"day: {day}, month: {month}, year: {year}, type day: {type(day)}, month: {type(month)}, year: {type(year)}")
            date_incident_data = str(day) + "-" + str(month) + "-" + str(year)
            print(f"date incident: {date_incident_data}")
            return date_incident_data
        except Exception as ex:
            print("date_incident_data : ", ex)

    def date_incident_time(self):
        try:
            datetime = dt.datetime.now()
            date_incident_time_am_pm = self.common_test_data_config.get("Enrollments_Data", "date_incident_time")
            hr = date_incident_time_am_pm[:2]
            min = date_incident_time_am_pm[2:4]
            print(f"hr: {hr}, min: {min}")
            hr = int(hr)
            min = int(min)
            if hr > 12:
                if datetime.hour < 10:
                    hr = datetime.hour
                    hr = "0" + str(hr)
                else:
                    hr = datetime.hour
                    hr = str(hr)
            elif 12 > hr > 10:
                hr = str(hr)
            else:
                hr = "0" + str(hr)
            if min > 59:
                if datetime.hour < 10:
                    min = "0" + str(datetime.hour)
                else:
                    min = str(datetime.hour)
            elif 59 > min > 10:
                min = str(min)
            else:
                min = "0" + str(min)
            date_incident_time_am_pm = hr + ":" + min
            print(f"time sending: {date_incident_time_am_pm}")
            return date_incident_time_am_pm
        except Exception as ex:
            print(ex.args)

    def date_incident_am_pm(self):
        try:
            date_incident_am_pm = self.common_test_data_config.get("Enrollments_Data", "date_incident_am_pm")
            return date_incident_am_pm
        except Exception as ex:
            print(ex.args)

    def action_input_data(self):
        try:
            action_input_data = self.common_test_data_config.get("Enrollments_Data", "action_input_data")
            return action_input_data
        except Exception as ex:
            print("action_input_data : ", ex)

    def enrollment_success_msg_validation(self):
        try:
            enrollment_success_msg_validation = self.common_test_data_config \
                .get("Identify_and_Enroll_Data", "enrollment_success_msg_validation")
            return enrollment_success_msg_validation
        except Exception as ex:
            print("enrollment_success_msg_validation : ", ex)

    def enrollment_success_msg_xpath(self):
        try:
            enrollment_success_msg_xpath = self.config.get("LOCATORS", "enrollment_success_msg_xpath")
            return enrollment_success_msg_xpath
        except Exception as ex:
            print("enrollment_success_msg_xpath : ", ex)

    def person_being_entered_text_by_xpath(self):
        try:
            person_being_entered_text_by_xpath = self.config.get("LOCATORS", "person_being_entered_text_by_xpath")
            return person_being_entered_text_by_xpath
        except Exception as ex:
            print("person_being_entered_text_by_xpath: ", ex)

    def enrollment_success_loader(self):
        try:
            enrollment_success_loader = self.config.get("LOCATORS", "enrollment_success_loader")
            return enrollment_success_loader
        except Exception as ex:
            print("enrollment_success_loader : ", ex)

    def add_details_panel_title_panel(self):
        try:
            ele = self.config.get("LOCATORS", "add_details_panel_title_panel")
            return ele
        except Exception as ex:
            print("add_details_panel_title_panel : ", ex)

    def add_details_panel_validation(self):
        try:
            ele = self.config.get("LOCATORS", "add_details_panel_validation")
            return ele
        except Exception as ex:
            print("add_details_panel_validation : ", ex)

    def review_enrollment_details_button_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "review_enrollment_details_button_xpath")
            return ele
        except Exception as ex:
            print("review_enrollment_details_button_xpath : ", ex)

    def review_added_groups_button_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "review_added_groups_button_xpath")
            return ele
        except Exception as ex:
            print("review_added_groups_button_xpath : ", ex)

    def add_more_faces_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "add_more_faces_xpath")
            return ele
        except Exception as ex:
            print("add_more_faces_xpath : ", ex)

    def review_enrollment_details_button_validation(self):
        try:
            ele = self.config.get("LOCATORS", "review_enrollment_details_button_validation")
            return ele
        except Exception as ex:
            print("review_enrollment_details_button_validation : ", ex)

    def review_added_groups_button_validation(self):
        try:
            ele = self.config.get("LOCATORS", "review_added_groups_button_validation")
            return ele
        except Exception as ex:
            print("review_added_groups_button_validation : ", ex)

    def add_more_faces_validation(self):
        try:
            ele = self.config.get("LOCATORS", "add_more_faces_validation")
            return ele
        except Exception as ex:
            print("add_more_faces_validation : ", ex)

    def enrollment_faces_panel_close_btn(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_panel_close_btn")
            return ele
        except Exception as ex:
            print("enrollment_faces_panel_close_btn : ", ex)

    def cloud_menu_button_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "cloud_menu_button_xpath")
            return ele
        except Exception as ex:
            print("cloud_menu_button_xpath : ", ex)

    def enrollment_menu_button_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_menu_button_xpath")
            return ele
        except Exception as ex:
            print("enrollment_menu_button_xpath : ", ex)

    def select_one_checkbox(self):
        try:
            checkbox = self.config.get("LOCATORS","select_one_checkbox")
            return checkbox
        except Exception as ex:
            print("select_all_enrollment_btn_xpath : ", ex)

    def enrollment_panel_action_btn(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_panel_action_btn")
            return ele
        except Exception as ex:
            print("enrollment_panel_action_btn : ", ex)

    def delete_enrollments_btn_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "delete_enrollments_btn_xpath")
            return ele
        except Exception as ex:
            print("delete_enrollments_btn_xpath : ", ex)

    def yes_delete_btn_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "yes_delete_btn_xpath")
            return ele
        except Exception as ex:
            print("yes_delete_btn_xpath : ", ex)

    def enrollment_details_action_button(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_details_action_button")
            return ele
        except Exception as ex:
            print("enrollment_details_action_button : ", ex)

    def enrollment_details_action_button_validation(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_details_action_button_validation")
            return ele
        except Exception as ex:
            print("enrollment_details_action_button_validation : ", ex)

    def yes_delete_btn_xpath_2(self):
        try:
            ele = self.config.get("LOCATORS", "yes_delete_btn_xpath_2")
            return ele
        except Exception as ex:
            print("yes_delete_btn_xpath_2 : ", ex)

    def add_details_expire_date_calender_pop_up_by_xpath(self):
        try:
            add_details_expire_date_calender_pop_up_by_xpath = self.config \
                .get("LOCATORS", "add_details_expire_date_calender_pop_up_by_xpath")
            return add_details_expire_date_calender_pop_up_by_xpath
        except Exception as ex:
            print("add_details_expire_date_calender_pop_up_by_xpath : ", ex)

    def add_details_expire_date_text_bx_by_xpath(self):
        try:
            add_details_expire_date_text_bx_by_xpath = self.config \
                .get("LOCATORS", "add_details_expire_date_text_bx_by_xpath")
            return add_details_expire_date_text_bx_by_xpath
        except Exception as ex:
            print("add_details_expire_date_text_bx_by_xpath : ", ex)

    def add_details_opt_out_by_xpath(self):
        try:
            add_details_opt_out_by_xpath = self.config \
                .get("LOCATORS", "add_details_opt_out_by_xpath")
            return add_details_opt_out_by_xpath
        except Exception as ex:
            print("add_details_opt_out_by_xpath : ", ex)

    def opt_out_txt_validation(self):
        try:
            opt_out_txt_validation = self.common_test_data_config.get("Identify_and_Enroll_Data", "opt_out_txt_validation")
            return opt_out_txt_validation
        except Exception as ex:
            print("opt_out_txt_validation : ", ex)

    def add_details_enrollment_groups_text_by_xpath(self):
        try:
            add_details_enrollment_groups_text_by_xpath = self.config \
                .get("LOCATORS", "add_details_enrollment_groups_text_by_xpath")
            return add_details_enrollment_groups_text_by_xpath
        except Exception as ex:
            print("add_details_enrollment_groups_text_by_xpath : ", ex)

    def add_details_enrollment_groups_options_by_xpath(self):
        try:
            add_details_enrollment_groups_options_by_xpath = self.config \
                .get("LOCATORS", "add_details_enrollment_groups_options_by_xpath")
            return add_details_enrollment_groups_options_by_xpath
        except Exception as ex:
            print("add_details_enrollment_groups_options_by_xpath : ", ex)

    def add_details_enrollment_groups_field_incomplete_by_xpath(self):
        try:
            add_details_enrollment_groups_field_incomplete_by_xpath = self.config \
                .get("LOCATORS", "add_details_enrollment_groups_field_incomplete_by_xpath")
            return add_details_enrollment_groups_field_incomplete_by_xpath
        except Exception as ex:
            print("add_details_enrollment_groups_field_incomplete_by_xpath : ", ex)

    def add_details_required_fields_by_xpath(self):
        try:
            add_details_required_fields_by_xpath = self.config \
                .get("LOCATORS", "add_details_required_fields_by_xpath")
            return add_details_required_fields_by_xpath
        except Exception as ex:
            print("add_details_required_fields_by_xpath : ", ex)

    def add_details_location_store_text_ele_by_xpath(self):
        try:
            add_details_location_store_text_ele_by_xpath = self.config \
                .get("LOCATORS", "add_details_location_store_text_ele_by_xpath")
            return add_details_location_store_text_ele_by_xpath
        except Exception as ex:
            print("add_details_location_store_text_ele_by_xpath : ", ex)

    def add_details_location_store_txt_validation(self):
        try:
            add_details_location_store_txt_validation = self.common_test_data_config.get("common_data", "location_store")
            return add_details_location_store_txt_validation
        except Exception as ex:
            print("add_details_location_store_txt_validation : ", ex)

    def add_details_location_store_data_input(self):
        try:
            add_details_location_store_data_input = self.common_test_data_config.get("common_data", "add_details_location_store_data_input")
            return add_details_location_store_data_input
        except Exception as ex:
            print("add_details_location_store_data_input : ", ex)

    def add_details_location_store_field_incomplete_by_xpath(self):
        try:
            add_details_location_store_field_incomplete_by_xpath = self.config \
                .get("LOCATORS", "add_details_location_store_field_incomplete_by_xpath")
            return add_details_location_store_field_incomplete_by_xpath
        except Exception as ex:
            print("add_details_location_store_field_incomplete_by_xpath : ", ex)

    def add_details_case_subject_text_ele_by_xpath(self):
        try:
            add_details_case_subject_text_ele_by_xpath = self.config \
                .get("LOCATORS", "add_details_case_subject_text_ele_by_xpath")
            return add_details_case_subject_text_ele_by_xpath
        except Exception as ex:
            print("add_details_case_subject_text_ele_by_xpath : ", ex)

    def add_details_case_subject_txt_validation(self):
        try:
            add_details_case_subject_txt_validation = self.common_test_data_config \
                .get("common_data", "add_details_case_subject_txt_validation")
            return add_details_case_subject_txt_validation
        except Exception as ex:
            print("add_details_case_subject_txt_validation : ", ex)

    def add_details_case_subject_data_input(self):
        try:
            add_details_case_subject_data_input = self.common_test_data_config \
                .get("Identify_and_Enroll_Data", "add_details_case_subject_data_input")
            return add_details_case_subject_data_input
        except Exception as ex:
            print("add_details_case_subject_data_input : ", ex)

    def add_details_case_subject_field_incomplete_by_xpath(self):
        try:
            add_details_case_subject_field_incomplete_by_xpath = self.config \
                .get("LOCATORS", "add_details_case_subject_field_incomplete_by_xpath")
            return add_details_case_subject_field_incomplete_by_xpath
        except Exception as ex:
            print("add_details_case_subject_field_incomplete_by_xpath : ", ex)

    def add_details_reported_loss_text_ele_by_xpath(self):
        try:
            add_details_reported_loss_text_ele_by_xpath = self.config \
                .get("LOCATORS", "add_details_reported_loss_text_ele_by_xpath")
            return add_details_reported_loss_text_ele_by_xpath
        except Exception as ex:
            print("add_details_reported_loss_text_ele_by_xpath : ", ex)

    def add_details_reported_loss_data_input(self):
        try:
            add_details_reported_loss_data_input = self.common_test_data_config \
                .get("Identify_and_Enroll_Data", "add_details_reported_loss_data_input")
            return add_details_reported_loss_data_input
        except Exception as ex:
            print("add_details_reported_loss_data_input : ", ex)

    def add_details_reported_loss_txt_validation(self):
        try:
            add_details_reported_loss_txt_validation = self.common_test_data_config \
                .get("common_data", "add_details_reported_loss_txt_validation")
            return add_details_reported_loss_txt_validation
        except Exception as ex:
            print("add_details_reported_loss_txt_validation : ", ex)

    def add_details_reported_loss_field_incomplete_by_xpath(self):
        try:
            add_details_reported_loss_field_incomplete_by_xpath = self.config \
                .get("LOCATORS", "add_details_reported_loss_field_incomplete_by_xpath")
            return add_details_reported_loss_field_incomplete_by_xpath
        except Exception as ex:
            print("add_details_reported_loss_field_incomplete_by_xpath : ", ex)

    def add_details_date_incident_text_ele_by_xpath(self):
        try:
            add_details_date_incident_text_ele_by_xpath = self.config \
                .get("LOCATORS", "add_details_date_incident_text_ele_by_xpath")
            return add_details_date_incident_text_ele_by_xpath
        except Exception as ex:
            print("add_details_date_incident_text_ele_by_xpath : ", ex)

    def add_details_date_incident_field_incomplete_by_xpath(self):
        try:
            add_details_date_incident_field_incomplete_by_xpath = self.config \
                .get("LOCATORS", "add_details_date_incident_field_incomplete_by_xpath")
            return add_details_date_incident_field_incomplete_by_xpath
        except Exception as ex:
            print("add_details_date_incident_field_incomplete_by_xpath : ", ex)

    def add_details_action_text_ele_by_xpath(self):
        try:
            add_details_action_text_ele_by_xpath = self.config \
                .get("LOCATORS", "add_details_action_text_ele_by_xpath")
            return add_details_action_text_ele_by_xpath
        except Exception as ex:
            print("add_details_action_text_ele_by_xpath : ", ex)

    def add_details_action_data_input(self):
        try:
            add_details_action_data_input = self.common_test_data_config \
                .get("Identify_and_Enroll_Data", "add_details_action_data_input")
            return add_details_action_data_input
        except Exception as ex:
            print("add_details_action_data_input : ", ex)

    def add_details_action_field_incomplete_by_xpath(self):
        try:
            add_details_action_field_incomplete_by_xpath = self.config \
                .get("LOCATORS", "add_details_action_field_incomplete_by_xpath")
            return add_details_action_field_incomplete_by_xpath
        except Exception as ex:
            print("add_details_action_field_incomplete_by_xpath : ", ex)

    def add_details_optional_fields_by_xpath(self):
        try:
            add_details_optional_fields_by_xpath = self.config \
                .get("LOCATORS", "add_details_optional_fields_by_xpath")
            return add_details_optional_fields_by_xpath
        except Exception as ex:
            print("add_details_optional_fields_by_xpath : ", ex)

    def add_details_case_event_type_text_ele_by_xpath(self):
        try:
            add_details_case_event_type_text_ele_by_xpath = self.config \
                .get("LOCATORS", "add_details_case_event_type_text_ele_by_xpath")
            return add_details_case_event_type_text_ele_by_xpath
        except Exception as ex:
            print("add_details_case_event_type_text_ele_by_xpath : ", ex)

    def action_button_identify_option(self):
        try:
            ele = self.config.get("LOCATORS", "action_button_identify_option")
            return ele
        except Exception as ex:
            print("action_button_identify_option : ", ex)

    def action_button_visitors_option(self):
        try:
            ele = self.config.get("LOCATORS", "action_button_visitors_option")
            return ele
        except Exception as ex:
            print("action_button_visitors_option : ", ex)

    def edite_button_validation_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "edite_button_validation_xpath")
            return ele
        except Exception as ex:
            print("edite_button_validation_xpath : ", ex)

    def edite_panel_save_button(self):
        try:
            ele = self.config.get("LOCATORS", "edite_panel_save_button")
            return ele
        except Exception as ex:
            print("edite_panel_save_button : ", ex)

    def identify_enroll_option_validation(self):
        try:
            ele = self.config.get("LOCATORS", "identify_enroll_option_validation")
            return ele
        except Exception as ex:
            print("identify_enroll_option_validation : ", ex)

    def location_store_text_validation(self):
        try:
            ele = self.config.get("LOCATORS", "location_store_text_validation")
            return ele
        except Exception as ex:
            print("location_store_text_validation : ", ex)

    def case_subject_text_validation(self):
        try:
            ele = self.config.get("LOCATORS", "case_subject_text_validation")
            return ele
        except Exception as ex:
            print("case_subject_text_validation : ", ex)

    def enrollment_details_img_validation(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_details_img_validation")
            return ele
        except Exception as ex:
            print("enrollment_details_img_validation : ", ex)

    def enrolled_on_text_validation(self):
        try:
            ele = self.config.get("LOCATORS", "enrolled_on_text_validation")
            return ele
        except Exception as ex:
            print("enrolled_on_text_validation : ", ex)

    def enrolled_time_validation(self):
        try:
            ele = self.config.get("LOCATORS", "enrolled_time_validation")
            return ele
        except Exception as ex:
            print("enrolled_time_validation : ", ex)

    def enable_button_symbol_validation(self):
        try:
            ele = self.config.get("LOCATORS", "enable_button_symbol_validation")
            return ele
        except Exception as ex:
            print("enable_button_symbol_validation : ", ex)

    def enable_text_with_symbol_validation(self):
        try:
            ele = self.config.get("LOCATORS", "enable_text_with_symbol_validation")
            return ele
        except Exception as ex:
            print("enable_text_with_symbol_validation : ", ex)

    def opt_out_status_validation(self):
        try:
            ele = self.config.get("LOCATORS", "opt_out_status_validation")
            return ele
        except Exception as ex:
            print("opt_out_status_validation : ", ex)

    def reported_loss_validation(self):
        try:
            ele = self.config.get("LOCATORS", "reported_loss_validation")
            return ele
        except Exception as ex:
            print("reported_loss_validation : ", ex)

    def date_incident_validation(self):
        try:
            ele = self.config.get("LOCATORS", "date_incident_validation")
            return ele
        except Exception as ex:
            print("date_incident_validation : ", ex)

    def action_data_validation(self):
        try:
            ele = self.config.get("LOCATORS", "action_data_validation")
            return ele
        except Exception as ex:
            print("action_data_validation : ", ex)

    def required_fields_title_validation(self):
        try:
            ele = self.config.get("LOCATORS", "required_fields_title_validation")
            return ele
        except Exception as ex:
            print("required_fields_title_validation : ", ex)

    def optional_fields_text_validation(self):
        try:
            ele = self.config.get("LOCATORS", "optional_fields_text_validation")
            return ele
        except Exception as ex:
            print("optional_fields_text_validation : ", ex)

    def case_event_type_dropdown(self):
        try:
            ele = self.config.get("LOCATORS", "case_event_type_dropdown")
            return ele
        except Exception as ex:
            print("case_event_type_dropdown : ", ex)

    def activity_type_dropdown(self):
        try:
            ele = self.config.get("LOCATORS", "activity_type_dropdown")
            return ele
        except Exception as ex:
            print("activity_type_dropdown : ", ex)

    def gender_dropdown(self):
        try:
            ele = self.config.get("LOCATORS", "gender_dropdown")
            return ele
        except Exception as ex:
            print("gender_dropdown : ", ex)

    def height_type_dropdown(self):
        try:
            ele = self.config.get("LOCATORS", "height_type_dropdown")
            return ele
        except Exception as ex:
            print("height_type_dropdown : ", ex)

    def reported_by_input(self):
        try:
            ele = self.config.get("LOCATORS", "reported_by_input")
            return ele
        except Exception as ex:
            print("reported_by_input : ", ex)

    def build_input(self):
        try:
            ele = self.config.get("LOCATORS", "build_input")
            return ele
        except Exception as ex:
            print("build_input : ", ex)

    def body_markings_input(self):
        try:
            ele = self.config.get("LOCATORS", "body_markings_input")
            return ele
        except Exception as ex:
            print("body_markings_input : ", ex)

    def narrative_Desc_input(self):
        try:
            ele = self.config.get("LOCATORS", "narrative_Desc_input")
            return ele
        except Exception as ex:
            print("narrative_Desc_input : ", ex)

    def case_event_type_validation(self):
        try:
            ele = self.config.get("LOCATORS", "case_event_type_validation")
            return ele
        except Exception as ex:
            print("case_event_type_validation : ", ex)

    def activity_type_validation(self):
        try:
            ele = self.config.get("LOCATORS", "activity_type_validation")
            return ele
        except Exception as ex:
            print("activity_type_validation : ", ex)

    def method_of_offense_validation(self):
        try:
            ele = self.config.get("LOCATORS", "method_of_offense_validation")
            return ele
        except Exception as ex:
            print("method_of_offense_validation : ", ex)

    def reported_by_validation(self):
        try:
            ele = self.config.get("LOCATORS", "reported_by_validation")
            return ele
        except Exception as ex:
            print("reported_by_validation : ", ex)

    def add_details_activity_type_text_ele_by_xpath(self):
        try:
            add_details_activity_type_text_ele_by_xpath = self.config\
                .get("LOCATORS", "add_details_activity_type_text_ele_by_xpath")
            return add_details_activity_type_text_ele_by_xpath
        except Exception as ex:
            print("add_details_activity_type_text_ele_by_xpath : ", ex)

    def add_details_method_of_offence_text_ele_by_xpath(self):
        try:
            add_details_method_of_offence_text_ele_by_xpath = self.config\
                .get("LOCATORS", "add_details_method_of_offence_text_ele_by_xpath")
            return add_details_method_of_offence_text_ele_by_xpath
        except Exception as ex:
            print("add_details_method_of_offence_text_ele_by_xpath : ", ex)

    def add_details_reported_by_text_ele_by_xpath(self):
        try:
            add_details_reported_by_text_ele_by_xpath = self.config\
                .get("LOCATORS", "add_details_reported_by_text_ele_by_xpath")
            return add_details_reported_by_text_ele_by_xpath
        except Exception as ex:
            print("add_details_reported_by_text_ele_by_xpath : ", ex)

    def reported_by_data(self):
        try:
            reported_by_data = self.common_test_data_config\
                .get("Identify_and_Enroll_Data", "reported_by_data")
            return reported_by_data
        except Exception as ex:
            print("reported_by_data : ", ex)

    def add_details_build_text_ele_by_xpath(self):
        try:
            add_details_build_text_ele_by_xpath = self.config\
                .get("LOCATORS", "add_details_build_text_ele_by_xpath")
            return add_details_build_text_ele_by_xpath
        except Exception as ex:
            print("add_details_build_text_ele_by_xpath : ", ex)

    def build_data(self):
        try:
            build_data = self.common_test_data_config\
                .get("Identify_and_Enroll_Data", "build_data")
            return build_data
        except Exception as ex:
            print("build_data : ", ex)

    def add_details_body_marking_text_ele_by_xpath(self):
        try:
            add_details_body_marking_text_ele_by_xpath = self.config\
                .get("LOCATORS", "add_details_body_marking_text_ele_by_xpath")
            return add_details_body_marking_text_ele_by_xpath
        except Exception as ex:
            print("add_details_body_marking_text_ele_by_xpath : ", ex)

    def body_markings_data(self):
        try:
            body_markings_data = self.common_test_data_config\
                .get("Identify_and_Enroll_Data", "body_markings_data")
            return body_markings_data
        except Exception as ex:
            print("body_markings_data : ", ex)

    def add_details_gender_text_ele_by_xpath(self):
        try:
            add_details_gender_text_ele_by_xpath = self.config\
                .get("LOCATORS", "add_details_gender_text_ele_by_xpath")
            return add_details_gender_text_ele_by_xpath
        except Exception as ex:
            print("add_details_gender_text_ele_by_xpath : ", ex)

    def narratives_data(self):
        try:
            narratives_data = self.common_test_data_config\
                .get("Identify_and_Enroll_Data", "narratives_data")
            return narratives_data
        except Exception as ex:
            print("narratives_data : ", ex)

    def build_validation(self):
        try:
            ele = self.config.get("LOCATORS", "build_validation")
            return ele
        except Exception as ex:
            print("build_validation : ", ex)

    def body_markings_validation(self):
        try:
            ele = self.config.get("LOCATORS", "body_markings_validation")
            return ele
        except Exception as ex:
            print("body_markings_validation : ", ex)

    def gender_validation(self):
        try:
            ele = self.config.get("LOCATORS", "gender_validation")
            return ele
        except Exception as ex:
            print("gender_validation : ", ex)

    def height_validation(self):
        try:
            ele = self.config.get("LOCATORS", "height_validation")
            return ele
        except Exception as ex:
            print("height_validation : ", ex)

    def narratives_validation(self):
        try:
            ele = self.config.get("LOCATORS", "narratives_validation")
            return ele
        except Exception as ex:
            print("narratives_validation : ", ex)

    # def reported_by_data(self):
    #     try:
    #         ele = self.config.get("DATA", "reported_by_data")
    #         return ele
    #     except Exception as ex:
    #         print("reported_by_data : ", ex)

    # def build_data(self):
    #     try:
    #         ele = self.config.get("DATA", "build_data")
    #         return ele
    #     except Exception as ex:
    #         print("build_data : ", ex)

    # def body_markings_data(self):
    #     try:
    #         ele = self.config.get("DATA", "body_markings_data")
    #         return ele
    #     except Exception as ex:
    #         print("body_markings_data : ", ex)

    # def narratives_data(self):
    #     try:
    #         ele = self.config.get("DATA", "narratives_data")
    #         return ele
    #     except Exception as ex:
    #         print("narratives_data : ", ex)

    def enrollment_details_panel_close_validation(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_details_panel_close_text")
            return ele
        except Exception as ex:
            print("enrollment_details_panel_close : ", ex)

    def enrollment_details_panel_close_1(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_details_panel_close_1")
            return ele
        except Exception as ex:
            print("enrollment_details_panel_close_1 : ", ex)

    def filter_dropdown_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "filter_dropdown_xpath")
            return ele
        except Exception as ex:
            print("filter_dropdown_xpath : ", ex)

    def filter_dropdown_validation(self):
        try:
            ele = self.config.get("LOCATORS", "filter_dropdown_validation")
            return ele
        except Exception as ex:
            print("filter_dropdown_validation : ", ex)

    def linked_enroll_option(self):
        try:
            ele = self.config.get("LOCATORS", "linked_enroll_option")
            return ele
        except Exception as ex:
            print("linked_enroll_option : ", ex)

    def unlinked_enroll_option(self):
        try:
            ele = self.config.get("LOCATORS", "unlinked_enroll_option")
            return ele
        except Exception as ex:
            print("unlinked_enroll_option : ", ex)

    def enrollment_group_action_btn_validation(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_group_action_btn_validation")
            return ele
        except Exception as ex:
            print("enrollment_group_action_btn_validation : ", ex)

    def enrollment_group_action_btn(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_group_action_btn")
            return ele
        except Exception as ex:
            print("enrollment_group_action_btn : ", ex)

    def action_btn_add_person_option(self):
        try:
            ele = self.config.get("LOCATORS", "action_btn_add_person_option")
            return ele
        except Exception as ex:
            print("action_btn_add_person_option : ", ex)

    def action_btn_create_group_option(self):
        try:
            ele = self.config.get("LOCATORS", "action_btn_create_group_option")
            return ele
        except Exception as ex:
            print("action_btn_create_group_option : ", ex)

    def action_btn_refresh_option(self):
        try:
            ele = self.config.get("LOCATORS", "action_btn_refresh_option")
            return ele
        except Exception as ex:
            print("action_btn_refresh_option : ", ex)

    def remove_person_from_group(self):
        try:
            ele = self.config.get("LOCATORS", "remove_person_from_group")
            return ele
        except Exception as ex:
            print("remove_person_from_group : ", ex)

    def select_all_text_validation(self):
        try:
            ele = self.config.get("LOCATORS", "select_all_text_validation")
            return ele
        except Exception as ex:
            print("select_all_text_validation : ", ex)

    def select_all_check_box_click(self):
        try:
            ele = self.config.get("LOCATORS", "select_all_check_box_click")
            return ele
        except Exception as ex:
            print("select_all_check_box_click : ", ex)

    def enrollment_faces_action_btn(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_action_btn")
            return ele
        except Exception as ex:
            print("enrollment_faces_action_btn : ", ex)

    def enrollments_option_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollments_option_xpath")
            return ele
        except Exception as ex:
            print("enrollments_option_xpath : ", ex)

    def visitors_option_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "visitors_option_xpath")
            return ele
        except Exception as ex:
            print("visitors_option_xpath : ", ex)

    def add_photo_option_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "add_photo_option_xpath")
            return ele
        except Exception as ex:
            print("add_photo_option_xpath : ", ex)

    def delete_faces_option_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "delete_faces_option_xpath")
            return ele
        except Exception as ex:
            print("delete_faces_option_xpath : ", ex)

    def location_cases_name_validation(self):
        try:
            ele = self.config.get("LOCATORS", "location_cases_name_validation")
            return ele
        except Exception as ex:
            print("location_cases_name_validation : ", ex)

    def sample_img_box_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "sample_img_box_xpath")
            return ele
        except Exception as ex:
            print("sample_img_box_xpath : ", ex)

    def draggable_photo_text(self):
        try:
            ele = self.config.get("LOCATORS", "draggable_photo_text")
            return ele
        except Exception as ex:
            print("draggable_photo_text : ", ex)

    def check_box_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "check_box_xpath")
            return ele
        except Exception as ex:
            print("check_box_xpath : ", ex)

    def check_box_click_validation(self):
        try:
            ele = self.config.get("LOCATORS", "check_box_click_validation")
            return ele
        except Exception as ex:
            print("check_box_click_validation : ", ex)

    def download_img_button_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "download_img_button_xpath")
            return ele
        except Exception as ex:
            print("download_img_button_xpath : ", ex)

    def view_img_info_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "view_img_info_xpath")
            return ele
        except Exception as ex:
            print("view_img_info_xpath : ", ex)

    def enrollment_faces_panel_close(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "enrollment_faces_panel_close_text")
            return ele
        except Exception as ex:
            print("enrollment_faces_panel_close : ", ex)

    def enrollment_faces_panel_close_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_faces_panel_close_xpath")
            return ele
        except Exception as ex:
            print("enrollment_faces_panel_close_xpath : ", ex)

    def add_details_height_text_ele_by_xpath(self):
        try:
            add_details_height_text_ele_by_xpath = self.config\
                .get("LOCATORS", "add_details_height_text_ele_by_xpath")
            return add_details_height_text_ele_by_xpath
        except Exception as ex:
            print("add_details_height_text_ele_by_xpath : ", ex)

    def add_details_narratives_text_ele_by_xpath(self):
        try:
            add_details_narratives_text_ele_by_xpath = self.config\
                .get("LOCATORS", "add_details_narratives_text_ele_by_xpath")
            return add_details_narratives_text_ele_by_xpath
        except Exception as ex:
            print("add_details_narratives_text_ele_by_xpath : ", ex)

    def associate_group_validation(self):
        try:
            ele = self.config.get("LOCATORS", "associate_group_validation")
            return ele
        except Exception as ex:
            print("associate_group_validation : ", ex)

    def warning_msg_close_button(self):
        try:
            ele = self.config.get("LOCATORS", "warning_msg_close_button")
            return ele
        except Exception as ex:
            print("warning_msg_close_button : ", ex)

    def reselect_photo_icon(self):
        try:
            ele = self.config.get("LOCATORS", "reselect_photo_icon")
            return ele
        except Exception as ex:
            print("reselect_photo_icon : ", ex)

    def identify_enroll_icon(self):
        try:
            ele = self.config.get("LOCATORS", "identify_enroll_icon")
            return ele
        except Exception as ex:
            print("identify_enroll_icon : ", ex)

    def crop_photo_icon(self):
        try:
            ele = self.config.get("LOCATORS", "crop_photo_icon")
            return ele
        except Exception as ex:
            print("crop_photo_icon : ", ex)

    def reselect_btn_below_text_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "reselect_btn_below_text_xpath")
            return ele
        except Exception as ex:
            print("reselect_btn_below_text_xpath : ", ex)

    def identify_enroll_btn_below_text_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "identify_enroll_btn_below_text_xpath")
            return ele
        except Exception as ex:
            print("identify_enroll_btn_below_text_xpath : ", ex)

    def crop_photo_btn_below_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "crop_photo_btn_below_xpath")
            return ele
        except Exception as ex:
            print("crop_photo_btn_below_xpath : ", ex)

    def identify_enroll_btn_below_text(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "identify_enroll_btn_below_text")
            return ele
        except Exception as ex:
            print("identify_enroll_btn_below_text : ", ex)

    def reselect_photo_btn_below_text(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "reselect_photo_btn_below_text")
            return ele
        except Exception as ex:
            print("reselect_photo_btn_below_text : ", ex)

    def crop_photo_btn_below_text(self):
        try:
            ele = self.common_test_data_config.get("Identify_and_Enroll_Data", "crop_photo_btn_below_text")
            return ele
        except Exception as ex:
            print("crop_photo_btn_below_text : ", ex)

    def get_pop_up_msg_person_not_registered_by_xpath(self):
        pop_up_msg_person_not_registered_by_xpath = self.config.get("LOCATORS", "pop_up_msg_person_not_registered_by_xpath")
        return pop_up_msg_person_not_registered_by_xpath

    def get_close_and_cancel_enrollment_btn_by_xpath(self):
        close_and_cancel_enrollment_btn_by_xpath = self.config.get("LOCATORS", "close_and_cancel_enrollment_btn_by_xpath")
        return close_and_cancel_enrollment_btn_by_xpath

    def get_panel_by_xpath(self):
        panel_by_xpath = self.config.get("LOCATORS", "panel_by_xpath")
        return panel_by_xpath

    def get_close_all_panel_menu_item_by_xpath(self):
        close_all_panel_menu_item_by_xpath = self.config.get("LOCATORS", "close_all_panel_menu_item_by_xpath")
        return close_all_panel_menu_item_by_xpath

    def close_all_panel_one_by_one(self):
        try:
            close_all_panel_one_by_one = self.config.get("LOCATORS", "close_panel_one_by_one_list")
            return close_all_panel_one_by_one
        except Exception as ex:
            print("close_all_panel_one_by_one : ", ex)

    def close_all_panels_btn_by_xpath(self):
        close_all_panels_btn_by_xpath = self.config.get("LOCATORS", "close_all_panels_btn_by_xpath")
        return close_all_panels_btn_by_xpath

    def region_btn_by_xpath(self):
        try:
            region_btn_by_xpath = self.config.get("LOCATORS", "region_btn_by_xpath")
            return region_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def action_input_by_xpath(self):
        try:
            action_input_by_xpath = self.config.get("LOCATORS", "action_input_by_xpath")
            return action_input_by_xpath
        except Exception as ex:
            print(ex.args)

    def edge_name_list(self):
        try:
            edge_name_list = self.config.get("LOCATORS", "edge_name_list")
            return edge_name_list
        except Exception as ex:
            print(ex.args)

    def save_btn_by_xpath(self):
        try:
            save_btn_by_xpath = self.config.get("LOCATORS", "save_btn_by_xpath")
            return save_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def edge_name(self):
        try:
            edge_name = self.common_test_data_config.get("Identify_and_Enroll_Data", "edge_name")
            return edge_name
        except Exception as ex:
            print(ex.args)

    def un_enrolled_visitor_images_path_1(self):
        un_enrolled_visitor_images_path_1 = self.common_test_data_config.get("common_data", "un-enrolled_visitor_images_path_1")
        return un_enrolled_visitor_images_path_1

    def un_enrolled_visitor_images_path_2(self):
        un_enrolled_visitor_images_path_2 = self.common_test_data_config.get("common_data", "un-enrolled_visitor_images_path_2")
        return un_enrolled_visitor_images_path_2

    def un_enrolled_visitor_images_path_3(self):
        un_enrolled_visitor_images_path_3 = self.common_test_data_config.get("common_data", "un-enrolled_visitor_images_path_3")
        return un_enrolled_visitor_images_path_3

    def un_enrolled_visitor_images_path_4(self):
        un_enrolled_visitor_images_path_4 = self.common_test_data_config.get("common_data", "un-enrolled_visitor_images_path_4")
        return un_enrolled_visitor_images_path_4

    def enrolled_visitor_image_path_1(self):
        enrolled_visitor_image_path_1 = self.common_test_data_config.get("common_data", "enrolled_visitor_image_path_1")
        return enrolled_visitor_image_path_1

    def enrolled_visitor_image_path_2(self):
        enrolled_visitor_image_path_2 = self.common_test_data_config.get("common_data", "enrolled_visitor_image_path_2")
        return enrolled_visitor_image_path_2

    def enrolled_visitor_image_path_3(self):
        enrolled_visitor_image_path_3 = self.common_test_data_config.get("common_data", "enrolled_visitor_image_path_3")
        return enrolled_visitor_image_path_3

    def enrolled_visitor_image_path_4(self):
        enrolled_visitor_image_path_4 = self.common_test_data_config.get("common_data", "enrolled_visitor_image_path_4")
        return enrolled_visitor_image_path_4


# Read_Identify_and_Enroll_Components().date_incident_time()


    def get_portal_login_username_textbox_by_xpath(self):

        try:
            portal_login_username_texbox = self.config.get("portal_Login",
                                                           "portal_login_username_textbox_by_xpath")
            print("portal username textbox: ", portal_login_username_texbox)
            return portal_login_username_texbox
        except Exception as ex:
            print(ex.args)

    def get_portal_login_password_textbox_by_xpath(self):
        try:
            portal_login_password_textbox = self.config.get("portal_Login",
                                                            "portal_login_password_textbox_by_xpath")
            print("portal password textbox: ", portal_login_password_textbox)
            return portal_login_password_textbox
        except Exception as ex:
            print(ex.args)

    def get_cloud_login_button_on_portal_by_xpath(self):
        try:
            cloud_login_button_on_portal = self.config.get("portal_Login", "cloud_login_button_on_portal_by_xpath")
            print("cloud login button on portal: ", cloud_login_button_on_portal)
            return cloud_login_button_on_portal
        except Exception as ex:
            print(ex.args)

    def get_portal_url(self):
        try:
            portal_url = self.config.get("Login_Data", "cloud_login_url")
            print("portal page url: ", portal_url)
            return portal_url
        except Exception as ex:
            print(ex)

    def get_username_to_login(self):
        try:
            user = self.config.get("Login_Data", "username")
            return user
        except Exception as ex:
            print(ex.args)

    def get_password_to_login(self):
        try:
            password = self.config.get("Login_Data","password")
            return password
        except Exception as ex:
            print(ex.args)

    def get_enrollment_link(self):
        try:
            enrollment_link = self.config.get("portal_Login","Enrollment_Link")
            return enrollment_link
        except Exception as ex:
            print(ex)


    def get_load_more_button_by_xpath(self):
        try:
            load_more = self.config.get("LOCATORS","load_more_button")
            return load_more
        except Exception as ex:
            print(ex.args)

    def get_checkboxes_by_xpath(self):
        try:
            checkboxes = self.config.get("LOCATORS","Enrollment_cheeck_boxes" )
            return  checkboxes
        except Exception as ex:
            print(ex.args)

    def get_filter_dropdown(self):
        try:
            filter = self.config.get("LOCATORS","Filter_button_on_Enrollment_panel")
            return filter
        except Exception as ex:
            print(ex.args)

    def pending_for_review_option(self):
        try:
            pending_for_review = self.config.get("LOCATORS","pending_for_review_option")
            return pending_for_review
        except Exception as ex:
            print(ex.args)
    def Action_button_by_Xpath(self):
        try:
            Action = self.config.get("LOCATORS","action_dropdown_button_by_xpath")
            return  Action
        except Exception as ex:
            print(ex.args)

    def approve_enrollment_link(self):
        try:
            approve_enrollment_link = self.config.get("LOCATORS","approve_enrollment_link")
            return approve_enrollment_link
        except Exception as ex:
            print(ex.args)

    def after_approving_message_to_user(self):
        try:
            message = self.config.get("LOCATORS","after_approving_enrollment_message")
            return message
        except Exception as ex:
            print(ex.args)

    def image_Xpath(self):
        try:
           image = self.config.get("LOCATORS","image_Xpath")
           return image
        except Exception as ex:
            print(ex.args)

    def get_expiration_date_xpath(self):
        try:
            expiration = self.config.get("LOCATORS", "expiration_date_xpath")
            return expiration
        except Exception as ex:
            print(ex)

    def get_expiration_date_data(self):
        try:
            expiration_data = self.config.get("DATA", "expiration_data_range")
            return expiration_data
        except Exception as ex:
            print(ex)

    def get_user_name_input_data(self):
        try:
            user_name_input_data = self.common_test_data_config.get("system_level_test_Data", "user_name_input_data")
            print(f"user_name_input_data: {user_name_input_data}")
            return user_name_input_data
        except Exception as ex:
            print(ex.args)

    def get_approver_to_login(self):
        try:
            user = self.config.get("Login_Data", "username1")
            return user
        except Exception as ex:
            print(ex.args)

    def get_operator_to_login(self):
        try:
            user = self.config.get("Login_Data", "username")
            return user
        except Exception as ex:
            print(ex.args)

    def get_responder_to_login(self):
        try:
            user = self.config.get("Login_Data", "username2")
            return user
        except Exception as ex:
            print(ex.args)

    def get_executive_to_login(self):
        try:
            user = self.config.get("Login_Data", "username3")
            return user
        except Exception as ex:
            print(ex.args)

    def get_it_admin_to_login(self):
        try:
            user = self.config.get("Login_Data", "user")
            return user
        except Exception as ex:
            print(ex.args)

    def Enrollment_link(self):
        try:
            enrollment_link = self.config.get("portal_Login","Enrollment_Link")
            return enrollment_link
        except Exception as ex:
            print(ex.args)

    def region_names_by_xpath(self):
        try:
            region_name = self.config.get("portal_Login","region_name_on_enrollment_xpath")
            return region_name
        except Exception as ex:
            print(ex.args)

    def read_region_data(self):
        try:
            read_region_data = self.common_test_data_config.get("Users_Data", "region_data_input")
            return read_region_data
        except Exception as ex:
            print(ex.args)

    def read_reported_loss_values_from_ini(self):
        try:
            region_name = self.config.get("portal_Login","reported_Loss_vaues")
            return region_name
        except Exception as ex:
            print(ex.args)

    def details_button(self):
        try:
            details_button = self.config.get("portal_Login","details_button_xpath")
            return details_button
        except Exception as ex:
            print(ex.args)

    def select_tribar_button_on_enrollment_panel(self):
        try:
            tribar = self.config.get("portal_Login","tribar_button")
            return tribar
        except Exception as ex:
            print(ex.args)

    def search_dropdow_on_enrollment(self):
        try:
            search = self.config.get("portal_Login","search_dropdown")
            return search
        except Exception as ex:
            print(ex.args)

    def case_subject_xpath(self):
        try:
            case_subject = self.config.get("portal_Login","case_subject_xpath")
            return case_subject
        except Exception as ex:
            print(ex.args)

    def enter_case_subject_data(self):
        try:
            case_subject = self.config.get("portal_Login","case_subject_xpath")
            return case_subject
        except Exception as ex:
            print(ex.args)

    def search_button(self):
        try:
            search_button = self.config.get("portal_Login","search_button")
            return search_button
        except Exception as ex:
            print(ex.args)

    def reported_loss_value_xpath(self):
        try:
            loss = self.config.get("portal_Login","reported_loss_xpath")
            return loss
        except Exception as ex:
            print(ex.args)

    def list_of_enrollments_by_xpath(self):
        try:
            en_list = self.config.get("portal_Login","list_of_enrollments_by_xpath")
            return en_list
        except Exception as ex:
            print(ex.args)





import time
from pathlib import Path
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

from All_Config_Packages._6_Notes_Module_Config_Files.Notes_Read_Ini import notes_Read_Ini
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini
from All_Config_Packages._8_Visitor_Search_Jobs_Module_Config_Files.Visitor_Search_Jobs_Read_INI import \
    Read_Visitor_Search_jobs_Components
from Base_Package.Web_Logger import web_logger
from Base_Package.Web_Driver import web_driver
from Base_Package.Login_Logout_Ops import login, logout



class notes_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def wait_for_element_to_appear(self, element_list, xpath):
        count = 0
        if len(element_list) == 0:
            while len(element_list) == 0 or count == 10:
                element_list = self.d.find_elements(By.XPATH, xpath)
                time.sleep(web_driver.one_second)
                if len(element_list) > 0:
                    self.logger.info("element is visible...")
                    return element_list[0]
                else:
                    self.logger.info("waiting for element...")
                count += 1
                self.logger.info(f"wait count: {count}")
        else:
            self.logger.info(f"element length: {len(element_list)}")
            return element_list[0]

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.two_second)
            logout_button = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().logout_btn_by_xpath(), self.d)
            logout_button.click()
            time.sleep(web_driver.two_second)
        except Exception as ex:
            print(ex)

    def verify_user_able_create_notes_successfully(self):
        try:
            self.logger.info("*********TC_Notes_01********** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            self.logger.info(f"notes visible: {notes.is_displayed()}")
            notes.click()
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            self.logger.info(f"notes heading: {heading_notes[0].text}")
            time.sleep(web_driver.three_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            self.logger.info(f"action dropdown visible: {Action_dropdown.is_displayed()}")
            Action_dropdown.click()
            time.sleep(web_driver.three_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            self.logger.info(f"create note visible: {create_note.is_displayed()}")
            create_note.click()
            time.sleep(web_driver.two_second)
            print("reached to img box")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\fraud\\00081.png"

            self.d.find_element(By.ID, "image0").send_keys(file_image_path)
            time.sleep(web_driver.two_second)
            add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            time.sleep(web_driver.three_second)
            skip_cropping = self.d.find_element(By.XPATH, notes_Read_Ini().skip_cropping_button_in_add_image())
            skip_cropping.click()
            time.sleep(web_driver.two_second)
            select_image = self.d.find_element(By.XPATH, notes_Read_Ini().select_image_button())
            select_image.click()
            time.sleep(web_driver.three_second)

            Location_store_textbox_in_createnote = self.d.find_element(By.XPATH,
                                                                       notes_Read_Ini().Location_store_textbox_on_create_note())
            self.logger.info(f"location store text visible: {Location_store_textbox_in_createnote.is_displayed()}")
            Location_store_textbox_in_createnote.clear()
            self.logger.info(f"location text: {notes_Read_Ini().Enter_text_in_Location_store_in_create_note()}")
            Location_store_textbox_in_createnote.send_keys(
                notes_Read_Ini().Enter_text_in_Location_store_in_create_note())
            time.sleep(web_driver.one_second)
            case_subject_in_createnote = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().case_subject_textbox_in_create_note())
            self.logger.info(f"case subject visible: {case_subject_in_createnote.is_displayed()}")
            case_subject_in_createnote.clear()
            self.logger.info(f"case subject: {notes_Read_Ini().Enter_text_in_case_subject_in_create_note()}")
            case_subject_in_createnote.send_keys(notes_Read_Ini().Enter_text_in_case_subject_in_create_note())
            time.sleep(web_driver.one_second)
            reported_loss = self.d.find_element(By.XPATH, notes_Read_Ini().reported_loss_in_create_note())
            self.logger.info(f"reported loss visible: {reported_loss.is_displayed()}")
            reported_loss.clear()
            self.logger.info(f"data : {notes_Read_Ini().Enter_reported_loss()}")
            reported_loss.send_keys(notes_Read_Ini().Enter_reported_loss())
            time.sleep(web_driver.one_second)
            build_on_create_note = self.d.find_element(By.XPATH, notes_Read_Ini().build_on_createnote())
            self.logger.info(f"build visible: {build_on_create_note.is_displayed()}")
            self.logger.info(f"data: {notes_Read_Ini().Enter_a_test_in_build()}")
            build_on_create_note.send_keys(notes_Read_Ini().Enter_a_test_in_build())
            time.sleep(web_driver.one_second)
            body_markings = self.d.find_element(By.XPATH, notes_Read_Ini().body_markings_textbox())
            self.logger.info(f"body markings visible: {body_markings.is_displayed()}")
            self.logger.info(f"data: {notes_Read_Ini().Enter_a_text_on_bodymarkings()}")
            body_markings.send_keys(notes_Read_Ini().Enter_a_text_on_bodymarkings())
            time.sleep(web_driver.one_second)
            gender_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().gender_dropdown())
            self.logger.info(f"gender visible: {gender_dropdown.is_displayed()}")
            gender_dropdown.click()
            time.sleep(web_driver.one_second)
            female_option_in_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().female_in_genderdropdown())
            self.logger.info(f"female option visible: {female_option_in_dropdown.is_displayed()}")
            female_option_in_dropdown.click()
            time.sleep(web_driver.one_second)
            Height_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown())
            self.logger.info(f"height dropdown visible: {Height_dropdown.is_displayed()}")
            Height_dropdown.click()
            time.sleep(web_driver.one_second)
            Height_dropdown_options = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown_options())
            self.logger.info(f"height dropdown option visible: {Height_dropdown_options.is_displayed()}")
            Height_dropdown_options.click()
            time.sleep(web_driver.one_second)
            narratives_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().Narratives_textbox())
            narratives_textbox.send_keys(notes_Read_Ini().enter_text_in_narratives_textbox())
            time.sleep(web_driver.one_second)
            action_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().action_textbox())
            action_textbox.send_keys(notes_Read_Ini().entering_text_in_action_textbox())
            time.sleep(web_driver.one_second)
            add_location_button = self.d.find_element(By.XPATH, notes_Read_Ini().add_location_button())
            add_location_button.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            move_cursur_to_map = self.d.find_element(By.XPATH, notes_Read_Ini().moving_mouse_into_map())
            action = ActionChains(self.d).move_to_element_with_offset(move_cursur_to_map, 50, 70).click().perform()
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, notes_Read_Ini().save_button_in_createnote())
            save_button.click()
            time.sleep(web_driver.one_second)
            notes_panel_heading = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if notes_panel_heading.is_displayed():
                self.logger.info("notes_details are visible")
                self.status.append(True)
            else:
                self.logger.info("notes details are not visible")
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_01.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_01.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_01.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_01.png")
            self.logger.error(f"TC_notes_01 got exception as: {ex} ")
            print(ex)

    def verify_user_able_to_delete_notes_successfully(self):
        try:
            self.logger.info("********TC_Notes_07***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes.click()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            checkbox = self.d.find_element(By.XPATH, notes_Read_Ini().delete_notes_checkbox())
            checkbox.click()
            time.sleep(web_driver.three_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            delete_selected_notes = self.d.find_element(By.XPATH, notes_Read_Ini().delete_selected_notes())
            delete_selected_notes.click()
            time.sleep(web_driver.three_second)
            no_of_selected_notes_text = self.d.find_element(By.XPATH, notes_Read_Ini().gives_no_for_deleting_notes_text())
            print(no_of_selected_notes_text.text)
            if no_of_selected_notes_text.text == notes_Read_Ini().text_present_in_deleted_notes():
                self.logger.info("gives number for selected deleting notes")
                self.status.append(True)
            else:
                self.logger.info("not showing number for deleting selected deleting notes")
                self.status.append(False)
                time.sleep(web_driver.one_second)
            yes_delete_selected_button = self.d.find_element(By.XPATH,
                                                                 notes_Read_Ini().yes_delete_selected_notes_button())
            yes_delete_selected_button.click()

            self.logger.info(f"status: {self.status}")
            self.click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_07.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_07.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_07.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_07.png")
            self.logger.error(f"TC_notes_07 got exception as: {ex} ")
            print(ex)

    def click_on_three_horizantal_lines_button_and_verify_enrollments_button_is_visible(self):
        try:
            cloud_menu_after_login = self.d.find_element(By.XPATH,
                                                         notes_Read_Ini().get_afterlogin_cloud_menu_is_visible())
            cloud_menu_after_login.click()
            time.sleep(web_driver.two_second)
            notes = self.explicit_wait(5, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            # tribar = self.d.find_element(By.XPATH, notes_Read_Ini().tribar_in_notes())
            tribar = self.d.find_elements(By.XPATH, notes_Read_Ini().tribar_in_notes())
            for i in range(len(tribar)):
                tribar[i].click()
                enrollment_button = self.d.find_element(By.XPATH, notes_Read_Ini().enrollment_button())
                if enrollment_button.is_displayed():
                    enrollment_button.click()
                    break
                else:
                    tribar[i].click()
            return True

        except Exception as ex:
            self.logger.error(f"TC_notes_103 got exception as: {ex} ")

    def click_on_three_horizantal_lines_button_and_verify_image_button_is_visible(self):
        try:
            cloud_menu_after_login = self.d.find_element(By.XPATH,
                                                         notes_Read_Ini().get_afterlogin_cloud_menu_is_visible())
            cloud_menu_after_login.click()
            time.sleep(web_driver.two_second)
            notes = self.explicit_wait(5, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            # tribar = self.d.find_element(By.XPATH, notes_Read_Ini().tribar_in_notes())
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().tribar_in_notes())
            tribar.click()
            image_button = self.d.find_element(By.XPATH, notes_Read_Ini().images_button())
            # enrollment_button = self.d.find_element(By.XPATH, notes_Read_Ini().enrollment_button())

            if image_button.is_displayed():
                image_button.click()
                self.logger.info("Clicked on Image icon..")
                return True
            else:
                return False

        except Exception as ex:
            self.logger.error(f"click_on_three_horizontal_lines_button_and_verify_image_button_is_visible got exception as: {ex} ")

    def close_panels_one_by_one(self):
        try:
            close_panel = self.d.find_elements(By.XPATH,notes_Read_Ini().close_panels_one_by_one())
            for c in close_panel:
                c.click()
        except Exception as ex:
            print(ex)

    def verify_user_able_to_edit_details_by_selecting_details_icon(self):
        try:
            self.logger.info("**********TC_Notes_02******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().view_details_button(), self.d)
            view_details = self.d.find_element(By.XPATH, notes_Read_Ini().view_details_button())
            view_details.click()
            self.explicit_wait(10, "XPATH", notes_Read_Ini().action_dropdown_in_notes_details_panel(), self.d)
            # time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().action_dropdown_in_notes_details_panel())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            edit_notes = self.d.find_element(By.XPATH, notes_Read_Ini().Edit_note_option())
            edit_notes.click()
            time.sleep(web_driver.one_second)
            Height_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown())
            Height_dropdown.click()
            time.sleep(web_driver.three_second)
            Height_dropdown_options = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown_options())
            Height_dropdown_options.click()
            time.sleep(web_driver.three_second)
            save_button = self.d.find_element(By.XPATH, notes_Read_Ini().save_button_on_notes_details())
            save_button.click()
            time.sleep(web_driver.one_second)

            notes_panel_heading = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if notes_panel_heading.is_displayed():
                self.logger.info("notes_details are visible")
                self.status.append(True)
            else:
                self.logger.info("notes details are not visible")
                self.status.append(False)
            self.close_panels_one_by_one()

            self.logger.info(f"status is {self.status}")
            self.click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_02.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_02.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_02.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_02.png")
            self.logger.error(f"TC_notes_02 got exception as: {ex} ")

    def verify_user_is_able_to_select_any_one_note_and_click_on_location_in_view_dropdown(self):
        try:
            self.logger.info("********TC_Notes_03***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes.click()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            checkbox = self.d.find_element(By.XPATH, notes_Read_Ini().delete_notes_checkbox())
            checkbox.click()
            time.sleep(web_driver.three_second)
            view_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.two_second)
            location_in_view_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().location_in_view_dropdown())
            location_in_view_dropdown.click()
            time.sleep(web_driver.two_second)
            self.explicit_wait(5, "XPATH", notes_Read_Ini().get_heading_of_notes_location(), self.d)
            heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            if heading_notes_location.is_displayed():
                self.logger.info("notes-location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-location panel heading is not visible")
                self.status.append(False)
            self.close_panels_one_by_one()

            self.logger.info(f"status: {self.status}")
            self.click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_03.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_03.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verif_use_is_able_to_select_any_one_note_and_click_on_location_in_view_dropdown ex: {ex.args}")

    def verify_user_is_able_to_select_any_one_note_and_click_on_location_icon(self):
        try:
            self.logger.info("********TC_Notes_04******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            self.explicit_wait(5, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            location_symbol = self.d.find_element(By.XPATH, notes_Read_Ini().location_symbol())
            location_symbol.click()
            time.sleep(web_driver.two_second)
            self.explicit_wait(5, "XPATH", notes_Read_Ini().get_heading_of_notes_location(), self.d)
            heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            if heading_notes_location.is_displayed():
                self.logger.info("notes-location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()

            self.logger.info(f"status: {self.status}")
            self.click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_04.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_04.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_04.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_04.png")
            self.logger.error(f"TC_notes_04 got exception as: {ex} ")
            print(ex)

    def verify_user_is_able_to_see_the_enrollment_associated_to_particular_note(self):
        try:
            self.logger.info("********TC_Notes_05***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_enrollments_panel()
            self.click_on_extend_menu_on_enrollments_panel()
            self.click_on_notes_btn_on_enrollments_panel()
            if self.verify_no_notes_error_msg_on_enrollment_notes_panel():
                self.logger.info("Note is associated with enrollment.")
                self.status.append(True)
            else:
                self.click_on_Action_Drop_down()
                self.click_on_add_a_new_note_option()
                self.verify_enrollment_create_note_panel_displayed()
                file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset2\\img1.png"
                self.upload_image_and_create_a_note(file_path)

            self.close_panels_one_by_one()
            self.click_on_three_horizantal_lines_button_and_verify_enrollments_button_is_visible()
            self.logger.info(f"status: {self.status}")
            self.click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_5.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_5.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"exception: {ex.args}")

    def Verify_user_is_able_to_add_photo_when_image_icon_is_clicked(self):
        try:
            self.logger.info("********TC_Notes_06***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            self.click_on_three_horizantal_lines_button_and_verify_image_button_is_visible()
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset2\\img1.png"
            self.click_on_image_icon_and_add_photo(file_path)
            self.verify_image_uploaded_to_image_box_on_create_note_panel()

            self.logger.info(f"status: {self.status}")
            self.click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_6.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_6.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Verify_user_is_able_to_add_photo_when_image_icon_is_clicked ex: {ex.args}")


    # **************************************** User Methods ***************************************

    def verify_image_uploaded_to_image_box_on_create_note_panel(self):
        try:
            image_box_post_image_upload = self.explicit_wait(5, "XPATH", notes_Read_Ini().image_uploaded_to_img_box_by_xpath(), self.d)
            self.logger.info(f"verify_image_uploaded_to_image_box_on_create_note_panel visible: {image_box_post_image_upload.is_displayed()}")
            if image_box_post_image_upload.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
                self.logger.info(f"verify_image_uploaded_to_image_box_on_create_note_panel is not displayed.")

        except Exception as ex:
            self.logger.info(f"verify_image_uploaded_to_image_box_on_create_note_panel ex: {ex.args}")

    def click_on_image_icon_and_add_photo(self, img_file):
        try:
            time.sleep(web_driver.one_second)
            print("reached to img box")
            # file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
            self.d.find_element(By.ID, "image0").send_keys(img_file)
            time.sleep(web_driver.two_second)
            add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            time.sleep(web_driver.three_second)
            skip_cropping = self.d.find_element(By.XPATH, notes_Read_Ini().skip_cropping_button_in_add_image())
            skip_cropping.click()
            time.sleep(web_driver.two_second)
            select_image = self.d.find_element(By.XPATH, notes_Read_Ini().select_image_button())
            select_image.click()
            time.sleep(web_driver.three_second)
            time.sleep(web_driver.two_second)

        except Exception as ex:
            self.logger.info(f"click_on_image_icon_and_add_photo ex: {ex.args}")

    def upload_image_and_create_a_note(self, img_file):
        try:
            print("reached to img box")
            # file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
            self.d.find_element(By.ID, "image0").send_keys(img_file)
            time.sleep(web_driver.two_second)
            add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            time.sleep(web_driver.three_second)
            skip_cropping = self.d.find_element(By.XPATH, notes_Read_Ini().skip_cropping_button_in_add_image())
            skip_cropping.click()
            time.sleep(web_driver.two_second)
            select_image = self.d.find_element(By.XPATH, notes_Read_Ini().select_image_button())
            select_image.click()
            time.sleep(web_driver.three_second)
            Location_store_textbox_in_createnote = self.d.find_element(By.XPATH,
                                                                       notes_Read_Ini().Location_store_textbox_on_create_note())
            Location_store_textbox_in_createnote.clear()
            Location_store_textbox_in_createnote.send_keys(
                notes_Read_Ini().Enter_text_in_Location_store_in_create_note())
            time.sleep(web_driver.one_second)
            case_subject_in_createnote = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().case_subject_textbox_in_create_note())
            case_subject_in_createnote.clear()
            case_subject_in_createnote.send_keys(notes_Read_Ini().Enter_text_in_case_subject_in_create_note())
            time.sleep(web_driver.one_second)
            reported_loss = self.d.find_element(By.XPATH, notes_Read_Ini().reported_loss_in_create_note())
            reported_loss.clear()
            reported_loss.send_keys(notes_Read_Ini().Enter_reported_loss())
            time.sleep(web_driver.one_second)
            build_on_create_note = self.d.find_element(By.XPATH, notes_Read_Ini().build_on_createnote())
            build_on_create_note.send_keys(notes_Read_Ini().Enter_a_test_in_build())
            time.sleep(web_driver.one_second)
            body_markings = self.d.find_element(By.XPATH, notes_Read_Ini().body_markings_textbox())
            body_markings.send_keys(notes_Read_Ini().Enter_a_text_on_bodymarkings())
            time.sleep(web_driver.one_second)
            gender_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().gender_dropdown())
            gender_dropdown.click()
            time.sleep(web_driver.one_second)
            female_option_in_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().female_in_genderdropdown())
            female_option_in_dropdown.click()
            time.sleep(web_driver.one_second)
            Height_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown())
            Height_dropdown.click()
            time.sleep(web_driver.one_second)
            Height_dropdown_options = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown_options())
            Height_dropdown_options.click()
            time.sleep(web_driver.one_second)
            narratives_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().Narratives_textbox())
            narratives_textbox.send_keys(notes_Read_Ini().enter_text_in_narratives_textbox())
            time.sleep(web_driver.one_second)
            action_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().action_textbox())
            action_textbox.send_keys(notes_Read_Ini().entering_text_in_action_textbox())
            time.sleep(web_driver.one_second)
            add_location_button = self.d.find_element(By.XPATH, notes_Read_Ini().add_location_button())
            add_location_button.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            move_cursur_to_map = self.d.find_element(By.XPATH, notes_Read_Ini().moving_mouse_into_map())
            action = ActionChains(self.d).move_to_element_with_offset(move_cursur_to_map, 50, 70).click().perform()
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, notes_Read_Ini().save_button_in_createnote())
            save_button.click()
            self.logger.info("clicked on SAve button..")
        except Exception as ex:
            self.logger.info(f"upload_image_and_create_a_note ex: {ex.args}")

    def verify_enrollment_create_note_panel_displayed(self):
        try:
            panel_heading = self.explicit_wait(5, "XPATH", notes_Read_Ini().create_note_panel_heading(), self.d)
            self.logger.info(f"enrollment create note panel heading visible: {panel_heading.is_displayed()}")
            if panel_heading.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
                self.logger.info(f"enrollment create note  panel is not displayed.")
        except Exception as ex:
            self.logger.info(f"verify_enrollment_create_note_panel_displayed ex: {ex.args}")

    def click_on_add_a_new_note_option(self):
        try:
            add_a_new_note_to_person_option = self.explicit_wait(5, "XPATH", notes_Read_Ini().add_a_new_note_to_person_option_by_xpath(), self.d)
            self.logger.info(f"add_a_new_note_to_person_option_by_xpath is visible: {add_a_new_note_to_person_option.is_displayed()}")
            if add_a_new_note_to_person_option.is_displayed():
                self.status.append(True)
                add_a_new_note_to_person_option.click()
            else:
                self.status.append(False)
                self.logger.info(f"add_a_new_note_to_person_option_by_xpath is not displayed.")

        except Exception as ex:
            self.logger.info(f"click_on_add_a_new_note_option ex: {ex.args}")

    def click_on_Action_Drop_down(self):
        try:
            action_dropdown = self.explicit_wait(5, "XPATH", notes_Read_Ini().get_Action_dropdown_on_notes_page(), self.d)
            self.logger.info(f"action dropdown is visible: {action_dropdown.is_displayed()}")
            if action_dropdown.is_displayed():
                self.status.append(True)
                action_dropdown.click()
            else:
                self.status.append(False)
                self.logger.info(f"action dropdown is not visible.")
        except Exception as ex:
            self.logger.info(f"click_on_Action_Drop_down ex: {ex.args}")

    def verify_no_notes_error_msg_on_enrollment_notes_panel(self):
        try:
            time.sleep(web_driver.one_second)
            no_notes_msg = self.d.find_elements(By.XPATH, notes_Read_Ini().no_notes_error_msg_on_enrollment_notes_panel_by_xpath())
            note_associated = self.d.find_elements(By.XPATH, "//ul[@data-items='notes']//li")
            self.logger.info(f"no notes msg is visible: {no_notes_msg[0].is_displayed()}")
            if len(note_associated) > 0:
                self.logger.info(f"Number of Notes associated: {len(note_associated)}")
                return True
            else:
                self.logger.info("no notes msg is displayed...")
                return False
        except Exception as ex:
            self.logger.info(f"verify_no_notes_error_msg_on_enrollment_notes_panel ex: {ex.args}")

    def click_on_notes_btn_on_enrollments_panel(self):
        try:
            notes_btn = self.explicit_wait(5, "XPATH", notes_Read_Ini().notes_btn_by_xpath(), self.d)
            self.logger.info(f"notes btn is visible: {notes_btn.is_displayed()}")
            if notes_btn.is_displayed():
                self.status.append(True)
                notes_btn.click()
            else:
                self.status.append(False)
                self.logger.info(f"notes_btn is not displayed.")

        except Exception as ex:
            self.logger.info(f"click_on_notes_btn_on_enrollments_panel ex: {ex.args}")

    def click_on_extend_menu_on_enrollments_panel(self):
        try:
            extend_menu = self.explicit_wait(5, "XPATH", notes_Read_Ini().tribar_in_notes(), self.d)
            self.logger.info(f"extend btn visible: {extend_menu.is_displayed()}")
            if extend_menu.is_displayed():
                self.status.append(True)
                extend_menu.click()
            else:
                self.status.append(False)
                self.logger.info(f"extend btn is not displayed. ")

        except Exception as ex:
            self.logger.info(f"click_on_extend_menu_on_enrollments_panel ex:{ex.args}")

    def open_enrollments_panel(self):
        try:
            enrollments_menu_item = self.explicit_wait(5, "XPATH", Portal_Menu_Module_read_ini().get_Enrollments_menu_by_xpath(), self.d)
            self.logger.info(f"enrollment menu item is visible: {enrollments_menu_item.is_displayed()}")
            if enrollments_menu_item.is_displayed():
                self.status.append(True)
                enrollments_menu_item.click()
            else:
                self.status.append(False)
                self.logger.info(f"enrollments panel is not displayed.")
        except Exception as ex:
            self.logger.info(f"open_enrollments_panel ex: {ex.args}")



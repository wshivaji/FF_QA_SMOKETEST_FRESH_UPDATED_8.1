import datetime
import time
from pathlib import Path
import re

import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Config_Packages._11_Enrollment_Module_Config_Files.Enrollment_Module_Read_INI import read_enrollment_components
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import \
    Read_Notification_Groups_Components
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login,logout
from All_Config_Packages._12_Identify_and_Enroll_Config_Files.Identify_and_Enroll_Readd_INI import Read_Identify_and_Enroll_Components
from All_POM_Packages.Identify_and_Enroll_Module_POM.Identify_and_Enroll_Module_POM import Identify_And_Enroll_POM


class enrollments_POM(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    now = (datetime.datetime.now())
    DATE_IE = now.strftime('%m/%d/%Y')
    TIME_IE = now.strftime('%H%M')
    AM_PM_IE = now.strftime('%p')

    def Verify_user_is_able_to_see_total_enrollment_count_as_25(self):
        try:
            self.logger.info("Enrollment_module_TC_001 started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            Enrollment_link = self.d.find_element(By.XPATH, read_enrollment_components().Enrollment_link())
            Enrollment_link.click()
            self.logger.info("Enrollment link is clicked")
            time.sleep(web_driver.one_second)
            # self.d.execute_script("arguments[0].scrollIntoView();", )
            Enrollments_count = self.d.find_element(By.XPATH,read_enrollment_components().Total_number_of_enrollments())
            self.logger.info(f"Enrollment count is :,{Enrollments_count.text}")
            self.d.execute_script("arguments[0].scrollIntoView();",Enrollments_count )
            if Enrollments_count.is_displayed():
                self.logger.info("Enrollment count is displayed")
                self.status.append(True)
            else:
                self.logger.info("Enrollment count is not dispalyed")
                self.status.append(False)
            self.logger.info(f"status is {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_Enrollent_01.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Enrollment_01_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IEnrollment_01 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Enrollment_01_Exception.png")
            print(ex.args)
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def Verify_user_is_able_to_perform_enable_mask_enrollment_which_is_in_disable_state(self):
        try:
            self.logger.info("Enrollment_Module_tc_002 started")
            login().login_to_cloud_if_not_done(self.d)

            self.status.clear()

            time.sleep(web_driver.two_second)
            link = self.explicit_wait(10, "XPATH",
                                      Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            upload_photo = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                              .upload_image_by_xpath(), self.d)
            upload_photo.click()
            self.logger.info(f"clicked on upload image icon")
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\disabled.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

        # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)

            enrollment_basis = self.explicit_wait(10, "XPATH",
                                                  Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(2)
            time.sleep(web_driver.two_second)
            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(2)
            # self.Select_Enrollment_Group(2)
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            self.logger.info("region btn clicked")
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            self.logger.info(f"edge name: {edge_name}")
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    self.logger.info(f"region name selected: {region_names[i].text}")
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            # save_btn.click()
            self.logger.info(f"save btn : {save_btn.text}")
            time.sleep(web_driver.two_second)

            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().action_input_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            reported_loss = self.d.find_element(By.XPATH,
                                                Read_Identify_and_Enroll_Components().reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            save_btn = self.d.find_element(By.XPATH,
                                           Read_Identify_and_Enroll_Components().add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.logger.info(f"save btn displayed: {save_btn.is_displayed()}")
                self.status.append(True)
            else:
                self.logger.info(f"save btn displayed: {save_btn.is_displayed()}")
                self.status.append(False)
            self.d.execute_script("arguments[0].click();", save_btn)
            self.logger.info("Enrollment details filled and save btn is clicked")

            try:
                success_msg = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                 .enrollment_success_msg_xpath(), self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.d.refresh()
            title = self.d.find_elements(By.XPATH,
                                         Read_Identify_and_Enroll_Components().add_details_panel_title_panel())

            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components().add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(2)
            Identify_And_Enroll_POM().click_on_logout_button()
            time.sleep(web_driver.two_second)
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_link = self.d.find_element(By.XPATH,read_enrollment_components().Enrollment_link())
            enrollment_link.click()
            time.sleep(web_driver.one_second)
            disabled_text = self.d.find_element(By.XPATH,read_enrollment_components().disabled_text_xpath())
            print(disabled_text.text)
            self.logger.info(f"actual text is {disabled_text.text}")
            actual_text = disabled_text.text
            get_disabled_text = read_enrollment_components().get_disabled_text()
            expected_text = get_disabled_text
            print(get_disabled_text)
            self.logger.info(f"expected text is {get_disabled_text}")
            if actual_text == expected_text:
                self.status.append(True)
                self.logger.info("Disabled subject is visible")
            else:
                self.status.append(False)

            filter_dropdown = self.d.find_element(By.XPATH,read_enrollment_components().filter_dropdown_by_xpath())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)

            disabled_option = self.d.find_element(By.XPATH,read_enrollment_components().disabled_option_())
            disabled_option.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Disabled Enrollment option")

            disabled_enrollments = self.d.find_elements(By.XPATH, read_enrollment_components().enabled_en_list())
            count_of_disabled_enrollments_before = len(disabled_enrollments)
            self.logger.info(f"count_of_disabled_enrollments_before: {count_of_disabled_enrollments_before}")

            select_check_box_of_pending_Enrollment = self.d.find_element(By.XPATH,
                                                                         read_enrollment_components().select_checkbox_of_pending_for_review())
            select_check_box_of_pending_Enrollment.click()
            time.sleep(web_driver.two_second)

            Action_button = self.d.find_element(By.XPATH,
                                                read_enrollment_components().Action_button_on_enrollment_panel())
            Action_button.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Action button")
            enable_enrollment_option_in_Action = self.d.find_element(By.XPATH,
                                                                      read_enrollment_components().enable_enrollment_option_by_xpath())
            enable_enrollment_option_in_Action.click()
            self.logger.info("Clicked on Enable Enrollment option")
            time.sleep(web_driver.two_second)

            disabled_enrollments = self.d.find_elements(By.XPATH, read_enrollment_components().enabled_en_list())
            count_of_disabled_enrollments_after = len(disabled_enrollments)
            self.logger.info(f"count_of_disabled_enrollments_after: {count_of_disabled_enrollments_after}")

            filter_dropdown1 = self.d.find_element(By.XPATH, read_enrollment_components().filter_dropdown_by_xpath())
            filter_dropdown1.click()
            time.sleep(web_driver.one_second)

            enabled_enrollments_option_in_filter = self.d.find_element(By.XPATH,
                                                                       read_enrollment_components().enabled_option_xpath())
            enabled_enrollments_option_in_filter.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Enabled Enrollments filter")

            if count_of_disabled_enrollments_before > count_of_disabled_enrollments_after:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            Identify_And_Enroll_POM().click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_02.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_02_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_02 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_02_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def Verify_user_is_able_to_add_single_face_for_enabled_mask_enrollment(self):
        try:
            self.logger.info("Enrollment_Module_tc_03 started")
            self.status.clear()
            time.sleep(web_driver.one_second)
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().
                                                                     get_it_admin_to_login(),
                                                                     Read_Identify_and_Enroll_Components().
                                                                     get_password_to_login())
            time.sleep(web_driver.one_second)
            Enrollment_link = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                 Enrollment_link(), self.d)
            Enrollment_link.click()
            time.sleep(web_driver.one_second)
            faces_button = self.d.find_element(By.XPATH,read_enrollment_components().faces_button_on_enrollment_panel())
            faces_button.click()
            self.logger.info("clicked on faces button of enrollment to add faces...")
            time.sleep(web_driver.one_second)
            add_face_img_box = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                  add_face_image_box_by_xpath(), self.d)
            add_face_img_box.click()
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\img8.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")
            time.sleep(web_driver.two_second)


            skip_cropping_button = self.explicit_wait(10, "XPATH", read_enrollment_components().skip_cropping_button_xpath(), self.d)
            skip_cropping_button.click()
            self.logger.info("clicked on Skip Cropping button...")
            time.sleep(web_driver.two_second)


            add_photo_button = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                  add_face_button_xpath(), self.d)
            add_photo_button.click()
            self.logger.info("clicked on Add Photo button...")
            time.sleep(web_driver.two_second)
            success_message = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                 success_message_of_add_photo(), self.d)
            if success_message.is_displayed():
                self.logger.info(f"success photo has been  added:, {success_message.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            Identify_And_Enroll_POM().click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_03`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_03_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"test_TC_En_03 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_03_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()


    def Verify_user_is_able_to_add_single_note_for_enabled_mask_enrollment(self):
        try:
            self.logger.info("Enrollment module Tc=04 started")
            self.status.clear()
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_executive_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)
            Enrollment_link = self.d.find_element(By.XPATH, read_enrollment_components().Enrollment_link())
            Enrollment_link.click()
            self.logger.info("clicking on enrollment link  on cloud menu")
            time.sleep(web_driver.one_second)

            extended_menu = self.d.find_element(By.XPATH,read_enrollment_components().extend_menu_icon_by_xpath())
            extended_menu.click()
            self.logger.info("clicking extend menu of an enrollment")
            time.sleep(web_driver.two_second)

            notes_icon = self.d.find_element(By.XPATH, read_enrollment_components().notes_icon_by_xpath())
            notes_icon.click()
            self.logger.info("clicking notes button of an enrollment")
            time.sleep(web_driver.two_second)

            action_button = self.d.find_element(By.XPATH,read_enrollment_components().action_button_in_enrollment_notes())
            action_button.click()
            self.logger.info("clicking action button on enrollment notes panel")
            time.sleep(web_driver.two_second)


            add_notes_to_enrollment = self.d.find_element(By.XPATH,read_enrollment_components().link_to_add_notes_to_an_enrollment_xpath())
            add_notes_to_enrollment.click()
            self.logger.info("clicking add notes to an enrollment option ")
            time.sleep(web_driver.two_second)


            upload_image_to_notes = self.d.find_element(By.XPATH,read_enrollment_components().image_box_to_add_notes())
            upload_image_to_notes.click()
            time.sleep(web_driver.one_second)
            self.logger.info("upload image box xpath")

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\img8.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")
            time.sleep(web_driver.two_second)


            skip_cropping_button = web_driver.explicit_wait(self,5,"XPATH", read_enrollment_components().skip_cropping_button_xpath(),self.d)
            skip_cropping_button.click()
            self.logger.info("clicking on skip cropping button")
            time.sleep(web_driver.two_second)


            add_photo_button = web_driver.explicit_wait(self,5,"XPATH", read_enrollment_components().add_photo_button_xpath(),self.d)
            add_photo_button.click()
            self.logger.info("clicking on add photo button")
            # time.sleep(8)

            location_input = web_driver.explicit_wait(self,5,"XPATH",read_enrollment_components().get_location_store_input_xpath(),self.d)
            location_input.click()
            location_input.send_keys(read_enrollment_components().get_location_data())
            time.sleep(web_driver.one_second)

            case_subject = web_driver.explicit_wait(self,5,"XPATH",read_enrollment_components().get_case_subject_input_xpath(),self.d)
            case_subject.click()
            case_subject.send_keys(read_enrollment_components().get_case_subject_data())
            time.sleep(web_driver.two_second)

            date_of_incident = web_driver.explicit_wait(self,5,"XPATH",read_enrollment_components().get_date_and_incident_by_xpath(),self.d)
            self.dateTimeAMPM(date_of_incident)
            time.sleep(web_driver.two_second)

            save_button = web_driver.explicit_wait(self,5,"XPATH",read_enrollment_components().save_button_xpath(),self.d)
            save_button.click()

            time.sleep(web_driver.one_second)

            notes_list = self.d.find_element(By.XPATH,read_enrollment_components().after_creating_notes_list())
            if notes_list.is_displayed():
                self.logger.info("notes created successfully")
                self.status.append(True)
            else:
                self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_04`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_04_failed.png")
                return False
            else:
                return True

        except Exception as ex:
               self.logger.error(f"test_TC_En_04 got an exception as: {ex}")
               self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_04_Exception.png")
               return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def Verify_user_is_able_to_see_5_subjects_for_pending_review_condition_using_VIP_user_enroll_5_subjects_for_pending_review(self):
        try:
            self.logger.info("Enrollment_tc_05 started")
            self.status.clear()
            Identify_And_Enroll_POM().enroll_5_images("pending")
            Identify_And_Enroll_POM().click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Enrollment_tc_05.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\Enrollment_tc_05.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"Enrollment_tc_05 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\Enrollment_tc_05_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def Verify_approver_user_is_able_to_approve_pending_subjects(self):
        try:
            self.logger.info("enrollment module tc=06 started")
            self.status.clear()
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_approver_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)
            Enrollment_link = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                 Enrollment_link(), self.d)
            Enrollment_link.click()
            time.sleep(web_driver.two_second)

            filter_dropdown = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                 filter_dropdown_by_xpath(), self.d)
            filter_dropdown.click()
            time.sleep(web_driver.one_second)

            pending_for_review_option = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                           pending_for_review_option(), self.d)
            pending_for_review_option.click()
            time.sleep(web_driver.two_second)

            select_check_box_of_pending_Enrollment = self.explicit_wait(10, "XPATH",
                                                                        read_enrollment_components().
                                                                        select_checkbox_of_pending_for_review(), self.d)
            select_check_box_of_pending_Enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("selecting checkbox")

            Action_button = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                               Action_button_on_enrollment_panel(), self.d)
            Action_button.click()
            time.sleep(web_driver.two_second)

            approve_enrollment_option_in_Action = self.explicit_wait(10, "XPATH",
                                                                     read_enrollment_components().
                                                                     Approve_enrollment_option_xpath(), self.d)
            approve_enrollment_option_in_Action.click()
            time.sleep(web_driver.two_second)

            filter_dropdown1 = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                  filter_dropdown_by_xpath(), self.d)
            filter_dropdown1.click()
            time.sleep(web_driver.one_second)

            enabled_enrollments_option_in_filter = self.explicit_wait(10, "XPATH",
                                                                      read_enrollment_components().
                                                                      enabled_option_xpath(), self.d)
            enabled_enrollments_option_in_filter.click()
            time.sleep(web_driver.one_second)

            enabled_text = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                              enabled_text(), self.d)
            if enabled_text.is_displayed():
                self.logger.info("enrollment approved successfully")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            Identify_And_Enroll_POM().click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_03`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_03_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_03 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_03_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def Verify_approver_user_is_able_to_reject_pending_subjects(self):
        try:
            self.logger.info("Enrollment module tc=07 started")
            self.status.clear()
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_approver_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)

            Enrollment_link = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                 Enrollment_link(), self.d)
            Enrollment_link.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on enrollments link")

            filter_dropdown = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                 filter_dropdown_by_xpath(), self.d)
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on filter dropdown")

            pending_for_review_option = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                           pending_for_review_option(), self.d)
            pending_for_review_option.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on pending for review option")

            select_check_box_of_pending_Enrollment = self.explicit_wait(10, "XPATH",
                                                                        read_enrollment_components().
                                                                        select_checkbox_of_pending_for_review(), self.d)
            select_check_box_of_pending_Enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("selecting checkbox")

            Action_button = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                               Action_button_on_enrollment_panel(), self.d)
            Action_button.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on Action dropdown")

            reject_enrollment_option_in_Action = self.explicit_wait(10, "XPATH",
                                                                    read_enrollment_components().
                                                                    reject_enrollment_option(), self.d)
            reject_enrollment_option_in_Action.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on reject enrollment option in action dropdown")

            yes_reject_button = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                   get_rejected_buttton_in_dialouge_tooltip(), self.d)
            time.sleep(web_driver.two_second)
            # yes_reject_button.click()
            self.d.execute_script("arguments[0].click();", yes_reject_button)
            time.sleep(web_driver.one_second)

            filter_dropdown1 = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                  filter_dropdown_by_xpath(), self.d)
            filter_dropdown1.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on filter dropdown")

            rejected_option_in_filter = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                           rejected_enrollment_option_in_filter(), self.d)
            rejected_option_in_filter.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicked on Reject Enrollment option")

            rejected_enrollment_text = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                          rejected_enrollment_text(), self.d)
            if rejected_enrollment_text.is_displayed():
                self.logger.info("rejected text is visible")
                self.status.append(True)
            else:
                self.logger.info("rejected text is not displayed")
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            # logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_07`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_07_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_07 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_07_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def Verify_core_or_itadmin_user_is_able_to_delete_pending_subjects(self):
        try:
            self.logger.info("Enrollment tc_08 started ")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            Enrollment_link = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                 Enrollment_link(), self.d)
            Enrollment_link.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on enrollments link")

            filter_dropdown = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                 filter_dropdown_by_xpath(), self.d)
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on filter dropdown")

            pending_for_review_option = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                           pending_for_review_option(), self.d)
            pending_for_review_option.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on pending for review option")

            select_check_box_of_pending_Enrollment = self.explicit_wait(10, "XPATH",
                                                                        read_enrollment_components().
                                                                        select_checkbox_of_pending_for_review(), self.d)
            select_check_box_of_pending_Enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("selecting checkbox")

            Action_button = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                               Action_button_on_enrollment_panel(), self.d)
            Action_button.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on Action dropdown")

            delete_enrollment_xpath = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                         delete_option_in_action_dropdown(), self.d)
            delete_enrollment_xpath.click()
            time.sleep(web_driver.one_second)
            self.logger.info("deleting enrollment successfully")

            yes_delete_button = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                   yes_delete_button_xpath(), self.d)
            yes_delete_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on yes delete button")

            delete_enrollment_success_msg = self.explicit_wait(10, "XPATH",
                                                               read_enrollment_components().
                                                               delete_enrollment_successfully_message(), self.d)
            if delete_enrollment_success_msg.is_displayed():
                self.logger.info("Enrollment deleted successfully")
                self.status.append(True)
            else:
                self.status.append(False)
                self.status.append("Enrollment is not deleted")
            self.logger.info(f"status: {self.status}")
            Identify_And_Enroll_POM().click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_08`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_08_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_07 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_08_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def Verify_user_is_able_to_enable_the_reject_subject_user_with_all_permissions(self):
        try:
            self.logger.info("enrollment module tc=09 started")
            self.status.clear()
            # login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_user_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)
            self.Verify_approver_user_is_able_to_reject_pending_subjects()
            time.sleep(web_driver.one_second)
            Identify_And_Enroll_POM().click_on_logout_button()
            time.sleep(web_driver.one_second)

            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_approver_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_executive_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)
            Enrollment_link = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                 Enrollment_link(), self.d)
            Enrollment_link.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on enrollments link")
            filter_dropdown1 = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                  filter_dropdown_by_xpath(), self.d)
            filter_dropdown1.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on filter dropdown")

            rejected_option_in_filter = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                           rejected_enrollment_option_in_filter(), self.d)
            rejected_option_in_filter.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on rejected option")

            select_check_box_of_pending_Enrollment = self.explicit_wait(10, "XPATH",
                                                                        read_enrollment_components().
                                                                        select_checkbox_of_pending_for_review(), self.d)
            select_check_box_of_pending_Enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("selected_check_box")

            Action_button = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                               Action_button_on_enrollment_panel(), self.d)
            Action_button.click()
            time.sleep(web_driver.two_second)

            enable_enrollment_option_in_Action = self.explicit_wait(10, "XPATH",
                                                                     read_enrollment_components().
                                                                     enable_enrollment_option_by_xpath(), self.d)
            enable_enrollment_option_in_Action.click()
            time.sleep(web_driver.two_second)
            self.logger.info("enable_enrollment_option clicked")

            filter_dropdown1.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on filter dropdown")

            enabled_option_in_filter = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                           enabled_option_xpath(), self.d)
            enabled_option_in_filter.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on rejected option")

            enabled_text = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                              enabled_text(), self.d)
            if enabled_text.is_displayed():
                self.logger.info("rejected enrollment enabled")
                self.status.append(True)
            else:
                self.logger.info("rejected enrollment is not enabled")
            self.logger.info(f"status: {self.status}")
            Identify_And_Enroll_POM().click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_09`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_09_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_07 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_09_Exception.png")
            return False


            Enrollment_link = self.d.find_element(By.XPATH, read_enrollment_components().Enrollment_link())
            Enrollment_link.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on enrollments link")

            Expired_date_on_enrollment = self.d.find_element(By.XPATH,read_enrollment_components().expired_date_on_enrollment())
            time.sleep(web_driver.one_second)

            if Expired_date_on_enrollment.is_displayed():
                self.logger.info("expired date is visible on enrollment")
                self.status.append(True)
            else:
                self.logger.info("expired date is not visible")
                self.status.append(False)
            Identify_And_Enroll_POM().delete_enrollment()

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_11`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_11_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_11 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_11_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def Enrollments_search_with_filter_dropdown_option_result_should_be_dropdown_options(self):
        try:
            self.logger.info("Enrollment module tc=12 started")
            pass
        except Exception as ex:
            print(ex.args)

    def verify_user_enroller_of_an_enrollment_able_to_link_a_enrollment_group_and_add_the_person_to_the_group(self):
        try:
            self.logger.info("Enrollment_module_tc=13 started")
            login().login_to_cloud_if_not_done(self.d)

            time.sleep(web_driver.one_second)

            self.click_on_Enrollment_link()
            time.sleep(web_driver.one_second)

            self.clicking_on_one_enrollment_group_button()
            time.sleep(web_driver.one_second)

            before_linking_eg_count = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                         get_enrollment_group_count(), self.d)
            print(before_linking_eg_count.text)
            linked_eg_count = before_linking_eg_count.text
            self.logger.info(f"before linking enrolllment group count is : {linked_eg_count}")
            time.sleep(web_driver.two_second)
            self.click_filter_dropdopwn_on_enrollment_group()
            time.sleep(web_driver.one_second)

            unlinked_eg_option = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                    unlinked_eg_option_xpath(), self.d)
            unlinked_eg_option.click()
            self.logger.info("clicked on unlinked eg option")
            time.sleep(web_driver.two_second)

            eg_list = []
            Enrollments_groups_list = self.d.find_elements(By.XPATH,read_enrollment_components().list_of_egs())
            for group in Enrollments_groups_list:
                eg_list.append(group.text)

            self.logger.info(f"list of eg are :{eg_list}")
            time.sleep(web_driver.two_second)
            read_eg_name = Read_Notification_Groups_Components().default_enrollment_group_details()
            read_eg_name = read_eg_name.split(',')
            self.logger.info(f"eg name is :{read_eg_name[0]}")
            time.sleep(web_driver.two_second)
            checkbox_xpath_1 = read_enrollment_components().checkbox_xpath_1()
            checkbox_xpath_2 = read_enrollment_components().checkbox_xpath_2()
            check_box_xpath = f"{checkbox_xpath_1}{read_eg_name[0]}{checkbox_xpath_2}"
            self.logger.info(f"checkbox custom xpath: {check_box_xpath}")
            checkbox = self.d.find_element(By.XPATH, check_box_xpath)

            for i in range(len(Enrollments_groups_list)-1):
                if read_eg_name[0] == Enrollments_groups_list[i].text:
                    time.sleep(web_driver.one_second)
                    checkbox.click()
                    self.logger.info("check box is clicked")
                    self.status.append(True)
                    break

            time.sleep(web_driver.two_second)
            self.Action_dropdown_on_eg()

            add_group_to_enrollment_option = self.explicit_wait(10, "XPATH",
                                                                read_enrollment_components().
                                                                add_group_to_enrollment_option(), self.d)
            add_group_to_enrollment_option.click()
            self.logger.info("add group to enrollment option is clicked inside action dropdown")
            time.sleep(web_driver.two_second)
            self.close_single_panel()
            after_linking_eg_count = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                        after_linking_eg_count(), self.d)
            self.logger.info(f"after linking enrollment group count is :{after_linking_eg_count.text}")
            after_linking_eg_count1 = after_linking_eg_count.text

            if after_linking_eg_count1 != int(linked_eg_count)+1:
                self.logger.info("Enrollment group is linked")
                self.status.append(True)
            else:
                self.logger.info("Enrollment group is not linked")
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            Identify_And_Enroll_POM().click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_11`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_11_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_11 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_11_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()


    def verify_user_enroller_of_an_enrollment_able_to_unlink_same_enrollment_group_and_remove_the_person_from_selected_group(self):
        try:

            self.logger.info("Enrollment_module_tc=12 started")
            login().login_to_cloud_if_not_done(self.d)

            time.sleep(web_driver.one_second)

            self.click_on_Enrollment_link()
            time.sleep(web_driver.one_second)

            self.clicking_on_one_enrollment_group_button()
            time.sleep(web_driver.one_second)

            before_unlinking_eg_count = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                           after_linking_eg_count(), self.d)
            print(before_unlinking_eg_count.text)
            before_unlinked_eg_count = before_unlinking_eg_count.text
            self.logger.info(f"before unlinking enrolllment group count is : {before_unlinked_eg_count}")
            time.sleep(web_driver.one_second)

            eg_list = []
            Enrollments_groups_list = self.d.find_elements(By.XPATH, read_enrollment_components().list_of_egs())
            for group in Enrollments_groups_list:
                eg_list.append(group.text)

            self.logger.info(f"list of eg are :{eg_list}")
            time.sleep(web_driver.one_second)
            read_eg_name = Read_Notification_Groups_Components().default_enrollment_group_details()
            read_eg_name = read_eg_name.split(',')
            self.logger.info(f"eg name is :{read_eg_name[0]}")
            time.sleep(web_driver.two_second)


            checkbox_xpath_1 = read_enrollment_components().checkbox_xpath_1()
            checkbox_xpath_2 = read_enrollment_components().checkbox_xpath_2()
            check_box_xpath = f"{checkbox_xpath_1}{read_eg_name[0]}{checkbox_xpath_2}"
            self.logger.info(f"custom xpath : {check_box_xpath}")
            checkbox = self.d.find_element(By.XPATH, check_box_xpath)

            for i in range(len(Enrollments_groups_list)):
                if read_eg_name[0] == Enrollments_groups_list[i].text:
                    time.sleep(web_driver.one_second)
                    checkbox.click()
                    self.logger.info("check box is clicked")
                    self.status.append(True)
                    break

            time.sleep(web_driver.two_second)
            self.Action_dropdown_on_eg()

            remove_group_to_enrollment_option = self.explicit_wait(10, "XPATH",
                                                                   read_enrollment_components().
                                                                   remove_enrollment_group_to_enrollment(), self.d)
            remove_group_to_enrollment_option.click()
            self.logger.info("add group to enrollment option is clicked inside action dropdown")
            time.sleep(web_driver.one_second)

            self.close_single_panel()

            after_unlinking_eg_count = self.explicit_wait(10, "XPATH", read_enrollment_components().
                                                          get_enrollment_group_count(), self.d)
            self.logger.info(f"after linking enrollment group count is :{after_unlinking_eg_count.text}")
            after_unlinking_eg_count1 = after_unlinking_eg_count.text

            if before_unlinking_eg_count != after_unlinking_eg_count1:
                self.logger.info("Enrollment group is linked")
                self.status.append(True)
            else:
                self.logger.info("Enrollment group is not linked")
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            Identify_And_Enroll_POM().click_on_logout_button()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_12`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_12_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_11 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_12_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def verify_user_able_to_add_more_faces_to_an_enrollment(self):
        try:
            self.logger.info("Enrollment module tc=13 started")
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_executive_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)

            self.click_on_Enrollment_link()
            time.sleep(web_driver.one_second)

            before_adding_faces_count = self.d.find_element(By.XPATH,read_enrollment_components().before_adding_faces_count())
            before_adding_face_count1 = before_adding_faces_count.text
            self.logger.info(f"before adding faces count is : {before_adding_face_count1}")

            self.selecting_one_faces_button()
            time.sleep(web_driver.one_second)

            upload_photo = self.explicit_wait(7, "XPATH", read_enrollment_components()
                                              .image_box_xpath(), self.d)
            upload_photo.click()
            self.logger.info(f"clicked on upload image icon")
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\img4.png."
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")
            time.sleep(web_driver.two_second)

            skip_cropping_button = self.d.find_element(By.XPATH,read_enrollment_components().skip_cropping_button())
            skip_cropping_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on skip cropping button")


            select_photo_button = self.d.find_element(By.XPATH,read_enrollment_components().select_photo_button())
            select_photo_button.click()
            time.sleep(4)
            self.logger.info("clicking on select photo button")

            success_msg = self.d.find_element(By.XPATH,read_enrollment_components().success_photo_added_message())
            self.logger.info(f"success message is {success_msg.text}")

            if success_msg.is_displayed():
                self.logger.info("sucess photo has been added message is displayed")
                self.status.append(True)

            else:
                self.logger.info("success message is not displayed")
                self.status.append(False)



            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_13`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_13_failed.png")
                return False
            else:
                return True
        except Exception as ex:
                self.logger.error(f"test_TC_En_13 got an exception as: {ex}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_13_Exception.png")
                return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def verify_user_enroller_of_an_enrollment_able_to_see_events_for_a_enrolled_person_on_enrrollments_panel(self):
        try:
            self.logger.info("enrollment_module tc 014 started")
            self.status.clear()
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_executive_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)

            self.click_on_Enrollment_link()
            time.sleep(web_driver.one_second)

            self.clicking_on_one_of_the_tribar_button()
            time.sleep(web_driver.one_second)

            self.clicking_on_one_events_buttons()
            time.sleep(web_driver.one_second)

            list_of_events = self.d.find_elements(By.XPATH,read_enrollment_components().list_of_events())
            time.sleep(web_driver.one_second)

            no_events_msg = self.d.find_element(By.XPATH,read_enrollment_components().no_events_msg())

            for event in list_of_events:
                if event.is_displayed():
                    self.logger.info("events are dispalyed")
                    self.status.append(True)
                elif no_events_msg.is_displayed():
                    self.logger.info("There are no events in the system is visible")
                    self.status.append(True)
                else:
                    self.status.append(False)
            #self.close_all_panel_one_by_one()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_14`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_14_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_13 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_14_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def verify_user_enroller_of_an_enrollment_able_to_edit_the_enrollment(self):
        try:
            self.logger.info("enrollment module tc 016 started")
            time.sleep(web_driver.one_second)
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_executive_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            self.status.clear()

            self.click_on_Enrollment_link()
            time.sleep(web_driver.one_second)

            self.clicking_on_one_of_the_tribar_button()
            time.sleep(web_driver.one_second)

            self.click_one_of_details_button_of_enrollment()
            time.sleep(web_driver.one_second)

            self.clicking_on_action_dropdown_on_en_details()
            time.sleep(web_driver.one_second)

            edit_option = self.d.find_element(By.XPATH,read_enrollment_components().edit_option_on_en_details_panel())
            edit_option.click()
            time.sleep(web_driver.one_second)

            case_event_type_dropdown = self.d.find_element(By.XPATH,read_enrollment_components().case_event_type_dropdown())
            select = Select(case_event_type_dropdown)
            select.select_by_index(1)
            time.sleep(web_driver.two_second)

            save_button = self.d.find_element(By.XPATH,read_enrollment_components().save_button_on_en_details())
            save_button.click()
            time.sleep(web_driver.one_second)

            edited_case_event_type = self.d.find_element(By.XPATH,read_enrollment_components().get_edited_text())
            self.logger.info(f"edited case event type : {edited_case_event_type.text}")
            time.sleep(web_driver.one_second)

            case_event_type = read_enrollment_components().read_case_event_type()

            if edited_case_event_type.text == case_event_type:
                self.logger.info("edited case event is edited")
                self.status.append(True)
            else:
                self.logger.info("edited case event is not edited")
                self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_16png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_16_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_13 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_16_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def verify_executive_it_admin_enroller_of_an_enrollment_able_to_delete_enrollment(self):
        try:
            self.logger.info("Enrollment group module tc=17 started")
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_it_admin_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            self.status.clear()
            time.sleep(web_driver.one_second)

            Identify_And_Enroll_POM().Create_New_Enrollment_using_Identify_and_Enroll()
            time.sleep(web_driver.one_second)

            self.click_on_Enrollment_link()
            time.sleep(web_driver.one_second)

            Identify_And_Enroll_POM().delete_enrollment()
            time.sleep(web_driver.one_second)

            delete_enrollment_success_msg = self.d.find_element(By.XPATH,
                                                                read_enrollment_components().delete_enrollment_successfully_message())
            if delete_enrollment_success_msg.is_displayed():
                self.logger.info("Enrollment deleted successfully")
                self.status.append(True)
            else:
                self.status.append(False)
                self.status.append("Enrollment is not deleted")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_03`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_03_failed.png")
                return False
            else:
                return True
        except Exception as ex:
                    self.logger.error(f"test_TC_En_07 got an exception as: {ex}")
                    self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_07_Exception.png")
                    return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()
    def verify_user_able_to_see_rejected_status_for_rejected_enrollment(self):
        try:
            self.logger.info("enrollment module testcases started")
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_operator_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            Action_button = self.d.find_element(By.XPATH, read_enrollment_components().Action_button_on_enrollment_panel())
            Action_button.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on Action dropdown")

            reject_enrollment_option_in_Action = self.d.find_element(By.XPATH,read_enrollment_components().reject_enrollment_option())
            reject_enrollment_option_in_Action.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on reject enrollment option in action dropdown")

            yes_reject_button = self.d.find_element(By.XPATH,
                                                    read_enrollment_components().get_rejected_buttton_in_dialouge_tooltip())
            time.sleep(web_driver.two_second)
            # yes_reject_button.click()
            self.d.execute_script("arguments[0].click();", yes_reject_button)
            time.sleep(web_driver.one_second)

            filter_dropdown1 = self.d.find_element(By.XPATH,read_enrollment_components().filter_dropdown_by_xpath())
            filter_dropdown1.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on filter dropdown")

            rejected_option_in_filter = self.d.find_element(By.XPATH,read_enrollment_components().rejected_enrollment_option_in_filter())
            rejected_option_in_filter.click()
            time.sleep(web_driver.one_second)
            self.logger.info("")

            rejected_enrollment_text = self.d.find_element(By.XPATH,read_enrollment_components().rejected_enrollment_text())
            if rejected_enrollment_text.is_displayed():
                self.logger.info("rejected text is visible")
                self.status.append(True)
            else:
                self.logger.info("rejected text is not dispalyed")
                self.status.append(False)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_03`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_03_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_07 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_07_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def Verify_core_user_or_it_admin_is_able_to_delete_pending_subjects(self):
        try:
            self.logger.info("Enrollment tc_08 started ")
            login().login_to_cloud_if_not_done(self.d)
            Enrollment_link = self.d.find_element(By.XPATH, read_enrollment_components().Enrollment_link())
            Enrollment_link.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on enrollments link")

            filter_dropdown = self.d.find_element(By.XPATH, read_enrollment_components().filter_dropdown_by_xpath())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on filter dropdown")

            pending_for_review_option = self.d.find_element(By.XPATH,
                                                            read_enrollment_components().pending_for_review_option())
            pending_for_review_option.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on pending for review option")

            select_check_box_of_pending_Enrollment = self.d.find_element(By.XPATH,
                                                                         read_enrollment_components().select_checkbox_of_pending_for_review())
            select_check_box_of_pending_Enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("selecting checkbox")

            Action_button = self.d.find_element(By.XPATH, read_enrollment_components().Action_button_on_enrollment_panel())
            Action_button.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on Action dropdown")

            delete_enrollment_xpath = self.d.find_element(By.XPATH,read_enrollment_components().delete_option_in_action_dropdown())
            delete_enrollment_xpath.click()
            time.sleep(web_driver.one_second)
            self.logger.info("deleting enrollment successfully")

            yes_delete_button = self.d.find_element(By.XPATH,read_enrollment_components().yes_delete_button_xpath())
            yes_delete_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on yes delete button")

            delete_enrollment_success_msg = self.d.find_element(By.XPATH,read_enrollment_components().delete_enrollment_successfully_message())
            if delete_enrollment_success_msg.is_displayed():
                self.logger.info("Enrollment deleted successfully")
                self.status.append(True)
            else:
                self.status.append(False)
                self.status.append("Enrollment is not deleted")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_03`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_03_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_07 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_07_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def Verify_user_is_able_to_enable_the_reject_subject_user_with_all_permissionss(self):
        try:
            self.logger.info("enrollment module tc=09 started")
            # login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_user_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)
            self.Verify_approver_user_is_able_to_reject_pending_subjects()
            time.sleep(web_driver.one_second)
            Identify_And_Enroll_POM().click_on_logout_button()
            time.sleep(web_driver.one_second)


            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_approver_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)
            filter_dropdown1 = self.d.find_element(By.XPATH, read_enrollment_components().filter_dropdown_by_xpath())
            filter_dropdown1.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on filter dropdown")

            rejected_option_in_filter = self.d.find_element(By.XPATH,
                                                            read_enrollment_components().rejected_enrollment_option_in_filter())
            rejected_option_in_filter.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on rejected option")
            time.sleep(web_driver.one_second)

            select_check_box_of_pending_Enrollment = self.d.find_element(By.XPATH,
                                                                         read_enrollment_components().select_checkbox_of_pending_for_review())
            select_check_box_of_pending_Enrollment.click()
            time.sleep(web_driver.two_second)
            rejected_text = self.d.find_element(By.XPATH,read_enrollment_components().rejected_enrollment_text())
            if rejected_text.is_displayed():
                self.logger.info("enrollment is rejected")
                self.status.append(True)

            else:
                self.logger.info("enrollment is not rejected")
                self.status.append(False)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_09`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_09_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_09 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_07_Exception.png")
            return False
        finally:
           Identify_And_Enroll_POM().click_on_logout_button()

    def verify_user_able_to_add_notes_for_a_enrolled_person_on_enrollments_panel(self):
        try:
            self.logger.info("enrollmrnt module testcases started")
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_executive_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)
            Enrollment_link = self.d.find_element(By.XPATH, read_enrollment_components().Enrollment_link())
            Enrollment_link.click()
            self.logger.info("clicking on enrollment link  on cloud menu")
            time.sleep(web_driver.one_second)

            extended_menu = self.d.find_element(By.XPATH, read_enrollment_components().extend_menu_icon_by_xpath())
            extended_menu.click()
            self.logger.info("clicking extend menu of an enrollment")
            time.sleep(web_driver.two_second)

            notes_icon = self.d.find_element(By.XPATH, read_enrollment_components().notes_icon_by_xpath())
            notes_icon.click()
            self.logger.info("clicking notes button of an enrollment")
            time.sleep(web_driver.two_second)

            action_button = self.d.find_element(By.XPATH, read_enrollment_components().action_button_in_enrollment_notes())
            action_button.click()
            self.logger.info("clicking action button on enrollment notes panel")
            time.sleep(web_driver.two_second)

            add_notes_to_enrollment = self.d.find_element(By.XPATH,
                                                          read_enrollment_components().link_to_add_notes_to_an_enrollment_xpath())
            add_notes_to_enrollment.click()
            self.logger.info("clicking add notes to an enrollment option ")
            time.sleep(web_driver.two_second)

            upload_image_to_notes = self.d.find_element(By.XPATH, read_enrollment_components().image_box_to_add_notes())
            upload_image_to_notes.click()
            time.sleep(web_driver.one_second)
            self.logger.info("upload image box xpath")

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\ab\\00076.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")
            time.sleep(web_driver.two_second)

            skip_cropping_button = web_driver.explicit_wait(self,5,"XPATH", read_enrollment_components().skip_cropping_button_xpath(),self.d)
            skip_cropping_button.click()
            self.logger.info("clicking on skip cropping button")
            time.sleep(web_driver.two_second)

            add_photo_button = web_driver.explicit_wait(self,10,"XPATH", read_enrollment_components().add_photo_button_xpath(),self.d)
            add_photo_button.click()
            self.logger.info("clicking on add photo button")
            time.sleep(5)

            location_input = web_driver.explicit_wait(self,5,"XPATH", read_enrollment_components().get_location_store_input_xpath(),self.d)
            location_input.click()
            location_input.send_keys(read_enrollment_components().get_location_data())
            time.sleep(web_driver.one_second)

            case_subject = web_driver.explicit_wait(self,5,"XPATH", read_enrollment_components().get_case_subject_input_xpath(),self.d)
            case_subject.click()
            case_subject.send_keys(read_enrollment_components().get_case_subject_data())
            time.sleep(web_driver.two_second)

            date_of_incident = web_driver.explicit_wait(self,5,"XPATH", read_enrollment_components().get_date_and_incident_by_xpath(),self.d)
            self.dateTimeAMPM(date_of_incident)
            time.sleep(web_driver.two_second)

            save_button = self.d.find_element(By.XPATH, read_enrollment_components().save_button_xpath())
            save_button.click()

            time.sleep(web_driver.one_second)

            notes_list = self.d.find_element(By.XPATH, read_enrollment_components().after_creating_notes_list())
            if notes_list.is_displayed():
                self.logger.info("notes created successfully")
                self.status.append(True)
            else:
                self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_04`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_04_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"test_TC_En_04 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_04_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()



    def logout_from_portal(self):
        try:
            logout_btn = self.explicit_wait(5, "XPATH", Read_Identify_and_Enroll_Components().logout_btn_by_xpath(), self.d)
            self.logger.info(f"logout btn is visible: {logout_btn.is_displayed()}")
            if logout_btn.is_displayed():
                logout_btn.click()
            else:
                self.logger.info("logout btn is not visible.")

        except Exception as ex:
            self.logger.info(f"logout_from_portal ex: {ex.args}")

    ###################################3 Userful_methods##############################################
    def click_on_Enrollment_link(self):
        Enrollment_link = self.d.find_element(By.XPATH, read_enrollment_components().Enrollment_link())
        Enrollment_link.click()
        time.sleep(web_driver.two_second)
        self.logger.info("clicking on enrollments link")

    def selecting_first_enrollment_checkbox(self):
        selecting_first_checkbox = self.d.find_element(By.XPATH,
                                                                     read_enrollment_components().select_checkbox_of_pending_for_review())
        time.sleep(web_driver.two_second)
        selecting_first_checkbox.click()
        self.logger.info("clicking on first checkbox of an enrollment")

    def clicking_on_one_enrollment_group_button(self):
        Enrollment_group_button = self.d.find_element(By.XPATH,read_enrollment_components().clicking_on_one_enrollment_group_button())
        time.sleep(web_driver.one_second)
        Enrollment_group_button.click()
        self.logger.info("clicking on enrollment group button")

    def click_filter_dropdopwn_on_enrollment_group(self):
        enrollment_group_filter_dropdown = self.d.find_element(By.XPATH,read_enrollment_components().filter_dropdown_on_enrollment_group())
        enrollment_group_filter_dropdown.click()
        self.logger.info("clicking on enrollment group filter dropdown")

    def Action_dropdown_on_eg(self):
        action_dropdown = self.d.find_element(By.XPATH,read_enrollment_components().action_dropdown_on_eg())
        time.sleep(web_driver.one_second)
        action_dropdown.click()
        self.logger.info("clicking on action dropdown")

    def selecting_one_faces_button(self):
        faces_button = self.d.find_element(By.XPATH,read_enrollment_components().faces_button_by_xpath())
        time.sleep(web_driver.one_second)
        faces_button.click()
        self.logger.info("clicking on faces button")


    def  clicking_on_one_of_the_tribar_button(self):
        tribar_button = self.d.find_element(By.XPATH,read_enrollment_components().select_tribar_button_on_enrollment_panel())
        time.sleep(web_driver.one_second)
        tribar_button.click()
        self.logger.info("clicking on tribar button")

    def clicking_on_one_events_buttons(self):
        events_button = self.d.find_element(By.XPATH,read_enrollment_components().probable_match_events_button())
        time.sleep(web_driver.one_second)
        events_button.click()
        self.logger.info("clicking on events button")

    def click_one_of_details_button_of_enrollment(self):

            details_button = self.d.find_element(By.XPATH,read_enrollment_components().details_button())
            details_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on details button ")

    def clicking_on_action_dropdown_on_en_details(self):
        action = self.d.find_element(By.XPATH,read_enrollment_components().Action_dropdown_on_en_details_panel())
        action.click()
        self.logger.info("clicking on action dropdown option on enrollment details")

    def clicking_on_search_dropdown(self):
        search_dropdown = self.d.find_element(By.XPATH,read_enrollment_components().search_dropdown_xpath())
        search_dropdown.click()
        self.logger.info("clicking on search deopdown")

    def enter_case_subject(self,case_subject):
        try:
            case_subject = self.d.find_element(By.XPATH,read_enrollment_components().case_subject_xpath())
            case_subject.click()
            case_subject.send_keys(case_subject)
            self.logger.info("entering case/subject ")
        except Exception as ex:
            print(ex.args)

    def close_single_panel(self):
        try:
            close_single_panel = self.d.find_element(By.XPATH,read_enrollment_components().close_single_panel())
            close_single_panel.click()
            self.logger.info(f"panel closed successfully")
        except Exception as ex:
            print(ex.args)

            Action_button = self.d.find_element(By.XPATH, read_enrollment_components().Action_button_on_enrollment_panel())
            Action_button.click()
            time.sleep(web_driver.two_second)

            approve_enrollment_option_in_Action = self.d.find_element(By.XPATH,
                                                                      read_enrollment_components().Approve_enrollment_option_xpath())
            approve_enrollment_option_in_Action.click()
            time.sleep(web_driver.two_second)

        except Exception as ex:
            print(ex.args)

    def Verify_if_user_is_enrolled_the_person_with_expiry_date_validate_expired_date_is_visible_on_Enrollment_module_panel(self):
        try:
            self.logger.info("Enrollment module tc=11 started")
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_approver_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.two_second)
            self.logger.info("login with approver user")

            Identify_And_Enroll_POM().Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_and_adding_the_required_details_for_the_same_along_with_expiry_date_and_time_range()
            time.sleep(web_driver.two_second)
            self.logger.info("enrolling a person with expiration date")

            Identify_And_Enroll_POM().click_on_logout_button()
            time.sleep(web_driver.one_second)

            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)

            Enrollment_link = self.d.find_element(By.XPATH, read_enrollment_components().Enrollment_link())
            Enrollment_link.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on enrollments link")

            Expired_date_on_enrollment = self.d.find_element(By.XPATH,read_enrollment_components().expired_date_on_enrollment())
            time.sleep(web_driver.one_second)

            if Expired_date_on_enrollment.is_displayed():
                self.logger.info("expired date is visible on enrollment")
                self.status.append(True)

            else:
                self.logger.info("expired date is not visible")
                self.status.append(False)
            Identify_And_Enroll_POM().delete_enrollment()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_11`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_11_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_11 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_11_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def enrollments_search_with_filter_dropdown_option_result_should_be_dropdown_options(self):
        try:
            self.logger.info("enrollment module started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)

            self.click_on_Enrollment_link()
            time.sleep(web_driver.one_second)

            filter_dropdown = self.d.find_element(By.XPATH,read_enrollment_components().filter_dropdown_by_xpath())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            self.logger.info("filter dropdown option is clicked")

            list_of_filter_dropdown_options = self.d.find_elements(By.XPATH,read_enrollment_components().list_of_filter_dropdown_option())
            for i in list_of_filter_dropdown_options:
                i.click()
                list_en = self.d.find_elements(By.XPATH, read_enrollment_components().list_of_filter_dropdown_option())

                filter_dropdown = self.d.find_element(By.XPATH, read_enrollment_components().filter_dropdown_by_xpath())
                filter_dropdown.click()
                msg = self.d.find_elements(By.XPATH, read_enrollment_components().message_there_are_no_enrollment())
                if len(list_en) > 0:
                    for j in list_en:
                        if j.is_displayed():
                            self.logger.info("list of enrollments are displayed")
                            self.status.append(True)
                        elif msg.is_displayed():

                            self.status.append(True)
                        else:
                            self.status.append(False)
                elif len(msg) > 0:
                     if msg[0].is_displayed():
                         self.logger.info("msg is displayed")
                         self.status.append(True)

                else:
                    self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_11`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_11_failed.png")
                return False
            else:
                return True
        except Exception as ex:
                self.logger.error(f"test_TC_En_11 got an exception as: {ex}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_11_Exception.png")
                return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()


    def verify_user_able_to_see_disabled_status_for_masked_enrollment(self):
        try:
            self.logger.info("Enrollment_Module_tc_002 started")
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_it_admin_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            self.status.clear()
            time.sleep(web_driver.two_second)
            link = self.explicit_wait(10, "XPATH",
                                      Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath(),
                                      self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            upload_photo = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                              .upload_image_by_xpath(), self.d)
            upload_photo.click()
            self.logger.info(f"clicked on upload image icon")
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\disabled1.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH",
                                                  Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(),
                                                  self.d)
            select = Select(enrollment_basis)
            select.select_by_index(2)
            time.sleep(web_driver.two_second)
            enrollment_group = self.d.find_element(By.XPATH,
                                                   Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(2)
            # self.Select_Enrollment_Group(2)
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            self.logger.info("region btn clicked")
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            self.logger.info(f"edge name: {edge_name}")
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    self.logger.info(f"region name selected: {region_names[i].text}")
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            # save_btn.click()
            self.logger.info(f"save btn : {save_btn.text}")
            time.sleep(web_driver.two_second)

            action_input = self.d.find_element(By.XPATH,
                                               Read_Identify_and_Enroll_Components().action_input_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            reported_loss = self.d.find_element(By.XPATH,
                                                Read_Identify_and_Enroll_Components().reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            save_btn = self.d.find_element(By.XPATH,
                                           Read_Identify_and_Enroll_Components().add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.logger.info(f"save btn displayed: {save_btn.is_displayed()}")
                self.status.append(True)
            else:
                self.logger.info(f"save btn displayed: {save_btn.is_displayed()}")
                self.status.append(False)
            self.d.execute_script("arguments[0].click();", save_btn)
            self.logger.info("Enrollment details filled and save btn is clicked")

            try:
                success_msg = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                 .enrollment_success_msg_xpath(), self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.d.refresh()
            title = self.d.find_elements(By.XPATH,
                                         Read_Identify_and_Enroll_Components().add_details_panel_title_panel())

            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components().add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(2)
            logout().logout_from_core(self.d)
            time.sleep(web_driver.two_second)
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_link = self.d.find_element(By.XPATH, read_enrollment_components().Enrollment_link())
            enrollment_link.click()
            time.sleep(web_driver.one_second)
            disabled_text = self.d.find_element(By.XPATH, read_enrollment_components().disabled_text_xpath())
            print(disabled_text.text)
            self.logger.info(f"actual text is {disabled_text.text}")
            actual_text = disabled_text.text
            get_disabled_text = read_enrollment_components().get_disabled_text()
            expected_text = get_disabled_text
            print(get_disabled_text)
            self.logger.info(f"expected text is {get_disabled_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_11`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_11_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_En_11 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_11_Exception.png")
            return False
        finally:
            Identify_And_Enroll_POM().click_on_logout_button()

    def click_on_logout(self):
        try:
            logout_btn = self.explicit_wait(5, "XPATH", read_enrollment_components.logout_btn_by_xpath(), self.d)
            self.logger.info(f"logout btn is visible: {logout_btn.is_displayed()}")
            if logout_btn.is_displayed():
                logout_btn.click()
            else:
                self.logger.info("logout btn is not visible.")

        except Exception as ex:
            self.logger.info(f"logout_from_portal ex: {ex.args}")




















    def dateTimeAMPM(self, date_incident):
        date_incident.send_keys(self.DATE_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(self.TIME_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(self.AM_PM_IE)
        time.sleep(web_driver.one_second)

    def close_all_panel_one_by_one(self):
        pass










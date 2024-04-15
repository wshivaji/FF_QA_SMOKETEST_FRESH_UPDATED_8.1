import datetime
import time
from pathlib import Path

import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Config_Packages._11_Enrollment_Module_Config_Files.Enrollment_Module_Read_INI import read_enrollment_components
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login,logout
from All_Config_Packages._12_Identify_and_Enroll_Config_Files.Identify_and_Enroll_Readd_INI import Read_Identify_and_Enroll_Components
from All_POM_Packages._12_Identify_and_Enroll_Module_POM.Identify_and_Enroll_Module_POM import Identify_And_Enroll_POM


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
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_Enrollent_01.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Enrollment_01_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IEnrollment_01 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Enrollment_01_Exception.png")
            print()

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
            logout().logout_from_core(self.d)
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
            else:
                self.status.append(False)
        # ***************************************Enrollment Process end here**********************

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_00.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_00_failed.png")
                return False
            else:
                return True

        except Exception as ex:
                    self.logger.error(f"test_TC_IE_00 got an exception as: {ex}")
                    self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_00_Exception.png")
                    return False

    def Verify_user_is_able_to_add_single_face_for_enabled_mask_enrollment(self):
        try:
            self.logger.info("Enrollment_Module_tc_23 started")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            Enrollment_link = self.d.find_element(By.XPATH,read_enrollment_components().Enrollment_link())
            Enrollment_link.click()
            time.sleep(web_driver.one_second)
            faces_button = self.d.find_element(By.XPATH,read_enrollment_components().faces_button_on_enrollment_panel())
            faces_button.click()
            time.sleep(web_driver.one_second)
            add_face_img_box = self.d.find_element(By.XPATH,read_enrollment_components().add_face_image_box_by_xpath())
            add_face_img_box.click()
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\img8.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")
            time.sleep(web_driver.two_second)
            skip_cropping_button = self.d.find_element(By.XPATH,read_enrollment_components().skip_cropping_button_xpath())
            skip_cropping_button.click()
            time.sleep(web_driver.two_second)
            add_photo_button = self.d.find_element(By.XPATH,read_enrollment_components().add_photo_button_xpath())
            add_photo_button.click()
            time.sleep(8)
            success_message = self.d.find_element(By.XPATH,read_enrollment_components().success_message_of_add_photo())
            if success_message.is_displayed():
                self.logger.info(f"sucess photo has been  added :",{success_message.text})
                self.status.append(True)
            else:
                self.status.append(False)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_En_02`.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_02_failed.png")
                return False
            else:
                return True

        except Exception as ex:
               self.logger.error(f"test_TC_En_02 got an exception as: {ex}")
               self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_En_02_Exception.png")
               return False

    def Verify_user_is_able_to_add_single_note_for_enabled_mask_enrollment(self):
        try:
            self.logger.info("Enrollment module Tc=05 started")
            login().login_to_cloud_if_not_done(self.d)
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


            skip_cropping_button = self.d.find_element(By.XPATH, read_enrollment_components().skip_cropping_button_xpath())
            skip_cropping_button.click()
            self.logger.info("clicking on skip cropping button")
            time.sleep(web_driver.two_second)


            add_photo_button = self.d.find_element(By.XPATH, read_enrollment_components().add_photo_button_xpath())
            add_photo_button.click()
            self.logger.info("clicking on add photo button")
            time.sleep(8)

            location_input = self.d.find_element(By.XPATH,read_enrollment_components().get_location_store_input_xpath())
            location_input.click()
            location_input.send_keys(read_enrollment_components().get_location_data())
            time.sleep(web_driver.one_second)

            case_subject = self.d.find_element(By.XPATH,read_enrollment_components().get_case_subject_input_xpath())
            case_subject.click()
            case_subject.send_keys(read_enrollment_components().get_case_subject_data())
            time.sleep(web_driver.two_second)

            date_of_incident = self.d.find_element(By.XPATH,read_enrollment_components().get_date_and_incident_by_xpath())
            self.dateTimeAMPM(date_of_incident)
            time.sleep(web_driver.two_second)

            save_button = self.d.find_element(By.XPATH,read_enrollment_components().save_button_xpath())
            save_button.click()

            time.sleep(web_driver.one_second)

            notes_list = self.d.find_element(By.XPATH,read_enrollment_components().after_creating_notes_list())
            if notes_list.is_displayed():
                self.logger.info("notes created successfully")
                self.status.append(True)
            else:
                self.status.append(False)
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


    def Verify_user_is_able_to_see_5_subjects_for_pending_review_condition_using_VIP_user_enroll_5_subjects_for_pending_review(self):
        try:
            self.logger.info("Enrollment_tc_05 started")
            Identify_And_Enroll_POM().enroll_5_images("pending")
        except Exception as ex:
            print(ex)
































    def dateTimeAMPM(self, date_incident):
        date_incident.send_keys(self.DATE_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(self.TIME_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(self.AM_PM_IE)
        time.sleep(web_driver.one_second)

    def close_all_panel_one_by_one(self):
        pass










from selenium.webdriver.support.select import Select

from All_Config_Packages._5_Enrollment_Groups_Config_Files.Enrollment_Groups_Read_INI import Read_Enrollment_Groups_Components
from selenium.webdriver.common.by import By
from All_POM_Packages.Notification_Groups_Module.notification_groups_module_POM import Notification_Groups_Module_pom
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import Read_Notification_Groups_Components
from pathlib import Path
from selenium.webdriver import ActionChains
from Base_Package.Login_Logout_Ops import login, logout
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
import time
import random


def generate_random_number():
    return random.randint(1, 1000)


class Enrollments_Groups_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()

    def Create_5_Enrollment_groups_fill_the_details_and_link_the_particular_NG_to_particular_EG_based_on_naming_convention(self):
        try:
            self.logger.info("********** Test_EG_01 Begin  **********")
            status = []
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            login().login_with_persona_user(self.d, username[4])
            time.sleep(web_driver.one_second)
            x = Read_Enrollment_Groups_Components().get_enrollment_group_name()
            enrollment_group_names_list = x.split(',')
            self.logger.info(f"eg list: {enrollment_group_names_list}")
            count = 0
            for eg in enrollment_group_names_list:
                count = count + 1
                time.sleep(web_driver.one_second)
                enrollment_groups_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                            enrollment_groups_button_by_xpath())
                time.sleep(web_driver.one_second)
                enrollment_groups_btn.click()
                action_btn = web_driver.explicit_wait(self, 5, "XPATH", Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(), self.d)
                time.sleep(web_driver.one_second)
                action_btn.click()
                time.sleep(web_driver.one_second)
                create_enrollment = self.d.find_element(By.XPATH,
                                                        Read_Enrollment_Groups_Components().create_enrollment_group_button_by_xpath())
                create_enrollment.click()
                time.sleep(web_driver.one_second)

                name_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().name_field_by_xpath())
                name_field.send_keys(eg)

                description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().description_field_by_xpath())
                description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())

                time.sleep(web_driver.one_second)
                dp_dwn_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                   .serious_offender_drop_down_by_xpath(), self.d)
                select = Select(dp_dwn_btn)
                options = select.options
                for option in options:
                    value = option.get_attribute("value")
                    if (eg == enrollment_group_names_list[
                        0]) and (value == Read_Enrollment_Groups_Components().serious_offender_high()):
                        select.select_by_visible_text(value)
                        self.logger.info(f"{enrollment_group_names_list[0]} is selected as serious offender {value}")
                    elif (eg == enrollment_group_names_list[
                        1]) and (value == Read_Enrollment_Groups_Components().serious_offender_input_data()):
                        select.select_by_visible_text(value)
                        self.logger.info(f"{enrollment_group_names_list[1]} is selected as serious offender {value}")
                    elif (eg == enrollment_group_names_list[
                        2]) and (value == Read_Enrollment_Groups_Components().serious_offender_low()):
                        select.select_by_visible_text(value)
                        self.logger.info(f"{enrollment_group_names_list[2]} is selected as serious offender {value}")
                    else:
                        pass

                time.sleep(web_driver.two_second)
                save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
                time.sleep(web_driver.one_second)
                save_button.click()

                time.sleep(web_driver.two_second)
                success_message = self.d.find_element(By.XPATH,
                                                      Read_Enrollment_Groups_Components().success_message_by_xpath()).text
                self.logger.info(f"actual message: {success_message}")
                ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
                self.logger.info(f"expected message: {ex_success_msg}")
                if ex_success_msg == success_message:
                    status.append(True)
                else:
                    status.append(False)
                # *************************************************************************
                time.sleep(web_driver.one_second)
                notification_group_btn = self.d.find_element(By.XPATH,
                                                             Read_Enrollment_Groups_Components().notification_group_in_enrollment_group())
                notification_group_btn.click()
                time.sleep(web_driver.one_second)
                filter_button_on_alert = self.d.find_element(By.XPATH,
                                                             Read_Enrollment_Groups_Components().get_filter_btn_on_notification_groups_panel_by_xpath())
                filter_button_on_alert.click()
                time.sleep(web_driver.two_second)
                unlinked_notification_groups = self.d.find_element(By.XPATH,
                                                                   Read_Enrollment_Groups_Components().unlinked_notification_groups())
                unlinked_notification_groups.click()
                time.sleep(web_driver.one_second)
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                x = Read_Notification_Groups_Components().get_notification_group_name()
                notification_group_names_list = x.split(',')

                for i in range(len(alert_groups)-1):
                    if alert_groups[i].text == notification_group_names_list[count-1]:

                        checkbox[i].click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Enrollment_Groups_Components().get_action_dropdown_on_notification_groups_panel_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        add_to_enrollment_group = self.d.find_element(By.XPATH,
                                                                      Read_Enrollment_Groups_Components().get_add_to_enrollment_groups_option_by_xpath())
                        add_to_enrollment_group.click()
                        time.sleep(web_driver.one_second)
                        alert_groups = self.d.find_elements(By.XPATH,
                                                            Read_Notification_Groups_Components().alert_group_list_by_xpath())
                        # users_btn = self.d.find_elements(By.XPATH,
                        #                                  Read_Enrollment_Groups_Components().get_users_btn_on_notification_groups_panel_by_xpath())
                        for j in range(len(alert_groups)):
                            if alert_groups[j].text == notification_group_names_list[count-1]:
                                self.logger.info(
                                    f"{notification_group_names_list[count-1]} alert group linked successfully with enrollment group..")
                                status.append(True)
                        close_panel = self.d.find_elements(By.XPATH,
                                                           Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                        for panels in close_panel:
                            panels.click()
                            time.sleep(web_driver.one_second)
                        break

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_04_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_04_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_04_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_04_exception.png")
            self.logger.error(f"TC_SLT_04 got exception as: {ex.args}")
            return False
        finally:
            logout().logout_from_core(self.d)

    def Verify_total_count_of_EGs_is_6_including_default_EG(self):
        try:
            self.logger.info("********** Test_EG_TC02 Begin  **********")
            status = []
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            login().login_with_persona_user(self.d, username[4])
            time.sleep(web_driver.one_second)
            enrollment_groups_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath())
            time.sleep(web_driver.one_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)

            number_of_egs = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().get_number_of_egs_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"actual count: {number_of_egs.text}")
            expected_ngs = Read_Enrollment_Groups_Components().get_total_number_of_egs()
            time.sleep(web_driver.one_second)
            self.logger.info(f"expected count: {expected_ngs}")
            if expected_ngs in number_of_egs.text:
                status.append(True)
            else:
                status.append(False)
            time.sleep(web_driver.one_second)
            close_panel = self.d.find_element(By.XPATH,
                                               Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            close_panel.click()
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_EG_02_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_EG_02_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_EG_02_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_EG_02_exception.png")
            self.logger.error(f"TC_EG_02 got exception as: {ex.args}")
            return False
        finally:
            logout().logout_from_core(self.d)

    def Verify_for_above_all_5_EG_face_and_mask_threshold_value_should_be_point_83_and_suppress_duplicate_events_value_should_be_0_minute(self):
        try:
            self.logger.info("********** Test_EG_TC03 Begin  **********")
            status = []
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            login().login_with_persona_user(self.d, username[4])
            time.sleep(web_driver.one_second)
            enrollment_groups_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath())
            time.sleep(web_driver.one_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            x = Read_Enrollment_Groups_Components().get_enrollment_group_name()
            enrollment_group_names_list = x.split(',')

            enrollment_group_list = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath())

            for i in range(len(enrollment_group_list)):
                if enrollment_group_list[i].text == enrollment_group_names_list[0]:
                    face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().face_threshold_for_eg_by_xpath())
                    if Read_Enrollment_Groups_Components().default_face_threshold() in face_threshold.text:
                        self.logger.info(f"Face Threshold for {enrollment_group_names_list[0]} is: {Read_Enrollment_Groups_Components().default_face_threshold()}")
                        status.append(True)
                    else:
                        status.append(False)
                    time.sleep(web_driver.one_second)
                    mask_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().masked_face_threshold_for_eg_by_xpath())
                    if Read_Enrollment_Groups_Components().default_masked_face_threshold() in mask_threshold.text:
                        self.logger.info(
                            f"Masked Face Threshold for {enrollment_group_names_list[0]} is: {Read_Enrollment_Groups_Components().default_masked_face_threshold()}")
                        status.append(True)
                    else:
                        status.append(False)
                time.sleep(web_driver.one_second)
                if enrollment_group_list[i].text == enrollment_group_names_list[1]:
                    face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().face_threshold_for_eg_by_xpath())
                    if Read_Enrollment_Groups_Components().default_face_threshold() in face_threshold.text:
                        self.logger.info(f"Face Threshold for {enrollment_group_names_list[1]} is: {Read_Enrollment_Groups_Components().default_face_threshold()}")
                        status.append(True)
                    else:
                        status.append(False)
                    time.sleep(web_driver.one_second)
                    mask_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().masked_face_threshold_for_eg_by_xpath())
                    if Read_Enrollment_Groups_Components().default_masked_face_threshold() in mask_threshold.text:
                        self.logger.info(
                            f"Masked Face Threshold for {enrollment_group_names_list[1]} is: {Read_Enrollment_Groups_Components().default_masked_face_threshold()}")
                        status.append(True)
                    else:
                        status.append(False)
                time.sleep(web_driver.one_second)
                if enrollment_group_list[i].text == enrollment_group_names_list[2]:
                    face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().face_threshold_for_eg_by_xpath())
                    if Read_Enrollment_Groups_Components().default_face_threshold() in face_threshold.text:
                        self.logger.info(f"Face Threshold for {enrollment_group_names_list[2]} is: {Read_Enrollment_Groups_Components().default_face_threshold()}")
                        status.append(True)
                    else:
                        status.append(False)
                    time.sleep(web_driver.one_second)
                    mask_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().masked_face_threshold_for_eg_by_xpath())
                    if Read_Enrollment_Groups_Components().default_masked_face_threshold() in mask_threshold.text:
                        self.logger.info(
                            f"Masked Face Threshold for {enrollment_group_names_list[2]} is: {Read_Enrollment_Groups_Components().default_masked_face_threshold()}")
                        status.append(True)
                    else:
                        status.append(False)
                time.sleep(web_driver.one_second)
                if enrollment_group_list[i].text == enrollment_group_names_list[3]:
                    face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().face_threshold_for_eg_by_xpath())
                    if Read_Enrollment_Groups_Components().default_face_threshold() in face_threshold.text:
                        self.logger.info(f"Face Threshold for {enrollment_group_names_list[3]} is: {Read_Enrollment_Groups_Components().default_face_threshold()}")
                        status.append(True)
                    else:
                        status.append(False)
                    time.sleep(web_driver.one_second)
                    mask_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().masked_face_threshold_for_eg_by_xpath())
                    if Read_Enrollment_Groups_Components().default_masked_face_threshold() in mask_threshold.text:
                        self.logger.info(
                            f"Masked Face Threshold for {enrollment_group_names_list[3]} is: {Read_Enrollment_Groups_Components().default_masked_face_threshold()}")
                        status.append(True)
                    else:
                        status.append(False)
                time.sleep(web_driver.one_second)
                if enrollment_group_list[i].text == enrollment_group_names_list[4]:
                    face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().face_threshold_for_eg_by_xpath())
                    if Read_Enrollment_Groups_Components().default_face_threshold() in face_threshold.text:
                        self.logger.info(f"Face Threshold for {enrollment_group_names_list[4]} is: {Read_Enrollment_Groups_Components().default_face_threshold()}")
                        status.append(True)
                    else:
                        status.append(False)
                    time.sleep(web_driver.one_second)
                    mask_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().masked_face_threshold_for_eg_by_xpath())
                    if Read_Enrollment_Groups_Components().default_masked_face_threshold() in mask_threshold.text:
                        self.logger.info(
                            f"Masked Face Threshold for {enrollment_group_names_list[4]} is: {Read_Enrollment_Groups_Components().default_masked_face_threshold()}")
                        status.append(True)
                    else:
                        status.append(False)
                time.sleep(web_driver.one_second)

            close_panel = self.d.find_element(By.XPATH,
                                              Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            close_panel.click()
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_EG_03_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_EG_03_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_EG_03_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_EG_03_exception.png")
            self.logger.error(f"TC_EG_03 got exception as: {ex.args}")
            return False
        finally:
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_button_on_portal_by_xpath()).click()

    def Verify_user_able_to_create_a_new_Enrollment_Group_by_filling_all_the_fields_and_verify_present_3_buttons_below_are_activated(self):
        try:
            self.logger.info("********** Test_EG_04 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            enrollment_groups_btn.click()
            action_btn = web_driver.explicit_wait(self, 5, "XPATH", Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH",
                                                    Read_Enrollment_Groups_Components().create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("enrollment group details if filled and save btn is clicked")
            enrollments_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                  .enrollment_button_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            status.append(enrollments_text.is_enabled())
            self.logger.info(f"Enrollment btn is activated: {enrollments_text.is_enabled()}")

            notification_groups_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                          .notification_groups_button_by_xpath())
            status.append(notification_groups_text.is_enabled())
            self.logger.info(f"Notification groups btn is activated: {notification_groups_text.is_enabled()}")
            time.sleep(web_driver.one_second)
            events_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                             .events_button_by_xpath())
            status.append(events_text.is_enabled())
            self.logger.info(f"Events btn is activated: {events_text.is_enabled()}")

            close_panel = self.d.find_elements(By.XPATH,
                                              Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            for panels in close_panel:
                panels.click()
                time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}")
            print(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_EG_04_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_EG_04_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_EG_04_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_EG_04_exception.png")
            self.logger.error(f"TC_EG_04 got exception as: {ex.args}")
            return False

    def verify_user_able_to_edit_enrollment_group(self):
        try:
            self.logger.info("********** Test_EG_05 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                               enrollment_groups_button_by_xpath(),
                               self.d)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                         .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("Enrollment groups btn is clicked")
            time.sleep(web_driver.one_second)

            case_groups = self.d.find_elements(By.XPATH,
                                                Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath())
            extends_menu = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().eg_extends_menu_btns_by_xpath())
            details = self.d.find_elements(By.XPATH,
                                           Read_Enrollment_Groups_Components().eg_details_btns_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"total no. of groups: {len(case_groups)}")
            for i in range(len(case_groups)):
                self.logger.info(f"{case_groups[i].text}")
                time.sleep(web_driver.one_second)
                if case_groups[i].text == Read_Enrollment_Groups_Components().name_field_data():
                    extends_menu[i].click()
                    self.logger.info("Clicked on Extends menu button....")
                    time.sleep(web_driver.one_second)
                    details[i].click()
                    self.logger.info("Clicked on Extends menu button....")

            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .enrollment_groups_details_action_dropdown_button_by_xpath(),
                               self.d)
            eg_action_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .enrollment_groups_details_action_dropdown_button_by_xpath())
            eg_action_btn.click()
            self.logger.info("Enrollment group details, action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().edit_button_by_xpath(),
                               self.d)
            edit_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().edit_button_by_xpath())
            time.sleep(web_driver.one_second)
            status.append(edit_btn.is_enabled())
            edit_btn.click()
            self.logger.info("edit option is clicked")

            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().name_field_by_xpath(),
                               self.d)
            new_name_field = self.explicit_wait(10, "XPATH",
                                                Read_Enrollment_Groups_Components().name_field_by_xpath(), self.d)
            new_name_field.clear()
            new_name_field.send_keys(Read_Enrollment_Groups_Components().new_name_field_data())

            new_description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .description_field_by_xpath())
            new_description_field.clear()
            new_description_field.send_keys(Read_Enrollment_Groups_Components().description_field_new_data())
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            status.append(save_button.is_enabled())
            save_button.click()
            self.logger.info("Enrollment group details is modified and save btn is clicked")
            time.sleep(web_driver.two_second)

            close_panel = self.d.find_elements(By.XPATH,
                                               Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            for panels in close_panel:
                panels.click()
                time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_EG_05_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_05_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_EG_05_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_05_exception.png")
            self.logger.error(f"test_TC_EG_05 got exception as: {ex.args}")
            return False

    def verify_user_able_to_link_a_notification_group_from_enrollments_groups_panel(self):
        try:
            self.logger.info("********** Test_EG_06 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            enrollment_groups_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath())
            time.sleep(web_driver.one_second)
            enrollment_groups_btn.click()
            self.logger.info("Enrollment groups button is clicked....")
            action_btn = web_driver.explicit_wait(self, 5, "XPATH", Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Action button clicked.....")
            create_enrollment = self.d.find_element(By.XPATH,
                                                    Read_Enrollment_Groups_Components().create_enrollment_group_button_by_xpath())
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Create Enrollment group button.....")

            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Enrollment_Groups_Components().link_eg1_to_ng1())

            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()

            time.sleep(web_driver.two_second)
            success_message = self.d.find_element(By.XPATH,
                                                  Read_Enrollment_Groups_Components().success_message_by_xpath()).text
            self.logger.info(f"actual message: {success_message}")
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.logger.info(f"expected message: {ex_success_msg}")
            if ex_success_msg == success_message:
                status.append(True)
            else:
                status.append(False)
            # *************************************************************************
            time.sleep(web_driver.one_second)
            notification_group_btn = self.d.find_element(By.XPATH,
                                                         Read_Enrollment_Groups_Components().notification_group_in_enrollment_group())
            notification_group_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Notification groups button is clicked....")
            action_dropdown = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().get_action_dropdown_on_notification_groups_panel_by_xpath())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            create_notification = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath())
            create_notification.click()
            self.logger.info("Create Notification groups button is clicked....")
            # name_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().name_field_by_xpath())
            name_field = web_driver.explicit_wait(self, 10, "XPATH",
                                                  Read_Enrollment_Groups_Components().name_placeholder_on_ng_panel_by_xpath(), self.d)
            name_field.send_keys(Read_Enrollment_Groups_Components().link_ng1_to_eg1())

            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                    description_placeholder_on_ng_panel_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().get_notification_group_description())

            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().second_save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("clicked on Save button..")

            time.sleep(web_driver.two_second)

            filter_button_on_alert = self.d.find_element(By.XPATH,
                                                         Read_Enrollment_Groups_Components().get_filter_btn_on_notification_groups_panel_by_xpath())
            filter_button_on_alert.click()
            time.sleep(web_driver.two_second)
            unlinked_notification_groups = self.d.find_element(By.XPATH,
                                                               Read_Enrollment_Groups_Components().unlinked_notification_groups())
            unlinked_notification_groups.click()
            self.logger.info("Clicked on Unlinked notification groups button....")

            time.sleep(web_driver.one_second)
            alert_groups = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_group_list_by_xpath())
            checkbox = self.d.find_elements(By.XPATH,
                                            Read_Notification_Groups_Components().alert_checkbox_by_xpath())

            for i in range(len(alert_groups)-1):
                if alert_groups[i].text == Read_Enrollment_Groups_Components().link_ng1_to_eg1():
                    checkbox[i].click()
                    time.sleep(web_driver.one_second)
                    self.d.find_element(By.XPATH,
                                        Read_Enrollment_Groups_Components().get_action_dropdown_on_notification_groups_panel_by_xpath()).click()
                    time.sleep(web_driver.one_second)
                    add_to_enrollment_group = self.d.find_element(By.XPATH,
                                                                  Read_Enrollment_Groups_Components().get_add_to_enrollment_groups_option_by_xpath())
                    add_to_enrollment_group.click()
                    self.logger.info("Clicked on Add to Enrollment Group button....")

                    time.sleep(web_driver.one_second)
                    alert_groups = self.d.find_elements(By.XPATH,
                                                        Read_Notification_Groups_Components().alert_group_list_by_xpath())
                    # users_btn = self.d.find_elements(By.XPATH,
                    #                                  Read_Enrollment_Groups_Components().get_users_btn_on_notification_groups_panel_by_xpath())
                    for j in range(len(alert_groups)):
                        if alert_groups[j].text == Read_Enrollment_Groups_Components().link_ng1_to_eg1():
                            self.logger.info(
                                f"{Read_Enrollment_Groups_Components().link_ng1_to_eg1()} alert group linked successfully with enrollment group..")
                            status.append(True)
                    close_panel = self.d.find_elements(By.XPATH,
                                                       Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                    for panels in close_panel:
                        panels.click()
                        time.sleep(web_driver.one_second)
                    break

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_EG_06_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_EG_06_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_EG_06_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_EG_06_exception.png")
            self.logger.error(f"TC_EG_06 got exception as: {ex.args}")
            return False

    def verify_user_able_to_unlink_a_notification_group_from_enrollments_groups_panel(self):
        try:
            self.logger.info("********** Test_EG_07 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            enrollment_groups_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath())
            self.logger.info(f"enrollment groups btn visible: {enrollment_groups_btn.is_displayed()}")
            time.sleep(web_driver.one_second)
            enrollment_groups_btn.click()

            enrollment_groups = web_driver.explicit_wait(self, 5, "XPATH", Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath(), self.d)
            enrollment_groups = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath())
            notification_icon = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().notification_icon_btns_on_eg_panel())
            self.logger.info(f"enrollment groups length: {len(enrollment_groups)}")
            for i in range(len(enrollment_groups)):
                if enrollment_groups[i].text == Read_Enrollment_Groups_Components().link_eg1_to_ng1():
                    self.logger.info(f"enrollment group: {enrollment_groups[i].text}")
                    notification_icon[i].click()
                    time.sleep(web_driver.one_second)
                    checkbox = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().linked_ng_checkbox_by_xpath())
                    self.logger.info(f"checkbox length: {len(checkbox)}")
                    notification_groups = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().linked_notification_groups_list_by_xpath())
                    self.logger.info(f"notification groups length: {len(notification_groups)}")
                    for j in range(len(notification_groups)):
                        if notification_groups[j].text == Read_Enrollment_Groups_Components().link_ng1_to_eg1():
                            self.logger.info(f"notification group text: {notification_groups[j].text}")
                            checkbox[j].click()
                            time.sleep(web_driver.one_second)
                            status.append(True)
                            action_dropdown = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().get_action_dropdown_on_notification_groups_panel_by_xpath())
                            self.logger.info(f"action dropdown visible: {action_dropdown.is_displayed()}")

                            action_dropdown.click()
                            time.sleep(web_driver.one_second)
                            remove_from_eg = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().remove_from_eg_on_ng_panel_by_xpath())
                            self.logger.info(f"option visible: {remove_from_eg.text}")
                            remove_from_eg.click()
                            status.append(True)
                            time.sleep(web_driver.one_second)

                            close_panel = self.d.find_elements(By.XPATH,
                                                               Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                            self.logger.info(f"panel count: {len(close_panel)}")
                            for panels in close_panel:
                                self.logger.info("closing panel...")
                                panels.click()
                                time.sleep(web_driver.one_second)

                            break
                    break
            self.logger.info(f"status: {status}")

            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_EG_07_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_EG_07_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_EG_07_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_EG_07_exception.png")
            self.logger.error(f"TC_EG_07 got exception as: {ex.args}")
            return False

    def verify_user_able_to_see_enrollments_from_associated_group(self):
        try:
            self.logger.info("***************** test_TC_EG_08 **************************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)

            enrollment_groups = web_driver.explicit_wait(self, 5, "XPATH",
                                                         Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath(),
                                                         self.d)
            enrollment_groups = self.d.find_elements(By.XPATH,
                                                     Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath())

            linked_enrollments_count = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().linked_enrollments_count_on_icon_by_xpath())

            for i in range(len(linked_enrollments_count)):
                linked_enrollments_count[i].click()
                self.logger.info("Enrollment icon btn is clicked")
                time.sleep(web_driver.one_second)
                enrollment_in_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                        .enrollment_in_text_title_by_xpath(), self.d)
                if enrollment_in_text.is_displayed():
                    status.append(True)
                    self.logger.info(f"Enrollment panel title is visible: {enrollment_in_text.is_displayed()}")
                else:
                    status.append(False)
                time.sleep(web_driver.one_second)

                linked_enrollments_list = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().list_of_linked_enrollments_by_xpath())
                self.logger.info(f"{i+1}. linked enrollments count on panel is: {len(linked_enrollments_list)}")
                self.logger.info(f"{i+1}. linked enrollments count on icon btn is: {linked_enrollments_count[i].text}")
                if str(len(linked_enrollments_list)) == str(linked_enrollments_count[i].text):
                    status.append(True)
                else:
                    status.append(False)

                close_panel = self.d.find_elements(By.XPATH,
                                                   Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                self.logger.info(f"panel count: {len(close_panel)}")
                for j in range(len(close_panel)-1):
                    close_panel[j + 1].click()
                    self.logger.info("closing panel...")
                    time.sleep(web_driver.one_second)

            close_panel = self.d.find_element(By.XPATH,
                                               Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            close_panel.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_08_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_08_Exception.png")
            self.logger.info(f"test_TC_EG_08 got exception as: {ex}")
            return False

    def verify_user_able_to_see_possible_match_events_associated_to_enrollements_group_and_possible_match_events_associated_to_details_of_enrollment_group_for_both_event_count_should_be_match(self):
        try:
            self.logger.info("*********************** test_TC_EG_09 *********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("Enrollment Groups btn is clicked")

            x = Read_Enrollment_Groups_Components().get_enrollment_group_name()
            enrollment_group_names_list = x.split(',')

            enrollment_groups_list = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath())
            extends_menu = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().eg_extends_menu_btns_by_xpath())
            details_icon = self.d.find_elements(By.XPATH,
                                                Read_Enrollment_Groups_Components().eg_details_btns_by_xpath())
            events_count1 = 0
            events_count2 = 0
            for i in range(len(enrollment_groups_list)):
                if enrollment_groups_list[i].text == enrollment_group_names_list[0]:
                    time.sleep(web_driver.one_second)
                    self.logger.info(f"{enrollment_group_names_list[0]} is selected..")
                    extends_menu[i].click()
                    time.sleep(web_driver.one_second)

                    events_icon = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().probable_match_events_icon_by_xpath())
                    events_icon[i].click()
                    time.sleep(web_driver.one_second)
                    self.logger.info("In Enrollment Groups panel, events icon btn is clicked")

                    events_list = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().events_list_by_xpath())

                    events_count1 = events_count1 + len(events_list)
                    close_panel = self.d.find_elements(By.XPATH,
                                                       Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                    self.logger.info(f"panel count: {len(close_panel)}")
                    for j in range(len(close_panel) - 1):
                        close_panel[j + 1].click()
                        self.logger.info("closing panel...")
                        time.sleep(web_driver.one_second)

                    extends_menu[i].click()
                    time.sleep(web_driver.one_second)

                    details_icon[i].click()
                    time.sleep(web_driver.one_second)
                    self.logger.info("In Enrollment Groups panel, details icon btn is clicked")

                    events_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().events_button_by_xpath())
                    if events_button.is_displayed():
                        status.append(True)
                        events_button.click()
                    else:
                        status.append(False)
                    time.sleep(web_driver.two_second)
                    events_list = self.d.find_elements(By.XPATH,
                                                       Read_Enrollment_Groups_Components().events_list_by_xpath())

                    events_count2 = events_count2 + len(events_list)

                    if events_count1 == events_count2:
                        self.logger.info(f"Events count on both panels are same...")
                        status.append(True)
                    else:
                        status.append(False)
                    break

            close_panel = self.d.find_elements(By.XPATH,
                                               Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            self.logger.info(f"panel count: {len(close_panel)}")
            for panels in close_panel:
                panels.click()
                time.sleep(web_driver.one_second)

            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_09_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_09_Exception.png")
            self.logger.info(f"test_TC_EG_09 got exception as: {ex}")
            return False

    def verify_user_able_to_link_the_enrollments_from_enrollments_groups_panel(self):
        try:
            self.logger.info("*********************** test_TC_EG_010 *********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("Enrollment Groups btn is clicked")

            x = Read_Enrollment_Groups_Components().default_enrollment_group_details()
            enrollment_group_names_list = x.split(',')

            enrollment_groups = web_driver.explicit_wait(self, 5, "XPATH",
                                                         Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath(),
                                                         self.d)
            enrollment_groups = self.d.find_elements(By.XPATH,
                                                     Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath())

            linked_enrollments_count = self.d.find_elements(By.XPATH,
                                                            Read_Enrollment_Groups_Components().linked_enrollments_count_on_icon_by_xpath())

            for i in range(len(linked_enrollments_count)):
                if enrollment_groups[i].text == enrollment_group_names_list[0]:
                    linked_enrollments_count[i].click()
                    self.logger.info("Enrollment icon btn is clicked")
                    time.sleep(web_driver.one_second)
                    enrollment_in_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                            .enrollment_in_text_title_by_xpath(), self.d)
                    if enrollment_in_text.is_displayed():
                        status.append(True)
                        self.logger.info(f"Enrollment panel title is visible: {enrollment_in_text.is_displayed()}")
                    else:
                        status.append(False)
                        time.sleep(web_driver.one_second)

                    self.explicit_wait(10, "XPATH",
                                       Read_Enrollment_Groups_Components().enroll_filter_button_by_xpath(),
                                       self.d)
                    filter_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enroll_filter_button_by_xpath())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"filer btn visible: {filter_button.is_displayed()}")
                    filter_button.click()
                    self.logger.info(f"filter dropdown is clicked")
                    time.sleep(web_driver.two_second)
                    self.explicit_wait(10, "XPATH",
                                       Read_Enrollment_Groups_Components().unlinked_enrollments_by_xpath(),
                                       self.d)
                    unlinked_enroll = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().unlinked_enrollments_by_xpath())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"unlinked enrollment btn visible: {unlinked_enroll.is_displayed()}")
                    unlinked_enroll.click()
                    self.logger.info(f"Unlinked enrollment option is clicked")
                    time.sleep(web_driver.two_second)
                    enroll_check_box = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enroll_check_box())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)

                    enroll_check_box.click()
                    time.sleep(web_driver.one_second)

                    self.explicit_wait(10, "XPATH",
                                       Read_Enrollment_Groups_Components().enrollment_groups_details_action_dropdown_button_by_xpath(),
                                       self.d)
                    action_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_groups_details_action_dropdown_button_by_xpath())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"action btn visible: {action_btn.is_displayed()}")
                    action_btn.click()
                    self.logger.info(f"action dropdown is clicked")
                    time.sleep(web_driver.one_second)
                    self.explicit_wait(10, "XPATH",
                                       Read_Enrollment_Groups_Components().add_enrollments_to_groups(),
                                       self.d)
                    add_enrollment_to_groups = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().add_enrollments_to_groups())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"add_enrollment_to_groups visible: {add_enrollment_to_groups.is_displayed()}")
                    if add_enrollment_to_groups.is_displayed():
                        add_enrollment_to_groups.click()
                        self.logger.info(f"Enrollment added to group...")
                        time.sleep(web_driver.one_second)
                        status.append(True)
                    else:
                        self.logger.info(f"Enrollment not added to group...")
                        status.append(False)
                    break

            close_panel = self.d.find_elements(By.XPATH,
                                              Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            for panels in close_panel:
                panels.click()
                time.sleep(web_driver.one_second)

            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_010_failed.png")

                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_010_Exception.png")
            self.logger.info(f"test_TC_EG_010 got exception as: {ex}")
            return False

    def verify_user_able_to_unlink_the_enrollments_from_enrollments_groups_panel(self):
        try:
            self.logger.info("*********************** test_TC_EG_011 *********************")
            Enrollments_Groups_Module_pom().verify_user_able_to_link_the_enrollments_from_enrollments_groups_panel()
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("Enrollment Groups btn is clicked")

            x = Read_Enrollment_Groups_Components().default_enrollment_group_details()
            enrollment_group_names_list = x.split(',')

            enrollment_groups = web_driver.explicit_wait(self, 5, "XPATH",
                                                         Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath(),
                                                         self.d)
            enrollment_groups = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath())

            linked_enrollments_count = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().linked_enrollments_count_on_icon_by_xpath())

            for i in range(len(linked_enrollments_count)):
                if enrollment_groups[i].text == enrollment_group_names_list[0]:
                    linked_enrollments_count[i].click()
                    self.logger.info("Enrollment icon btn is clicked")
                    time.sleep(web_driver.one_second)
                    enrollment_in_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                            .enrollment_in_text_title_by_xpath(), self.d)
                    if enrollment_in_text.is_displayed():
                        status.append(True)
                        self.logger.info(f"Enrollment panel title is visible: {enrollment_in_text.is_displayed()}")
                    else:
                        status.append(False)
                        time.sleep(web_driver.one_second)

                    time.sleep(web_driver.two_second)
                    enroll_check_box = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enroll_check_box())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)

                    enroll_check_box.click()
                    time.sleep(web_driver.one_second)

                    self.explicit_wait(10, "XPATH",
                                       Read_Enrollment_Groups_Components().enrollment_groups_details_action_dropdown_button_by_xpath(),
                                       self.d)
                    action_btn = self.d.find_element(By.XPATH,
                                                     Read_Enrollment_Groups_Components().enrollment_groups_details_action_dropdown_button_by_xpath())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"action btn visible: {action_btn.is_displayed()}")
                    action_btn.click()
                    self.logger.info(f"action dropdown is clicked")
                    time.sleep(web_driver.one_second)
                    self.explicit_wait(10, "XPATH",
                                       Read_Enrollment_Groups_Components().add_enrollments_to_groups(),
                                       self.d)
                    remove_enrollment_from_groups = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().remove_enrollments_from_group_by())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"remove_enrollment_from_groups visible: {remove_enrollment_from_groups.is_displayed()}")
                    if remove_enrollment_from_groups.is_displayed():
                        remove_enrollment_from_groups.click()
                        self.logger.info(f"Enrollment removed from group...")
                        time.sleep(web_driver.one_second)
                        status.append(True)
                    else:
                        self.logger.info(f"Enrollment not removed from group...")
                        status.append(False)
                    break

            close_panel = self.d.find_elements(By.XPATH,
                                               Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            for panels in close_panel:
                panels.click()
                time.sleep(web_driver.one_second)

            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_011_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_011_Exception.png")
            self.logger.info(f"test_TC_EG_011 got exception as: {ex}")
            return False

    def verify_user_able_to_delete_newly_created_enrollment_group(self):
        try:
            self.logger.info("*********************** test_TC_EG_012 *******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",
                                                       Read_Enrollment_Groups_Components().
                                                       enrollment_groups_button_by_xpath(),self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH",
                                            Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(),self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                                   create_enrollment_group_button_by_xpath(),self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment option is clicked")
            group_name = Read_Enrollment_Groups_Components().name_field_data() + str(generate_random_number())
            print(group_name)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(group_name)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            self.delete_enrollment_group(group_name)
            time.sleep(web_driver.two_second)
            if self.check_if_the_group_is_deleted(group_name):
                status.append(True)
            else:
                status.append(False)
            close_panel = self.d.find_elements(By.XPATH,
                                               Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            for panels in close_panel:
                panels.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_012_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_012_Exception.png")
            self.logger.info(f"test_TC_EG_012 got an exception as: {ex}")
            return False

    def Verify_details_of_default_enrollment_group(self):
        try:
            self.logger.info("*********************** test_TC_EG_013 *******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",
                                                       Read_Enrollment_Groups_Components().
                                                       enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")

            x = Read_Enrollment_Groups_Components().default_enrollment_group_details()
            default_enrollment_group_details = x.split(',')
            time.sleep(web_driver.one_second)
            enrollment_groups_list = self.d.find_elements(By.XPATH,
                                                          Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath())
            extends_menu = self.d.find_elements(By.XPATH,
                                                Read_Enrollment_Groups_Components().eg_extends_menu_btns_by_xpath())
            details_icon = self.d.find_elements(By.XPATH,
                                                Read_Enrollment_Groups_Components().eg_details_btns_by_xpath())

            for i in range(len(enrollment_groups_list)):
                time.sleep(web_driver.one_second)
                # self.logger.info(f"{default_enrollment_group_details[i]} is visible...")
                if enrollment_groups_list[i].text == default_enrollment_group_details[0]:
                    extends_menu[i].click()
                    time.sleep(web_driver.one_second)
                    details_icon[i].click()

                    time.sleep(web_driver.one_second)
                    default_enrollment_group_details_list = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().default_enrollment_group_details_by_xpath())

                    for j in range(len(default_enrollment_group_details)):
                        if default_enrollment_group_details[j] in default_enrollment_group_details_list[j].text:
                            self.logger.info(f"{default_enrollment_group_details_list[j].text} is visible...")
                            status.append(True)
                        else:
                            status.append(False)
                    break
            time.sleep(web_driver.one_second)
            close_panel = self.d.find_elements(By.XPATH,
                                               Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            for panels in close_panel:
                panels.click()
                time.sleep(web_driver.one_second)

            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_013_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_013_Exception.png")
            self.logger.info(f"test_TC_EG_013 got exception as: {ex}")
            return False

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().close_all_panel_list_in_tags())
            for i in close_panel_list:
                i.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_all_panel_one_by_one_failed.png")
            self.log.info(f"close_all_panel_one_by_one_failed:  {ex}")

    def delete_enrollment_group(self, group_name):
        action = ActionChains(self.d)
        time.sleep(web_driver.two_second)
        check_bx = self.d \
            .find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_group_name_delete(group_name))
        # action.scroll_to_element(check_bx).perform()
        # time.sleep(web_driver.two_second)
        check_bx.click()
        # self.d.execute_script("arguments[0].click();", check_bx)
        time.sleep(web_driver.two_second)
        action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                         action_dropdown_button_by_xpath(), self.d)
        time.sleep(web_driver.two_second)
        action_btn.click()
        time.sleep(web_driver.two_second)
        delete = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().delete_button_by_xpath(), self.d)
        delete.click()
        time.sleep(web_driver.two_second)
        confirm = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                     .delete_popup_yes_btn_by_xpath(), self.d)
        self.d.execute_script("arguments[0].click();", confirm)

    def check_if_the_group_is_deleted(self, group_name):
        group_names = []
        list_ele = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath())
        for e in list_ele:
            group_names.append(e.text)
        return group_name not in group_names

    def select_serious_offender(self, serious_offender):
        ele = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().serious_offender_drop_down_by_xpath())
        select = Select(ele)
        select.select_by_visible_text(serious_offender)

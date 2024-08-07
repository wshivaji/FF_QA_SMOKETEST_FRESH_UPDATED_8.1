import random
import time
from pathlib import Path
from selenium.webdriver.support.select import Select

from All_Config_Packages._1_Portal_Login_Module_Config_Files.Portal_Login_Page_Read_INI import \
    Portal_login_page_read_ini
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import \
    Read_Notification_Groups_Components
from All_Config_Packages._5_Enrollment_Groups_Config_Files.Enrollment_Groups_Read_INI import Read_Enrollment_Groups_Components
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import \
    Portal_Menu_Module_read_ini
from All_Config_Packages._0_login_logout_config_file.login_logout_read_ini import LoginLogout_Read_ini
from Base_Package.Login_Logout_Ops import login, logout


def select_options_value(web_element, value):
    """
    handles drop-down using value
    :param web_element:
    :param value: provide the value present in the value attribute
    :return:
    """
    select = Select(web_element)
    select.select_by_value(value)
    

def select_options_visible_text(web_element, visible_text):
    """
    handles a drop-down using visible text
    :param web_element:
    :param visible_text: provide the visible text of the web element
    :return:
    """
    select = Select(web_element)
    select.select_by_visible_text(visible_text)


def generate_random_number():
    return random.randint(1, 1000)


class Notification_Groups_Module_pom(web_driver, web_logger):
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

    def open_notification_groups_module(self):
        try:
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
        except Exception as ex:
            self.logger.info(f"opening notification module got an exception as: {ex}")

    def close_all_panels(self):
        try:
            time.sleep(web_driver.one_second)
            cloud_menu_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().get_CLOUD_MENU_button_by_xpath())
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)
            close_all_panels_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                          get_close_all_panels_menu_by_xpath())
            if close_all_panels_button.is_displayed():
                close_all_panels_button.click()
            else:
                pass
        except Exception as ex:
            print(ex)

    def Create_5_Notification_groups_fill_the_details_and_link_the_particular_user_to_particular_NG_based_on_naming_convention(self):
        try:
            self.logger.info("********** Test_NG_TC01 Begin  **********")
            status = []

            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            login().login_with_persona_user(self.d, username[4])
            time.sleep(web_driver.one_second)

            x = Read_Notification_Groups_Components().get_dummy_notification_group_name()
            notification_group_names_list = x.split(',')
            self.logger.info(f"notification Groups List: {notification_group_names_list}")
            for ng in notification_group_names_list:
                self.open_notification_groups_module()
                action_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                 action_dropdown_button_by_xpath())
                time.sleep(web_driver.two_second)
                action_btn.click()
                time.sleep(web_driver.one_second)
                create_notification = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                          .create_notification_group_btn_by_xpath())
                create_notification.click()
                # name_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().name_field_by_xpath())
                name_field = web_driver.explicit_wait(self, 10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)
                name_field.send_keys(ng)

                description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                        .description_field_by_xpath())
                description_field.send_keys(Read_Notification_Groups_Components().get_notification_group_description())

                save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
                time.sleep(web_driver.one_second)
                save_button.click()
                time.sleep(web_driver.two_second)
                status.append(Notification_Groups_Module_pom().validate_successful_message())
                time.sleep(web_driver.one_second)
                self.close_all_panels()
            # ------------------------------------------------

            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            self.logger.info(f"username list: {username}")
            y = Read_Notification_Groups_Components().get_notification_group_name()
            notification_group_names_list = y.split(',')
            self.logger.info(f"ng list: {notification_group_names_list}")
            z = Read_Notification_Groups_Components().get_enrollment_group_name()
            enrollment_group_names_list = z.split(',')
            self.logger.info(f"eg list: {enrollment_group_names_list}")
            users_menu = web_driver.explicit_wait(self, 10, "XPATH",
                                                  Portal_Menu_Module_read_ini().get_Users_menu_by_xpath(),
                                                  self.d)
            users_menu.click()
            time.sleep(web_driver.one_second)

            for u in range(len(username)):
                print("username length:", len(username))
                user_search_filter = self.d.find_element(By.XPATH,
                                                         Read_Notification_Groups_Components().search_box_by_xpath())

                user_search_filter.clear()
                user_search_filter.send_keys(username[u])
                user = username[u]
                time.sleep(web_driver.two_second)

                notification_group_icon = self.d.find_element(By.XPATH,
                                                              Read_Notification_Groups_Components().get_notification_group_icon_btn_on_users_panel_by_xpath())
                time.sleep(web_driver.one_second)
                notification_group_icon.click()
                filter_button_on_alert = web_driver.explicit_wait(self, 10, "XPATH",
                                                                  Read_Notification_Groups_Components().get_filter_btn_on_notification_groups_panel_by_xpath(),
                                                                  self.d)
                if filter_button_on_alert.is_displayed():
                    filter_button_on_alert.click()
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                unlinked_notification_groups = self.d.find_element(By.XPATH,
                                                                   Read_Notification_Groups_Components().get_unlinked_notification_groups_btn_by_xpath())
                unlinked_notification_groups.click()
                time.sleep(web_driver.one_second)
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())

                for i in range(len(alert_groups)):
                    self.logger.info(f"{len(alert_groups)}")
                    self.logger.info(f"i:{i}")
                    if alert_groups[i].text == notification_group_names_list[u]:
                        ng_name2 = notification_group_names_list[u]
                        checkbox[i].click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().get_action_dropdown_on_notification_groups_panel_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        add_to_user = web_driver.explicit_wait(self, 10, "XPATH",
                                                               Read_Notification_Groups_Components().get_add_to_user_option_in_action_dropdown_by_xpath(),
                                                               self.d)
                        add_to_user.click()
                        time.sleep(web_driver.two_second)
                        self.logger.info(f"{ng_name2} group successfully linked with user {user}")
                        break
            self.close_all_panels()
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_NG_01_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_NG_01_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_NG_01_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_NG_01_exception.png")
            self.logger.error(f"TC_NG_01 got exception as: {ex.args}")
            return False
        finally:
            logout().logout_from_core(self.d)

    def Verify_total_count_of_NGs_is_6_including_default_NG(self):
        try:
            self.logger.info("********** Test_NG_TC02 Begin  **********")
            status = []
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            login().login_with_persona_user(self.d, username[4])
            self.open_notification_groups_module()

            number_of_ngs = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().get_number_of_ngs_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"actual count: {number_of_ngs.text}")
            expected_ngs = Read_Notification_Groups_Components().get_total_number_of_ngs()
            time.sleep(web_driver.one_second)
            self.logger.info(f"expected count: {expected_ngs}")
            if expected_ngs in number_of_ngs.text:
                status.append(True)
            else:
                status.append(False)

            self.close_all_panels()
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_NG_02_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_NG_02_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_NG_02_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_NG_02_exception.png")
            self.logger.error(f"TC_NG_02 got exception as: {ex.args}")
            return False
        finally:
            logout().logout_from_core(self.d)

    def Verify_user_able_to_create_a_new_Notification_Group_by_filling_all_the_fields_and_verify_present_3_buttons_below_are_activated(self):
        try:
            self.logger.info("********** Test_NG_TC03 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.open_notification_groups_module()

            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create notification option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())

            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            description_field.is_displayed()

            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("notification details if filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            users_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                             .user_button_by_xpath(), self.d)
            status.append(users_text.is_enabled())
            self.logger.info(f"In notification details panel, users btn is activated: {users_text.is_enabled()}")
            time.sleep(web_driver.one_second)
            enrollment_grp_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                      enrollment_group_btn_by_xpath())
            status.append(enrollment_grp_text.is_enabled())
            self.logger.info(f"In Notification details, EG btn is activated : {enrollment_grp_text.is_enabled()}")
            time.sleep(web_driver.one_second)
            events_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                              .event_button_by_xpath())
            status.append(events_text.is_enabled())
            self.logger.info(f"In Notification details, Events btn is activated : {events_text.is_enabled()}")
            self.close_all_panels()
            self.logger.info(f"status: {status}")

            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_03_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_03_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_03_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_03_exception.png")
            self.logger.error(f"test_TC_NG_03 got exception as: {ex.args}")
            return False

    def verify_user_able_to_edit_notification_group(self):
        try:
            self.logger.info("********** Test_NG_TC04 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.open_notification_groups_module()

            alert_groups = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_group_list_by_xpath())
            extends_menu = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().extends_menu_by_xpath())
            details = self.d.find_elements(By.XPATH,
                                           Read_Notification_Groups_Components().alert_details_btn_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"total no. of groups: {len(alert_groups)}")
            for i in range(len(alert_groups)):
                self.logger.info(f"{alert_groups[i].text}")
                time.sleep(web_driver.one_second)
                if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                    extends_menu[i].click()
                    time.sleep(web_driver.one_second)
                    details[i].click()

            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                               .new_second_action_dropdown_button_by_xpath(),
                               self.d)
            second_action_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .new_second_action_dropdown_button_by_xpath())
            second_action_btn.click()
            self.logger.info("Notification group details, action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().edit_button_by_xpath(),
                               self.d)
            edit_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().edit_button_by_xpath())
            status.append(edit_btn.is_enabled())
            edit_btn.click()
            self.logger.info("edit option is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(),
                               self.d)
            new_name_field = self.explicit_wait(10, "XPATH",
                                                Read_Notification_Groups_Components().name_field_by_xpath(), self.d)
            new_name_field.clear()
            new_name_field.send_keys(Read_Notification_Groups_Components().new_name_field_data())

            new_description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                        .description_field_by_xpath())
            new_description_field.clear()
            new_description_field.send_keys(Read_Notification_Groups_Components().description_field_new_data())
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Notification details is modified and save btn is clicked")
            time.sleep(web_driver.two_second)
            self.close_all_panels()
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_04_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_04_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_04_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_04_exception.png")
            self.logger.error(f"test_TC_NG_04 got exception as: {ex.args}")
            return False

    def verify_user_able_to_link_an_enrollments_groups_to_notification_groups(self):
        try:
            self.logger.info("********** Test_NG_TC05 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.open_notification_groups_module()

            action_btn = web_driver.explicit_wait(self, 5, "XPATH",
                                                  Read_Notification_Groups_Components().action_dropdown_button_by_xpath(),
                                                  self.d)
            time.sleep(web_driver.one_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Action button clicked.....")
            create_notification = self.d.find_element(By.XPATH,
                                                    Read_Notification_Groups_Components().create_notification_group_btn_by_xpath())
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Create Notification group button.....")

            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Notification_Groups_Components().link_ng2_to_eg2())

            description_field = self.d.find_element(By.XPATH,
                                                    Read_Notification_Groups_Components().description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info(" Clicked on Save button..")
            time.sleep(web_driver.two_second)
            status.append(self.validate_successful_message())
            # *************************************************************************
            time.sleep(web_driver.one_second)
            enrollment_group_btn = self.d.find_element(By.XPATH,
                                                         Read_Notification_Groups_Components().enrollment_group_btn_by_xpath())
            enrollment_group_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Enrollment groups button is clicked....")
            action_dropdown = self.d.find_element(By.XPATH,
                                                  Read_Notification_Groups_Components().third_action_dropdown_button_by_xpath())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Action dropdown on Enrollment Groups panel")
            create_enrollment_group = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                      .create_enrollment_group_by_xpath())
            create_enrollment_group.click()
            self.logger.info("Create Enrollment groups button is clicked....")
            # name_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().name_field_by_xpath())
            name_field = web_driver.explicit_wait(self, 10, "XPATH",
                                                  Read_Notification_Groups_Components().name_field_by_xpath_enrolment(),
                                                  self.d)
            name_field.send_keys(Read_Notification_Groups_Components().link_eg2_to_ng2())

            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().second_save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("clicked on Save button..")

            time.sleep(web_driver.two_second)

            filter_button_on_case_group = self.d.find_element(By.XPATH,
                                                         Read_Notification_Groups_Components().users_filter_button_by_xpath())
            filter_button_on_case_group.click()
            time.sleep(web_driver.two_second)
            unlinked_enrollment_groups = self.d.find_element(By.XPATH,
                                                               Read_Notification_Groups_Components().unlinked_enrollment_group_by_xpath())
            unlinked_enrollment_groups.click()
            self.logger.info("Clicked on Unlinked enrollment groups button....")

            time.sleep(web_driver.one_second)
            case_groups = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().unlinked_case_groups_list_by_xpath())
            checkbox = self.d.find_elements(By.XPATH,
                                            Read_Notification_Groups_Components().enrollment_groups_checkboxes_by_xpath())

            time.sleep(web_driver.one_second)
            for i in range(len(case_groups)):
                self.logger.info(f"case_groups: {case_groups[i].text}")

                if case_groups[i].is_displayed():
                    status.append(True)
                else:
                    status.append(False)
                time.sleep(web_driver.one_second)

                if case_groups[i].text == Read_Notification_Groups_Components().link_eg2_to_ng2():
                    status.append(True)
                    self.logger.info(f"{Read_Notification_Groups_Components().link_eg2_to_ng2()} = {case_groups[i].text}")
                    time.sleep(web_driver.one_second)
                    checkbox[i].click()

                    self.d.find_element(By.XPATH,
                                        Read_Notification_Groups_Components().third_action_dropdown_button_by_xpath()).click()
                    time.sleep(web_driver.one_second)
                    add_to_enrollment_group = self.d.find_element(By.XPATH,
                                                                  Read_Notification_Groups_Components().add_alert_to_groups())
                    add_to_enrollment_group.click()
                    self.logger.info("Clicked on Add to Notification Group button....")

                    time.sleep(web_driver.one_second)
                    case_groups = self.d.find_elements(By.XPATH,
                                                       Read_Notification_Groups_Components().enrollment_groups_list_by_xpath())
                    # users_btn = self.d.find_elements(By.XPATH,
                    #                                  Read_Enrollment_Groups_Components().get_users_btn_on_notification_groups_panel_by_xpath())
                    for j in range(len(case_groups)):
                        if case_groups[j].text == Read_Notification_Groups_Components().link_eg2_to_ng2():
                            self.logger.info(
                                f"{Read_Notification_Groups_Components().link_eg2_to_ng2()} case group linked successfully with notification group..")
                            status.append(True)

                    self.close_all_panels()
                    break

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_NG_05_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_NG_05_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_NG_05_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_NG_05_exception.png")
            self.logger.error(f"TC_NG_05 got exception as: {ex.args}")
            return False

    def verify_user_able_to_unlink_an_enrollments_groups_from_notification_groups(self):
        try:
            self.logger.info("********** Test_NG_TC06 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.open_notification_groups_module()

            alert_groups = web_driver.explicit_wait(self, 5, "XPATH",
                                                         Read_Notification_Groups_Components().notification_groups_list_by_xpath(),
                                                         self.d)
            enrollment_group_icon = self.d.find_elements(By.XPATH,
                                                     Read_Notification_Groups_Components().enrollment_groups_icon_button_by_xpath())
            alert_groups = self.d.find_elements(By.XPATH,
                                                     Read_Notification_Groups_Components().notification_groups_list_by_xpath())

            self.logger.info(f"alert groups length: {len(alert_groups)}")
            for i in range(len(alert_groups)):
                if alert_groups[i].text == Read_Notification_Groups_Components().link_ng2_to_eg2():
                    self.logger.info(f"alert group: {i}{alert_groups[i].text}")
                    enrollment_group_icon[i].click()
                    time.sleep(web_driver.one_second)
                    checkbox = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().enrollment_groups_checkboxes_by_xpath())
                    self.logger.info(f"checkbox length: {len(checkbox)}")
                    enrollment_groups = self.d.find_elements(By.XPATH,
                                                               Read_Notification_Groups_Components().unlinked_case_groups_list_by_xpath())
                    self.logger.info(f"enrollment groups length: {len(enrollment_groups)}")
                    for j in range(len(enrollment_groups)):
                        if enrollment_groups[j].text == Read_Notification_Groups_Components().link_eg2_to_ng2():

                            self.logger.info(f"enrollment group text: {enrollment_groups[j].text}")

                            checkbox[j].click()
                            self.logger.info("Checkbox is selected...")
                            status.append(True)
                            time.sleep(web_driver.one_second)
                            action_dropdown = self.d.find_element(By.XPATH,
                                                                  Read_Notification_Groups_Components().enrollment_groups_action_dropdown_by_xpath())
                            self.logger.info(f"action dropdown visible: {action_dropdown.is_displayed()}")

                            action_dropdown.click()
                            time.sleep(web_driver.one_second)
                            remove_from_ng = self.d.find_element(By.XPATH,
                                                                 Read_Notification_Groups_Components().remove_alert_from_selected_groups_by_xpath())
                            self.logger.info(f"option visible: {remove_from_ng.text}")
                            if remove_from_ng.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)

                            remove_from_ng.click()
                            self.close_all_panels()
                            break
                    break
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_NG_06_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_NG_06_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_NG_06_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_NG_0_exception.png")
            self.logger.error(f"TC_NG_06 got exception as: {ex.args}")
            return False

    def verify_user_able_to_see_events_associated_to_Notification_group_and_events_associated_to_details_of_Notification_group_for_both_event_count_should_be_match(self):
        try:
            self.logger.info("********** Test_NG_TC07 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.open_notification_groups_module()

            y = Read_Notification_Groups_Components().get_notification_group_name()
            notification_group_names_list = y.split(',')

            notification_groups_list = self.d.find_elements(By.XPATH,
                                                          Read_Notification_Groups_Components().notification_groups_list_by_xpath())
            extends_menu = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().extends_menu_by_xpath())
            details_icon = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_details_btn_by_xpath())
            events_count1 = 0
            events_count2 = 0

            for i in range(len(notification_groups_list)):
                if notification_groups_list[i].text == notification_group_names_list[0]:
                    time.sleep(web_driver.one_second)
                    self.logger.info(f"{notification_group_names_list[0]} is selected..")
                    extends_menu[i].click()
                    time.sleep(web_driver.one_second)

                    events_icon = self.d.find_elements(By.XPATH,
                                                       Read_Notification_Groups_Components().probable_match_event_icon_btn_by_xpath())
                    events_icon[i].click()
                    time.sleep(web_driver.one_second)
                    self.logger.info("In Notification Groups panel, events icon btn is clicked")

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
                    self.logger.info("In Notification Groups panel, details icon btn is clicked")

                    events_button = self.d.find_element(By.XPATH,
                                                        Read_Enrollment_Groups_Components().events_button_by_xpath())
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

            self.close_all_panels()
            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_07_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_07_Exception.png")
            self.logger.info(f"test_TC_NG_07 got exception as: {ex}")
            return False

    def verify_user_able_to_link_a_user_to_notification_group(self):
        try:
            self.logger.info("********** Test_NG_TC08 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.open_notification_groups_module()

            y = Read_Notification_Groups_Components().get_notification_group_name()
            notification_group_names_list = y.split(',')

            notification_groups = web_driver.explicit_wait(self, 5, "XPATH",
                                                           Read_Notification_Groups_Components().
                                                           notification_groups_list_by_xpath(), self.d)
            notification_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().
                                                       notification_groups_list_by_xpath())

            linked_users_count = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().
                                                      linked_users_count_on_users_icon_by_xpath())
            time.sleep(web_driver.one_second)
            for i in range(len(linked_users_count)):
                if notification_groups[i].text == notification_group_names_list[1]:
                    linked_users_count[i].click()
                    self.logger.info("Users icon btn is clicked")
                    time.sleep(web_driver.one_second)

                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().users_filter_button_by_xpath(),
                                       self.d)
                    filter_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                        users_filter_button_by_xpath())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"filer btn visible: {filter_button.is_displayed()}")
                    filter_button.click()
                    self.logger.info(f"filter dropdown is clicked")
                    time.sleep(web_driver.two_second)
                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().unlinked_users_option_by_xpath(),
                                       self.d)
                    unlinked_users = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                         unlinked_users_option_by_xpath())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"unlinked users btn visible: {unlinked_users.is_displayed()}")
                    unlinked_users.click()
                    self.logger.info(f"Unlinked users option is clicked")
                    time.sleep(web_driver.two_second)
                    user_check_box = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().
                                                         users_checkboxes_by_xpath())
                    unlinked_users = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().users_list_by_xpath())

                    for j in range(len(unlinked_users)):
                        time.sleep(web_driver.one_second)
                        if unlinked_users[j].text == LoginLogout_Read_ini().get_username():
                            user_check_box[j].click()
                            time.sleep(web_driver.one_second)
                            self.logger.info(f"user selected as: {unlinked_users[j].text}")
                            status.append(True)
                            break
                    else:
                        status.append(False)

                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().user_action_drpdwn_button_by_xpath(),
                                       self.d)
                    action_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                     user_action_drpdwn_button_by_xpath())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"action btn visible: {action_btn.is_displayed()}")
                    action_btn.click()
                    self.logger.info(f"action dropdown is clicked")
                    time.sleep(web_driver.one_second)
                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().add_users_by_xpath(),
                                       self.d)
                    add_user_to_groups = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                             add_users_by_xpath())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"add_users_by_xpath visible: {add_user_to_groups.is_displayed()}")
                    if add_user_to_groups.is_displayed():
                        add_user_to_groups.click()
                        self.logger.info(f"{LoginLogout_Read_ini().get_username()} user added to {notification_group_names_list[1]}")
                        time.sleep(web_driver.one_second)
                        status.append(True)
                    else:
                        self.logger.info(f"User not added to group...")
                        status.append(False)
                    break
            else:
                status.append(False)
            self.close_all_panels()

            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_08_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_08_Exception.png")
            self.logger.info(f"test_TC_NG_08 got exception as: {ex}")
            return False

    def verify_user_able_to_unlink_a_user_to_notification_group(self):
        try:
            self.logger.info("********** Test_NG_TC09 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.open_notification_groups_module()

            y = Read_Notification_Groups_Components().get_notification_group_name()
            notification_group_names_list = y.split(',')

            notification_groups = web_driver.explicit_wait(self, 5, "XPATH",
                                                           Read_Notification_Groups_Components().
                                                           notification_groups_list_by_xpath(), self.d)
            notification_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().
                                                       notification_groups_list_by_xpath())

            linked_users_count = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().
                                                      linked_users_count_on_users_icon_by_xpath())
            time.sleep(web_driver.one_second)
            for i in range(len(linked_users_count)):
                if notification_groups[i].text == notification_group_names_list[1]:
                    linked_users_count[i].click()
                    self.logger.info("Users icon btn is clicked")
                    time.sleep(web_driver.one_second)

                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().check_box_list_by_xpath(),
                                       self.d)
                    users = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().users_list_by_xpath())
                    checkbox = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().users_checkboxes_by_xpath())

                    for i in range(len(users)):
                        time.sleep(web_driver.one_second)
                        if users[i].text == LoginLogout_Read_ini().get_username():
                            checkbox[i].click()
                            self.logger.info(f"{LoginLogout_Read_ini().get_username()} user is selected..")
                            status.append(True)
                            break
                    else:
                        status.append(False)

                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().user_action_drpdwn_button_by_xpath(),
                                       self.d)
                    action_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                     user_action_drpdwn_button_by_xpath())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"action btn visible: {action_btn.is_displayed()}")
                    action_btn.click()
                    self.logger.info(f"action dropdown is clicked")
                    time.sleep(web_driver.one_second)
                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().remove_user_from_group_option_by_xpath(),
                                       self.d)
                    remove_user_from_group = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                             remove_user_from_group_option_by_xpath())
                    web_driver.implicit_wait(self, web_driver.two_second, self.d)
                    self.logger.info(f"remove_user_from_group visible: {remove_user_from_group.is_displayed()}")
                    if remove_user_from_group.is_displayed():
                        remove_user_from_group.click()
                        self.logger.info(f"{LoginLogout_Read_ini().get_username()} user removed from {notification_group_names_list[1]}")
                        time.sleep(web_driver.one_second)
                        status.append(True)
                    else:
                        self.logger.info(f"User not removed from group...")
                        status.append(False)
                    break
            else:
                status.append(False)
            self.close_all_panels()

            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_09_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_09_Exception.png")
            self.logger.info(f"test_TC_NG_09 got exception as: {ex}")
            return False

    def Verify_user_able_to_delete_the_newly_created_notification_group(self):
        try:
            self.logger.info("********** Test_NG_TC10 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)

            self.open_notification_groups_module()
            action_btn = self.explicit_wait(10, "XPATH",
                                            Read_Notification_Groups_Components().action_dropdown_button_by_xpath(),
                                            self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_ng = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                   create_notification_group_btn_by_xpath(), self.d)
            create_ng.click()
            self.logger.info("Create Notification group option is clicked")
            alert_group_name = Read_Notification_Groups_Components().name_field_data() + str(generate_random_number())
            print(alert_group_name)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(alert_group_name)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Notification details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)

            notification_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().
                                                       notification_groups_list_by_xpath())
            checkbox = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_checkbox_by_xpath())
            time.sleep(web_driver.one_second)

            for j in range(len(notification_groups)):
                if notification_groups[j].text == alert_group_name:
                    checkbox[j].click()
                    self.logger.info(f"{notification_groups[j].text} group is selected..")
                    status.append(True)
                    break
            else:
                status.append(False)

            action_btn.click()
            time.sleep(web_driver.one_second)
            delete_notification = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                      .delete_selected_option_by_xpath())
            time.sleep(web_driver.one_second)
            if delete_notification.is_displayed():
                delete_notification.click()
                yes_delete_warning = self.explicit_wait(10, "XPATH",
                                                        Read_Enrollment_Groups_Components().
                                                        delete_popup_yes_btn_by_xpath(), self.d)
                yes_delete_warning = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().delete_popup_yes_btn_by_xpath())
                yes_delete_warning.click()
                time.sleep(web_driver.one_second)
                self.logger.info(f"{alert_group_name} group is deleted..")
                status.append(True)
            else:
                status.append(False)

            self.close_all_panels()
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_10_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_10_Exception.png")
            self.logger.info(f"test_TC_NG_10 got an exception as: {ex}")
            return False

    def Verify_details_of_default_notification_group(self):
        try:
            self.logger.info("*********************** test_TC_NG_012 *******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.open_notification_groups_module()

            x = Read_Notification_Groups_Components().default_notification_group_details()
            default_notification_group_details = x.split(',')
            time.sleep(web_driver.one_second)

            notification_groups_list = self.d.find_elements(By.XPATH,
                                                          Read_Notification_Groups_Components().notification_groups_list_by_xpath())
            extends_menu = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().extends_menu_by_xpath())
            details_icon = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_details_btn_by_xpath())

            for i in range(len(notification_groups_list)):
                time.sleep(web_driver.one_second)
                if notification_groups_list[i].text == default_notification_group_details[0]:
                    extends_menu[i].click()
                    time.sleep(web_driver.one_second)
                    details_icon[i].click()

                    default_notification_group_name = self.explicit_wait(10, "XPATH",
                                                                         Read_Notification_Groups_Components().
                                                                         get_default_alert_group_name_on_details_by_xpath(), self.d)

                    if default_notification_group_name.text == default_notification_group_details[0]:
                        self.logger.info(f"{default_notification_group_name.text} is visible...")
                        status.append(True)
                    else:
                        status.append(False)

                    user_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                  user_button_by_xpath(), self.d)
                    user_btn.click()
                    users_list = self.explicit_wait(10, "XPATH",
                                                    Read_Notification_Groups_Components().users_list_by_xpath(), self.d)
                    users_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().
                                                      users_list_by_xpath())
                    if (len(users_list) == 1) and (users_list[0].text == Portal_login_page_read_ini().
                            get_valid_login_username()):
                        self.logger.info(f"Default User linked with default alert group is: {users_list[0].text}")
                        status.append(True)
                    else:
                        status.append(False)

                    enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                  enrollment_group_btn_by_xpath(), self.d)
                    enrollment_groups_btn.click()
                    case_groups_list = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                          enrollment_groups_list_by_xpath(), self.d)
                    case_groups_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().
                                                            enrollment_groups_list_by_xpath())
                    self.logger.info(f"length of case group list: {len(case_groups_list)}, {case_groups_list[0].text}")
                    default_case_group = Read_Enrollment_Groups_Components().default_enrollment_group_details()
                    default_case_group = default_case_group.split(',')
                    self.logger.info(f"default_case_group name: {default_case_group[0]}")
                    if (len(case_groups_list) == 1) and (case_groups_list[0].text == default_case_group[0]):
                        self.logger.info(f"Default Enrollment Group linked with default alert group is: {case_groups_list[0].text}")
                        status.append(True)
                    else:
                        status.append(False)

            self.close_all_panels()

            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_012_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_012_Exception.png")
            self.logger.info(f"test_TC_NG_012 got exception as: {ex}")
            return False

    # ***************************** Reusable Methods ************************************ #

    def validate_successful_message(self):
        """
        checks if the error message "Success! A user has been created." is displayed.
        """
        ex_result = [True, True]
        ac_result = []
        ele = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().success_message_by_xpath(), self.d)
        msg_validation = ele.text
        self.logger.info(f"actual success msg: {msg_validation}")
        ac_result.append(msg_validation == Read_Notification_Groups_Components().success_message_validation_text())
        self.logger.info(f"expected msg: {Read_Notification_Groups_Components().success_message_validation_text()}")
        ac_result.append(ele.is_displayed())
        if ex_result == ac_result:
            return True
        else:
            return False

    def enter_name(self, name):
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().name_field_by_xpath())
        ele.send_keys(name)

    def enter_description(self, description):
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().description_field_by_xpath())
        ele.send_keys(description)

    def validate_error_msg(self):
        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().validation_error_message_by_xpath(),
                           self.d)
        ele = self.d.find_element(By.XPATH,
                                  Read_Notification_Groups_Components().validation_error_message_by_xpath()).text
        self.logger.info(f"actual msg: {ele}")
        self.logger.info(f"expected msg: {Read_Notification_Groups_Components().validation_error_message_validation_text()}")
        return ele == Read_Notification_Groups_Components().validation_error_message_validation_text()

    def close_all_panel_one_by_one(self):
        time.sleep(web_driver.one_second)
        close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
        if len(close_panel) > 0:
            for i in range(len(close_panel)):
                close_panel[i].click()
                alerts_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().user_close_panel_and_discard_changes())
                if len(alerts_list) > 0:
                    if self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_close_panel_and_discard_changes()).is_displayed():
                        self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_close_panel_and_discard_changes()).click()
                    else:
                        pass
                time.sleep(web_driver.one_second)
        return True

    def close_all_panel_one_by_one_no_popup(self):
        try:
            time.sleep(web_driver.one_second)
            close_panel_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())                                                    
            for i in close_panel_list:
                i.click()
                time.sleep(web_driver.one_second)
            return True

        except Exception as ex:
            self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\close_all_panel_failed_pg_03.png")
            return False

    # ############################################################################

    def click_on_save_btn(self):
        """
        clicks on save button
        """
        save = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
        save.click()

    def enter_user_name(self, user_name):
        """
        fills user name field
        :param user_name:
        """
        user_name_txt_bx = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                              .user_name_by_xpath(), self.d)
        user_name_txt_bx.send_keys(user_name)

    def enter_first_name(self, first_name):
        """
        fills first name field
        :param first_name:
        """
        first_name_txt_bx = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().first_name_by_xpath())
        first_name_txt_bx.send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        fills last name field
        :param last_name:
        """
        last_name_txt_bx = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().last_name_by_xpath())
        last_name_txt_bx.send_keys(last_name)

    def select_user_role(self, role_data_text):
        """
        handles user role drop down using visible text of the element
        :param role_data_text:
        :return:
        """
        user_role_ele = self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().user_role_options_by_xpath())
        sel = Select(user_role_ele)
        sel.select_by_visible_text(role_data_text)

    def enter_password(self, password):
        """
        fills password field
        :param password:
        :return:
        """
        new_password = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().new_password_by_xpath())
        confirm_password = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                               .confirm_password_by_xpath())
        new_password.send_keys(password)
        confirm_password.send_keys(password)

    def select_options_visible_text(web_element, visible_text):
        """
        handles a drop-down using visible text
        :param web_element:
        :param visible_text: provide the visible text of the web element
        :return:
        """
        select = Select(web_element)
        select.select_by_visible_text(visible_text)

    def enter_mis_match_password(self, password, confirm_password):
        """
        fills password field
        :param password:
        :param confirm_password:
        :return:
        """
        new_password = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().new_password_by_xpath())
        conf_password = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().confirm_password_by_xpath())
        new_password.send_keys(password)
        conf_password.send_keys(confirm_password)

    def enter_title(self, title):
        title_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().title_by_xpath())
        title_ele.send_keys(title)

    def enter_department(self, department):
        department_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().department_by_xpath())
        department_ele.send_keys(department)

    def validate_required_user_role_is_selected(self, required_option):
        """
        validate the user role provided is selected.
        :param required_option:
        """
        user_role_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_role_by_xpath())
        select = Select(user_role_ele)
        if select.first_selected_option.text == required_option:
            return True
        else:
            return False

    def select_region(self, region_text):
        """
        This function is used to handle the region drop-down and select the required options
        :param region_text:
        :return:
        """
        region_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().region_by_xpath())
        region_ele.click()
        time.sleep(web_driver.two_second)
        region_text_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().region_list_by_xpath())
        expected_region_text = region_text
        try:
            for i in range(len(region_text_list) + 1):
                actual_zone_text = region_text_list.__getitem__(i).text
                print(actual_zone_text)
                print(expected_region_text)
                if expected_region_text.upper() in actual_zone_text.upper():
                    region_text_list.__getitem__(i).click()
                    break
            save = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().region_save_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", save)
        except Exception as ex:
            str(ex)

    def validate_region(self, region_text):
        """
        validate the selected region is correct
        :param region_text:
        :return:
        """
        region_output = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().region_selected_by_xpath())
        return region_output.text.lower() in str(region_text).lower()

    def select_time_zone(self, use_value):
        """
        selects time zone using the value of the element
        :param use_value:
        :return:
        """
        time_zone = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().time_zone_by_xpath())
        select_options_value(time_zone, use_value)

    def user_email_by_xpath(self, email):
        """
        fills email field
        :param email:
        """
        email_txt_bx = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_email_by_xpath())
        email_txt_bx.send_keys(email)

    def enter_alert_email(self, alert_email):
        """
        fills email field
        :param alert_email:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().alert_email_by_xpath())
        ele.send_keys(alert_email)

    def enter_alert_phone_no(self, alert_phone_no):
        """
        fills email field
        :param alert_phone_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().alert_phone_number_by_xpath())
        ele.send_keys(alert_phone_no)

    def enter_address(self, address):
        """
        fills email field
        :param address:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().address_by_xpath())
        ele.send_keys(address)

    def enter_city(self, city):
        """
        fills email field
        :param city:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().city_by_xpath())
        ele.send_keys(city)

    def enter_state(self, state):
        """
        fills email field
        :param state:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().state_by_xpath())
        ele.send_keys(state)

    def enter_postal_code(self, postal_code):
        """
        fills email field
        :param postal_code:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().postal_code_by_xpath())
        ele.send_keys(postal_code)

    def enter_home_ph_no(self, home_ph_no):
        """
        fills email field
        :param home_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().home_phone_number_by_xpath())
        ele.send_keys(home_ph_no)

    def enter_work_ph_no(self, work_ph_no):
        """
        fills email field
        :param work_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().work_phone_number_by_xpath())
        ele.send_keys(work_ph_no)

    def enter_fax_ph_no(self, fax_ph_no):
        """
        fills email field
        :param fax_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().fax_phone_number_by_xpath())
        ele.send_keys(fax_ph_no)

    def enter_phone_type(self, phone_type):
        """
        fills email field
        :param phone_type:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().phone_type_by_xpath())
        ele.send_keys(phone_type)

    def enter_address2(self, address2):
        """
        fills email field
        :param address2:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().address2_by_xpath())
        ele.send_keys(address2)

    def select_phone_provider(self, phone_provider):
        ph_prov_bx = self.d.find_element(By.XPATH,
                                         Read_Notification_Groups_Components().phone_provider_drop_dwn_by_xpath())
        select = Select(ph_prov_bx)
        select.select_by_visible_text(phone_provider)

    def validate_required_time_zone_is_selected(self, required_option):
        """
        checks if the required time zone is selected
        :param required_option:
        """
        time_zone_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().time_zone_by_xpath())
        select = Select(time_zone_ele)
        selected_option = select.first_selected_option
        selected_value = selected_option.get_attribute("value")
        if selected_value == required_option:
            return True
        else:
            return False

    def validate_error_message(self):
        """
        checks if the error message "PLEASE NOTE: Required Fields Are Incomplete" is displayed.
        """
        ex_result = [True, True]
        ac_result = []
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().error_message_by_xpath())
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Notification_Groups_Components().error_msg_validation_text())
        ac_result.append(ele.is_displayed())
        if ex_result == ac_result:
            return True
        else:
            return False

    def check_if_user_is_created(self, user_name):
        """
        checks if the error message "Success! A user has been created." is displayed.
        """
        ex_result = [True, True, True]
        ac_result = []
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().success_message_by_xpath())
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Notification_Groups_Components().success_msg_validation_text())
        ac_result.append(ele.is_displayed())
        search_box = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().search_box_by_xpath())
        search_box.send_keys(user_name)
        time.sleep(web_driver.one_second)
        user = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().users_list_board_username_by_xpath())
        ac_result.append(user_name == user.text)

        if ex_result == ac_result:
            return True
        else:
            return False

    def time_zone_by_xpath(self):
        try:
            time_zone_by_xpath = self.config.get("LOCATORS", "time_zone_by_xpath")
            return time_zone_by_xpath
        except Exception as ex:
            print(ex)

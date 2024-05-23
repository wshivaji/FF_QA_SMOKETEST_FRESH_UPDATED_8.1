import random
import time
from pathlib import Path
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from All_Config_Packages._12_Identify_and_Enroll_Config_Files.Identify_and_Enroll_Readd_INI import \
    Read_Identify_and_Enroll_Components
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import \
    Read_Notification_Groups_Components
# from All_POM_Package.Portal_Menu_Module.Portal_Menu_POM import Portal_Menu_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login, logout
from All_Other_Utility_Packages.Excel_utilites import XLUtils
from All_Config_Packages._9_tags_module_Config_Files.Tags_Read_INI import Read_Tags_Components


# Test data from excel sheet
test_data = f"{Path(__file__).parent.parent.parent}\\All_Other_Utility_Packages\\Data_From_Excel\\Test_Data_XLSX.xlsx"


class Tags_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    log = web_logger.logger_obj()
    screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"
    '''
    def login_before(self):
        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            self.d.execute_script("arguments[0].click();", login_btn)
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\tags_menu_login_failed.png")
            self.log.info(f"login_before:  {ex}")
            return False
    '''

    def wait_for_element_to_appear(self, element_list, xpath):
        count = 0
        if len(element_list) == 0:
            while len(element_list) == 0 or count == 10:
                element_list = self.d.find_elements(By.XPATH, xpath)
                time.sleep(web_driver.one_second)
                if len(element_list) > 0:
                    self.log.info("element is visible...")
                    return element_list[0]
                else:
                    self.log.info("waiting for element...")
                count += 1
                self.log.info(f"wait count: {count}")
        else:
            self.log.info(f"element length: {len(element_list)}")
            return element_list[0]

    def Create_3_serious_tags_assault_threat_and_push_cart(self):
        # rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')
        try:
            self.log.info("************* test_TC_TAG_01 ***************")
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            login().login_with_persona_user(self.d, username[4])
            time.sleep(web_driver.one_second)
            self.click_on_tags_menu()
            result = []
            x = Read_Tags_Components().read_tags_input_data()
            tags_list = x.split(',')
            self.logger.info(f"eg list: {tags_list}")
            for tag in range(len(tags_list)):
                time.sleep(web_driver.one_second)
                action_button = self.explicit_wait(10, "XPATH", Read_Tags_Components().action_btn_by_xpath(), self.d)
                action_button.click()
                self.logger.info("action button is clicked")
                time.sleep(web_driver.three_second)
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                create_button.click()
                self.logger.info("create button is clicked")
                time.sleep(web_driver.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                tag_name.send_keys(tags_list[tag])
                time.sleep(web_driver.one_second)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                commit.is_displayed()
                serious_event_checkbox = self.d.find_element(By.XPATH,
                                                             Read_Tags_Components().
                                                             get_serious_event_checkbox_by_xpath())
                serious_event_checkbox.click()
                time.sleep(web_driver.one_second)
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                save.click()
                self.logger.info("save button is clicked")
                time.sleep(web_driver.one_second)
                duplicate_tag_msg = self.d.find_element(By.XPATH,Read_Tags_Components().duplicate_tag_msg_by_xpath())

                if duplicate_tag_msg.is_displayed():
                    close_panel = self.d.find_element(By.XPATH,Read_Tags_Components().close_create_tag_panel_by_xpath())

                    close_panel.click()
                    self.logger.info("close panel button is clicked")
                    close_warning = self.d.find_element(By.XPATH,
                                                            Read_Tags_Components().close_panel_and_discard_changes_btn_by_xpath())
                    close_warning.click()
                else:
                    success_msg = self.d.find_element(By.XPATH,Read_Tags_Components().tag_create_success_msg_by_xpath())
                    tag_create_success_actual_validation_msg = success_msg.text
                    self.logger.info(f"tag created msg: {tag_create_success_actual_validation_msg}")
                    self.logger.info(f"expected msg: {tags_list[tag].upper()}")
                    result.append(tag_create_success_actual_validation_msg == tags_list[tag].upper())

            if False in result:
                self.logger.info(f"Status: {False}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_01_failed.png")
                return False
            else:
                self.logger.info(f"Status: {True}")
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_01_Exception.png")
            self.log.info(f"create_tags_for_serious_event:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def Create_2_non_serious_tags_fraud_and_vip(self):
        rows = XLUtils.getRowCount(test_data, 'non_serious_event_tags_data')
        try:
            self.log.info("************* test_TC_TAG_02 ***************")
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            login().login_with_persona_user(self.d, username[4])
            time.sleep(web_driver.one_second)
            self.click_on_tags_menu()
            result = []
            x = Read_Tags_Components().read_non_serious_tags_input_data()
            tags_list = x.split(',')
            self.logger.info(f"eg list: {tags_list}")
            for tag in range(len(tags_list)):
                time.sleep(web_driver.one_second)
                action_button = self.explicit_wait(10, "XPATH", Read_Tags_Components().action_btn_by_xpath(), self.d)
                action_button.click()
                self.logger.info("action button is clicked")
                time.sleep(web_driver.three_second)
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                create_button.click()
                self.logger.info("create button is clicked")
                time.sleep(web_driver.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                tag_name.send_keys(tags_list[tag])
                time.sleep(web_driver.one_second)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                commit.is_displayed()

                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                save.click()
                self.logger.info("save button is clicked")
                time.sleep(web_driver.one_second)
                duplicate_tag_msg = self.d.find_element(By.XPATH, Read_Tags_Components().duplicate_tag_msg_by_xpath())

                if duplicate_tag_msg.is_displayed():
                    close_panel = self.d.find_element(By.XPATH, Read_Tags_Components().close_create_tag_panel_by_xpath())

                    close_panel.click()
                    self.logger.info("close panel button is clicked")
                    close_warning = self.d.find_element(By.XPATH,
                                                        Read_Tags_Components().close_panel_and_discard_changes_btn_by_xpath())
                    close_warning.click()
                else:
                    success_msg = self.d.find_element(By.XPATH, Read_Tags_Components().tag_create_success_msg_by_xpath())
                    tag_create_success_actual_validation_msg = success_msg.text
                    self.logger.info(f"tag created msg: {tag_create_success_actual_validation_msg}")
                    self.logger.info(f"expected msg: {tags_list[tag].upper()}")
                    result.append(tag_create_success_actual_validation_msg == tags_list[tag].upper())

            if False in result:
                self.logger.info(f"Status: {False}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_02_failed.png")
                return False
            else:
                self.logger.info(f"Status: {True}")
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_02_Exception.png")
            self.log.info(f"create_tags_for_non_serious_event:  {ex}")
            return False

        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def Verify_filter_dropdown(self):
        try:
            self.log.info("************ test_TC_TAG_04 **************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_tags_menu()
            result = []
            x = Read_Tags_Components().read_tags_input_data()
            serious_tags = x.split(',')

            self.explicit_wait(10, "XPATH", Read_Tags_Components().filter_btn_by_xpath(), self.d)
            filter_btn = self.d.find_element(By.XPATH, Read_Tags_Components().filter_btn_by_xpath())
            filter_btn.click()
            self.log.info("clicking filter dropdown")
            time.sleep(web_driver.two_second)
            serious_event_filter = self.explicit_wait(10, "XPATH",
                                                       Read_Tags_Components().serious_event_filter_btn_by_xpath(), self.d)
            serious_event_filter.click()
            self.log.info("clicking on serious event  yes filter")
            time.sleep(web_driver.two_second)
            tags_name_list = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            serious_event_tags_name_list_actual = []
            for r in tags_name_list:
                tag = r.text
                tag.lower()
                serious_event_tags_name_list_actual.append(tag)
                serious_event_tags_name_list_actual = [x.lower() for x in serious_event_tags_name_list_actual]
                serious_event_tags_name_list_actual.sort()
            time.sleep(web_driver.one_second)
            for i in range(len(serious_tags)):
                if serious_tags[i].lower() in serious_event_tags_name_list_actual:
                    result.append(True)

            x = Read_Tags_Components().read_non_serious_tags_input_data()
            non_serious_tags = x.split(',')
            self.explicit_wait(10, "XPATH", Read_Tags_Components().filter_btn_by_xpath(), self.d)
            filter_dropdown = self.d.find_element(By.XPATH, Read_Tags_Components().filter_dropdown_by_xpath())
            filter_dropdown.click()
            time.sleep(web_driver.two_second)
            non_serious_ele = self.explicit_wait(10, "XPATH", Read_Tags_Components().non_serious_element_by_xpath(), self.d)
            non_serious_ele.click()
            time.sleep(web_driver.two_second)
            tags_name_list = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            non_serious_event_tags_name_list_actual = []
            for r in tags_name_list:
                tag = r.text.strip()
                tag = tag.lower()
                non_serious_event_tags_name_list_actual.append(tag)
            non_serious_event_tags_name_list_actual = non_serious_event_tags_name_list_actual[
                                                  1:len(non_serious_event_tags_name_list_actual) + 1]
            non_serious_event_tags_name_list_actual = [x.lower() for x in non_serious_event_tags_name_list_actual]
            non_serious_event_tags_name_list_actual.sort()
            time.sleep(web_driver.two_second)
            for i in range(len(non_serious_tags)):
                if non_serious_tags[i].lower() in non_serious_event_tags_name_list_actual:
                    result.append(True)

            self.logger.info(f"status: {result}")
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_04_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_04_exception.png")
            self.log.info(f"filter_serious_event_tags_varify_it:  {ex}")
            return False
        finally:
            self.logout_from_portal()

    def filter_serious_event_tags_varify_it(self):
        # rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')
        try:
            self.log.info("************ test_TC_TAG_04 **************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_tags_menu()
            result = []
            serious_tags = [
                Read_Tags_Components().input_for_create_serious_event_tags_threat(),
                Read_Tags_Components().input_for_create_serious_event_tags_assault()
            ]

            self.explicit_wait(10, "XPATH", Read_Tags_Components().filter_btn_by_xpath(), self.d)
            filter_btn = self.d.find_element(By.XPATH, Read_Tags_Components().filter_btn_by_xpath())
            filter_btn.click()
            self.log.info("clicking filter dropdown")
            time.sleep(web_driver.two_second)
            serious_event_filter = self.d.find_element(By.XPATH,
                                                       Read_Tags_Components().serious_event_filter_btn_by_xpath())
            serious_event_filter.click()
            self.log.info("clicking on serious event  yes filter")
            time.sleep(web_driver.two_second)
            tags_name_list = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            serious_event_tags_name_list_actual = []
            for r in tags_name_list:
                tag = r.text
                tag.lower()
                serious_event_tags_name_list_actual.append(tag)
                serious_event_tags_name_list_actual = [x.lower() for x in serious_event_tags_name_list_actual]
                serious_event_tags_name_list_actual.sort()
            time.sleep(web_driver.one_second)
            for i in serious_tags:
                if i.lower() in serious_event_tags_name_list_actual:
                    result.append(True)
            # result.append(serious_tags == serious_event_tags_name_list_actual)
            self.logger.info(f"status: {result}")
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_04_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_04_exception.png")
            self.log.info(f"filter_serious_event_tags_varify_it:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def filter_non_serious_event_tags_varify_it(self):
        rows = XLUtils.getRowCount(test_data, 'non_serious_event_tags_data')
        try:
            self.log.info("************* test_TC_TAG_05 *************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_tags_menu()
            result = []
            non_serious_tags = [
                Read_Tags_Components().input_for_create_non_serious_event_tags_assault(),
                Read_Tags_Components().input_for_create_non_serious_event_tags_threat()
            ]

            self.explicit_wait(10, "XPATH", Read_Tags_Components().filter_btn_by_xpath(), self.d)
            filter_dropdown = self.d.find_element(By.XPATH, Read_Tags_Components().filter_dropdown_by_xpath())
            filter_dropdown.click()
            time.sleep(web_driver.two_second)
            non_serious_ele = self.d.find_element(By.XPATH, Read_Tags_Components().non_serious_element_by_xpath())
            non_serious_ele.click()
            time.sleep(web_driver.two_second)
            tags_name_list = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            serious_event_tags_name_list_actual = []
            for r in tags_name_list:
                tag = r.text.strip()
                tag = tag.lower()
                serious_event_tags_name_list_actual.append(tag)
            serious_event_tags_name_list_actual = serious_event_tags_name_list_actual[
                                                  1:len(serious_event_tags_name_list_actual) + 1]
            serious_event_tags_name_list_actual = [x.lower() for x in serious_event_tags_name_list_actual]
            serious_event_tags_name_list_actual.sort()
            time.sleep(web_driver.two_second)
            for i in non_serious_tags:
                if i.lower() in serious_event_tags_name_list_actual:
                    result.append(True)
            # result.append(non_serious_event_tags_expected == serious_event_tags_name_list_actual)
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_05_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_05_Exception.png")
            self.log.info(f"filter_non_serious_event_tags_varify_it_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def duplicate_tags_not_create_validation(self):
        rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')
        try:
            self.log.info("************ test_TC_TAG_06 ***************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_tags_menu()
            non_serious_tags = Read_Tags_Components().input_for_create_non_serious_event_tags_assault()
            dup_tag2 = ""
            result = []
            for i in range(2):
                action_button = self.explicit_wait(10, "XPATH", Read_Tags_Components().action_btn_by_xpath(), self.d)
                action_button.click()
                self.logger.info("action button is clicked")
                time.sleep(web_driver.one_second)
                create_button = self.explicit_wait(10, "XPATH", Read_Tags_Components().create_tags_btn_by_xpath(), self.d)
                create_button.click()
                self.logger.info("create button is clicked")
                time.sleep(web_driver.one_second)
                tag_name = self.explicit_wait(10, "XPATH", Read_Tags_Components().get_tag_name_field_by_xpath(), self.d)
                random_num = random.randint(1, 1000)
                if i == 0:
                    dup_tag = non_serious_tags
                    dup_tag2 = dup_tag
                    tag_name.send_keys(dup_tag)
                else:
                    tag_name.send_keys(dup_tag2)
                commit = self.explicit_wait(10, "XPATH", Read_Tags_Components().get_commit_changes_actual_msg_by_xpath(), self.d)
                # commit.is_displayed()
                # result.append(commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath())
                serious_event_checkbox = self.explicit_wait(10, "XPATH",
                                                             Read_Tags_Components().
                                                             get_serious_event_checkbox_by_xpath(), self.d)
                serious_event_checkbox.click()
                save = self.explicit_wait(10, "XPATH", Read_Tags_Components().get_save_btn_by_xpath(), self.d)
                save.click()
                self.logger.info("save button is clicked")
                try:
                    tag_name_already_exists = self.explicit_wait(10, "XPATH",
                                                                  Read_Tags_Components().
                                                                  tag_name_already_exists_validation_by_xpath(), self.d)
                    actual_duplicate_tag_validation_msg = tag_name_already_exists.text
                    expected_duplicate_tag_validation_msg = Read_Tags_Components(). \
                        expected_duplicate_tag_validation_msg()
                    if tag_name_already_exists.is_displayed():
                        result.append(actual_duplicate_tag_validation_msg == expected_duplicate_tag_validation_msg)
                        close_panel = self.explicit_wait(10, "XPATH",
                                                          Read_Tags_Components().close_create_tag_panel_by_xpath(), self.d)
                        close_panel.click()

                        self.logger.info("close panel button is clicked")
                        close_panel_and_discard_changes_btn = self.explicit_wait(10, "XPATH", Read_Tags_Components()
                                                                                 .close_panel_and_discard_changes_btn_by_xpath(), self.d)
                        close_panel_and_discard_changes_btn.click()
                    else:
                        close_panel = self.explicit_wait(10, "XPATH",
                                                          Read_Tags_Components().close_create_tag_panel_by_xpath(), self.d)
                        close_panel.click()
                        self.logger.info("close panel button is clicked")
                except Exception as ex:
                    self.log.info(f"duplicate_tags_not_create_validation_failed:  {ex}")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_06_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_06_Exception.png")
            self.log.info(f"duplicate_tags_not_create_validation_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def edit_serious_event_tag_name(self):
        rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')
        try:
            self.log.info("********** test_TC_TAG_07 ************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_tags_menu()
            time.sleep(web_driver.two_second)
            result = []
            exp_tag_name = [Read_Tags_Components().input_for_create_serious_event_tags_test(),
                            Read_Tags_Components().input_for_create_serious_event_tags_test2()]
            tags_name = []

            serious_tags = [
                Read_Tags_Components().input_for_create_serious_event_tags_test(),
                Read_Tags_Components().input_for_create_serious_event_tags_test2()
            ]
            tags_to_update = []
            for tags in serious_tags:
                # tags_name = XLUtils.readdata(test_data, 'serious_event_tags_data', r, 2)
                time.sleep(web_driver.three_second)
                action_button = self.explicit_wait(10, "XPATH", Read_Tags_Components().action_btn_by_xpath(), self.d)
                action_button.click()
                self.logger.info("action button is clicked")
                time.sleep(web_driver.three_second)
                create_button = self.explicit_wait(10, "XPATH", Read_Tags_Components().create_tags_btn_by_xpath(), self.d)
                create_button.click()
                self.logger.info("create button is clicked")
                time.sleep(web_driver.three_second)
                tag_name = self.explicit_wait(10, "XPATH", Read_Tags_Components().get_tag_name_field_by_xpath(), self.d)
                random_num = random.randint(1, 1000)
                tag_name_input = tags + str(random_num)
                tags_to_update.append(tag_name_input)
                tag_name.send_keys(tag_name_input)
                time.sleep(web_driver.three_second)
                commit = self.explicit_wait(10, "XPATH", Read_Tags_Components().get_commit_changes_actual_msg_by_xpath(), self.d)
                commit.is_displayed()
                # result.append(commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath())
                serious_event_checkbox = self.explicit_wait(10, "XPATH",
                                                             Read_Tags_Components().
                                                             get_serious_event_checkbox_by_xpath(), self.d)
                serious_event_checkbox.click()
                time.sleep(web_driver.three_second)
                save = self.explicit_wait(10, "XPATH", Read_Tags_Components().get_save_btn_by_xpath(), self.d)
                save.click()
                self.logger.info("save button is clicked")
            filter_btn = self.explicit_wait(10, "XPATH", Read_Tags_Components().filter_btn_by_xpath(), self.d)
            filter_btn.click()
            self.log.info("clicking filter dropdown")
            time.sleep(web_driver.three_second)
            serious_event_filter = self.explicit_wait(10, "XPATH",
                                                       Read_Tags_Components().serious_event_filter_btn_by_xpath(), self.d)
            serious_event_filter.click()
            self.log.info("clicking on serious event filter ")
            time.sleep(web_driver.three_second)
            edit_btn_list = self.d.find_elements(By.XPATH,
                                                 Read_Tags_Components().tags_edit_button_by_xpath())
            time.sleep(web_driver.three_second)
            for i in range(len(tags_to_update)):
                try:
                    ac_tg_name = str(tags_to_update[i]).lower().strip()
                    ele = self.d.find_element(By.XPATH, "//p[normalize-space(text())='" + str(
                        ac_tg_name) + "']/following-sibling::div[@class='right-margin-menu']/descendant::div["
                                      "@data-toggle='tooltip']")
                    self.d.execute_script("arguments[0].click();", ele)
                    time.sleep(web_driver.one_second)
                    action_btn = self.explicit_wait(10, "XPATH", Read_Tags_Components()
                                                    .edit_tag_action_btn_by_xpath(), self.d)
                    self.d.execute_script("arguments[0].click();", action_btn)
                    time.sleep(web_driver.one_second)
                except Exception as ex:
                    self.log.info(f"update_serious_event_tag_name_failed:  {ex}")
                edit_btn = self.explicit_wait(10, "XPATH", Read_Tags_Components().edit_btn_by_xpath(), self.d)
                self.d.execute_script("arguments[0].click();", edit_btn)
                time.sleep(web_driver.one_second)
                tag_name_field = self.d.find_element(By.XPATH,
                                                     Read_Tags_Components().get_tag_name_field_by_xpath())
                tag_name_field.send_keys(Keys.CONTROL, 'a')
                tag_name_field.send_keys(Keys.DELETE)
                random_num = random.randint(1, 1000)
                tag_name_update = exp_tag_name[i] + str(random_num)
                tag_name_field.send_keys(tag_name_update)
                time.sleep(web_driver.one_second)
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                save.click()
                self.logger.info("save button is clicked")
                time.sleep(web_driver.one_second)
                self.explicit_wait(10, "XPATH", Read_Tags_Components().update_tag_validation(), self.d)
                updated_tags = self.d.find_element(By.XPATH, Read_Tags_Components().update_tag_validation())
                result.append(updated_tags.text.lower() == tag_name_update.lower())
                print(updated_tags.text.lower())
                print(tag_name_update.lower())
                time.sleep(web_driver.one_second)
            close_panel = self.d.find_element(By.XPATH,
                                              Read_Tags_Components().close_create_tag_panel_by_xpath())
            close_panel.click()
            self.logger.info("close panel button is clicked")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_TAG_07_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_TAG_07_Exception.png")
            self.log.info(f"update_serious_event_tag_name_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def verify_user_able_to_delete_a_tag(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_tags_menu()
            result = []
            tag_input = Read_Tags_Components().delete_tag_data()
            self.explicit_wait(10, "XPATH", Read_Tags_Components().action_btn_by_xpath(), self.d)
            action_button = self.explicit_wait(10, "XPATH", Read_Tags_Components().action_btn_by_xpath(), self.d)
            action_button.click()
            self.logger.info("action button is clicked")
            time.sleep(web_driver.three_second)
            create_button = self.explicit_wait(10, "XPATH", Read_Tags_Components().create_tags_btn_by_xpath(), self.d)
            create_button.click()
            self.logger.info("create button is clicked")
            time.sleep(web_driver.three_second)
            tag_name = self.explicit_wait(10, "XPATH", Read_Tags_Components().get_tag_name_field_by_xpath(), self.d)
            tag_name.send_keys(tag_input)
            time.sleep(web_driver.three_second)
            commit = self.explicit_wait(10, "XPATH", Read_Tags_Components().get_commit_changes_actual_msg_by_xpath(), self.d)
            commit.is_displayed()
            # result.append(commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath())
            serious_event_checkbox = self.explicit_wait(10, "XPATH", Read_Tags_Components().get_serious_event_checkbox_by_xpath(), self.d)
            serious_event_checkbox.click()
            time.sleep(web_driver.three_second)
            save = self.explicit_wait(10, "XPATH", Read_Tags_Components().get_save_btn_by_xpath(), self.d)
            save.click()
            self.logger.info("save button is clicked")
            time.sleep(web_driver.two_second)
            search_box = self.explicit_wait(10, "XPATH", Read_Tags_Components().filter_search_box(), self.d)
            search_box.send_keys(tag_input)
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Tags_Components().tag_select_checkbox_list_by_xpath(), self.d)
            tags_checkbox = self.d.find_elements(By.XPATH, Read_Tags_Components().tag_select_checkbox_list_by_xpath())
            tags_checkbox[0].click()

            time.sleep(web_driver.one_second)
            action_button = self.explicit_wait(10, "XPATH", Read_Tags_Components().tags_action_btn_by_xpath(), self.d)
            action_button.click()
            self.logger.info("action button is clicked")
            time.sleep(web_driver.one_second)
            delete_btn = self.explicit_wait(10, "XPATH", Read_Tags_Components().delete_btn_by_xpath(), self.d)
            delete_btn.click()
            time.sleep(web_driver.one_second)
            delete_yes_btn = self.explicit_wait(10, "XPATH", Read_Tags_Components().yes_delete_selected(), self.d)
            delete_yes_btn.click()
            time.sleep(web_driver.two_second)
            delete_msg = self.explicit_wait(10, "XPATH", Read_Tags_Components().delete_tag_msg_by_xpath(), self.d)

            result.append(delete_msg.is_displayed())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_08_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_TAG_08_Exception.png")
            self.log.info(f"delete_all_tags_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def verify_deterred_tag_is_present_at_first(self):
        try:
            self.log.info("******** test_TC_TAG_09 ********")
            result = []
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_tags_menu()
            self.explicit_wait(10, "XPATH", Read_Tags_Components().list_of_all_tags_name_by_xpath(), self.d)
            deterred_tag = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            actual_deterred_tag = deterred_tag[0].text
            expected_deterred_tag = Read_Tags_Components().expected_deterred_tag()
            result.append(actual_deterred_tag.lower() == expected_deterred_tag.lower())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_TAG_09_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_TAG_09_Exception.png")
            self.log.info(f"verify_deterred_tag_is_present_at_first_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def tags_search_functionality(self):
        try:
            self.log.info("************* test_TC_TAG_03 *************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_tags_menu()
            result = []
            time.sleep(web_driver.three_second)
            search_box = self.explicit_wait(10, "XPATH", Read_Tags_Components().tags_search_field_by_xpath(), self.d)
            search_box.send_keys(Read_Tags_Components().tag_search_input())
            time.sleep(web_driver.three_second)
            search_result = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            actual_tag_result = search_result[0].text
            expected_tag_result = Read_Tags_Components().tag_search_result_expected()
            result.append(actual_tag_result in expected_tag_result)
            self.logger.info(f"status: {result}")
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_03_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_03_exception.png")
            self.log.info(f"tags_search_functionality:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def close_panel_and_discard_changes_verify(self):
        try:
            self.log.info("************* test_TC_TAG_10 ***************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_tags_menu()
            result = []
            action_button = self.d.find_element(By.XPATH, Read_Tags_Components().close_and_discard_panel_btn())
            action_button.click()
            self.logger.info("action button is clicked")
            time.sleep(web_driver.one_second)
            create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
            create_button.click()
            self.logger.info("create button is clicked")
            time.sleep(web_driver.one_second)
            tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
            tag_name.send_keys(Read_Tags_Components().close_panel_and_discard_changes_input())
            close_panel = self.d.find_element(By.XPATH, Read_Tags_Components().close_create_tag_panel_by_xpath())
            close_panel.click()
            self.logger.info("close panel button is clicked")
            time.sleep(web_driver.one_second)
            warning_msg = self.d.find_element(By.XPATH,
                                              Read_Tags_Components().expected_discard_changes_warning_by_xpath())
            actual_warning_msg = warning_msg.text
            excepted_warning_msg = Read_Tags_Components().expected_discard_changes_warning()
            assert actual_warning_msg == excepted_warning_msg
            uncommitted_changes_msg = self.d.find_element(By.XPATH,
                                                          Read_Tags_Components().
                                                          expected_uncommitted_changes_msg_by_xpath())
            time.sleep(web_driver.one_second)
            actual_uncommitted_changes_msg = uncommitted_changes_msg.text
            excepted_uncommitted_changes_msg = Read_Tags_Components().expected_uncommitted_changes_msg()
            result.append(actual_uncommitted_changes_msg == excepted_uncommitted_changes_msg)
            close_panel_btn = self.d.find_element(By.XPATH,
                                                  Read_Tags_Components().close_panel_btn_text_validation())
            actual_close_panel_btn_text = close_panel_btn.text
            excepted_close_panel_btn_text = Read_Tags_Components().expected_close_panel_btn_text()
            result.append(actual_close_panel_btn_text == excepted_close_panel_btn_text)
            close_panel_and_discard_changes_btn = self.d.find_element(By.XPATH,
                                                                      Read_Tags_Components().
                                                                      close_panel_and_discard_changes_btn_by_xpath())
            close_panel_and_discard_changes_btn.click()
            self.logger.info(f"status: {result}")
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_10_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_10_exception.png")
            self.log.info(f"close_panel_and_discard_changes_verify_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def create_tags_for_serious_event_without_login(self):
        rows = XLUtils.getRowCount(test_data, 'Tags_Data')
        try:
            result = []
            for r in range(3, rows + 1):
                tags_name = XLUtils.readdata(test_data, 'Tags_Data', r, 2)
                action_button = self.d.find_element(By.XPATH, Read_Tags_Components().action_btn_by_xpath())
                action_button.click()
                self.logger.info("action button is clicked")
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                create_button.click()
                self.logger.info("create button is clicked")
                time.sleep(web_driver.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                tag_name.send_keys(tags_name)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                commit.is_displayed()
                result.append(commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath())
                serious_event_checkbox = self.d.find_element(By.XPATH,
                                                             Read_Tags_Components().
                                                             get_serious_event_checkbox_by_xpath())
                serious_event_checkbox.click()
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                save.click()
                self.logger.info("save button is clicked")
                duplicate_tag = self.d.find_element(By.XPATH,
                                                    Read_Tags_Components().
                                                    tag_name_already_exists_validation_by_xpath())
                if duplicate_tag.is_displayed():
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
                    self.logger.info("close panel button is clicked")
                    close_warning = self.d.find_element(By.XPATH,
                                                        Read_Tags_Components().
                                                        close_panel_and_discard_changes_btn_by_xpath())
                    close_warning.click()
                else:
                    success_msg = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                    result.append(success_msg.is_displayed())
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
                    self.logger.info("close panel button is clicked")
            self.logger.info(f"status: {result}")
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\"
                                       f"create_tags_for_serious_event_without_login_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\create_tags_for_serious_event_without_login_failed.png")
            self.log.info(f"create_tags_for_serious_event_without_login_failed:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()

    def Verify_total_tags_are_n_including_default_Deterred_tag(self):
        try:
            result = []
            self.logger.info("tags module test exceution started")
            x = Read_Notification_Groups_Components().get_user_name_input_data()
            username = x.split(',')
            login().login_with_persona_user(self.d, username[4])
            time.sleep(web_driver.one_second)
            self.click_on_tags_menu()
            time.sleep(web_driver.one_second)
            list_of_tags = self.d.find_elements(By.XPATH,Read_Tags_Components().lenght_of_tags())
            tags_list = len(list_of_tags)
            self.logger.info(f"tags list is :{tags_list}")
            if tags_list>0:
                self.logger.info("Tags are available in tags panel")
                result.append(True)
            else:
                self.logger.info("Tags are not available in the tags panel")
                result.append(False)
            if result.__contains__(False):
                self.d.save_screenshot(f"{self.screenshots_path}\\"
                                       f"create_tags_for_serious_event_without_login_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\list of tags available .png")
            self.log.info(f"list of taggs available:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.logout_from_portal()











    '''
    def close_all_panel(self):
        try:
            cloud_menu_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_cloud_menu_btn_by_xpath())
            cloud_menu_button.click()
            closed_all_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_closed_all_btn_by_xpath())
            closed_all_button.click()
            return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_all_panel_failed.png")
            self.log.info(f"close_all_panel_failed:  {ex}")
            return False
    '''
    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH, Read_Tags_Components().close_all_panel_list_in_tags())
            for i in close_panel_list:
                i.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_all_panel_one_by_one_failed.png")
            self.log.info(f"close_all_panel_one_by_one_failed:  {ex}")

    def click_on_tags_menu(self):
        tags_button = self.explicit_wait(10, "XPATH", Read_Tags_Components().portal_menu_tags_btn_by_xpath(), self.d)
        tags_button.click()

    def logout_from_portal(self):
        try:
            logout_btn = self.explicit_wait(5, "XPATH", Read_Identify_and_Enroll_Components().logout_btn_by_xpath(),
                                            self.d)
            self.logger.info(f"logout btn is visible: {logout_btn.is_displayed()}")
            if logout_btn.is_displayed():
                logout_btn.click()
            else:
                self.logger.info("logout btn is not visible.")

        except Exception as ex:
            self.logger.info(f"logout_from_portal ex: {ex.args}")
    '''
    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton()). \
                is_displayed():
            self.login_before()

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Tags_Components().logout_btn_by_xpath())
            logout_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\Button_not_clickable_logout_pg_03.png")
            self.log.info(f"logout:  {ex}")
            return False
    '''

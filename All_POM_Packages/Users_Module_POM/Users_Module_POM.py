import json
import pandas as pd
import random
import time
from pathlib import Path

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Config_Packages._1_Portal_Login_Module_Config_Files.Portal_Login_Page_Read_INI import \
    Portal_login_page_read_ini
from All_Config_Packages._4_Users_Module_Config_Files.Users_Read_INI import Read_Users_Components
from All_Config_Packages._4_Users_Module_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from All_Config_Packages._7_Visitor_Search_Module_Config_Files.Visitor_Search_Read_INI import \
    Read_Visitor_Search_Components
from All_POM_Packages.Visitor_Search_Module_POM.Visitor_Search_Module_POM import Visitor_Search_Module_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Login_Logout_Ops import login, logout, web_logger

driver = web_driver.d()
action = ActionChains(driver)


def move_to_element(web_element):
    """
    moves the mouse cursor to a particular element
    :param web_element:
    :return:
    """
    action.move_to_element(web_element).perform()


def scroll_to_element(web_element):
    """
    scrolls the scrollbar to the particular element
    :param web_element:
    :return:
    """
    action.scroll_to_element(web_element).perform()


def javascript_executor_click(web_element):
    """
    click on a web element
    :param web_element:
    :return:
    """
    driver.execute_script("arguments[0].click();", web_element)


def select_options_visible_text(web_element, visible_text):
    """
    handles a drop-down using visible text
    :param web_element:
    :param visible_text: provide the visible text of the web element
    :return:
    """
    select = Select(web_element)
    select.select_by_visible_text(visible_text)


def select_options_value(web_element, value):
    """
    handles drop-down using value
    :param web_element:
    :param value: provide the value present in the value attribute
    :return:
    """
    select = Select(web_element)
    select.select_by_value(value)


def generate_random_number():
    return random.randint(1, 10000)


class Users_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    status = []

    log = web_logger.logger_obj()
    screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots\\"

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID,
                                                     Read_Portal_Menu_Components().get_loginButton()).is_displayed():
            self.login_before()

    def login_before(self):

        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(web_driver.one_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            if not username.is_displayed():
                self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(web_driver.one_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            javascript_executor_click(login_btn)
            time.sleep(web_driver.one_second)

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}login_failed_for_users_menu_failed.png")
            self.log.info(f"login_before_failed: {ex}")
            return False

    def Read_user_from_json(self):
        try:
            file_path = f'{Path(__file__).parent.parent.parent}\\All_Test_Data\\4_Users_Module\\Data_From_JSON\\users_creation.json'
            print(f"json file path: {file_path}")
            # users_dict = json.loads(file_path)
            # print(f"users dictionary: {users_dict["date_range"]}")
            user_dict_pd = pd.read_json(file_path)
            print(f"user dict dataframe: {user_dict_pd['users']}")
            return user_dict_pd
        except Exception as ex:
            self.logger.info(f"readiing users  from json: {ex.args}")

    def verify_user_able_to_see_delete_selected_user(self):
        try:
            ex_result = [True, True]
            ac_result = []
            # #self.login()()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_btn()
            delete_user = self.d.find_element(By.XPATH, Read_Users_Components().delete_selected_user_by_xpath())
            ac_result.append(delete_user.text == Read_Users_Components().delete_selected_user_validation_text())
            ac_result.append(delete_user.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_006_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_006_exception.png")
            self.log.info(f"test_TC_US_006_exception: {ex}")
            return False
        finally:
            logout().logout_from_core(self.d)

    def verify_user_able_to_see_user_role_dropdown_is_present_and_choose_the_user_roles(self):
        try:
            result = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            self.explicit_wait(10, "XPATH", Read_Users_Components().user_role_by_xpath(), self.d)
            user_role = self.d.find_element(By.XPATH, Read_Users_Components().user_role_by_xpath())
            user_role.click()
            self.log.info("clik on user role dropdown")
            time.sleep(web_driver.two_second)
            user_role_ele_with_options_ele = self.d \
                .find_elements(By.XPATH, Read_Users_Components().user_role_options_by_xpath())
            user_role_ele_options = []
            for e in user_role_ele_with_options_ele:
                user_role_ele_options.append(e.text)
            print(user_role_ele_options)
            select = Select(user_role)
            select.select_by_visible_text(user_role_ele_options[0])
            self.log.info(f"selected user role : {user_role_ele_options[0]}")
            if user_role_ele_options[0] == select.first_selected_option.text:
                result.append(True)
            else:
                result.append(False)
            logout().logout_from_core(self.d)
            self.d.refresh()
            self.log.info(f"Status : {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_022_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_022_exception.png")
            self.log.info(f"test_TC_US_022_exception: {ex}")
            return False

    def user_fills_username_firstname_lastname_user_role_password_region_email_timezone_display_success_msg(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            if self.validate_successful_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_109_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_109_exception.png")
            self.log.info(f"test_TC_US_109_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def create_it_admin_user(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            users_dict = self.Read_user_from_json()
            users_list = []
            dictionary_length = len(users_dict["users"])
            print("length of dictionary is", dictionary_length)

            self.logger.info(f"{users_dict['users'][4]}")
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            # username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(users_dict["users"][4]["username"])
            self.enter_first_name(users_dict["users"][4]["firstname"])
            self.enter_last_name(users_dict["users"][4]["lastname"])
            self.d.find_element(By.XPATH, "//select[@name='userRoleId']").click()
            self.select_user_role(users_dict["users"][4]["userrole"])
            self.enter_password(users_dict["users"][4]["password"])
            self.select_region(users_dict["users"][4]["user_orgahierarchy"])
            self.enter_email(users_dict["users"][4]["Email"])
            self.enter_alert_email(users_dict["users"][4]["Email"])
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.two_second)

            # i+=1
            if self.check_if_user_is_created(users_dict["users"][4]["username"]):
                time.sleep(web_driver.one_second)
                self.click_on_alert_schedule_icon()
                time.sleep(web_driver.one_second)
                self.click_on_alert_schedule_action_option_edit()
                time.sleep(web_driver.one_second)
                if True in self.verify_settings_yes_or_no_button():
                    time.sleep(web_driver.one_second)
                    alert_save_button = self.d.find_element(By.XPATH, Read_Users_Components().
                                                            alert_schedule_save_btn_by_xpath())
                    alert_save_button.click()
                    self.logger.info("user created successfully")
                    # self.close_all_panel_one_by_one()
                    users_list.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_1_failed.png")
                users_list.append(False)
            # self.close_all_panel_one_by_one()
            self.logger.info(f"user list contains {users_list}")
            if False in users_list:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_1_exception.png")
            self.log.info(f"test_TC_US_1_exception: {ex}")
            return False
        finally:
            self.click_on_logout_button()

    def Create_5_users_standard_operator_responder_approver_executive_with_all_required_field(self):
        try:
            users_dict = self.Read_user_from_json()
            users_list = []
            username = users_dict["users"][4]["username"]
            login().login_with_persona_user(self.d, username)
            time.sleep(web_driver.one_second)
            dictionary_length = len(users_dict["users"])-1
            print("length of dictionary is", dictionary_length)
            i = 0
            for i in range(dictionary_length):
                print(users_dict["users"][i])
                self.click_user_on_cloud_menu()
                self.click_on_action_create_user_option()
                time.sleep(web_driver.one_second)
                # username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
                self.enter_user_name(users_dict["users"][i]["username"])
                self.enter_first_name(users_dict["users"][i]["firstname"])
                self.enter_last_name(users_dict["users"][i]["lastname"])
                self.d.find_element(By.XPATH, "//select[@name='userRoleId']").click()
                self.select_user_role(users_dict["users"][i]["userrole"])
                self.enter_password(users_dict["users"][i]["password"])
                self.select_region(users_dict["users"][i]["user_orgahierarchy"])
                self.select_store_group(users_dict["users"][i]["store_group"])
                self.enter_email(users_dict["users"][i]["Email"])
                self.enter_alert_email(users_dict["users"][i]["Email"])
                self.select_time_zone(Read_Users_Components().time_zone_input_data())
                time.sleep(web_driver.one_second)
                self.click_on_save_btn()
                time.sleep(web_driver.two_second)

                # i+=1
                if self.check_if_user_is_created(users_dict["users"][i]["username"]):
                    time.sleep(web_driver.one_second)
                    self.click_on_alert_schedule_icon()
                    time.sleep(web_driver.one_second)
                    self.click_on_alert_schedule_action_option_edit()
                    time.sleep(web_driver.one_second)
                    if True in self.verify_settings_yes_or_no_button():
                        time.sleep(web_driver.one_second)
                        alert_save_button = self.d.find_element(By.XPATH,
                                                                Read_Users_Components().alert_schedule_save_btn_by_xpath())
                        alert_save_button.click()
                        self.logger.info("user created successfully")
                        # self.close_all_panel_one_by_one()
                        users_list.append(True)
                else:
                    self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_1_failed.png")
                    users_list.append(False)
                self.close_all_panel_one_by_one()
            self.logger.info(f"user list contains {users_list}")
            if False in users_list:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_1_exception.png")
            self.log.info(f"test_TC_US_1_exception: {ex}")
            return False
        # finally:
        #     self.click_on_logout_button()

    def verify_login_with_newly_created_user_and_validate_login_successful(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data()
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.two_second)

            self.click_on_logout_button()
            time.sleep(web_driver.one_second)
            Entering_username = self.d.find_element(By.XPATH,
                                                    Read_Users_Components().get_portal_login_username_textbox_by_xpath())
            Entering_username.send_keys(Read_Users_Components().user_name_input_data())
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            Entering_password = self.d.find_element(By.XPATH,
                                                    Read_Users_Components().get_portal_login_password_textbox_by_xpath())
            Entering_password.send_keys(Read_Users_Components().password_data_input())
            time.sleep(web_driver.one_second)
            login_button = self.d.find_element(By.XPATH,
                                               Read_Users_Components().get_cloud_login_button_on_portal_by_xpath())
            login_button.click()
            login().accept_terms_and_conditions_for_login_for_new_user(self.d)
            time.sleep(web_driver.one_second)
            current_user_info = self.d.find_element(By.XPATH, Read_Users_Components().get_current_login_username())
            if Read_Users_Components().user_name_input_data() == current_user_info.text:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_02_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_02_exception.png")
            self.log.info(f"test_TC_US_06_exception: {ex}")
            return False
        finally:
            # self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_user_able_to_create_a_new_users_by_filling_all_the_fields(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.two_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            company = Read_Users_Components().company_input_data()
            self.enter_company(company)

            title = Read_Users_Components().title_input_data()
            self.enter_title(title)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            department = Read_Users_Components().department_input_data()
            self.enter_department(department)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            alert_email = Read_Users_Components().alert_email_input_data()
            self.enter_alert_email(alert_email)

            alert_phone_no = Read_Users_Components().alert_phone_no_input_data()
            self.enter_alert_phone_no(alert_phone_no)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            address = Read_Users_Components().address_input_data()
            self.enter_address(address)

            address2 = Read_Users_Components().address2_input_data()
            self.enter_address2(address2)

            city = Read_Users_Components().city_input_data()
            self.enter_city(city)

            state = Read_Users_Components().state_input_data()
            self.enter_state(state)

            postal_code = Read_Users_Components().postal_code_input_data()
            self.enter_postal_code(postal_code)

            home_ph_no = Read_Users_Components().home_phone_no_input_data()
            self.enter_home_ph_no(home_ph_no)

            work_ph_no = Read_Users_Components().work_phone_no_input_data()
            self.enter_work_ph_no(work_ph_no)

            fax_ph_no = Read_Users_Components().fax_phone_no_input_data()
            self.enter_fax_ph_no(fax_ph_no)

            phone_type = Read_Users_Components().phone_type_input_data()
            self.enter_phone_type(phone_type)

            phone_provider = Read_Users_Components().phone_provider_input_data()
            self.select_phone_provider(phone_provider)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.two_second)

            if self.check_if_user_is_created(user_name=username):
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_112_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_112_exception.png")
            self.log.info(f"test_TC_US_112_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_user_able_to_see_all_the_details_filled_for_the_newly_created_user(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            company = Read_Users_Components().company_input_data()
            self.enter_company(company)

            title = Read_Users_Components().title_input_data()
            self.enter_title(title)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            department = Read_Users_Components().department_input_data()
            self.enter_department(department)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            alert_email = Read_Users_Components().alert_email_input_data()
            self.enter_alert_email(alert_email)

            alert_phone_no = Read_Users_Components().alert_phone_no_input_data()
            self.enter_alert_phone_no(alert_phone_no)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            address = Read_Users_Components().address_input_data()
            self.enter_address(address)

            address2 = Read_Users_Components().address2_input_data()
            self.enter_address2(address2)

            city = Read_Users_Components().city_input_data()
            self.enter_city(city)

            state = Read_Users_Components().state_input_data()
            self.enter_state(state)

            postal_code = Read_Users_Components().postal_code_input_data()
            self.enter_postal_code(postal_code)

            home_ph_no = Read_Users_Components().home_phone_no_input_data()
            self.enter_home_ph_no(home_ph_no)

            work_ph_no = Read_Users_Components().work_phone_no_input_data()
            self.enter_work_ph_no(work_ph_no)

            fax_ph_no = Read_Users_Components().fax_phone_no_input_data()
            self.enter_fax_ph_no(fax_ph_no)

            phone_type = Read_Users_Components().phone_type_input_data()
            self.enter_phone_type(phone_type)

            phone_provider = Read_Users_Components().phone_provider_input_data()
            self.select_phone_provider(phone_provider)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.two_second)

            if self.check_if_users_able_to_see_all_details(user_name=username):
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_113_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_113_exception.png")
            self.log.info(f"test_TC_US_113_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_if_user_creates_a_new_users_marked_as_enabled_it_should_reflect_as_enabled(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            self.select_disabled()
            self.select_enabled()

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            if self.check_if_user_marked_as_enabled():
                self.log.info(f"Status: {True}")
                return True
            else:
                self.log.info(f"Status: {False}")
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_02_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_02_exception.png")
            self.log.info(f"test_TC_US_02_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_if_user_creates_a_new_users_marked_as_disabled_it_should_reflect_as_disabled(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            self.select_disabled()

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            if self.check_if_user_marked_as_disabled():
                self.log.info(f"Status : {True}")
                return True
            else:
                self.log.info(f"Status : {False}")
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_02_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_02_exception.png")
            self.log.info(f"test_TC_US_115_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_user_able_to_see_if_the_enabled_is_displayed_for_users_marked_as_enabled_under_users_panel(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.two_second)

            if self.check_users_marked_as_enabled_under_users_panel():
                self.logger.info(f"Status : {True}")
                return True
            else:
                self.logger.info(f"Status : {False}")
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_121_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_121_exception.png")
            self.log.info(f"test_TC_US_121_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_user_able_to_see_if_the_disabled_is_displayed_for_users_marked_as_disabled_under_users_panel(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            time.sleep(web_driver.one_second)
            self.select_disabled()
            time.sleep(web_driver.one_second)
            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.check_users_marked_as_disabled_under_users_panel():
                self.log.info(f"Status : {True}")
                return True
            else:
                self.log.info(f"Status : {False}")
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_122_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_122_exception.png")
            self.log.info(f"test_TC_US_122_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            # logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_user_able_to_open_the_details_for_the_newly_created_user_under_users_panel(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.check_if_details_can_be_opened():
                self.log.info(f"Status : {True}")
                return True
            else:
                self.log.info(f"Status : {False}")
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_128_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_128_exception.png")
            self.log.info(f"test_TC_US_128_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_for_the_newly_created_user_the_hover_text_is_visible_for_alert_schedule_under_users_panel(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_hover_text_alert_schedule():
                self.log.info(f"Status : {False}")
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_130_failed.png")
                return False
            else:
                self.log.info(f"Status : {True}")
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_130_exception.png")
            self.log.info(f"test_TC_US_130_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_user_able_to_edit_the_details_for_the_newly_created_user_details(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.two_second)

            if self.check_if_users_able_to_edit_details():
                self.logger.info(f"Status : {True}")
                return True
            else:
                self.logger.info(f"Status : {False}")
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_04_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_04_exception.png")
            self.log.info(f"test_TC_US_04_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_user_able_to_delete_the_newly_created_user(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_if_users_able_to_delete_a_user():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_06_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_06_exception.png")
            self.log.info(f"test_TC_US_06_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_user_should_not_be_able_to_create_user_which_already_exist(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            result = self.check_users_not_be_able_to_create_user_which_already_exist()
            self.log.info(f" result is {result}")

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_07_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_07_exception.png")
            self.log.info(f"test_TC_US_07_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_user_able_to_link_unlink_the_newly_created_user_to_a_notification_group(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.verify_user_able_to_assign_user_to_notification_group():
                self.log.info(f"Status : {False}")
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_11_failed.png")
                return False
            else:
                self.log.info(f"Status : {True}")
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_11_exception.png")
            self.log.info(f"test_TC_US_11_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def verify_send_sms_send_mms_send_email_send_in_app_notifications_enable_disable_alerts_Yes_No_button(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_settings_yes_or_no_button():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_09_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_09_exception.png")
            self.log.info(f"test_TC_US_09_exception: {ex}")
            return False
        finally:
            logout().logout_from_core(self.d)
            self.d.refresh()

    def on_alert_schedule_edit_user_alert_schedule_and_verify_the_panel_should_be_editable(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            if False in self.verify_panel_is_editable():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_08_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_08_exception.png")
            self.log.info(f"test_TC_US_08_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def on_alert_schedule_panel_click_on_close_panel_button_and_verify_alert_schedule_panel_is_closing(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            time.sleep(web_driver.two_second)
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            if self.verify_alert_schedule_panel_is_closing():
                self.logger.info(f"Status : {True}")
                return True
            else:
                self.logger.info(f"Status : {False}")
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_177_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_177_exception.png")
            self.log.info(f"test_TC_US_177_exception: {ex}")
            return False
        finally:
            logout().logout_from_core(self.d)
            self.d.refresh()

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.one_second)
            # logout_button = self.d.find_element(By.XPATH, Read_Users_Components().logout_btn_by_xpath())
            logout_button = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().logout_btn_by_xpath(),
                                                     self.d)
            time.sleep(web_driver.one_second)
            logout_button.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}click_on_logout_button_failed_from_users_module.png")
            self.log.info(f"click_on_logout_button_failed: {ex}")
            return False

    def click_user_on_cloud_menu(self):
        """
        This function clicks on users on the cloud menu
        """
        # users = self.d.find_element(By.XPATH, Read_Users_Components().users_cloud_menu_by_xpath())
        users = web_driver.explicit_wait(self, 8, "XPATH", Read_Users_Components().users_cloud_menu_by_xpath(), self.d)
        users.click()
        self.logger.info("click on users on the cloud menu")

    def click_on_action_btn(self):
        """
        clicks on action button
        """
        # action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
        action_btn = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().action_dropdown_by_xpath(),
                                              self.d)
        action_btn.click()
        self.logger.info("click on action dropdown")

    def click_on_action_refresh_option(self):
        """
        clicks on refresh
        """
        self.click_on_action_btn()
        time.sleep(web_driver.one_second)
        # refresh = self.d.find_element(By.XPATH, Read_Users_Components().refresh_by_xpath())
        refresh = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().refresh_by_xpath(), self.d)
        refresh.click()
        self.logger.info("click on refresh option")

    def click_on_action_create_user_option(self):
        """
        clicks on create user
        """
        time.sleep(web_driver.one_second)
        self.click_on_action_btn()
        time.sleep(web_driver.one_second)
        # create_user = self.d.find_element(By.XPATH, Read_Users_Components().create_user_by_xpath())
        create_user = web_driver.explicit_wait(self, 10, "XPATH", Read_Users_Components().create_user_by_xpath(),
                                               self.d)
        create_user.click()
        self.logger.info("click on create user option")

    def click_on_action_delete_option(self):
        """
        clicks on delete selected user
        """
        self.click_on_action_btn()
        time.sleep(web_driver.one_second)
        # delete = self.d.find_element(By.XPATH, Read_Users_Components().delete_selected_user_by_xpath())
        delete = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().delete_selected_user_by_xpath(),
                                          self.d)
        delete.click()
        time.sleep(web_driver.one_second)
        self.d.find_element(By.XPATH, Read_Users_Components().delete_confirmation_yes_by_xpath()).click()

    def click_on_save_btn(self):
        """
        clicks on save button
        """
        # save = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_save_button_by_xpath())
        save = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().user_panel_save_button_by_xpath(),
                                        self.d)
        # save.click()
        javascript_executor_click(save)
        self.logger.info("click on save button")

    def click_on_cancel_btn(self):
        """
        clicks on cancel button
        """
        # cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().user_panel_cancel_button_by_xpath(),
                                          self.d)
        cancel.click()

    def select_enabled(self):
        """
        selects enabled checkbox
        """
        # checkbox = self.d.find_element(By.XPATH, Read_Users_Components().enabled_by_xpath())
        checkbox = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().enabled_by_xpath(), self.d)
        checkbox.click()
        self.logger.info("click on enabled checkbox")

    def select_disabled(self):
        """
        selects disabled checkbox
        """
        # checkbox = self.d.find_element(By.XPATH, Read_Users_Components().disabled_by_xpath())
        checkbox = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().disabled_by_xpath(), self.d)
        checkbox.click()
        self.logger.info("click on disabled checkbox")

    def enter_user_name(self, user_name):
        """
        fills username field
        :param user_name:
        """
        self.explicit_wait(10, "XPATH", Read_Users_Components().user_name_by_xpath(), self.d)
        user_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().user_name_by_xpath())
        user_name_txt_bx.send_keys(user_name)
        self.logger.info(f"Enter Username : {user_name}")

    def enter_first_name(self, first_name):
        """
        fills first name field
        :param first_name:
        """
        self.explicit_wait(10, "XPATH", Read_Users_Components().first_name_by_xpath(), self.d)
        first_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().first_name_by_xpath())
        first_name_txt_bx.send_keys(first_name)
        self.logger.info(f"Enter first name : {first_name}")

    def enter_last_name(self, last_name):
        """
        fills last name field
        :param last_name:
        """
        last_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().last_name_by_xpath())
        last_name_txt_bx.send_keys(last_name)
        self.logger.info(f"Enter Last name : {last_name}")

    def select_user_role(self, role_data_text):
        """
        handles user role drop down using visible text of the element
        :param role_data_text:
        :return:
        """
        user_role_ele = self.d.find_element(By.XPATH, Read_Users_Components().user_role_by_xpath())
        select_options_visible_text(user_role_ele, role_data_text)
        self.logger.info(f"Select user role : {role_data_text.upper()}")

    def enter_password(self, password):
        """
        fills password field
        :param password:
        :return:
        """
        new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
        confirm_password = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_by_xpath())
        new_password.send_keys(password)
        self.logger.info(f"Enter new password : {password}")
        confirm_password.send_keys(password)
        self.logger.info(f"Enter confirm password : {password}")

    def enter_mis_match_password(self, password, confirm_password):
        """
        fills password field
        :param password:
        :param confirm_password:
        :return:
        """
        new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
        conf_password = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_by_xpath())
        new_password.send_keys(password)
        conf_password.send_keys(confirm_password)

    def enter_company(self, company):
        company_ele = self.d.find_element(By.XPATH, Read_Users_Components().company_by_xpath())
        company_ele.send_keys(company)
        self.logger.info(f"Enter Company : {company}")

    def enter_title(self, title):
        title_ele = self.d.find_element(By.XPATH, Read_Users_Components().title_by_xpath())
        title_ele.send_keys(title)
        self.logger.info(f"Enter Title : {title}")

    def enter_department(self, department):
        department_ele = self.d.find_element(By.XPATH, Read_Users_Components().department_by_xpath())
        department_ele.send_keys(department)
        self.logger.info(f"Enter Department : {department}")

    def validate_required_user_role_is_selected(self, required_option):
        """
        validate the user role provided is selected.
        :param required_option:
        """
        user_role_ele = self.d.find_element(By.XPATH, Read_Users_Components().user_role_by_xpath())
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
        # region_ele = self.d.find_element(By.XPATH, Read_Users_Components().region_by_xpath())
        region_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Users_Components().region_by_xpath(), self.d)
        region_ele.click()
        time.sleep(web_driver.two_second)
        region_text_list = self.d.find_elements(By.XPATH, Read_Users_Components().region_list_by_xpath())
        expected_region_text = region_text
        try:
            for i in range(len(region_text_list) + 1):
                actual_zone_text = region_text_list.__getitem__(i).text
                self.log.info(actual_zone_text)
                self.log.info(expected_region_text)
                if expected_region_text.upper() in actual_zone_text.upper():
                    region_text_list.__getitem__(i).click()
                    break
            save = self.d.find_element(By.XPATH, Read_Users_Components().region_save_btn_by_xpath())
            # save.click()
            self.d.execute_script("arguments[0].click();", save)
            self.logger.info(f"selected region: {region_text}")
        except Exception as ex:
            str(ex)

    def validate_region(self, region_text):
        """
        validate the selected region is correct
        :param region_text:
        :return:
        """
        region_output = self.d.find_element(By.XPATH, Read_Users_Components().region_selected_by_xpath())
        self.log.info(f"Ex Selected Region : {region_text}")
        self.log.info(f"AC Selected Region : {region_output.text.lower()}")
        return region_output.text.lower() in str(region_text).lower()

    def select_time_zone(self, use_value):
        """
        selects time zone using the value of the element
        :param use_value:
        :return:
        """
        time_zone = self.d.find_element(By.XPATH, Read_Users_Components().time_zone_by_xpath())
        time.sleep(web_driver.one_second)
        select_options_value(time_zone, use_value)
        self.logger.info(f"Selected time zone: {use_value}")

    def select_store_group(self, store):
        """
        selects store group using the value of the element
        :param store:
        :return:
        """
        self.logger.info(f"entered in store group selection method")
        time.sleep(web_driver.two_second)
        store_group = self.explicit_wait(10, "XPATH", Read_Users_Components().select_group_dropdown_by_xpath(), self.d)
        # select_options_value(store_group, store)
        time.sleep(web_driver.one_second)
        store_group.click()
        time.sleep(web_driver.one_second)
        options = self.d.find_elements(By.XPATH, Read_Users_Components().store_groups_options_from_dropdown_by_xpath())
        options[1].click()
        self.logger.info(f"Selected store group: {store}")

    def enter_email(self, email):
        """
        fills email field
        :param email:
        """
        email_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().email_by_xpath())
        email_txt_bx.send_keys(email)
        self.logger.info(f"Enter Email : {email}")

    def enter_alert_email(self, alert_email):
        """
        fills email field
        :param alert_email:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_email_by_xpath())
        ele.send_keys(alert_email)
        self.logger.info(f"Enter Alert Email : {alert_email}")

    def enter_alert_phone_no(self, alert_phone_no):
        """
        fills email field
        :param alert_phone_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_phone_number_by_xpath())
        ele.send_keys(alert_phone_no)
        self.logger.info(f"Enter Alert Phone No. : {alert_phone_no}")

    def enter_address(self, address):
        """
        fills email field
        :param address:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().address_by_xpath())
        ele.send_keys(address)
        self.logger.info(f"Enter Address : {address}")

    def enter_city(self, city):
        """
        fills email field
        :param city:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().city_by_xpath())
        ele.send_keys(city)
        self.logger.info(f"Enter City : {city}")

    def enter_state(self, state):
        """
        fills email field
        :param state:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().state_by_xpath())
        ele.send_keys(state)
        self.logger.info(f"Enter state : {state}")

    def enter_postal_code(self, postal_code):
        """
        fills email field
        :param postal_code:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().postal_code_by_xpath())
        ele.send_keys(postal_code)
        self.logger.info(f"Enter Postal Code : {postal_code}")

    def enter_home_ph_no(self, home_ph_no):
        """
        fills email field
        :param home_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().home_phone_number_by_xpath())
        ele.send_keys(home_ph_no)
        self.logger.info(f"Enter Home Phone No. : {home_ph_no}")

    def enter_work_ph_no(self, work_ph_no):
        """
        fills email field
        :param work_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().work_phone_number_by_xpath())
        ele.send_keys(work_ph_no)
        self.logger.info(f"Enter Work Phone no. : {work_ph_no}")

    def enter_fax_ph_no(self, fax_ph_no):
        """
        fills email field
        :param fax_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().fax_phone_number_by_xpath())
        ele.send_keys(fax_ph_no)
        self.logger.info(f"Enter Fax Phone no. : {fax_ph_no}")

    def enter_phone_type(self, phone_type):
        """
        fills email field
        :param phone_type:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().phone_type_by_xpath())
        ele.send_keys(phone_type)
        self.logger.info(f"Enter Phone Type : {phone_type}")

    def enter_address2(self, address2):
        """
        fills email field
        :param address2:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().address2_by_xpath())
        ele.send_keys(address2)
        self.logger.info(f"Enter Address2 : {address2}")

    def select_phone_provider(self, phone_provider):
        ph_prov_bx = self.d.find_element(By.XPATH, Read_Users_Components().phone_provider_drop_dwn_by_xpath())
        select = Select(ph_prov_bx)
        select.select_by_visible_text(phone_provider)
        self.logger.info(f"Enter Phone provider : {phone_provider}")

    def validate_required_time_zone_is_selected(self, required_option):
        """
        checks if the required time zone is selected
        :param required_option:
        """
        time_zone_ele = self.d.find_element(By.XPATH, Read_Users_Components().time_zone_by_xpath())
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
        time.sleep(web_driver.one_second)
        # ele = self.d.find_element(By.XPATH, Read_Users_Components().error_message_by_xpath())
        ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Users_Components().error_message_by_xpath(), self.d)
        self.log.info(f"actual: {ele.text}")
        msg_validation = ele.text
        self.log.info(f"msg validation: {msg_validation}")
        ac_result.append(msg_validation == Read_Users_Components().error_msg_validation_text())
        ac_result.append(ele.is_displayed())
        self.log.info(f"ex status: {ex_result}")
        self.log.info(f"ac status: {ac_result}")
        if ex_result == ac_result:
            self.log.info(f"validation Success: ")
            return True
        else:
            self.log.info(f"validation Failed: ")
            return False

    def validate_successful_message(self):
        """
        checks if the error message "Success! A user has been created." is displayed.
        """
        ex_result = [True, True]
        ac_result = []
        # ele = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ele = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().success_message_by_xpath(), self.d)
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Users_Components().success_msg_validation_text())
        ac_result.append(ele.is_displayed())
        self.log.info(f"ex status: {ex_result}")
        self.log.info(f"ac status: {ac_result}")
        if ex_result == ac_result:
            self.log.info(f"validation Success: ")
            return True
        else:
            self.log.info(f"validation Failed: ")
            return False

    def check_if_user_is_created(self, user_name):
        """
        checks if the error message "Success! A user has been created." is displayed.
        """
        ex_result = [True, True, True]
        ac_result = []
        # ele = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ele = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().success_message_by_xpath(), self.d)
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Users_Components().success_msg_validation_text())
        self.logger.info(f"Success Msg is visible : {ele.is_displayed()}")
        self.logger.info(f"Ex success Msg : {Read_Users_Components().success_msg_validation_text()}")
        self.logger.info(f"Ac success Msg : {msg_validation}")
        ac_result.append(ele.is_displayed())
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(user_name)
        time.sleep(web_driver.three_second)
        user = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath())
        ac_result.append(user_name == user.text)
        self.logger.info(f"Ex Username : {user_name}")
        self.logger.info(f"Ac Username : {user.text}")
        self.logger.info(f"Ex Status : {ex_result}")
        self.logger.info(f"Ac Status : {ac_result}")
        if ex_result == ac_result:
            return True
        else:
            return False

    def check_if_users_able_to_see_mandatory_details(self, ex_user_name, ex_first_name, ex_last_name, ex_user_role,
                                                     ex_region, ex_email, ex_time_zone):
        """
        checks if user details shows mandatory details that has been filled during the user creation process.
        """
        ex_result = [True, True, True, True, True, True, True]
        ac_result = []
        self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_username_by_xpath(), self.d)
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        firstname = self.d.find_element(By.XPATH, Read_Users_Components().user_details_first_name_by_xpath()).text
        lastname = self.d.find_element(By.XPATH, Read_Users_Components().user_details_last_name_by_xpath()).text
        user_role = self.d.find_element(By.XPATH, Read_Users_Components().user_details_user_role_by_xpath()).text
        region = self.d.find_element(By.XPATH, Read_Users_Components().user_details_region_by_xpath()).text
        email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text
        time_zone = self.d.find_element(By.XPATH, Read_Users_Components().user_details_timezone_by_xpath()).text
        self.logger.info(f"username: {ex_user_name} = {username}")
        self.logger.info(f"first name: {ex_first_name} = {firstname}")
        self.logger.info(f"last name: {ex_last_name} = {lastname}")
        self.logger.info(f"user role: {ex_user_role} = {user_role}")
        self.logger.info(f"region: {ex_region} == {region}")
        self.logger.info(f"email: {ex_email} = {email}")
        self.logger.info(f"timezone: {ex_time_zone} = {time_zone}")
        self.logger.info(f"username displayed: {True if ex_user_name == username else False}")
        self.logger.info(f"first name displayed: {True if ex_first_name == firstname else False}")
        self.logger.info(f"last name displayed: {True if ex_last_name == lastname else False}")
        self.logger.info(f"user role displayed: {True if ex_user_role == user_role else False}")
        self.logger.info(f"Region is displayed: {True if region in ex_region else False}")
        self.logger.info(f"email is displayed: {True if ex_email == email else False}")
        self.logger.info(f"timezone is displayed: {True if ex_time_zone == time_zone else False}")

        ac_result.append(True if ex_user_name == username else False)
        ac_result.append(True if ex_first_name == firstname else False)
        ac_result.append(True if ex_last_name == lastname else False)
        ac_result.append(True if ex_user_role == user_role else False)
        ac_result.append(True if region in ex_region else False)
        ac_result.append(True if ex_email == email else False)
        ac_result.append(True if ex_time_zone == time_zone else False)
        self.logger.info(f"ex_result: {ex_result}")
        self.logger.info(f"ac_result: {ac_result}")
        if ex_result == ac_result:
            return True
        else:
            return False

    def check_if_users_able_to_see_all_details(self, user_name):
        """
        checks if user details shows all details that has been filled during the user creation process.
        """
        ex_user_name = user_name
        ex_first_name = Read_Users_Components().first_name_input_data().strip()

        ex_last_name = Read_Users_Components().last_name_input_data().strip()

        ex_user_role = Read_Users_Components().user_role_input_data().strip()

        ex_company = Read_Users_Components().company_input_data().strip()

        ex_title = Read_Users_Components().title_input_data().strip()

        ex_region = Read_Users_Components().region_data_input()

        ex_department = Read_Users_Components().department_input_data().strip()

        ex_email = Read_Users_Components().email_input_data().strip()

        ex_alert_email = Read_Users_Components().alert_email_input_data().strip()

        ex_alert_phone_no = Read_Users_Components().alert_phone_no_input_data().strip()

        ex_time_zone = Read_Users_Components().time_zone_input_data().strip()

        ex_address = Read_Users_Components().address_input_data().strip()

        ex_address2 = Read_Users_Components().address2_input_data().strip()

        ex_city = Read_Users_Components().city_input_data().strip()

        ex_state = Read_Users_Components().state_input_data().strip()

        ex_postal_code = Read_Users_Components().postal_code_input_data().strip()

        ex_home_ph_no = Read_Users_Components().home_phone_no_input_data().strip()

        ex_work_ph_no = Read_Users_Components().work_phone_no_input_data().strip()

        ex_fax_ph_no = Read_Users_Components().fax_phone_no_input_data().strip()

        self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_username_by_xpath(), self.d)
        ac_user_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text

        ac_first_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_first_name_by_xpath()).text

        ac_last_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_last_name_by_xpath()).text

        ac_user_role = self.d.find_element(By.XPATH, Read_Users_Components().user_details_user_role_by_xpath()).text

        ac_company = self.d.find_element(By.XPATH, Read_Users_Components().user_details_company_by_xpath()).text

        ac_title = self.d.find_element(By.XPATH, Read_Users_Components().user_details_title_by_xpath()).text

        ac_region = self.d.find_element(By.XPATH, Read_Users_Components().user_details_region_by_xpath()).text

        ac_department = self.d.find_element(By.XPATH, Read_Users_Components().user_details_department_by_xpath()).text

        ac_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text

        ac_alert_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_alert_email_by_xpath()).text

        ac_alert_phone_no = self.d.find_element(By.XPATH,
                                                Read_Users_Components().user_details_alert_ph_no_by_xpath()).text

        ac_time_zone = self.d.find_element(By.XPATH, Read_Users_Components().user_details_timezone_by_xpath()).text

        ac_address = self.d.find_element(By.XPATH, Read_Users_Components().user_details_address_by_xpath()).text

        ac_address2 = self.d.find_element(By.XPATH, Read_Users_Components().user_details_address2_by_xpath()).text

        ac_city = self.d.find_element(By.XPATH, Read_Users_Components().user_details_city_by_xpath()).text

        ac_state = self.d.find_element(By.XPATH, Read_Users_Components().user_details_state_by_xpath()).text

        ac_postal_code = self.d.find_element(By.XPATH, Read_Users_Components().user_details_postal_code_by_xpath()).text

        ac_home_ph_no = self.d.find_element(By.XPATH, Read_Users_Components().user_details_home_ph_no_by_xpath()).text

        ac_work_ph_no = self.d.find_element(By.XPATH, Read_Users_Components().user_details_work_ph_no_by_xpath()).text

        ac_fax_ph_no = self.d.find_element(By.XPATH, Read_Users_Components().user_details_fax_ph_no_by_xpath()).text

        ac_result = [True if ex_user_name == ac_user_name.strip() else False,
                     True if ex_first_name == ac_first_name.strip() else False,
                     True if ex_last_name == ac_last_name.strip() else False,
                     True if ex_user_role == ac_user_role.strip() else False,
                     True if ex_company == ac_company.strip() else False,
                     True if ex_title == ac_title.strip() else False,
                     True if ac_region in ex_region else False,
                     True if ex_department == ac_department.strip() else False,
                     True if ex_email == ac_email.strip() else False,
                     True if ex_alert_email == ac_alert_email.strip() else False,
                     True if ex_alert_phone_no == ac_alert_phone_no.strip() else False,
                     True if ex_time_zone == ac_time_zone.strip() else False,
                     True if ex_address == ac_address.strip() else False,
                     True if ex_address2 == ac_address2.strip() else False,
                     True if ex_city == ac_city.strip() else False,
                     True if ex_state == ac_state.strip() else False,
                     True if ex_postal_code == ac_postal_code.strip() else False,
                     True if ex_home_ph_no == ac_home_ph_no.strip() else False,
                     True if ex_work_ph_no == ac_work_ph_no.strip() else False,
                     True if ex_fax_ph_no == ac_fax_ph_no.strip() else False]
        print(ac_result)
        self.logger.info(f"ac_result: {ac_result}")
        if False in ac_result:
            self.logger.info("returning result: False")
            return False
        else:
            self.logger.info("returning result: True")
            return True

    def check_if_user_marked_as_enabled(self):
        """
        checks if user marked as enabled in user panel(User details)
        """
        enabled = self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_enabled_by_xpath(), self.d)
        self.logger.info(f"enabled is clicked : {enabled.is_displayed()}")
        return enabled.is_displayed()

    def check_if_user_marked_as_disabled(self):
        """
        checks if user marked as disabled in user panel(User details)
        """
        disabled = self.explicit_wait(10, "XPATH", Read_Users_Components().users_details_disabled_by_xpath(), self.d)
        self.logger.info(f"disabled is clicked : {disabled.is_displayed()}")
        return disabled.is_displayed()

    def check_if_alert_schedule_is_enabled(self):
        """
        checks if alert schedule is enabled when a new user is created.
        """
        alert_schedule_btn = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_btn_by_xpath())
        self.log.info(f"Alert schedule is enabled : {alert_schedule_btn.is_enabled()}")
        return alert_schedule_btn.is_enabled()

    def verify_user_able_to_open_the_alert_schedule(self):
        """
        checks if alert schedule panel pops up.
        """
        self.explicit_wait(10, "XPATH", Read_Users_Components().alert_schedule_btn_by_xpath(), self.d)
        exp = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        alert_schedule_btn = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_btn_by_xpath())
        alert_schedule_btn.click()
        self.log.info(f"Alert Schedule is clicked")
        self.explicit_wait(10, "XPATH", Read_Users_Components().alert_panel_title_by_xpath(), self.d)
        alert_panel_text = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_title_by_xpath()).text
        act = alert_panel_text.replace("(", "").replace(")", "")
        self.log.info(f"ex : {exp}")
        self.log.info(f"ac : {act}")
        return exp == act

    def check_if_notification_groups_is_enabled(self):
        """
        checks if notification groups is enabled when a new user is created.
        """
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        self.log.info(f"notification_groups_btn is enabled : {notification_groups_btn.is_enabled()}")
        return notification_groups_btn.is_enabled()

    def verify_user_able_to_open_the_notification_groups(self):
        """
        checks if notification groups panel pops up.
        """
        exp = Read_Users_Components().notification_group_title_validation_text()
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()
        self.log.info(f"Notification groups btn is clicked")
        act = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_title_by_xpath()).text
        self.log.info(f"Ex Ng title : {exp}")
        self.log.info(f"Ac Ng title : {act}")
        return exp == act

    def verify_user_details_under_users_panel(self):
        """
        check user details under users_panel
        1. username
        2. first name
        3. last name
        4. email
        """
        result = []
        ex_username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        print(ex_username)
        first_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_first_name_by_xpath()).text
        print(first_name)
        last_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_last_name_by_xpath()).text
        print(last_name)
        ex_first_last_name = first_name + " " + last_name
        print(ex_first_last_name)
        ex_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text
        print(ex_email)
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(ex_username)
        time.sleep(web_driver.one_second)
        ac_username = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath()).text
        print(ac_username)
        ac_first_last_name = self.d \
            .find_element(By.XPATH, Read_Users_Components().users_list_board_first_and_last_name_by_xpath()).text
        print(ac_first_last_name)
        ac_email = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_email_by_xpath()).text
        print(ac_email)
        result.append(ex_username == ac_username)
        result.append(ex_first_last_name == ac_first_last_name)
        # result.append(ex_email == ac_email)
        return result

    def check_users_marked_as_enabled_under_users_panel(self):
        """
        checks if user marked as enabled in Users panel.
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        enabled_list_board = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_enabled_by_xpath())
        self.logger.info(f"Enabled status is visible for user : {enabled_list_board.is_displayed()}")
        return enabled_list_board.is_displayed()

    def check_users_marked_as_disabled_under_users_panel(self):
        """
        checks if user marked as disabled in Users panel.
        """
        self.explicit_wait(10, "XPATH", Read_Users_Components().user_created_success_by_xpath(), self.d)
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        disabled_list_board = self.d.find_element(By.XPATH,
                                                  Read_Users_Components().users_list_board_disabled_by_xpath())
        self.log.info(f"user is marked as disabled : {disabled_list_board.is_displayed()}")
        return disabled_list_board.is_displayed()

    def check_notification_groups_icon(self):
        """
        check notification groups icon is displayed and enabled
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        notification_groups_icon = self.d.find_element(By.XPATH,
                                                       Read_Users_Components().notification_group_icon_by_xpath())
        result.append(notification_groups_icon.is_displayed())
        self.log.info(f"Notification group icon is visible : {notification_groups_icon.is_displayed()}")
        result.append(notification_groups_icon.is_enabled())
        self.log.info(f"Notification group icon is clickable : {notification_groups_icon.is_enabled()}")
        self.log.info(f"Result : {result}")
        return result

    def check_hover_text_notification_groups_icon(self):
        """
        checks hover text for notification groups icon is visible
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_icon_by_xpath())
        move_to_element(ele)
        time.sleep(web_driver.one_second)
        exp = Read_Users_Components().notification_group_icon_hover_validation_text()
        hover_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_icon_hover_by_xpath())
        result.append(hover_ele.is_displayed())
        self.log.info(f"Hover text is visible : {hover_ele.is_displayed()}")
        act = hover_ele.text.split(":")[0]
        self.log.info(f"Ex Hover text : {exp}")
        self.log.info(f"Ac Hover text : {act}")
        result.append(exp == act)
        return result

    def check_if_notification_groups_can_be_opened(self):
        """
        checks notification groups icon can be opened
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_icon_by_xpath())
        ele.click()
        self.logger.info("notification group icon is clicked")
        time.sleep(web_driver.one_second)
        title = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_title_by_xpath()).text
        self.log.info(f"Ex NG title : {Read_Users_Components().notification_group_title_validation_text()}")
        self.log.info(f"Ac NG title : {title}")
        return Read_Users_Components().notification_group_title_validation_text() == title

    def check_details_icon(self):
        """
        check details icon is displayed and enabled
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        result.append(details_icon.is_displayed())
        self.log.info(f"details icon is visible : {details_icon.is_displayed()}")
        result.append(details_icon.is_enabled())
        self.log.info(f"details icon is clickable : {details_icon.is_enabled()}")
        self.log.info(f"Result : {result}")
        return result

    def check_hover_text_details_icon(self):
        """
        checks hover text for details icon is visible
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        move_to_element(details_icon)
        time.sleep(web_driver.one_second)
        exp = Read_Users_Components().details_icon_hover_validation_text()
        hover_ele = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_hover_by_xpath())
        result.append(hover_ele.is_displayed())
        self.log.info(f"details hover text is visible : {hover_ele.is_displayed()}")
        act = hover_ele.text
        result.append(exp == act)
        self.log.info(f"Ex details hover text : {exp}")
        self.log.info(f"Ac details hover text : {act}")
        self.log.info(f"Result : {result}")
        return result

    def check_if_details_can_be_opened(self):
        """
        checks details icon can be opened and user panel should pop up
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        ele.click()
        self.logger.info("details icon btn is clicked")
        time.sleep(web_driver.one_second)
        title = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_title_by_xpath()).text
        self.log.info(f"Ex title : {Read_Users_Components().user_panel_title_validation_text()}")
        self.log.info(f"Ac title : {title}")
        return Read_Users_Components().user_panel_title_validation_text() == title

    def check_alert_schedule_icon(self):
        """
        check alert schedule icon is displayed and enabled
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        result.append(details_icon.is_displayed())
        self.log.info(f"alert icon is visible : {details_icon.is_displayed()}")
        result.append(details_icon.is_enabled())
        self.log.info(f"alert icon is clickable : {details_icon.is_enabled()}")
        self.log.info(f"Result : {result}")
        return result

    def check_hover_text_alert_schedule(self):
        """
        checks hover text for alert schedule icon is visible
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        alert_icon = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        move_to_element(alert_icon)
        time.sleep(web_driver.one_second)
        exp = Read_Users_Components().alert_schedule_icon_hover_validation_text()
        hover_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_hover_by_xpath())
        result.append(hover_ele.is_displayed())
        self.log.info(f"alert schedule icon hover text is visible : {hover_ele.is_displayed()}")
        act = hover_ele.text
        result.append(exp == act)
        self.log.info(f"exp hover txt : {exp}")
        self.log.info(f"act hover txt : {act}")
        self.log.info(f"Result : {result}")
        return result

    def check_if_alert_schedule_can_be_opened(self):
        """
        checks Alert Schedule icon can be opened and alert panel should pop up.
        """
        result = []
        self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_username_by_xpath(), self.d)
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        self.explicit_wait(10, "XPATH", Read_Users_Components().alert_schedule_icon_by_xpath(), self.d)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        ele.click()
        self.logger.info("alert schedule icon is clicked")
        time.sleep(web_driver.one_second)
        exp_title = username
        self.explicit_wait(10, "XPATH", Read_Users_Components().alert_panel_title_by_xpath(), self.d)
        title = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_title_by_xpath()).text
        act_title = title.replace("(", "").replace(")", "")
        exp_sub_title = Read_Users_Components().alert_panel_sub_title_validation_text()
        act_sub_title = self.d.find_element(By.XPATH,
                                            Read_Users_Components().alert_panel_sub_title_by_xpath()).text.strip()
        result.append(exp_title == act_title)
        self.log.info(f"exp_title : {exp_title}")
        self.log.info(f"act_title : {act_title}")
        result.append(exp_sub_title == act_sub_title)
        self.log.info(f"exp_sub_title : {exp_sub_title}")
        self.log.info(f"act_sub_title : {act_sub_title}")
        self.log.info(f"Result : {result}")
        return result

    def check_if_users_able_to_edit_details(self):
        """
        check if users able to edit details.
        """
        time.sleep(web_driver.two_second)
        # action_bx = self.d.find_element(By.XPATH, Read_Users_Components().user_details_action_btn())
        action_bx = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().user_details_action_btn(),
                                             self.d)
        action_bx.click()
        self.logger.info("In Users Details panel, Action dropdown is clicked")
        self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_action_edit_user(), self.d).click()
        self.logger.info("Edit option is clicked")
        time.sleep(web_driver.one_second)
        email = self.d.find_element(By.XPATH, Read_Users_Components().email_by_xpath())
        email.clear()
        time.sleep(web_driver.one_second)
        exp_email = Read_Users_Components().update_email_input_data()
        email.send_keys(exp_email)
        self.logger.info(f"Email field is updated with : {exp_email}")
        self.click_on_save_btn()
        self.logger.info(f"click on save btn")
        time.sleep(web_driver.two_second)
        act_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text
        self.logger.info(f"Ex Email : {exp_email}")
        self.logger.info(f"Ac Email : {act_email}")
        return exp_email == act_email

    def check_if_users_able_to_delete_a_user(self):
        """
        check if users able to delete a user
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        check_box = self.d.find_element(By.XPATH, Read_Users_Components().users_check_box_by_xpath())
        check_box.click()
        time.sleep(web_driver.one_second)
        self.click_on_action_delete_option()
        time.sleep(web_driver.one_second)
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        msg = self.d.find_element(By.XPATH, Read_Users_Components().filter_message_by_xpath())
        result.append(msg.is_displayed())
        result.append(msg.text == Read_Users_Components().filter_msg_validation_text())
        return result

    def check_users_not_be_able_to_create_user_which_already_exist(self):
        """
        check if users not be able to create user which already exist
        """
        self.explicit_wait(10, "XPATH", Read_Users_Components().user_created_success_by_xpath(), self.d)
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text

        self.click_on_action_create_user_option()
        time.sleep(web_driver.one_second)

        self.enter_user_name(username)

        first_name = Read_Users_Components().first_name_input_data()
        self.enter_first_name(first_name)

        last_name = Read_Users_Components().last_name_input_data()
        self.enter_last_name(last_name)

        user_role = Read_Users_Components().user_role_input_data()
        self.select_user_role(user_role)

        password = Read_Users_Components().password_data_input()
        self.enter_password(password)

        region = Read_Users_Components().region_data_input()
        self.select_region(region)

        email = Read_Users_Components().email_input_data()
        self.enter_email(email)

        time_zone = Read_Users_Components().time_zone_input_data()
        self.select_time_zone(time_zone)

        time.sleep(web_driver.one_second)
        self.click_on_save_btn()

        time.sleep(web_driver.one_second)
        error_msg = self.explicit_wait(10, "XPATH", Read_Users_Components().user_name_exists_by_xpath(), self.d)
        print(error_msg.text)
        result.append(error_msg.is_displayed())
        self.log.info(f"error_msg is visible : {error_msg.is_displayed()}")
        result.append(error_msg.text == Read_Users_Components().user_name_exists_validation_text())
        self.log.info(f"Ex error msg : {Read_Users_Components().user_name_exists_validation_text()}")
        self.log.info(f"Ac error msg : {error_msg.text}")
        return result

    def check_if_error_msg_displayed_for_password_mismatch(self):
        """
        check if error msg displayed for password mismatch
        """
        result = []
        error_msg = self.d.find_element(By.XPATH, Read_Users_Components().password_mis_match_by_xpath())
        result.append(error_msg.is_displayed())
        self.log.info(f"error msg is visible : {error_msg.is_displayed()}")
        result.append(error_msg.text == Read_Users_Components().password_mis_match_validation_text())
        self.log.info(f"Ex Error msg : {Read_Users_Components().password_mis_match_validation_text()}")
        self.log.info(f"Ac Error msg : {error_msg.text}")
        self.log.info(f"Result : {result}")
        return result

    def check_if_users_able_to_cancel(self):
        """
        check if users able to cancel
        """
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        self.logger.info(f"click on cancel btn")
        panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_list_by_xpath())
        new_panel_count = len(panel_list)
        return new_panel_count == 1

    def close_all_panel_one_by_one(self):
        try:
            time.sleep(web_driver.one_second)
            close_panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_one_by_one_list())

            for i in close_panel_list:
                i.click()
                time.sleep(web_driver.one_second)
            while self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_and_discard_Changes()) \
                    .is_displayed():
                ele = self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_and_discard_Changes())
                javascript_executor_click(ele)
                if self.d.find_element(By.XPATH, Read_Users_Components().face_first_logo()).is_displayed():
                    break
            time.sleep(web_driver.one_second)
        except Exception as ex:

            self.d.save_screenshot(f"{self.screenshots_path}close_all_panel_one_by_one_failed.png")
            self.log.info(f"close_all_panel_one_by_one_failed: {ex}")

    def close_single_panel(self):
        try:
            time.sleep(web_driver.one_second)
            close_panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_one_by_one_list())
            for i in close_panel_list:
                javascript_executor_click(i)
            time.sleep(web_driver.one_second)
            if self.d.find_element(By.XPATH,
                                   Read_Users_Components().close_panel_and_discard_changes_warning_by_xpath()).is_displayed():
                self.d.find_element(By.XPATH,
                                    Read_Users_Components().close_panel_and_discard_changes_warning_by_xpath()).click()
            else:
                pass
        except Exception as ex:
            self.click_on_logout_button()
            self.d.save_screenshot(f"{self.screenshots_path}close_all_panel_one_by_one_failed.png")
            self.log.info(f"close_all_panel_one_by_one_failed: {ex}")

    def verify_user_able_to_open_the_filter_drop_down(self):
        """
        checks if filter drop down is enabled
        """
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()
        self.logger.info(f"click on notification groups btn")
        filter_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_filter_drop_dwn())
        self.logger.info(f"Filter dropdown is clickable : {filter_ele.is_enabled()}")
        return filter_ele.is_enabled()

    def verify_user_able_to_open_the_action_drop_down(self):
        """
        checks if action drop down is enabled
        """
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()
        self.logger.info(f"Notification btn is clicked")
        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_action_drop_dwn())
        self.logger.info(f"Action dropdown is clickable : {action_ele.is_enabled()}")
        return action_ele.is_enabled()

    def verify_user_able_to_assign_user_to_notification_group(self):
        """
        Add user to notification group
        """
        self.logger.info("Add user to notification group")
        result = []
        time.sleep(web_driver.one_second)

        notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Users_Components()
                                                     .notification_groups_btn_by_xpath(), self.d)
        notification_groups_btn.click()
        self.logger.info("notification groups btn is clicked")
        time.sleep(web_driver.one_second)
        action_ele = self.explicit_wait(10, "XPATH", Read_Users_Components().notification_groups_action_drop_dwn(),
                                        self.d)
        action_ele.click()
        self.logger.info("action dropdown is clicked")
        time.sleep(web_driver.one_second)
        create = self.explicit_wait(10, "XPATH", Read_Users_Components().option_create_notification_group(), self.d)
        create.click()
        self.logger.info("create notification group option is clicked")
        time.sleep(web_driver.one_second)

        name_value = Read_Users_Components().notification_group_name() + str(generate_random_number())
        name_ele = self.explicit_wait(10, "XPATH", Read_Users_Components()
                                      .notification_groups_details_name_input(), self.d)
        name_ele.send_keys(name_value)
        time.sleep(web_driver.one_second)
        save = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_details_save_btn())
        save.click()
        self.logger.info("Notification groups detail is filled and save btn is clicked")
        time.sleep(web_driver.one_second)
        close = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_details_close_panel())
        close.click()
        self.logger.info("Notification groups details close panel is clicked")
        time.sleep(web_driver.one_second)
        filter_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_filter_drop_dwn())
        filter_ele.click()
        self.logger.info("filter dropdown is clicked")
        time.sleep(web_driver.two_second)
        unlinked = self.explicit_wait(10, "XPATH", Read_Users_Components().option_unlinked_notification_groups(),
                                      self.d)
        unlinked.click()
        self.logger.info("unlinked option is clicked")
        time.sleep(web_driver.two_second)
        search = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_search_bar())
        search.send_keys(name_value)
        self.logger.info(f"Enter {name_value}, in notification groups search box")
        time.sleep(web_driver.two_second)
        check_box = self.d.find_element(By.XPATH, Read_Users_Components()
                                        .notification_groups_select_all_checkbox())
        check_box.click()
        self.logger.info(f"select the {name_value} notification group checkbox")
        time.sleep(web_driver.two_second)
        action_ele = self.explicit_wait(10, "XPATH", Read_Users_Components().notification_groups_action_drop_dwn(),
                                        self.d)
        action_ele.click()
        self.logger.info("click on the notification groups action box dropdown")
        time.sleep(web_driver.one_second)
        add_user = self.explicit_wait(10, "XPATH", Read_Users_Components().option_add_to_user(), self.d)
        add_user.click()
        self.logger.info("click on the add to user option")
        time.sleep(web_driver.two_second)
        close_notification_groups = self.d \
            .find_element(By.XPATH, Read_Users_Components().notification_groups_close_panel())
        close_notification_groups.click()
        self.logger.info("click on close notification groups")
        time.sleep(web_driver.one_second)
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()
        self.logger.info("click on notification groups btn")
        time.sleep(web_driver.two_second)
        ac_name = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_name_list()).text
        result.append(name_value == ac_name)
        self.logger.info(f"ex : {name_value}")
        self.logger.info(f"ac : {ac_name}")
        time.sleep(web_driver.one_second)
        check_box = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_select_all_checkbox())
        check_box.click()
        self.logger.info("click on the select all checkbox")
        time.sleep(web_driver.one_second)
        action_ele = self.explicit_wait(10, "XPATH", Read_Users_Components().notification_groups_action_drop_dwn(),
                                        self.d)
        action_ele.click()
        self.logger.info("click on the action dropdown")
        time.sleep(web_driver.one_second)
        remove_user = self.explicit_wait(10, "XPATH", Read_Users_Components().option_remove_from_user(), self.d)
        remove_user.click()
        self.logger.info("click on the remove from user option")
        time.sleep(web_driver.one_second)

        msg = self.explicit_wait(10, "XPATH", Read_Users_Components().notification_groups_no_linked_alerts(), self.d)
        result.append(msg.is_displayed())
        self.logger.info(f"no linked alerts msg is visible : {msg.is_displayed()}")
        time.sleep(web_driver.one_second)
        close_notification_groups = self.d.find_element(By.XPATH,
                                                        Read_Users_Components().notification_groups_close_panel())
        close_notification_groups.click()
        self.logger.info(f"Result : {result}")
        return result

    def Verify_user_able_to_link_notification_group_from_Users_panel(self):
        """
        Add user to notification group
        """
        self.logger.info("Add user to notification group")
        result = []
        time.sleep(web_driver.one_second)

        notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Users_Components()
                                                     .notification_groups_btn_by_xpath(), self.d)
        notification_groups_btn.click()
        self.logger.info("notification groups btn is clicked")
        time.sleep(web_driver.one_second)
        action_ele = self.explicit_wait(10, "XPATH", Read_Users_Components().notification_groups_action_drop_dwn(),
                                        self.d)
        action_ele.click()
        self.logger.info("action dropdown is clicked")
        time.sleep(web_driver.one_second)
        create = self.explicit_wait(10, "XPATH", Read_Users_Components().option_create_notification_group(), self.d)
        create.click()
        self.logger.info("create notification group option is clicked")
        time.sleep(web_driver.one_second)

        name_value = Read_Users_Components().notification_group_name() + str(generate_random_number())
        name_ele = self.explicit_wait(10, "XPATH", Read_Users_Components()
                                      .notification_groups_details_name_input(), self.d)
        name_ele.send_keys(name_value)
        time.sleep(web_driver.one_second)
        save = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_details_save_btn())
        save.click()
        self.logger.info("Notification groups detail is filled and save btn is clicked")
        time.sleep(web_driver.one_second)
        close = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_details_close_panel())
        close.click()
        self.logger.info("Notification groups details close panel is clicked")
        time.sleep(web_driver.one_second)
        filter_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_filter_drop_dwn())
        filter_ele.click()
        self.logger.info("filter dropdown is clicked")
        time.sleep(web_driver.two_second)
        unlinked = self.explicit_wait(10, "XPATH", Read_Users_Components().option_unlinked_notification_groups(),
                                      self.d)
        unlinked.click()
        self.logger.info("unlinked option is clicked")
        time.sleep(web_driver.two_second)
        search = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_search_bar())
        search.send_keys(name_value)
        self.logger.info(f"Enter {name_value}, in notification groups search box")
        time.sleep(web_driver.two_second)
        check_box = self.d.find_element(By.XPATH, Read_Users_Components()
                                        .notification_groups_select_all_checkbox())
        check_box.click()
        self.logger.info(f"select the {name_value} notification group checkbox")
        time.sleep(web_driver.two_second)
        action_ele = self.explicit_wait(10, "XPATH", Read_Users_Components().notification_groups_action_drop_dwn(),
                                        self.d)
        action_ele.click()
        self.logger.info("click on the notification groups action box dropdown")
        time.sleep(web_driver.one_second)
        add_user = self.explicit_wait(10, "XPATH", Read_Users_Components().option_add_to_user(), self.d)
        add_user.click()
        self.logger.info("click on the add to user option")
        time.sleep(web_driver.two_second)
        close_notification_groups = self.d \
            .find_element(By.XPATH, Read_Users_Components().notification_groups_close_panel())
        close_notification_groups.click()
        self.logger.info("click on close notification groups")
        time.sleep(web_driver.one_second)
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()
        self.logger.info("click on notification groups btn")
        time.sleep(web_driver.two_second)
        ac_name = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_name_list()).text
        result.append(name_value == ac_name)
        self.logger.info(f"ex : {name_value}")
        self.logger.info(f"ac : {ac_name}")
        time.sleep(web_driver.one_second)
        check_box = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_select_all_checkbox())
        check_box.click()
        self.logger.info("click on the select all checkbox")
        time.sleep(web_driver.one_second)
        action_ele = self.explicit_wait(10, "XPATH", Read_Users_Components().notification_groups_action_drop_dwn(),
                                        self.d)
        action_ele.click()
        self.logger.info("click on the action dropdown")
        time.sleep(web_driver.one_second)
        remove_user = self.explicit_wait(10, "XPATH", Read_Users_Components().option_remove_from_user(), self.d)
        remove_user.click()
        self.logger.info("click on the remove from user option")
        time.sleep(web_driver.one_second)

        msg = self.explicit_wait(10, "XPATH", Read_Users_Components().notification_groups_no_linked_alerts(), self.d)
        result.append(msg.is_displayed())
        self.logger.info(f"no linked alerts msg is visible : {msg.is_displayed()}")
        time.sleep(web_driver.one_second)
        close_notification_groups = self.d.find_element(By.XPATH,
                                                        Read_Users_Components().notification_groups_close_panel())
        close_notification_groups.click()
        self.logger.info(f"Result : {result}")
        return result

    def verify_password_7_characters(self):
        ex_msg = Read_Users_Components().password_less_than_8_characters_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        self.log.info(f"ex msg : {ex_msg}")
        self.log.info(f"ac msg : {ac_msg}")
        return ex_msg == ac_msg

    def verify_password_21_characters(self):
        ex_msg = Read_Users_Components().password_greater_than_20_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        self.log.info(f"ex msg : {ex_msg}")
        self.log.info(f"ac msg : {ac_msg}")
        return ex_msg == ac_msg

    def verify_password_only_alphabets(self):
        ex_msg = Read_Users_Components().password_only_alphabet_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        self.log.info(f"ex msg : {ex_msg}")
        self.log.info(f"ac msg : {ac_msg}")
        return ex_msg == ac_msg

    def verify_password_only_numeric(self):
        ex_msg = Read_Users_Components().password_only_numeric_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        self.log.info(f"ex msg : {ex_msg}")
        self.log.info(f"ac msg : {ac_msg}")
        return ex_msg == ac_msg

    def verify_password_only_special_character(self):
        ex_msg = Read_Users_Components().password_only_special_symbol_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        self.log.info(f"ex msg : {ex_msg}")
        self.log.info(f"ac msg : {ac_msg}")
        return ex_msg == ac_msg

    def verify_password_combination_lower_alphabet_and_number(self):
        ex_msg = Read_Users_Components().password_only_alphanumeric_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        self.log.info(f"ex msg : {ex_msg}")
        self.log.info(f"ac msg : {ac_msg}")
        return ex_msg == ac_msg

    def verify_password_combination_lower_alphabet_and_special_character(self):
        ex_msg = Read_Users_Components().password_only_alphabet_sp_symbol_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        self.log.info(f"ex msg : {ex_msg}")
        self.log.info(f"ac msg : {ac_msg}")
        return ex_msg == ac_msg

    def verify_password_combination_number_and_special_character(self):
        ex_msg = Read_Users_Components().password_only_number_sp_symbol_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        self.log.info(f"ex msg : {ex_msg}")
        self.log.info(f"ac msg : {ac_msg}")
        return ex_msg == ac_msg

    def verify_alert_schedule_title(self):
        """
        checks alert schedule panel title.
        """
        status = []
        exp = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath()).text.strip()
        alert_panel_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_title_by_xpath())
        alert_panel_text = alert_panel_ele.text
        act = alert_panel_text.replace("(", "").replace(")", "")
        status.append(alert_panel_ele.is_displayed())
        self.log.info(f"alert_panel_title is visible : {alert_panel_ele.is_displayed()}")
        status.append(exp == act)
        self.log.info(f"exp : {exp}")
        self.log.info(f"act : {act}")
        self.log.info(f"Status : {status}")
        return status

    def is_constant_user_created(self):
        user_name = Read_Users_Components().constant_user_name()
        # search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().search_box_by_xpath(), self.d)
        search_box.send_keys(user_name)
        time.sleep(web_driver.two_second)
        filter_msg = self.d.find_element(By.XPATH, Read_Users_Components().filter_message_by_xpath())
        if filter_msg.is_displayed():
            return False
        user = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath())
        return user_name == user.text

    def click_on_alert_schedule_icon(self):
        # alert_schedule = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        alert_schedule = web_driver.explicit_wait(self, 10, "XPATH",
                                                  Read_Users_Components().alert_schedule_icon_by_xpath(), self.d)
        alert_schedule.click()
        self.logger.info("click on alert schedule icon")

    def create_a_user_with_a_constant_username_else_continue(self, is_user_created):
        if not is_user_created:
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().constant_user_name()
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.two_second)

    def verify_alert_schedule_sub_title(self):
        """
        checks alert schedule sub title.
        """
        status = []
        exp = Read_Users_Components().alert_panel_sub_title_validation_text()
        sub_title_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_sub_title_by_xpath())
        act = sub_title_ele.text.strip()
        # self.log.info(exp, "==", act)
        status.append(sub_title_ele.is_displayed())
        self.logger.info(f"Alert subtitle is visible : {sub_title_ele.is_displayed()}")
        status.append(exp == act)
        self.logger.info(f"EXP : {exp}")
        self.logger.info(f"ACT : {act}")
        self.logger.info(f"Status : {status}")
        return status

    def verify_schedule_sub_title_is_visible(self):
        """
        checks alert schedule sub title 'Schedule'.
        """
        status = []
        exp = Read_Users_Components().alert_schedule_sub_title_schedule_validation_txt()
        sub_title_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_sub_title_schedule_by_xpath())
        act = sub_title_ele.text.strip()
        # self.log.info(exp, "==", act)
        status.append(sub_title_ele.is_displayed())
        self.logger.info(f"Alert panel sub title is visible : {sub_title_ele.is_displayed()}")
        status.append(exp == act)
        self.logger.info(f"EXP : {exp}")
        self.logger.info(f"ACT : {act}")
        self.logger.info(f"Status : {status}")
        return status

    def verify_settings_text_is_visible(self):
        """
        checks 'Schedule' is visible.
        """
        status = []
        exp = Read_Users_Components().alert_schedule_settings_validation_txt()
        settings = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_settings_by_xpath())
        act = settings.text
        status.append(settings.is_displayed())
        self.logger.info(f"Schedule is visible : {settings.is_displayed()}")
        status.append(exp == act)
        self.logger.info(f"EXP : {exp}")
        self.logger.info(f"ACT : {act}")
        self.logger.info(f"Status : {status}")
        return status

    def verify_settings_details_and_values_is_visible(self):
        """
        checks Settings items (Username, Timezone, Timezone ID, Send SMS, Send MMS, Send Email,
        Send In-App Notifications, Enable Alerts) and its values is visible.
        """
        status = []

        # Details
        username_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_username_by_xpath())
        timezone_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_timezone_by_xpath())
        timezone_id_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_timezone_id_by_xpath())
        send_sms_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_sms_by_xpath())
        send_mms_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_mms_by_xpath())
        send_email_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_email_by_xpath())
        send_in_app_ele = self.d.find_element(By.XPATH, Read_Users_Components()
                                              .settings_send_in_app_notifications_by_xpath())
        enable_alerts_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_enable_alerts_by_xpath())

        # Values
        username_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_username_value_by_xpath())
        timezone_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_timezone_value_by_xpath())
        timezone_id_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_timezone_id_value_by_xpath())
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_sms_value_by_xpath())
        send_mms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_mms_value_by_xpath())
        send_email_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_email_value_by_xpath())
        send_in_app_value = self.d \
            .find_element(By.XPATH, Read_Users_Components().settings_send_in_app_value_notifications_by_xpath())
        enable_alerts_value = self.d.find_element(By.XPATH, Read_Users_Components()
                                                  .settings_enable_alerts_value_by_xpath())

        # Details
        status.append(username_ele.is_displayed())
        status.append(timezone_ele.is_displayed())
        status.append(timezone_id_ele.is_displayed())
        status.append(send_sms_ele.is_displayed())
        status.append(send_mms_ele.is_displayed())
        status.append(send_email_ele.is_displayed())
        status.append(send_in_app_ele.is_displayed())
        status.append(enable_alerts_ele.is_displayed())
        self.logger.info(f"username_ele is visible : {username_ele.is_displayed()}")
        self.logger.info(f"timezone_ele is visible : {timezone_ele.is_displayed()}")
        self.logger.info(f"timezone_id_ele is visible : {timezone_id_ele.is_displayed()}")
        self.logger.info(f"send_sms_ele is visible : {send_sms_ele.is_displayed()}")
        self.logger.info(f"send_mms_ele is visible : {send_mms_ele.is_displayed()}")
        self.logger.info(f"send_email_ele is visible : {send_email_ele.is_displayed()}")
        self.logger.info(f"send_in_app_ele is visible : {send_in_app_ele.is_displayed()}")
        self.logger.info(f"enable_alerts_ele is visible : {enable_alerts_ele.is_displayed()}")

        status.append(username_ele.text == Read_Users_Components().settings_username_validation_txt())
        status.append(timezone_ele.text == Read_Users_Components().settings_timezone_validation_txt())
        status.append(timezone_id_ele.text == Read_Users_Components().settings_timezone_id_validation_txt())
        status.append(send_sms_ele.text == Read_Users_Components().settings_send_sms_validation_txt())
        status.append(send_mms_ele.text == Read_Users_Components().settings_send_mms_validation_txt())
        status.append(send_email_ele.text == Read_Users_Components().settings_send_email_validation_txt())
        status. \
            append(send_in_app_ele.text == Read_Users_Components().settings_send_in_app_notifications_validation_txt())
        status.append(enable_alerts_ele.text == Read_Users_Components().settings_enable_alerts_validation_txt())

        # Values
        status.append(username_value.is_displayed())
        status.append(timezone_value.is_displayed())
        status.append(timezone_id_value.is_displayed())
        status.append(send_sms_value.is_displayed())
        status.append(send_mms_value.is_displayed())
        status.append(send_email_value.is_displayed())
        status.append(send_in_app_value.is_displayed())
        status.append(enable_alerts_value.is_displayed())
        self.logger.info(f"username_value is visible : {username_value.is_displayed()}")
        self.logger.info(f"timezone_value is visible : {timezone_value.is_displayed()}")
        self.logger.info(f"timezone_id_value is visible : {timezone_id_value.is_displayed()}")
        self.logger.info(f"send_sms_value is visible : {send_sms_value.is_displayed()}")
        self.logger.info(f"send_mms_value is visible : {send_mms_value.is_displayed()}")
        self.logger.info(f"send_email_value is visible : {send_email_value.is_displayed()}")
        self.logger.info(f"send_in_app_value is visible : {send_in_app_value.is_displayed()}")
        self.logger.info(f"enable_alerts_value is visible : {enable_alerts_value.is_displayed()}")
        self.logger.info(f"Status : {status}")
        return status

    def verify_schedule_day_and_time_range_is_visible(self):
        """
        checks 'Schedule' day and time range.
        """
        status = []

        days_ele = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_day_by_xpath())
        for day in days_ele:
            status.append(day.is_displayed())
            self.log.info(day.is_displayed())
        time_range_ele = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_by_xpath())
        for ele in time_range_ele:
            status.append(ele.is_displayed())
            self.log.info(ele.is_displayed)
        self.logger.info(f"Status : {status}")
        return status

    def verify_alert_schedule_action_drop_down(self):
        """
        checks action drop down button
        """
        status = []
        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_action_btn_by_xpath())
        status.append(action_ele.is_displayed())
        status.append(action_ele.is_enabled())
        self.logger.info(f"Alert Schedule Action dropdwon is visible : {action_ele.is_displayed()}")
        self.logger.info(f"Alert Schedule Action dropdwon is clickable: {action_ele.is_enabled()}")
        self.logger.info(f"Status : {status}")
        return status

    def verify_action_drop_down_options(self):
        """
        checks action drop down options
        """
        status = []
        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_action_btn_by_xpath())
        action_ele.click()
        self.logger.info(f"Alert Schedule Action dropdwon is clicked")
        time.sleep(web_driver.one_second)
        edit = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_action_option_edit_by_xpath())
        status.append(edit.is_displayed())
        status.append(edit.is_enabled())
        self.logger.info(f"Edit option is visible : {edit.is_displayed()}")
        self.logger.info(f"Edit option is clickable: {edit.is_enabled()}")
        self.logger.info(f"Status : {status}")
        return status

    def click_on_alert_schedule_action_option_edit(self):
        self.explicit_wait(10, "XPATH", Read_Users_Components().alert_schedule_action_btn_by_xpath(), self.d)
        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_action_btn_by_xpath())
        action_ele.click()
        self.log.info("click on alert schedule action dropdown")
        time.sleep(web_driver.two_second)
        self.explicit_wait(10, "XPATH", Read_Users_Components().alert_schedule_action_option_edit_by_xpath(), self.d)
        edit = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_action_option_edit_by_xpath())
        edit.click()
        self.log.info("click on edit option")

    def verify_panel_is_editable(self):
        """
        checks alert schedule panel is editable
        """
        status = []
        self.explicit_wait(10, "XPATH", Read_Users_Components().alert_schedule_save_btn_by_xpath(), self.d)
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_cancel_btn_by_xpath())
        status.append(save.is_displayed())
        self.log.info(f"save btn is visible : {save.is_displayed()}")
        status.append(cancel.is_displayed())
        self.log.info(f"cancel btn is visible : {cancel.is_displayed()}")
        self.log.info(f"Status : {status}")
        return status

    def verify_save_and_cancel(self):
        """
        checks save and cancel
        """
        status = []
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_cancel_btn_by_xpath())
        status.append(save.is_displayed())
        self.log.info(f"save btn is visible : {save.is_displayed()}")
        status.append(cancel.is_displayed())
        self.log.info(f"save btn is visible : {cancel.is_displayed()}")
        status.append(save.is_enabled())
        self.log.info(f"save btn is clickable : {save.is_enabled()}")
        status.append(cancel.is_enabled())
        self.log.info(f"cancel btn is clickable : {cancel.is_enabled()}")
        self.log.info(f"Status : {status}")
        return status

    def verify_username_is_correct(self):
        """
        checks username is correct in alert schedule
        """
        user = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath())
        ex_user = user.text
        setting_user = self.d.find_element(By.XPATH, Read_Users_Components().settings_username_value_by_xpath())
        ac_user = setting_user.text
        self.log.info(f"ex_user : {ex_user}")
        self.log.info(f"ac_user : {ac_user}")
        return ex_user == ac_user

    def verify_timezone_id_is_correct(self):
        """
        checks timezone ID is correct in alert schedule
        """
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        details_icon.click()
        time.sleep(web_driver.one_second)
        timezone_ele = self.d.find_element(By.XPATH, Read_Users_Components().user_details_timezone_by_xpath())
        ex_timezone_id = timezone_ele.text
        setting_timezone_id = self.d.find_element(By.XPATH, Read_Users_Components().settings_timezone_value_by_xpath())
        ac_timezone_id = setting_timezone_id.text
        self.log.info(f"ex timezone : {ex_timezone_id}")
        self.log.info(f"ac timezone : {ac_timezone_id}")
        return ex_timezone_id == ac_timezone_id

    def verify_settings_yes_or_no_button(self):
        """
        checks the Send SMS, Send MMS, Send Email, Send In-App Notifications,
         Enable Alerts - Yes/No button is visible and clickable.
        """
        status = []
        send_sms_yes = self.d.find_element(By.XPATH, Read_Users_Components().send_sms_yes_btn_by_xpath())
        send_sms_yes.click()
        # send_sms_no = self.d.find_element(By.XPATH, Read_Users_Components().send_sms_no_btn_by_xpath())

        send_mms_yes = self.d.find_element(By.XPATH, Read_Users_Components().send_mms_yes_btn_by_xpath())
        send_mms_yes.click()
        # send_mms_no = self.d.find_element(By.XPATH, Read_Users_Components().send_mms_no_btn_by_xpath())

        send_email_yes = self.d.find_element(By.XPATH, Read_Users_Components().send_email_yes_btn_by_xpath())
        send_email_yes.click()
        # send_email_no = self.d.find_element(By.XPATH, Read_Users_Components().send_email_no_btn_by_xpath())

        send_in_app_notification_yes = self.d \
            .find_element(By.XPATH, Read_Users_Components().send_in_app_notification_yes_btn_by_xpath())
        send_in_app_notification_yes.click()
        # send_in_app_notification_no = self.d\
        #     .find_element(By.XPATH, Read_Users_Components().send_in_app_notification_no_btn_by_xpath())

        enable_alerts_yes = self.d.find_element(By.XPATH, Read_Users_Components().enable_alerts_yes_btn_by_xpath())
        # enable_alerts_no = self.d.find_element(By.XPATH, Read_Users_Components().enable_alerts_no_btn_by_xpath())

        status.append(send_sms_yes.is_displayed())
        self.logger.info(f"send_sms_yes is visible : {send_sms_yes.is_displayed()}")
        status.append(send_sms_yes.is_enabled())
        self.logger.info(f"send_sms_yes is clickable : {send_sms_yes.is_enabled()}")
        # status.append(send_sms_no.is_displayed())
        # self.logger.info(f"send_sms_no is visible : {send_sms_no.is_displayed()}")
        # status.append(send_sms_no.is_enabled())
        # self.logger.info(f"send_sms_no is clickable : {send_sms_no.is_enabled()}")

        status.append(send_mms_yes.is_displayed())
        status.append(send_mms_yes.is_enabled())
        # status.append(send_mms_no.is_displayed())
        # status.append(send_mms_no.is_enabled())
        self.logger.info(f"send_mms_yes is visible : {send_mms_yes.is_displayed()}")
        self.logger.info(f"send_mms_yes is clickable : {send_mms_yes.is_enabled()}")
        # self.logger.info(f"send_mms_no is visible : {send_mms_no.is_displayed()}")
        # self.logger.info(f"send_mms_no is clickable : {send_mms_no.is_enabled()}")

        status.append(send_email_yes.is_displayed())
        status.append(send_email_yes.is_enabled())
        # status.append(send_email_no.is_displayed())
        # status.append(send_email_no.is_enabled())
        self.logger.info(f"send_email_yes is visible : {send_email_yes.is_displayed()}")
        self.logger.info(f"send_email_yes is clickable : {send_email_yes.is_enabled()}")
        # self.logger.info(f"send_email_no is visible : {send_email_no.is_displayed()}")
        # self.logger.info(f"send_email_no is clickable : {send_email_no.is_enabled()}")

        status.append(send_in_app_notification_yes.is_displayed())
        status.append(send_in_app_notification_yes.is_enabled())
        # status.append(send_in_app_notification_no.is_displayed())
        # status.append(send_in_app_notification_no.is_enabled())
        self.logger.info(f"send_in_app_notification_yes is visible : {send_in_app_notification_yes.is_displayed()}")
        self.logger.info(f"send_in_app_notification_yes is clickable : {send_in_app_notification_yes.is_enabled()}")
        # self.logger.info(f"send_in_app_notification_no is visible : {send_in_app_notification_no.is_displayed()}")
        # self.logger.info(f"send_in_app_notification_no is clickable : {send_in_app_notification_no.is_enabled()}")

        status.append(enable_alerts_yes.is_displayed())
        status.append(enable_alerts_yes.is_enabled())
        # status.append(enable_alerts_no.is_displayed())
        # status.append(enable_alerts_no.is_enabled())
        self.logger.info(f"enable_alerts_yes is visible : {enable_alerts_yes.is_displayed()}")
        self.logger.info(f"enable_alerts_yes is clickable : {enable_alerts_yes.is_enabled()}")
        # self.logger.info(f"enable_alerts_no is visible : {enable_alerts_no.is_displayed()}")
        # self.logger.info(f"enable_alerts_no is clickable : {enable_alerts_no.is_enabled()}")
        self.logger.info(f"Status : {status}")
        return status

    def verify_day_checkbox(self):
        """
        checks schedule day checkbox is visible and clickable
        """
        status = []
        checkbox = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_day_checkbox_by_xpath())
        for x in checkbox:
            status.append(x.is_displayed())
            status.append(x.is_enabled())
            self.logger.info(f"day checkbox is visible : {x.is_displayed()}")
            self.logger.info(f"day checkbox is clickable : {x.is_enabled()}")
        self.logger.info(f"Status : {status}")
        return status

    def verify_time_range_slider(self):
        """
        checks schedule day checkbox is visible and clickable
        """
        status = []
        slider = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_slider_by_xpath())
        for x in slider:
            status.append(x.is_displayed())
        self.logger.info(f"Status : {status}")
        return status

    def verify_on_marking_the_time_range_slider_is_enabled(self):
        """
        checks time slider is enabled after selecting the days checkbox
        """
        status = []
        checkbox = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_day_checkbox_by_xpath())
        modified_path = Read_Users_Components().schedule_day_checkbox_by_xpath() + "/ins"
        checkbox_ins = self.d.find_elements(By.XPATH, modified_path)
        for x in range(len(checkbox)):
            if "checked" not in checkbox[x].get_attribute("class"):
                # checkbox_ins[x].click()
                javascript_executor_click(checkbox_ins[x])
                time.sleep(web_driver.one_second)

        slider = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_slider_by_xpath())
        for y in slider:
            status.append("disabled" not in y.get_attribute("class"))

        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        time_range = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_by_xpath())
        for z in time_range:
            status.append("Not Enabled" not in z.text)
        self.logger.info(f"Status : {status}")
        return status

    def verify_on_un_marking_the_time_range_slider_is_disabled(self):
        """
        checks time slider is disabled after un-selecting the days checkbox
        """
        status = []
        checkbox = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_day_checkbox_by_xpath())
        modified_path = Read_Users_Components().schedule_day_checkbox_by_xpath() + "/ins"
        checkbox_ins = self.d.find_elements(By.XPATH, modified_path)
        for x in range(len(checkbox)):
            if "checked" in checkbox[x].get_attribute("class"):
                javascript_executor_click(checkbox_ins[x])
                time.sleep(web_driver.one_second)

        slider = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_slider_by_xpath())
        for y in slider:
            status.append("disabled" in y.get_attribute("class"))

        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        time_range = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_by_xpath())
        for z in time_range:
            status.append("Not Enabled" in z.text)
        self.logger.info(f"Status : {status}")
        return status

    def verify_send_sms_toggle_yes_or_no(self):
        """
        checks if send sms yes or no button is functioning properly
        """
        status = []
        yes_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_sms_yes_btn_by_xpath())
        yes_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_sms_value_by_xpath())
        status.append(send_sms_value.text == "Yes")

        self.click_on_alert_schedule_action_option_edit()
        time.sleep(web_driver.one_second)
        no_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_sms_no_btn_by_xpath())
        no_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_sms_value_by_xpath())

        status.append(send_sms_value.text == "No")
        self.logger.info(f"Status : {status}")
        return status

    def verify_send_mms_toggle_yes_or_no(self):
        """
        checks if send mms yes or no button is functioning properly
        """
        status = []
        yes_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_mms_yes_btn_by_xpath())
        yes_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_mms_value_by_xpath())
        status.append(send_sms_value.text == "Yes")

        self.click_on_alert_schedule_action_option_edit()
        time.sleep(web_driver.one_second)
        no_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_mms_no_btn_by_xpath())
        no_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_mms_value_by_xpath())

        status.append(send_sms_value.text == "No")
        self.logger.info(f"Status : {status}")
        return status

    def verify_send_email_toggle_yes_or_no(self):
        """
        checks if send email yes or no button is functioning properly
        """
        status = []
        yes_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_email_yes_btn_by_xpath())
        yes_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_email_value_by_xpath())
        status.append(send_sms_value.text == "Yes")

        self.click_on_alert_schedule_action_option_edit()
        time.sleep(web_driver.one_second)
        no_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_email_no_btn_by_xpath())
        no_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_email_value_by_xpath())

        status.append(send_sms_value.text == "No")
        self.logger.info(f"Status : {status}")
        return status

    def verify_send_in_app_notifications_toggle_yes_or_no(self):
        """
        checks if enable alerts yes or no button is functioning properly
        """
        status = []
        yes_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_in_app_notification_yes_btn_by_xpath())
        yes_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d \
            .find_element(By.XPATH, Read_Users_Components().settings_send_in_app_value_notifications_by_xpath())
        status.append(send_sms_value.text == "Yes")

        self.click_on_alert_schedule_action_option_edit()
        time.sleep(web_driver.one_second)
        no_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_in_app_notification_no_btn_by_xpath())
        no_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d \
            .find_element(By.XPATH, Read_Users_Components().settings_send_in_app_value_notifications_by_xpath())

        status.append(send_sms_value.text == "No")
        self.logger.info(f"Status : {status}")
        return status

    def verify_enable_alerts_toggle_yes_or_no(self):
        """
        checks if enable alerts yes or no button is functioning properly
        """
        status = []
        yes_btn = self.d.find_element(By.XPATH, Read_Users_Components().enable_alerts_yes_btn_by_xpath())
        yes_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_enable_alerts_value_by_xpath())
        status.append(send_sms_value.text == "Yes")

        self.click_on_alert_schedule_action_option_edit()
        time.sleep(web_driver.one_second)
        no_btn = self.d.find_element(By.XPATH, Read_Users_Components().enable_alerts_no_btn_by_xpath())
        no_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_enable_alerts_value_by_xpath())

        status.append(send_sms_value.text == "No")
        self.logger.info(f"Status : {status}")
        return status

    def verify_close_panel_button_is_visible_and_clickable(self):
        status = []
        close_panel = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_close_panel_by_xpath())
        status.append(close_panel.is_displayed())
        status.append(close_panel.is_enabled())
        move_to_element(close_panel)
        time.sleep(web_driver.one_second)
        hover_txt = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_hover_text_by_xpath())
        for x in hover_txt:
            if x.is_displayed():
                status.append(x.text == Read_Users_Components().close_panel_hover_validation_txt())
        self.logger.info(f"Status : {status}")
        return status

    def verify_alert_schedule_panel_is_closing(self):
        all_panels = self.d.find_elements(By.XPATH, Read_Users_Components().all_open_panel_titles_by_xpath())
        for x in all_panels:
            self.log.info(x.text)
        close_panel = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_close_panel_by_xpath())
        close_panel.click()
        time.sleep(web_driver.one_second)
        all_panels = self.d.find_elements(By.XPATH, Read_Users_Components().all_open_panel_titles_by_xpath())

        return len(all_panels) == 1 and all_panels[0].text == \
            Read_Users_Components().users_panel_title_validation_text()

    def delete_randomly_created_users(self):
        pass
        # try:
        #     time.sleep(web_driver.one_second)
        #     # users_created = self.d.find_elements(By.XPATH, Read_Users_Components().facefirst_user_xpath())
        #     users_created = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().facefirst_user_xpath(), self.d)
        #     user_checkbox = self.d.find_elements(By.XPATH, Read_Users_Components().user_checkbox_by_xpath())
        #     time.sleep(web_driver.one_second)
        #     for i in range(len(users_created)):
        #         if Read_Users_Components().user_name_input_data() in users_created[i].text:
        #             print(f"{Read_Users_Components().user_name_input_data()}")
        #             user_checkbox[i].click()
        #             print(f"{user_checkbox[i]}")
        #             action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
        #             action_btn.click()
        #             time.sleep(web_driver.one_second)
        #             delete_user = self.d.find_element(By.XPATH, Read_Users_Components().delete_selected_user_by_xpath())
        #             delete_user.click()
        #             time.sleep(web_driver.one_second)
        #             yes_delete_selected = self.d.find_element(By.XPATH, Read_Users_Components().yes_delete_selected_button())
        #             yes_delete_selected.click()
        #
        # except Exception as ex:
        #     print(ex)

    def Verify_reassigning_user_to_diferrent_region(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.two_second)

            username = Read_Users_Components().constant_user_name()
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.two_second)

            details_button = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
            details_button.click()

            time.sleep(web_driver.two_second)

            action_bx = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().user_details_action_btn(),
                                                 self.d)
            action_bx.click()
            self.logger.info("In Users Details panel, Action dropdown is clicked")
            self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_action_edit_user(), self.d).click()
            self.logger.info("Edit option is clicked")
            time.sleep(web_driver.one_second)

            new_region = Read_Users_Components().new_region_data_input()
            self.select_region(new_region)
            region_save_button = self.d.find_element(By.XPATH, Read_Users_Components().region_save_btn_by_xpath())
            region_save_button.click()
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.two_second)

            if region != new_region:
                return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_10_exception.png")
            self.log.info(f"test_TC_US_10_exception: {ex}")
            return False
        finally:
            self.delete_randomly_created_users()
            logout().logout_from_core(self.d)
            self.d.refresh()

    def Verify_user_able_to_link_unlink_notification_group_from_Users_panel(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.two_second)

            username = Read_Users_Components().constant_user_name() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.two_second)

            self.check_if_user_is_created(user_name=username)

        except Exception as ex:
            print(ex)

    def verify_details_of_core_user(self):
        try:
            status = []
            users_dict = self.Read_user_from_json()
            users_list = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            time.sleep(web_driver.two_second)

            search_box_by_xpath = self.explicit_wait(10, "XPATH", Read_Users_Components().search_box_by_xpath(), self.d)
            search_box_by_xpath.send_keys(Read_Users_Components().get_core_username())
            time.sleep(web_driver.two_second)

            details_icon = self.explicit_wait(10, "XPATH", Read_Users_Components().get_core_details_button(), self.d)
            details_icon.click()

            username = self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_username_by_xpath(), self.d)
            self.logger.info(f"username is {username.text}")
            time.sleep(web_driver.one_second)
            username1 = Portal_login_page_read_ini().get_valid_login_username()
            self.logger.info(f"expected username: {username1}")
            userrole = self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_user_role_by_xpath(),
                                          self.d)
            self.logger.info(f"user role is {userrole.text}")
            time.sleep(web_driver.one_second)
            userrole1 = Read_Users_Components().read_core_user_user_role().upper()
            self.logger.info(f"expected user role: {userrole1}")
            region = self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_region_by_xpath(), self.d)
            self.logger.info(f"region is {region.text}")
            time.sleep(web_driver.one_second)
            region1 = Read_Users_Components().read_core_user_region()
            self.logger.info(f"expected region: {region1}")
            email = self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_email_by_xpath(), self.d)
            self.logger.info(f"email is {email.text}")
            time.sleep(web_driver.one_second)
            email1 = users_dict["users"][0]["Email"]
            self.logger.info(f"expected email: {email1}")
            time_Zone = self.explicit_wait(10, "XPATH", Read_Users_Components().user_details_timezone_by_xpath(),
                                           self.d)
            self.logger.info(f"time zone is {time_Zone.text}")
            time.sleep(web_driver.one_second)
            time_zone1 = Read_Users_Components().read_core_user_timezone()
            self.logger.info(f"expected time zone: {time_zone1}")
            time.sleep(web_driver.one_second)
            if username.text == username1:
                status.append(True)
            else:
                status.append(False)
            time.sleep(web_driver.one_second)
            if userrole.text == userrole1:
                status.append(True)
            else:
                status.append(False)
            time.sleep(web_driver.one_second)
            if region.text == region1:
                status.append(True)
            else:
                status.append(False)
            time.sleep(web_driver.one_second)
            if email.text == email1:
                status.append(True)
            else:
                status.append(False)
            time.sleep(web_driver.one_second)
            if time_Zone.text == time_zone1:
                status.append(True)
            else:
                status.append(False)
            self.logger.info(f"status: {status}")
            Visitor_Search_Module_pom().click_on_logout_button()
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_US_112.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_US_112_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_US_112 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_US_112_Exception.png")
            return False

    def Verify_total_users_are_n_including_default_user(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            time.sleep(web_driver.two_second)

            total_number_of_users_displayed = self.d.find_element(By.XPATH,
                                                                  Read_Users_Components().get_Total_number_of_user_displayed())
            print(total_number_of_users_displayed.text)
            self.logger.info(f"Total number of users created are {total_number_of_users_displayed.text}")
            time.sleep(web_driver.one_second)
            if total_number_of_users_displayed.is_displayed():
                return True
            else:
                return False
        except Exception as ex:
            print(ex.args)
        finally:
            logout().logout_from_core(self.d)

    def Create_5_users_with_all_required_field(self):
        global i
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            time.sleep(web_driver.two_second)
            x = []
            list_of_user = self.d.find_elements(By.XPATH, Read_Users_Components().get_list_of_users())
            time.sleep(web_driver.one_second)
            for i in list_of_user:
                # print(i.text)
                x = i.text
                print(x)

            for i in list_of_user:
                time.sleep(web_driver.one_second)
                search_box_by_xpath = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
                search_box_by_xpath.clear()
                search_box_by_xpath.send_keys(i.text)
                time.sleep(web_driver.two_second)
            i = i + 1
        except Exception as ex:
            print(ex.args)

    def Verify_for_above_5_users_region_edges_are_properly_assigned(self):
        try:
            status = []
            self.logger.info("users module started")
            users_dict = self.Read_user_from_json()
            users_list = []
            username = users_dict["users"][4]["username"]
            login().login_with_persona_user(self.d, username)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            dictionary_length = len(users_dict["users"])
            print("length of dictionary is", dictionary_length)
            # x = Read_Users_Components().region_names_from_ini()
            # user_list = x.split(',')
            # self.logger.info(f"eg list: {user_list}")

            count = 0
            for i in range(dictionary_length):
                time.sleep(web_driver.one_second)
                search_box_by_xpath = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
                search_box_by_xpath.clear()
                search_box_by_xpath.send_keys(users_dict["users"][i]["username"])
                time.sleep(web_driver.one_second)
                details_button = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
                details_button.click()
                time.sleep(web_driver.one_second)
                actual_region_name = self.d.find_element(By.XPATH, Read_Users_Components().region_name())
                self.logger.info(f"actual region name is: {actual_region_name.text}")
                expected_region_name = users_dict["users"][i]["user_orgahierarchy"]
                self.logger.info(f"expected username is {expected_region_name}")
                if actual_region_name.text == expected_region_name:
                    status.append(True)
                else:
                    status.append(False)
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_100.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_100_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_100 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_100_Exception.png")
            return False
        finally:
            logout().logout_from_core(self.d)

    def Verify_org_hierarchy_selection_root_name_should_be_able_to_match_with_DM_core_name(self):
        try:
            status = []

            self.logger.info("users module started")
            time.sleep(web_driver.one_second)
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            time.sleep(web_driver.two_second)
            self.click_on_action_btn()
            time.sleep(web_driver.one_second)
            create_user = self.d.find_element(By.XPATH, Read_Users_Components().create_user_by_xpath())
            create_user.click()
            time.sleep(web_driver.two_second)
            region_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Users_Components().region_by_xpath(), self.d)
            region_ele.click()
            self.logger.info("clicked on Users region panel")
            time.sleep(web_driver.two_second)
            root_name = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().root_region_name_by_xpath())
            root_region_name_on_US = root_name.text
            self.logger.info(f"Root region name on VS: {root_region_name_on_US}")
            save_btn = self.explicit_wait(10, "XPATH", Read_Users_Components().
                                          region_save_btn_by_xpath(), self.d)
            save_btn.click()
            self.d.switch_to.new_window()
            login().login_to_DM_if_not_done(self.d)
            Visitor_Search_Module_pom().get_root_region_name_on_DM()
            root_region_name_on_DM = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                         get_root_region_name_on_dm_by_xpath())
            self.logger.info(f"Root region name on DM: {root_region_name_on_DM.text.upper()}")
            time.sleep(web_driver.two_second)
            if root_region_name_on_US.upper() == root_region_name_on_DM.text.upper():
                self.logger.info(f"Root region names on US and DM are same...")
                status.append(True)
            else:
                self.logger.info(f"Root region names on US and DM are not same...")
                status.append(False)
            Visitor_Search_Module_pom().close_current_tab()
            Visitor_Search_Module_pom().click_on_logout_button()
            self.logger.info(f"status: {status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_100.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_100_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_100 got an exception as: {ex}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_100_Exception.png")
            return False

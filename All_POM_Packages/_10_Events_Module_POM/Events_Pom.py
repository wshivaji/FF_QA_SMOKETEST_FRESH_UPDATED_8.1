import time
from pathlib import Path

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from All_Config_Packages._10_Events_Config_Files.Events_Read_Ini import events_Read_Ini
from All_Config_Packages._11_Enrollment_Module_Config_Files.Enrollment_Module_Read_INI import read_enrollment_components
from All_Config_Packages._12_Identify_and_Enroll_Config_Files.Identify_and_Enroll_Readd_INI import \
    Read_Identify_and_Enroll_Components
from All_Config_Packages._9_tags_module_Config_Files.Tags_Read_INI import Read_Tags_Components
from Base_Package.Login_Logout_Ops import login
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


class events_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []
    # def __init__(self):
    #     self.d = web_driver.d()
    #     self.logger = web_logger.logger_obj()
    #     self.status = []

    def add_details_panel_cancel(self):
        self.logger.info("cancel btn on add details panel")
        cancle_btn = self.d.find_element(By.XPATH, events_Read_Ini().cancle_btn_on_add_details_panel_by_xpath())
        if cancle_btn.is_displayed():
            cancle_btn.click()
        else:
            pass

        time.sleep(web_driver.one_second)

        cancle_on_warning = self.d.find_element(By.XPATH, events_Read_Ini().cancel_button_in_warning_add_details())
        if cancle_on_warning.is_displayed():
            cancle_on_warning.click()
        else:
            pass

        time.sleep(web_driver.one_second)

    def verify_load_more_btn(self):
        try:
            self.logger.info("verifying load more btn")
            displaying_number_of_events_text = self.d.find_element(By.XPATH, events_Read_Ini().total_number_of_events_happened_out_of_total_number_of_events())
            self.logger.info(f"events text displayed: {displaying_number_of_events_text.text}")
            load_more_list = self.d.find_elements(By.XPATH, events_Read_Ini().loadmore_button())
            load_more_btn = 0

            if len(load_more_list) > 0:
                load_more_btn = load_more_list[0].is_displayed()
            else:
                load_more_btn = False
            print(f"displaying: {displaying_number_of_events_text.text}")
            text_displayed = displaying_number_of_events_text.text
            text_list = text_displayed.split(' ')
            self.logger.info(f"text list: {text_list}")
            num = []
            if len(text_list) > 0:
                for x in text_list:
                    if x.isdigit():
                        num.append(int(x))
                        self.logger.info(f"x: {x}")
                    else:
                        pass
            self.logger.info(f"num: {num}")
            displayed_events = 0
            total_events = 0
            if len(num) > 0:
                displayed_events = num[0]
                total_events = num[1]
            self.logger.info(f"events displayed: {displayed_events}")
            self.logger.info(f"total events: {total_events}")
            if total_events > 0:
                if total_events > 20 and load_more_btn == True:
                    return True
                if total_events < 20 and load_more_btn == False:
                    return True
                else:
                    return False
            else:
                print("No events displayed")
                return True

        except Exception as ex:
            print(f"Load More btn exception: {ex.args}")

    def Launching_login_page(self):
        try:
            self.logger.info(f"*****TC_001***** started")
            login().login_to_cloud_if_not_done(self.d)
            # self.d.get(events_Read_Ini().get_Launching_url())
            expected_url = events_Read_Ini().get_Launching_url()
            time.sleep(web_driver.one_second)
            # self.d.maximize_window()
            actual_url = self.d.current_url
            print(f"actual: {actual_url}, \nexpected: {expected_url}")
            if expected_url == actual_url:
                self.status.append(True)
            else:
                self.status.append(False)

            actual_title = self.d.title
            print("actual is", actual_title)
            expected_title = events_Read_Ini().get_expecting_title_webportal_login()
            print("expected title is", expected_title)
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            print(self.status)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_events_001.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_001.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_events_001.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\Tc_events_001.png")
            self.logger.error(f"Tc_events_001 got exception as: {ex}")

    def logo_username_texbox_password_textbox_is_visible(self):
        try:
            self.logger.info("*****TC_002***** started")
            login().login_to_cloud_if_not_done(self.d)
            # self.d.get(events_Read_Ini().get_Launching_url())
            self.status.clear()
            time.sleep(web_driver.three_second)
            # self.d.maximize_window()
            logo = self.d.find_element(By.XPATH, events_Read_Ini().get_logo_is_visible_on_login_page())
            username = self.d.find_element(By.XPATH, events_Read_Ini().get_username_textbox())
            username.is_displayed()
            password = self.d.find_element(By.XPATH, events_Read_Ini().get_password_textbox())
            password.is_displayed()
            if logo.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            print(self.status)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_events_002.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_002.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_002.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\Tc_events_002.png")
            self.logger.error(f"TC_events_002 got exception as: {ex} ")

    def load_login_page_if_not_loaded(self):
        try:
            self.d.get(events_Read_Ini().get_Launching_url())
            expected_url = events_Read_Ini().get_Launching_url()
            time.sleep(web_driver.one_second)
            self.d.maximize_window()
            actual_url = self.d.current_url
            print(f"actual: {actual_url}, \nexpected: {expected_url}")
            if expected_url == actual_url:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.three_second)
            username = self.d.find_element(By.XPATH, events_Read_Ini().get_username_textbox())
            username.clear()
            username.send_keys(events_Read_Ini().get_valid_username())
            time.sleep(web_driver.two_second)
            password = self.d.find_element(By.XPATH, events_Read_Ini().get_password_textbox())
            password.clear()
            password.send_keys(events_Read_Ini().get_valid_password())
            time.sleep(web_driver.two_second)
            cloud_login = self.d.find_element(By.XPATH, events_Read_Ini().get_cloudlogin_button())
            cloud_login.click()
            time.sleep(web_driver.two_second)
        except Exception as ex:
            print(ex)





    def on_Events_page_Enter_a_text_in_search_filter_by_action_textbox_and_verify_number_of_events_displayed(self):
        try:
            self.logger.info("*********TC_009****** started")
            # # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            search_filter_by_action_textbox = self.d.find_element(By.XPATH, events_Read_Ini().search_filter_by_action_textbox())
            search_filter_by_action_textbox.clear()
            search_filter_by_action_textbox.send_keys(events_Read_Ini().Enter_a_action_text())
            time.sleep(web_driver.two_second)
            diplaying_text_actualtext = self.d.find_element(By.XPATH, events_Read_Ini().total_number_of_events_happened_out_of_total_number_of_events())
            print(diplaying_text_actualtext.text)
            time.sleep(web_driver.one_second)
            number_of_events_happened_text = self.d.find_element(By.XPATH, events_Read_Ini().get_number_of_text())
            print(number_of_events_happened_text.text)
            if diplaying_text_actualtext.is_displayed():
                self.logger.info("displayed number of events of mentioned action")
                self.status.append(True)
            else:
                self.logger.info(" number of events of mention action is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_009.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_009.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_009.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_009.png")
            self.logger.error(f"TC_events_009 got exception as: {ex} ")


    def on_Events_page_click_on_load_more_button_and_verify_number_of_Events_count_is_40_displayed(self):
        try:
            self.logger.info("********TC_022******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_elements(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            if len(events) <= 0:
                self.d.refresh()

            events = self.explicit_wait(10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)

            self.logger.info("waiting for events")
            events.click()
            time.sleep(web_driver.three_second)

            # load_more_button = self.d.find_element(By.XPATH, events_Read_Ini().loadmore_button())
            # load_more_button = self.explicit_wait(10, "XPATH", events_Read_Ini().loadmore_button(), self.d)
            load_more_btn = self.verify_load_more_btn()
            self.logger.info("waiting for load more.")
            if load_more_btn:
                load_more_list = self.d.find_elements(By.XPATH, events_Read_Ini().loadmore_button())
                # load_more_btn = 0
                if len(load_more_list) > 0:
                    load_more = load_more_list[0]
                    load_more.click()
                    displaying_text_list = self.d.find_elements(By.XPATH, events_Read_Ini().total_number_of_events_happened_out_of_total_number_of_events())
                    if len(displaying_text_list) > 0:
                        displaying_text = displaying_text_list[0].text
                        print(displaying_text)
                        time.sleep(web_driver.one_second)
                        no_of_events_text = self.d.find_element(By.XPATH, events_Read_Ini().get_number_of_text())
                        print(no_of_events_text.text)
                        self.logger.info(f"number of events: {no_of_events_text.text}")
                        if int(no_of_events_text.text) > 20:
                            self.logger.info("after clicking loadmore button next 20 is displayed")
                            self.status.append(True)
                        else:
                            self.logger.info("next 20 events i.e, 40 is not displayed")
                            self.status.append(False)
                        self.logger.info(f"status :{self.status}")
            else:
                self.logger.info("Load More Btn is not displayed.")
                self.status.append(True)
            # time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_022.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_022.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_022.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_022.png")
            self.logger.error(f"TC_events_022 got exception as: {ex} ")


    def on_Events_location_page_verify_Find_textbox_is_visible(self):
        try:
            self.logger.info("********TC_026******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            textbox = self.d.find_element(By.XPATH, events_Read_Ini().get_find_location_textbox_in_notes_location())
            if textbox.is_displayed():
                self.logger.info("textbox is visible")
                self.status.append(True)
            else:
                self.logger.info("textbox is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_026.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_026.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_026.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_026.png")
            self.logger.error(f"TC_events_026 got exception as: {ex} ")

    def on_Events_location_page_on_map_facefirst_logo_is_visible_click_on_logo_event_is_visible(self):
        try:
            self.logger.info("*******TC_027****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            facefirstlogo = self.d.find_element(By.XPATH, events_Read_Ini().facefirst_logo_on_map())
            facefirstlogo.click()
            time.sleep(web_driver.one_second)
            live_image_onmap = self.d.find_element(By.XPATH, events_Read_Ini().live_image_on_map())
            time.sleep(web_driver.one_second)
            file_image_onmap = self.d.find_element(By.XPATH, events_Read_Ini().file_image_on_map())
            if live_image_onmap.is_displayed():

                self.logger.info("live image is visible")
                self.status.append(True)
            else:
                self.logger.info("live image  is not visible")
                self.status.append(False)
            if file_image_onmap.is_displayed():
                self.logger.info("file image is visible")
                self.status.append(True)
            else:
                self.logger.info("file image is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_027.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_027.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_027.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_027.png")
            self.logger.error(f"TC_events_027 got exception as: {ex} ")

    def on_Events_location_page_verify_Draw_circle_button_is_visible(self):
        try:
            self.logger.info("*********TC_028********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            draw_circle = self.d.find_element(By.XPATH, events_Read_Ini().get_drawcircle_button())
            if draw_circle.is_displayed():
                self.logger.info("draw circle button is visible")
                self.status.append(True)
            else:
                self.logger.info("draw circle button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_028.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_028.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_028.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_028.png")
            self.logger.error(f"TC_events_028 got exception as: {ex} ")

    def on_Events_Location_page_verify_serach_area_button_is_visible(self):
        try:
            self.logger.info("******TC_029**** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            search_area = self.d.find_element(By.XPATH, events_Read_Ini().get_search_area_button_on_notes_location())
            if search_area.is_displayed():
                self.logger.info("search area button is visible")
                self.status.append(True)
            else:
                self.logger.info("search area button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_029.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_029.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_029.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_029.png")
            self.logger.error(f"TC_events_029 got exception as: {ex} ")


    def on_Events_page_click_on_display_tags_and_verify_Tags_are_visible_inthe_formof_horizantal_line_below_the_events(self):
        try:
            self.logger.info("**********TC_045********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            display_tags = self.d.find_element(By.XPATH, events_Read_Ini().display_tags_in_eventspage())
            display_tags.click()
            time.sleep(web_driver.one_second)
            tags_display_belowline = self.d.find_element(By.XPATH, events_Read_Ini().tags_display_below_the_events())
            if tags_display_belowline.is_displayed():
                self.logger.info("tags are visible below the events")
                self.status.append(True)
            else:
                self.logger.info("tags are not visible below the events")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_045.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_045.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_045.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_045.png")
            self.logger.error(f"TC_events_04 got exception as: {ex} ")


    def on_Events_page_click_on_search_dropdow_and_verify_sort_by_AtoZ_radio_button_is_visible_and_clickable(self):
        try:
            self.logger.info("******TC_052******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.two_second)
            sort_by_atoz_radiobutton = self.d.find_element(By.XPATH, events_Read_Ini().sort_by_atoz_radiobutton())
            if sort_by_atoz_radiobutton.is_displayed():
                self.logger.info("sort by atoz radio button is visible")
                self.status.append(True)
            else:
                self.logger.info("sort by atoz radio button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_052.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_052.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_052.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_052.png")
            self.logger.error(f"TC_events_052 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdown_and_verify_sort_by_ZtoA_radio_button_is_visible_and_clickable(self):
        try:
            self.logger.info("******TC_053******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.three_second)
            sort_by_ztoa_radiobutton = self.d.find_element(By.XPATH, events_Read_Ini().sort_by_ztoa_radiobutton())
            if sort_by_ztoa_radiobutton.is_displayed():
                self.logger.info("sort by ztoa radio button is visible")
                self.status.append(True)
            else:
                self.logger.info("sort by ztoa radio button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_053.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_053.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_053.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_053.png")
            self.logger.error(f"TC_events_053 got exception as: {ex} ")


    def on_Events_page_click_on_search_dropdown_andverify_location_search_button_is_visible_and_clickable(self):
        try:
            self.logger.info("******TC_055******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.two_second)
            location_search_button = self.d.find_element(By.XPATH, events_Read_Ini().location_search_button_in_searchdropdown())
            print(location_search_button.text)
            if location_search_button.is_displayed():
                self.logger.info("location search button is visible")
                self.status.append(True)
            else:
                self.logger.info("location search button is not visible in search dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_055.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_055.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_055.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_055.png")
            self.logger.error(f"TC_events_055 got exception as: {ex} ")

    def on_Events_page_In_Action_dropdown_click_on_Edit_tags_option_and_verify_Events_tags_panel_is_visible_and_verify_panel_heading(self):
        try:
            self.logger.info("******TC_074******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            events_tags_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            if events_tags_panel_heading.is_displayed():
                self.logger.info("events_tags panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("events tags panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_074.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_074.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_074.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_074.png")
            self.logger.error(f"TC_events_074 got exception as: {ex} ")

    def on_Events_tags_panel_verify_filter_dropdown_is_visible_and_clickable(self):
        try:
            self.logger.info("*******TC_075****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            events_tags_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            filter_dropown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            if filter_dropown.is_displayed():
                self.logger.info("filter dropdown is visible in events tag panel is visible")
                self.status.append(True)
            else:
                self.logger.info("filter dropdown in events tag panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_075.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_075.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_075.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_075.png")
            self.logger.error(f"TC_events_075 got exception as: {ex} ")

    def on_Events_tags_panel_click_on_filter_dropdown_and_verify_linked_tags_and_unlinked_tag_options_are_visible(self):
        try:
            self.logger.info("*******TC_076******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            events_tags_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            filter_dropdown_options = self.d.find_elements(By.XPATH, events_Read_Ini().filter_dropdown_options())
            for options in filter_dropdown_options:
                if options.is_displayed():
                    self.logger.info(f"options are {options.text}")
                    self.status.append(True)
                else:
                    self.logger.info("filter dropdown options are not visible")
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_076.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_076.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_076.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_076.png")
            self.logger.error(f"TC_events_076 got exception as: {ex} ")

    def on_Events_tags_panel_click_on_linked_tags_in_filter_dropdown_and_verify_only_linked_tags_are_disiplayed(self):
        try:
            self.logger.info("*******TC_077******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            events_tags_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            # filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            # filter_dropdown.click()
            # time.sleep(web_driver.one_second)
            # linked_tags_option_in_filterdropdown = self.d.find_element(By.XPATH, events_Read_Ini().linked_tags_by_xpath())
            # linked_tags_option_in_filterdropdown.click()
            time.sleep(web_driver.one_second)
            linked_tags_banner = self.d.find_element(By.XPATH, events_Read_Ini().tags_banner())
            linked_tags = self.d.find_elements(By.XPATH, events_Read_Ini().tags_names())
            if linked_tags_banner.is_displayed():
                for i in linked_tags:
                    if i.is_displayed():
                        self.logger.info(f"linked tags are {i.text}")
                        self.status.append(True)
                    else:
                        self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")

            if False != [True, True, True, True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_077.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_077.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_077.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_077.png")
            self.logger.error(f"TC_events_077 got exception as: {ex} ")

    def on_Events_tags_panelclick_on_unlinked_tags_in_filter_dropdown_and_verify_only_unlinked_tags_banner_and_unlinked_tags_are_displayed(self):
        try:
            self.logger.info("*********TC_078******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            events_tags_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            unlinked_tags = self.d.find_element(By.XPATH, events_Read_Ini().unlinked_tags_by_xpath())
            unlinked_tags.click()
            time.sleep(web_driver.one_second)
            unlinked_tags_banner = self.d.find_element(By.XPATH, events_Read_Ini().tags_banner())
            unlinked_tags_names = self.d.find_elements(By.XPATH, events_Read_Ini().tags_names())
            if unlinked_tags_banner.is_displayed():
                self.logger.info("unlinked tags banner is visible")
                self.status.append(True)
                for i in unlinked_tags_names:
                    if i.is_displayed():
                        self.logger.info(f"unlinked tags are {i.text}")
            else:
                self.logger.info("unlinked tags banner is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False != [True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_078.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_078.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_078.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_078.png")
            self.logger.error(f"TC_events_078 got exception as: {ex} ")

    def on_Events_tags_panel_verify_filter_tag_name_text_box_is_visible(self):
        try:
            self.logger.info("*********TC_079******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            filter_tag_name_textbox = self.d.find_element(By.XPATH, events_Read_Ini().filter_tags_name_textbox())
            if filter_tag_name_textbox.is_displayed():
                self.logger.info("filter tag by name textbox is visible in events tag panel")
                self.status.append(True)
            else:
                self.logger.info("events tag by name textbox is not visible")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False !=  [True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_079.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_079.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_079.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_079.png")
            self.logger.error(f"TC_events_079 got exception as: {ex} ")

    def on_Events_tags_panelEnter_a_tagname_in_filter_tag_name_text_and_verify_only_text_entered_tags_are_displayed(self):
        try:
            self.logger.info("******TC_080****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            filter_tag_name_textbox = self.d.find_element(By.XPATH, events_Read_Ini().filter_tags_name_textbox())
            filter_tag_name_textbox.clear()
            filter_tag_name_textbox.send_keys(events_Read_Ini().enter_a_text_in_filter_tagname_texbox())
            time.sleep(web_driver.one_second)
            filter_tag_banner = self.d.find_element(By.XPATH, events_Read_Ini().tags_banner())
            if filter_tag_name_textbox.is_displayed():
                self.logger.info(f"tagname:{filter_tag_banner.text} is displayed")
                self.status.append(True)
            else:
                self.logger.info(f"tagname:{filter_tag_banner.text} is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False != [True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_080.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_080.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_080.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_080.png")
            self.logger.error(f"TC_events_080 got exception as: {ex} ")

    def Verify_user_is_able_to_link_the_tag_and_add_tag_to_probable_match_events_when_tag_icon_is_click(self):

        try:
            self.logger.info("********TC_085******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)

            tags_symbol = self.d.find_element(By.XPATH, events_Read_Ini().tags_button_in_eventspage())
            tags_symbol.click()
            time.sleep(web_driver.two_second)

            filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)

            unlinked_tags = self.d.find_element(By.XPATH,events_Read_Ini().unlinked_tags_by_xpath())
            unlinked_tags.click()
            time.sleep(web_driver.one_second)

            checkbox_in_tags = self.d.find_element(By.XPATH, events_Read_Ini().checkbox_number_twentyfour())
            checkbox_in_tags.click()
            time.sleep(web_driver.one_second)

            action_dropdown_in_eventstags = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events_tag())
            action_dropdown_in_eventstags.click()
            time.sleep(web_driver.one_second)

            add_tags =  self.d.find_element(By.XPATH, events_Read_Ini().add_tags_to_event_option_in_event_tags())
            add_tags.click()
            time.sleep(web_driver.two_second)
            tagnames = self.d.find_elements(By.XPATH, events_Read_Ini().tagnames_below_to_an_event())
            for op in tagnames:
                if op.is_displayed():
                    self.logger.info(f"tagnames are visible {op.text}")
                    self.status.append(True)
                else:
                    self.logger.info("tagnames are not visible")
                    self.status.append(False)
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_085.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_085.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_085.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_085.png")
            self.logger.error(f"TC_events_085 got exception as: {ex} ")


    def Verify_user_is_able_to_unlink_the_tag_and_remove_tag_from_probable_match_events_when_tag_icon_is_click(self):
        try:
            self.logger.info("********TC_087******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)

            tags_symbol = self.d.find_element(By.XPATH, events_Read_Ini().tags_button_in_eventspage())
            tags_symbol.click()
            time.sleep(web_driver.two_second)

            filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)

            linked_tags = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().linked_tags_by_xpath(), self.d)
            linked_tags.click()
            time.sleep(web_driver.one_second)

            checkbox_twentyfour = self.d.find_element(By.XPATH, events_Read_Ini().checkbox_number_twentyfour())
            checkbox_twentyfour.click()
            time.sleep(web_driver.one_second)

            action_dropdown_in_events_tag = self.d.find_element(By.XPATH,
                                                                events_Read_Ini().action_dropdown_in_events_tag())
            action_dropdown_in_events_tag.click()
            time.sleep(web_driver.one_second)
            remove_tags = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                   .remove_tags_to_event_in_eventstag(), self.d)
            remove_tags.click()
            time.sleep(web_driver.one_second)
            tagnames = self.d.find_elements(By.XPATH, events_Read_Ini().tagnames_below_to_an_event())
            for opt in tagnames:
                if opt.is_displayed():
                    self.logger.info(f"options are {opt.text} ")
                    self.status.append(True)
                else:
                    self.logger.info("options are not visible")
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_087.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_087.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_087.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_087.png")
            self.logger.error(f"TC_events_087 got exception as: {ex} ")


    def Verify_user_is_able_to_perform_identify_within_enrollments_fromEnrollment_View_panel_when_event_icon_is_click(self):

        try:
            self.logger.info("*******TC_05***** started")
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            self.logger.info("events panel opened")
            time.sleep(web_driver.one_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("events btn clicked.")
            action_dropdown = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                       .action_dropdown_in_enrollmentview(), self.d)
            action_dropdown.click()
            self.logger.info("action dropdown is visible.")
            identify_within_enrollments = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                                   .identify_within_enrollments_in_enrollmentview(), self.d)
            identify_within_enrollments.click()
            self.logger.info("identify within enrollments option visible")
            time.sleep(web_driver.one_second)
            identify_enroll_panel = web_driver.explicit_wait(self, 10, "XPATH",events_Read_Ini()
                                                             .identify_and_enroll_panel(), self.d)

            identify_results = web_driver.explicit_wait(self, 10, "XPATH",
                                     events_Read_Ini().identify_results_panel(), self.d)
            self.logger.info(f"identify result panel visible: {identify_results.is_displayed()}")
            if identify_enroll_panel.is_displayed():
                self.logger.info("identify and enroll panel is visible")
                self.status.append(True)
            else:
                self.logger.info("identify and enroll panel is not visible")
                self.status.append(False)
            if identify_results.is_displayed():
                self.logger.info("identify results panel is visible")
                self.status.append(True)
            else:
                self.logger.info("identify results panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            # self.add_details_panel_cancel()
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_05.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_05.png")
                self.logger.info("returning False.")
                return False
            else:
                self.logger.info("returning True.")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_05.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_05.png")
            self.logger.error(f"TC_events_05 got exception as: {ex} ")

    def Verify_user_is_able_to_perform_identify_within_visitors_from_Probable_Match_Enrollment_View_panel_when_event_icon_is_click(self):
        try:
            self.logger.info("********TC_06********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            identify_within_visitors = self.d.find_element(By.XPATH, events_Read_Ini().identify_within_visitors_in_enrollmentview())
            identify_within_visitors.click()
            time.sleep(web_driver.two_second)
            visitor_search_panel = self.d.find_element(By.XPATH, events_Read_Ini().visitor_search_panel())
            time.sleep(web_driver.two_second)
            submit_search = self.d.find_element(By.XPATH,events_Read_Ini().submit_search_button())
            submit_search.click()
            time.sleep(10)
            vs_completed_banner = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().visitor_search_complted_banner(), self.d)

            # vs_search = self.d.find_element(By.XPATH,events_Read_Ini().visitor_search_complted_banner())
            if vs_completed_banner.is_displayed():
                self.logger.info("visitor search completed banner is visible")
                self.status.append(True)
            else:
                self.logger.info(" visitor search banner is  not visible")
                self.status.append(False)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_06.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_06.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_06.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_06.png")
            self.logger.error(f"TC_events_06 got exception as: {ex} ")

    def on_Enrollment_view_click_on_view_Edits_details_in_Acton_dropdown_and_verify_Enrollment_details_panel_is_visible(self):
        try:
            self.logger.info("*******TC_07******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            edit_view_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_view_enrollment_option_in_actiondropdown())
            edit_view_option.click()
            time.sleep(web_driver.one_second)
            enrollment_details_panel = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_details_panel())
            if enrollment_details_panel.is_displayed():
                self.logger.info("enrollment details panel is visible")
                self.status.append(True)
            else:
                self.logger.info("enrollment details panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_07.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_07.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_07.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_07.png")
            self.logger.error(f"TC_events_07 got exception as: {ex} ")

    def Verify_user_enroller_of_an_enrollment_is_able_to_enable_the_disable_enrolled_subject_on_Enrollment_View_modules(self):
        try:
            self.logger.info("******TC_110******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            # events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            self.logger.info("events panel is opened.")
            time.sleep(web_driver.three_second)
            # event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            self.logger.info("events btn is clicked")
            time.sleep(web_driver.two_second)
            # action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            action_dropdown = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().action_dropdown_in_enrollmentview(), self.d)
            action_dropdown.click()
            self.logger.info("action dropdown is clicked.")
            time.sleep(web_driver.one_second)
            # disabled_enrollment = self.d.find_element(By.XPATH, events_Read_Ini().disabled_enrollment_in_enrollmentview())
            disabled_enrollment = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().disabled_enrollment_in_enrollmentview(), self.d)
            disabled_enrollment.click()
            self.logger.info("disable enrollment clicked.")
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.two_second)
            disabled_text_in_enrollmentview = self.d.find_element(By.XPATH, events_Read_Ini().disabled_text_in_enrollmentview_page())
            self.logger.info(f"disabled text visible: {disabled_text_in_enrollmentview.is_displayed()}")
            if disabled_text_in_enrollmentview.is_displayed():
                self.logger.info("disabled text is visible in enrollment view panel")
                self.status.append(True)
                self.logger.info("appending True")
            else:
                self.logger.info("disabled text is not visible in enrollment view panel")
                self.status.append(False)
                self.logger.info("appending False")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_110.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_110.png")
                self.logger.info("returning False")
                return False
            else:
                self.logger.info("returning True")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_110.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_110.png")
            self.logger.error(f"TC_events_110 got exception as: {ex} ")

    def Verify_user_is_able_to_edit_the_Enrollment_details_on_Enrollment_View_panel_when_ProbableMatch_Event_icon_is_click(self):
        try:
            self.logger.info("*********TC_08******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)

            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)

            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)

            enrollment_details_button = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_details_button_in_enrollment_view_panel())
            enrollment_details_button.click()
            time.sleep(web_driver.two_second)

            action_dropdown_on_en_details = self.d.find_element(By.XPATH,events_Read_Ini().action_dropdown_on_en_details())
            action_dropdown_on_en_details.click()
            time.sleep(web_driver.one_second)

            edit_option_inside_action = self.d.find_element(By.XPATH,events_Read_Ini().edit_option_inside_en_details())
            edit_option_inside_action.click()
            time.sleep(web_driver.one_second)

            case_event = self.d.find_element(By.XPATH,events_Read_Ini().case_event_dropdown())
            select = Select(case_event)
            select.select_by_index(1)
            time.sleep(web_driver.one_second)

            save_button = self.d.find_element(By.XPATH,events_Read_Ini().save_button_on_en_details())
            save_button.click()
            time.sleep(web_driver.one_second)

            visible_case_event = self.d.find_element(By.XPATH,events_Read_Ini().visible_case_event_data())
            self.logger.info(f"After editing case event is : {visible_case_event.text}")

            read_case_event = events_Read_Ini().read_case_event_data()

            if visible_case_event.text == read_case_event:
                self.logger.info("case event is sucessfully edited")
                self.status.append(True)
            else:
                self.logger.info("case event is not edited")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_08.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_08.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_08.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_08.png")
            self.logger.error(f"TC_events_08 got exception as: {ex} ")



    def Verify_user_is_able_to_add_face_on_Enrollment_view_panel_when_event_icon_is_click(self):
        try:
            self.logger.info("******TC_09********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            faces_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                    .faces_button_in_enrollmentview(), self.d)
            faces_button.click()
            time.sleep(web_driver.one_second)
            upload_photo = self.explicit_wait(7, "XPATH", read_enrollment_components()
                                              .image_box_xpath(), self.d)
            upload_photo.click()
            self.logger.info(f"clicked on upload image icon")
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\vip\\00096.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")
            time.sleep(web_driver.two_second)

            skip_cropping_button = self.d.find_element(By.XPATH, read_enrollment_components().skip_cropping_button())
            skip_cropping_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicking on skip cropping button")

            select_photo_button = self.d.find_element(By.XPATH, read_enrollment_components().select_photo_button())
            select_photo_button.click()
            time.sleep(4)
            self.logger.info("clicking on select photo button")

            success_msg = self.d.find_element(By.XPATH, read_enrollment_components().success_photo_added_message())
            self.logger.info(f"success message is {success_msg.text}")

            if success_msg.is_displayed():
                self.logger.info("sucess photo has been added message is displayed")
                self.status.append(True)

            else:
                self.logger.info("success message is not displayed")
                self.status.append(False)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_09.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_09.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_09.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_09.png")
            self.logger.error(f"TC_events_09 got exception as: {ex} ")

    def Verify_user_is_able_to_see_probable_match_events_associated_to_same_person_on_Enrollment_View_panel_when_probable_match_event_icon_is_click(self):

        try:
            self.logger.info("*********TC_10***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            events_button_in_enrollment_view = self.d.find_element(By.XPATH, events_Read_Ini().events_button_enrollment_view())
            events_button_in_enrollment_view.click()
            time.sleep(web_driver.one_second)
            # events_panel = self.d.find_element(By.XPATH, events_Read_Ini().events_panel_heading_after_clicking_events_button_in_enrollmentview())
            list_of_probable_match_events = self.d.find_elements(By.XPATH,events_Read_Ini().list_of_events_when_clicking_on_events_button())
            for li in list_of_probable_match_events:
                if li.is_displayed():
                    self.logger.info("list of events are visible")
                    self.status.append(True)
                else:
                    self.logger.info("list of events are not visible")
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_10.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_10.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_10.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_10.png")
            self.logger.error(f"TC_events_10 got exception as: {ex} ")

    def Verify_user_able_to_unlink_same_enrollment_group_and_remove_the_person_from_selected_group(self):

        try:
            self.logger.info("********TC_11******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)

            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)

            enrollment_group_button = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_groups_button_in_enrollmentview())
            enrollment_group_button.click()
            time.sleep(web_driver.one_second)

            before_unlinking_eg_count = self.d.find_element(By.XPATH,events_Read_Ini().before_linking_eg_count())
            print(before_unlinking_eg_count.text)
            before_unlinked_eg_count = before_unlinking_eg_count.text
            self.logger.info(f"before unlinking enrolllment group count is : {before_unlinked_eg_count}")

            filter_dropdown = self.d.find_element(By.XPATH,read_enrollment_components().filter_dropdown_on_enrollment_group())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)

            eg_list = []
            Enrollments_groups_list = self.d.find_elements(By.XPATH, read_enrollment_components().list_of_egs())
            for group in Enrollments_groups_list:
                eg_list.append(group.text)
            self.logger.info(f"list of eg are :{eg_list}")

            read_eg_name = read_enrollment_components().default_enrollment_group_details()
            eg_list_read = read_eg_name.split(',')
            self.logger.info(f" eg name is :{eg_list_read}")

            checkbox_xpath_1 = read_enrollment_components().checkbox_xpath_1()
            checkbox_xpath_2 = read_enrollment_components().checkbox_xpath_2()
            check_box_xpath = f"{checkbox_xpath_1}{eg_list_read[0]}{checkbox_xpath_2}"
            self.logger.info(f"custom xpath : {check_box_xpath}")
            if eg_list_read[0] in eg_list:
                checkbox = self.d.find_element(By.XPATH, check_box_xpath)
                checkbox.click()
            else:
                self.logger.info("check box is not clicked")

            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH,events_Read_Ini().action_dropdown_on_eg())
            action_dropdown.click()
            time.sleep(web_driver.one_second)

            remove_group_to_enrollment_option = self.d.find_element(By.XPATH,read_enrollment_components().remove_enrollment_group_to_enrollment())
            remove_group_to_enrollment_option.click()
            self.logger.info("add group to enrollment option is clicked inside action dropdown")
            time.sleep(web_driver.one_second)

            after_unlinking_eg_count = self.d.find_element(By.XPATH,
                                                           events_Read_Ini().before_linking_eg_count())
            self.logger.info(f"after linking enrollment group count is :{after_unlinking_eg_count.text}")
            after_unlinking_eg_count1 = after_unlinking_eg_count.text

            if before_unlinking_eg_count != after_unlinking_eg_count1:
                self.logger.info("Enrollment group is linked")
                self.status.append(True)
            else:
                self.logger.info("Enrollment group is not linked")

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_11.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_11.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_11.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_11.png")
            self.logger.error(f"TC_events_11 got exception as: {ex} ")

    def Verify_user_able_to_link_a_enrollment_group_and_add_the_person_to_the_group(self):
        try:
            self.logger.info("*******TC_12****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            # events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            self.logger.info("events menu clicked.")
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            self.logger.info("events btn clicked.")
            time.sleep(web_driver.two_second)
            # enrollment_group_button = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_groups_button_in_enrollmentview())
            enrollment_group_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().enrollment_groups_button_in_enrollmentview(), self.d)

            enrollment_group_button.click()

            self.logger.info("enrollment groups btn clicked.")
            time.sleep(web_driver.two_second)
            before_linking_eg_count = self.d.find_element(By.XPATH,
                                                          events_Read_Ini().before_linking_eg_count())
            print(before_linking_eg_count.text)
            linked_eg_count = before_linking_eg_count.text
            self.logger.info(f"before linking enrolllment group count is : {linked_eg_count}")

            filter_dropdown = self.d.find_element(By.XPATH,read_enrollment_components().filter_dropdown_on_enrollment_group())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)

            unlinked_eg_option = self.d.find_element(By.XPATH, read_enrollment_components().unlinked_eg_option_xpath())
            unlinked_eg_option.click()
            time.sleep(web_driver.one_second)
            eg_list = []
            Enrollments_groups_list = self.d.find_elements(By.XPATH, read_enrollment_components().list_of_egs())
            for group in Enrollments_groups_list:
                eg_list.append(group.text)
            self.logger.info(f"list of eg are :{eg_list}")

            read_eg_name = read_enrollment_components().default_enrollment_group_details()
            read_eg_name_list = read_eg_name.split(',')
            self.logger.info(f" eg name is :{read_eg_name_list}")

            checkbox_xpath_1 = read_enrollment_components().checkbox_xpath_1()
            checkbox_xpath_2 = read_enrollment_components().checkbox_xpath_2()
            check_box_xpath = f"{checkbox_xpath_1}{read_eg_name_list[0]}{checkbox_xpath_2}"
            self.logger.info(f"custom xpath : {check_box_xpath}")
            if read_eg_name_list[0] in eg_list:
                checkbox = self.d.find_element(By.XPATH, check_box_xpath)
                checkbox.click()
            else:
                self.logger.info("check box is not clicked")

            time.sleep(web_driver.two_second)
            Action_dropdown = self.d.find_element(By.XPATH,events_Read_Ini().action_dropdown_on_eg())
            Action_dropdown.click()
            time.sleep(web_driver.one_second)

            add_group_to_enrollment_option = self.d.find_element(By.XPATH,
                                                                 read_enrollment_components().add_group_to_enrollment_option())
            add_group_to_enrollment_option.click()
            self.logger.info("add group to enrollment option is clicked inside action dropdown")
            time.sleep(web_driver.one_second)

            after_linking_eg_count = self.d.find_element(By.XPATH,
                                                         events_Read_Ini().before_linking_eg_count())
            self.logger.info(f"after linking enrollment group count is :{after_linking_eg_count.text}")
            after_linking_eg_count1 = after_linking_eg_count.text

            if after_linking_eg_count1 != int(linked_eg_count) + 1:

                self.logger.info("Enrollment group is linked")
                self.status.append(True)
            else:
                self.logger.info("Enrollment group is not linked")
                self.status.append(False)

            time.sleep(web_driver.one_second)
            # self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            ele = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_facefirst_logout_button(), self.d)
            ele.click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_12.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_12.png")
                self.logger.info("returning False")
                return False
            else:
                self.logger.info("returning True")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_12.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_12.png")
            self.logger.error(f"TC_events_12 got exception as: {ex} ")

    def Verify_user_is_able_to_add_note_on_Enrollment_view_panel_when_Probable_Match_Event_icon_is_click(self):
        try:
            self.logger.info("*******test_events_TC_122****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)

            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.three_second)

            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            time.sleep(web_driver.two_second)

            notes_button = web_driver.explicit_wait(self, 10, "XPATH",
                                                    events_Read_Ini().notes_button_in_enrollmentview(), self.d)
            notes_button.click()
            time.sleep(web_driver.one_second)

            action_button = self.d.find_element(By.XPATH,
                                                read_enrollment_components().action_button_in_enrollment_notes())
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

            skip_cropping_button = self.d.find_element(By.XPATH,
                                                       read_enrollment_components().skip_cropping_button_xpath())
            skip_cropping_button.click()
            self.logger.info("clicking on skip cropping button")
            time.sleep(web_driver.two_second)

            add_photo_button = self.d.find_element(By.XPATH, read_enrollment_components().add_photo_button_xpath())
            add_photo_button.click()
            self.logger.info("clicking on add photo button")
            time.sleep(8)

            location_input = self.d.find_element(By.XPATH,
                                                 events_Read_Ini().notes_location_store())
            location_input.click()
            location_input.send_keys(read_enrollment_components().get_location_data())
            time.sleep(web_driver.one_second)

            case_subject = self.d.find_element(By.XPATH, events_Read_Ini().notes_case_subject())
            case_subject.click()
            case_subject.send_keys(read_enrollment_components().get_case_subject_data())
            time.sleep(web_driver.two_second)

            # date_of_incident = self.d.find_element(By.XPATH,
            #                                        read_enrollment_components().get_date_and_incident_by_xpath())
            # self.dateTimeAMPM(date_of_incident)
            time.sleep(web_driver.two_second)

            save_button = self.d.find_element(By.XPATH, events_Read_Ini().notes_save_button())
            save_button.click()

            time.sleep(web_driver.one_second)

            notes_list = self.d.find_element(By.XPATH, read_enrollment_components().after_creating_notes_list())
            if notes_list.is_displayed():
                self.logger.info("notes created successfully")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_events_TC_122.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_122.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Verify_user_is_able_to_add_note_on_Enrollment_view_panel_when_Probable_Match_Event_icon_is_click ex: {ex.args}")


    def Verify_user_is_able_to_add_note_on_Enrollment_view_panel_when_Probable_Match_Event_icon_is_click(self):
        try:
            self.logger.info("*******TC_13****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)

            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.three_second)


            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            time.sleep(web_driver.two_second)


            notes_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().notes_button_in_enrollmentview(), self.d)
            notes_button.click()
            time.sleep(web_driver.one_second)

            action_button = self.d.find_element(By.XPATH,
                                                read_enrollment_components().action_button_in_enrollment_notes())
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

            skip_cropping_button = self.d.find_element(By.XPATH,
                                                       read_enrollment_components().skip_cropping_button_xpath())
            skip_cropping_button.click()
            self.logger.info("clicking on skip cropping button")
            time.sleep(web_driver.two_second)

            add_photo_button = self.d.find_element(By.XPATH, read_enrollment_components().add_photo_button_xpath())
            add_photo_button.click()
            self.logger.info("clicking on add photo button")
            time.sleep(8)

            location_input = self.d.find_element(By.XPATH,
                                                 events_Read_Ini().notes_location_store())
            location_input.click()
            location_input.send_keys(read_enrollment_components().get_location_data())
            time.sleep(web_driver.one_second)

            case_subject = self.d.find_element(By.XPATH, events_Read_Ini().notes_case_subject())
            case_subject.click()
            case_subject.send_keys(read_enrollment_components().get_case_subject_data())
            time.sleep(web_driver.two_second)

            # date_of_incident = self.d.find_element(By.XPATH,
            #                                        read_enrollment_components().get_date_and_incident_by_xpath())
            # self.dateTimeAMPM(date_of_incident)
            time.sleep(web_driver.two_second)

            save_button = self.d.find_element(By.XPATH, events_Read_Ini().notes_save_button())
            save_button.click()

            time.sleep(web_driver.one_second)

            notes_list = self.d.find_element(By.XPATH, read_enrollment_components().after_creating_notes_list())
            if notes_list.is_displayed():
                self.logger.info("notes created successfully")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_13.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_13.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_13.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_13.png")
            self.logger.error(f"TC_events_13 got exception as: {ex} ")

    def on_Event_page_click_on_tags_symbol_and_verify_Events_Tags_panel_is_visible(self):
        try:
            self.logger.info("******TC_14***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)

            tags_symbol = self.d.find_element(By.XPATH, events_Read_Ini().tags_button_in_eventspage())
            tags_symbol.click()
            time.sleep(web_driver.two_second)


            filter_dropdown = self.d.find_element(By.XPATH,events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)

            unlinked_tags_option = self.d.find_element(By.XPATH,events_Read_Ini().unlinked_tags_by_xpath())
            unlinked_tags_option.click()
            time.sleep(web_driver.one_second)




            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_14.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_14.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_14.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_14.png")
            self.logger.error(f"TC_events_14 got exception as: {ex} ")

    def on_Eventpage_click_on_extent_menu_button_and_verify_video_location_symbol_is_visible(self):
        try:
            self.logger.info("**********TC_125**** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().extent_menu())
            extent_menu.click()
            time.sleep(web_driver.two_second)
            location_button_in_extentmenu = self.d.find_element(By.XPATH, events_Read_Ini().location_button_in_events_page())
            video_button = self.d.find_element(By.XPATH, events_Read_Ini().video_button_in_events_page())
            if location_button_in_extentmenu.is_displayed():
                self.logger.info("location button is visible")
                self.status.append(True)
            else:
                self.logger.info("location button is not visible")
                self.status.append(False)
            if video_button.is_displayed():
                self.logger.info("video button is visible")
                self.status.append(True)
            else:
                self.logger.info("video button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_125.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_125.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_125.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_125.png")
            self.logger.error(f"TC_events_125 got exception as: {ex} ")

    def on_Event_page_click_on_extent_menu_followed_by_video_symbol_and_verify_Event_video_panel_is_visible(self):
        try:
            self.logger.info("********TC_126******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            # events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            self.logger.info("events panel opened.")
            time.sleep(web_driver.three_second)
            # extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().extent_menu())
            extent_menu = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().extent_menu(), self.d)
            extent_menu.click()
            self.logger.info("extent menu clicked.")
            time.sleep(web_driver.two_second)
            # video_button = self.d.find_element(By.XPATH, events_Read_Ini().video_button_in_events_page())
            video_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().video_button_in_events_page(), self.d)
            video_button.click()
            self.logger.info("video btn is clicked.")
            time.sleep(web_driver.one_second)
            # Event_video_panel = self.d.find_element(By.XPATH, events_Read_Ini().video_details_panel())
            Event_video_panel = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().video_details_panel(), self.d)
            self.logger.info(f"events video panel is displayed: {Event_video_panel.is_displayed()}")
            if Event_video_panel.is_displayed():
                self.logger.info("video details panel is visible")
                self.logger.info("appending True")
                self.status.append(True)
            else:
                self.logger.info("video details panel is not visible")
                self.logger.info("appending False")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_126.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_126.png")
                self.logger.info("returning False")
                return False
            else:
                self.logger.info("returning True")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_126.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_126.png")
            self.logger.error(f"TC_events_126 got exception as: {ex} ")

    def on_Event_video_panel_verify_video_is_visible(self):
        try:
            self.logger.info("*******TC_127****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            self.logger.info("events panel is opened.")
            time.sleep(web_driver.three_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().extent_menu())
            extent_menu.click()
            self.logger.info("extent menu clicked.")
            time.sleep(web_driver.two_second)
            video_button = self.d.find_element(By.XPATH, events_Read_Ini().video_button_in_events_page())
            video_button.click()
            self.logger.info("video btn clicked.")
            time.sleep(web_driver.one_second)
            video = self.d.find_element(By.XPATH, events_Read_Ini().video_in_event_video_panel())
            self.logger.info(f"video is visible: {video.is_displayed()}")
            if video.is_displayed():
                self.logger.info("video is visible")
                self.status.append(True)
            else:
                self.logger.info("video is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_127.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_127.png")
                self.logger.info("returning False")
                return False
            else:
                self.logger.info("returning True.")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_127.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_127.png")
            self.logger.error(f"TC_events_127 got exception as: {ex} ")

    def on_Event_page_click_on_extentmenu_followed_by_location_symbol_and_verify_Events_Location_is_panel_is_visible(self):
        try:
            self.logger.info("********TC_128******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().extent_menu())
            extent_menu.click()
            time.sleep(web_driver.two_second)
            location_button = self.d.find_element(By.XPATH, events_Read_Ini().location_button_in_events_page())
            location_button.click()
            time.sleep(web_driver.one_second)
            event_location = self.d.find_element(By.XPATH, events_Read_Ini().events_location_panel())
            if event_location.is_displayed():
                self.logger.info("events location panel is visible")
                self.status.append(True)
            else:
                self.logger.info("events location panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_128.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_128.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_128.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_128.png")
            self.logger.error(f"TC_events_128 got exception as: {ex} ")

    def Verify_25_events_are_generated_for_25_enrolled_subjects(self):
        try:
            self.logger.info("*************************** Events testcases TC_001 started *******************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)

            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.three_second)

            load_more_button = self.d.find_element(By.XPATH,events_Read_Ini().loadmore_button())
            self.d.execute_script("arguments[0].scrollIntoView();", load_more_button)
            load_more_button.click()

            time.sleep(web_driver.one_second)

            displaying_total_number = self.d.find_element(By.XPATH,events_Read_Ini().total_number_of_events_happened_out_of_total_number_of_events())
            self.logger.info(f"Total number of events are : {displaying_total_number.text}")
            number_of_events = displaying_total_number.text
            time.sleep(web_driver.one_second)

            Total_number = events_Read_Ini().read_total_number_of_events()
            self.logger.info(f"Total number of events are {Total_number}")

            if Total_number in number_of_events:
                self.logger.info("number of total events are 25")
                self.status.append(True)

            else:
                self.status.append(False)

            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_15.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_15.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_128.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_128.png")
            self.logger.error(f"TC_events_128 got exception as: {ex} ")

    def Verify_5_events_for_each_group_soe_abe_pte_fraude_and_vipe_using_enrollment_group_selection_in_search_dropdown(self):
        try:
            self.logger.info("************************************ test_events_TC_002 *******************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            x = events_Read_Ini().get_enrollment_group()
            enrollment_group_list = x.split(',')
            self.logger.info(f"enrollment group list is :{enrollment_group_list}")
            for i in range(len(enrollment_group_list)):
                self.click_on_event_menu()
                self.click_on_search_button()
                self.click_on_enrollment_group()
                eg_name = enrollment_group_list[i]
                filter_text_box_in_eg = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_group_filter())
                filter_text_box_in_eg.clear()
                filter_text_box_in_eg.send_keys(eg_name)
                self.select_enrollment_group(eg_name)
                self.click_on_save_button()
                self.click_on_event_filter_search_button()
                # self.enrollment_group_search_result_validation()
                Total_events_count_of_each_group = self.explicit_wait(5, "XPATH", events_Read_Ini().Events_count_each_eg(), self.d)
                self.logger.info(f"Total number of events on each group is {Total_events_count_of_each_group.text}")
                time.sleep(web_driver.one_second)
                expected_events_counts = events_Read_Ini().five_events_from_each_group()
                if expected_events_counts in Total_events_count_of_each_group.text:
                    self.logger.info("Displaying 5 events from each group")
                    self.status.append(True)

                else:
                    self.status.append(False)
                self.click_on_search_button()
                self.click_on_enrollment_group()
                eg_name = enrollment_group_list[i]
                self.select_enrollment_group(eg_name)
                self.close_all_panel_one_by_one()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_events_TC_002.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_002.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_002.png")
            self.logger.info(f"event_search_with_enrollmentGroup_filter_combination failed:  {ex.args}")
            return False

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

    def Verify_25_events_using_Org_hierarchy_selection_in_search_dropdown(self):
        try:
            self.logger.info("************************* test_events_TC_003 ******************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            x = events_Read_Ini().get_enrollment_group()
            enrollment_group_list = x.split(',')
            self.logger.info(f"enrollment group list is :{enrollment_group_list}")
            # for i in range(len(enrollment_group_list)):
            self.click_on_event_menu()
            self.click_on_search_button()
            self.click_on_org_hierarchy_selection_btn()
            self.select_region_from_org_hierarchy()
            self.click_on_event_filter_search_button()
            # self.enrollment_group_search_result_validation()
            Total_events_count_of_each_group = self.explicit_wait(5, "XPATH", events_Read_Ini().Events_count_each_eg(), self.d)
            self.logger.info(f"Total number of events on each group is {Total_events_count_of_each_group.text}")
            time.sleep(web_driver.one_second)
            expected_events_counts = events_Read_Ini().read_total_number_of_events()
            if expected_events_counts in Total_events_count_of_each_group.text:
                self.logger.info("Displaying 25 events")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_events_TC_003.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_003.png")
                self.close_all_panel_one_by_one()
                return False
            else:
                self.close_all_panel_one_by_one()
                return True
        except Exception as ex:
            self.logger.info(f"Verify_25_events_using_Org_hierarchy_selection_in_search_dropdown ex: {ex.args}")

    def Verify_5_events_for_each_group_soe_abe_pte_fraude_and_vipe_using_enrollment_group_and_org_hierarchy_selection_in_search_dropdown(self):
        try:
            self.logger.info("************************ test_SM_TC036 **********************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            x = events_Read_Ini().get_enrollment_group()
            enrollment_group_list = x.split(',')
            self.logger.info(f"enrollment group list is :{enrollment_group_list}")
            for i in range(len(enrollment_group_list)):
                self.click_on_event_menu()
                self.click_on_search_button()
                self.click_on_enrollment_group()
                eg_name = enrollment_group_list[i]
                # filter_text_box_in_eg = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_group_filter())
                # filter_text_box_in_eg.clear()
                # filter_text_box_in_eg.send_keys(eg_name)
                self.select_enrollment_group(eg_name)
                self.click_on_save_button()
                self.click_on_event_filter_search_button()
                # self.enrollment_group_search_result_validation()
                Total_events_count_of_each_group = self.explicit_wait(5, "XPATH",
                                                                      events_Read_Ini().Events_count_each_eg(), self.d)
                self.logger.info(f"Total number of events on each group is {Total_events_count_of_each_group.text}")
                time.sleep(web_driver.one_second)
                expected_events_counts = events_Read_Ini().five_events_from_each_group()
                if expected_events_counts in Total_events_count_of_each_group.text:
                    self.logger.info("Displaying 5 events from each group")
                    self.status.append(True)

                else:
                    self.status.append(False)
                self.click_on_search_button()
                self.click_on_enrollment_group()
                eg_name = enrollment_group_list[i]
                self.select_enrollment_group(eg_name)
                self.close_all_panel_one_by_one()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_events_TC_004.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_004.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Verify_5_events_for_each_group_soe_abe_pte_fraude_and_vipe_using_enrollment_group_and_org_hierarchy_selection_in_search_dropdown ex: {ex.args}")

    def Add_the_tags_with_respective_enrollment_groups_and_org_hierarchy_selection_example_soe_deterred_and_assualt_abe_deterred_and_threat_pte_deterred_and_push_cart_fraude_and_vipe_deterred_and_fraud(self):
        try:
            self.logger.info("************************ test_events_TC_005 **********************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            x = events_Read_Ini().get_enrollment_group()
            enrollment_group_list = x.split(',')
            self.logger.info(f"enrollment group list is: {enrollment_group_list}")
            for i in range(len(enrollment_group_list)):
                self.click_on_event_menu()
                self.click_on_search_button()
                self.click_on_enrollment_group()
                eg_name = enrollment_group_list[i]
                # filter_text_box_in_eg = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_group_filter())
                # filter_text_box_in_eg.clear()
                # filter_text_box_in_eg.send_keys(eg_name)
                self.select_enrollment_group(eg_name)
                self.click_on_save_button()
                self.click_on_event_filter_search_button()
                # self.enrollment_group_search_result_validation()
                Total_events_count_of_each_group = self.explicit_wait(5, "XPATH",
                                                                      events_Read_Ini().Events_count_each_eg(), self.d)
                self.logger.info(f"Total number of events on each group is {Total_events_count_of_each_group.text}")
                time.sleep(web_driver.one_second)
                expected_events_counts = events_Read_Ini().five_events_from_each_group()
                if expected_events_counts in Total_events_count_of_each_group.text:
                    self.logger.info("Displaying 5 events from each group")
                    self.status.append(True)
                    self.click_on_select_all_checkbox()
                    self.click_on_action_dropdown()
                    self.click_on_edit_tags_option_inside_action_dropdown()
                    self.status.append(self.verify_probable_match_event_tags_panel_displayed())
                    self.click_on_filter_dropdown_on_event_tags_panel()
                    self.click_on_unlinked_tags_option_inside_filter_dropdown()
                    # self.verify_all_Tags_available()
                    self.select_tags_to_add_to_events(eg_name)
                    self.click_action_dropdown_on_event_tags_panel()
                    self.click_on_add_tags_to_selected_events_option_1()

                # else:
                #     self.status.append(False)
                self.click_on_search_button()
                self.click_on_enrollment_group()
                eg_name = enrollment_group_list[i]
                self.select_enrollment_group(eg_name)
                self.close_all_panel_one_by_one()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_events_TC_005.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_005.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Add_the_tags_with_respective_enrollment_groups_and_org_hierarchy_selection_example_soe_deterred_and_assualt_abe_deterred_and_threat_pte_deterred_and_push_cart_fraude_and_vipe_deterred_and_fraud  ex: {ex.args}")

    def Verify_5_events_are_visible_by_enrollment_group_org_hierarchy_and_Tag_selection(self):
        try:
            self.logger.info("************************ test_events_TC_006 **********************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            x = events_Read_Ini().get_enrollment_group()
            enrollment_group_list = x.split(',')
            for i in range(len(enrollment_group_list)):
                self.click_on_event_menu()
                self.click_on_search_button()
                self.click_on_enrollment_group()
                eg_name = enrollment_group_list[i]
                # filter_text_box_in_eg = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_group_filter())
                # filter_text_box_in_eg.clear()
                # filter_text_box_in_eg.send_keys(eg_name)
                self.select_enrollment_group(eg_name)
                self.click_on_save_button()
                self.click_on_org_hierarchy_selection_btn()
                self.select_region_from_org_hierarchy()
                self.click_on_tag_selection_btn()
                self.select_tag_from_tag_list(eg_name)

                self.click_on_event_filter_search_button()
                # self.enrollment_group_search_result_validation()
                Total_events_count_of_each_group = self.explicit_wait(5, "XPATH", events_Read_Ini().Events_count_each_eg(), self.d)
                self.logger.info(f"Total number of events on each group is {Total_events_count_of_each_group.text}")
                time.sleep(web_driver.one_second)
                # expected_events_counts = events_Read_Ini().five_events_from_each_group()
                self.verify_events_displayed_as_expected(eg_name)
                # if expected_events_counts in Total_events_count_of_each_group.text:
                #     self.logger.info("Displaying 5 events from each group")
                #     self.status.append(True)
                # else:
                #     self.status.append(False)
                self.click_on_search_button()
                self.click_on_enrollment_group()
                eg_name = enrollment_group_list[i]
                self.select_enrollment_group(eg_name)
                self.close_all_panel_one_by_one()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_events_TC_006.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_006.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Verify_5_events_are_visible_by_enrollment_group_org_hierarchy_and_Tag_selection ex: {ex.args}")

    def Verify_user_should_be_able_to_add_the_tags_and_see_that_same_tags_are_visible_when_user_clicks_on_display_tags_option_in_view_dropdown(self):
        try:
            self.logger.info("************************ test_events_TC_007 **********************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            tag_name = "Test_Tag"
            self.create_new_tag(tag_name)
            self.click_on_event_menu()
            self.click_on_tags_icon_on_first_event_enlisted()
            self.click_on_filter_dropdown_on_event_tags_panel()
            self.click_on_unlinked_tags_option_inside_filter_dropdown()
            self.select_tag_to_add_to_event_for_verification(tag_name)
            self.click_action_dropdown_on_event_tags_panel()
            self.click_on_add_tags_to_selected_events_option()
            self.click_on_filter_dropdown_on_event_tags_panel()
            self.click_on_linked_tags_option_inside_filter_dropdown()
            self.verify_tag_added_to_event(tag_name)
            self.close_all_panel_one_by_one()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_events_TC_007.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_007.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Verify_user_should_be_able_to_add_the_tags_and_see_that_same_tags_are_visible_when_user_clicks_on_display_tags_option_in_view_dropdown ex: {ex.args}")

    def Verify_user_able_to_delete_probable_match_events(self):
        try:
            self.logger.info("************************ test_events_TC_008 **********************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_event_menu()
            self.select_first_event_checkbox()
            self.click_on_action_dropdown()
            self.select_permanently_delete_selected_events_option()
            self.click_on_delete_selected_btn_on_warning_popup()
            self.verify_event_delete_success_message_displayed()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_events_TC_008.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_008.png")
                self.close_all_panel_one_by_one()
                return False
            else:
                self.close_all_panel_one_by_one()
                return True
        except Exception as ex:
            self.logger.info(f"Verify_user_able_to_delete_probable_match_events ")

    def Probable_Match_Event_search_with_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tag_filter_combination_result_should_be_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tagged_event(self):
        try:
            self.logger.info("************************ test_events_TC_009 **********************************")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_event_menu()
            self.click_on_search_button()
            self.click_on_enrollment_group()
            eg_name = "ABE"
            self.select_enrollment_group(eg_name)
            self.click_on_save_button()
            self.click_on_org_hierarchy_selection_btn()
            self.select_region_from_org_hierarchy()
            self.click_on_tag_selection_btn()
            self.select_tags_to_add_to_events(eg_name)
            self.click_on_save_tag_button()
            self.click_on_event_filter_search_button()
            self.verify_events_displayed_as_expected_after_filter(eg_name)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_events_TC_009.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_events_TC_009.png")
                self.close_all_panel_one_by_one()
                return False
            else:
                self.close_all_panel_one_by_one()
                return True
        except Exception as ex:
            self.logger.info(f"Probable_Match_Event_search_with_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tag_filter_combination_result_should_be_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tagged_event ex: {ex.args}")

    def on_Event_view_panel_click_on_Action_dropdown_followed_by_Identify_within_enrollments_option_in_dropdown_and_verify_Identify_enroll_and_identify_results_panel_are_visible(self):
        try:
            self.logger.info("******TC_099***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()

            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown_in_event_view_panel = self.d.find_element(By.XPATH,
                                                                      events_Read_Ini().action_dropdown_in_event_view())
            action_dropdown_in_event_view_panel.click()
            time.sleep(web_driver.one_second)
            identify_within_enrollments = self.d.find_element(By.XPATH, events_Read_Ini().identify_within_enrollments())
            identify_within_enrollments.click()
            time.sleep(web_driver.two_second)
            identify_and_enroll = self.d.find_element(By.XPATH, events_Read_Ini().identify_and_enroll_panel())
            time.sleep(web_driver.two_second)
            identify_results = self.d.find_element(By.XPATH, events_Read_Ini().identify_results_panel())
            if identify_and_enroll.is_displayed():
                self.logger.info("identify and enroll panel is visible")
                self.status.append(True)
            else:
                self.logger.info("identify and enroll panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            # self.add_details_panel_cancel()
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_099.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_099.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"on_Event_view_panel_click_on_Action_dropdown_followed_by_Identify_within_enrollments_option_in_dropdown_and_verify_Identify_enroll_and_identify_results_panel_are_visible ex: {ex.args}")

    def Verify_event_should_not_generate_for_opt_out_enrollment(self):
        try:
            pass
        except Exception as ex:
            self.logger.info(f"Verify_event_should_not_generate_for_opt_out_enrollment ex: {ex.args}")

    def Verify_event_should_not_generate_for_pending_review_enrollment(self):
        try:
            pass
        except Exception as ex:
            self.logger.info(f"Verify_event_should_not_generate_for_pending_review_enrollment ex: {ex.args}")

    def Verify_event_should_not_generate_for_disable_enrollment(self):
        try:
            pass
        except Exception as ex:
            self.logger.info(f"Verify_event_should_not_generate_for_disable_enrollment ex: {ex.args}")

    def Verify_event_should_not_generate_for_rejected_enrollment(self):
        try:
            pass
        except Exception as ex:
            self.logger.info(f"Verify_event_should_not_generate_for_rejected_enrollment ex: {ex.args}")

################################################ Event_search_filter_methods ##############################################

    def verify_events_displayed_as_expected_after_filter(self, eg_name):
        try:
            events_count = self.explicit_wait(5, "XPATH", events_Read_Ini().get_total_number_of_events(), self.d)
            self.logger.info(f"events displayed count: {events_count.text}")
            if "5" in events_count.text:
                self.status.append(True)
            else:
                self.status.append(False)

        except Exception as ex:
            self.logger.info(f"verify_events_displayed_as_expected_after_filter ex: {ex.args}")

    def verify_event_delete_success_message_displayed(self):
        try:
            success_msg = self.explicit_wait(5, "XPATH", events_Read_Ini().event_deleted_success_message_by_xpath(), self.d)
            self.logger.info(f"success message is visible: {success_msg.is_displayed()}")
            if success_msg.is_displayed():
                self.logger.info(f"success msg: {success_msg.text}")
                self.status.append(True)
            else:
                self.logger.info("success message not displayed")
                self.status.append(False)

        except Exception as ex:
            self.logger.info(f"verify_event_delete_success_message_displayed ex: {ex.args}")

    def click_on_delete_selected_btn_on_warning_popup(self):
        try:
            delete_Selected_btn_on_warning_popup = self.explicit_wait(5, "XPATH", events_Read_Ini().delete_Selected_btn_on_warning_popup_by_xpath(), self.d)
            self.logger.info(f"delete_Selected_btn_on_warning_popup_by_xpath is visible: {delete_Selected_btn_on_warning_popup.is_displayed()}")
            if delete_Selected_btn_on_warning_popup.is_displayed():
                delete_Selected_btn_on_warning_popup.click()
            else:
                self.logger.info("delete_Selected_btn_on_warning_popup_by_xpath is not displayed")
        except Exception as ex:
            self.logger.info(f"click_on_delete_selected_btn_on_warning_popup ex: {ex.args}")

    def select_permanently_delete_selected_events_option(self):
        try:
            permanently_delete_selected_events_option = self.explicit_wait(5, "XPATH", events_Read_Ini().permanently_delete_selected_events_option_by_xpath(), self.d)
            self.logger.info(f"permanently_delete_selected_events_option visible: {permanently_delete_selected_events_option.is_displayed()}")
            if permanently_delete_selected_events_option.is_displayed():
                permanently_delete_selected_events_option.click()
            else:
                self.logger.info("permanently_delete_selected_events_option not displayed.")
        except Exception as ex:
            self.logger.info(f"select_permanently_delete_selected_events_option ex: {ex.args}")


    def select_first_event_checkbox(self):
        try:
            event_checkbox = self.explicit_wait(5, "XPATH", events_Read_Ini().first_checkbox_in_events(), self.d)
            self.logger.info(f"event checkbox visible: {event_checkbox.is_displayed()}")
            if event_checkbox.is_displayed():
                event_checkbox.click()
            else:
                self.logger.info(f"first event checkbox not displayed.")
        except Exception as ex:
            self.logger.info(f"select_first_event_checkbox  ex: {ex.args}")

    def select_tag_to_add_to_event_for_verification(self, tag_name):
        try:
            time.sleep(web_driver.three_second)
            # self.explicit_wait(5, "XPATH", events_Read_Ini().tag_name_list_by_xpath(), self.d)
            tag_name_list = self.d.find_elements(By.XPATH, events_Read_Ini().tag_name_list_for_add_to_event_by_xpath())
            self.logger.info(f"length of tag names: {len(tag_name_list)}")
            # self.explicit_wait(5, "XPATH", events_Read_Ini().tag_name_checkbox_list(), self.d)
            tag_name_checkbox_list = self.d.find_elements(By.XPATH, events_Read_Ini().checkbox_list_for_add_tag_to_event_by_xpath())
            self.logger.info(f"tagname: {tag_name}")
            time.sleep(web_driver.two_second)
            for i in range(len(tag_name_list)):
                if tag_name.upper() in tag_name_list[i].text:
                    self.logger.info(f"tag name displayed: {tag_name_list[i].text}")
                    tag_name_checkbox_list[i].click()
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"select_tag_to_add_to_event_for_verification ex: {ex.args}")

    def verify_tag_added_to_event(self, tag_name):
        try:
            time.sleep(web_driver.one_second)
            # self.explicit_wait(5, "XPATH", events_Read_Ini().tag_name_list_by_xpath(), self.d)
            tag_name_list = self.d.find_elements(By.XPATH, events_Read_Ini().tag_name_list_for_add_to_event_by_xpath())
            self.logger.info(f"length of tag names: {len(tag_name_list)}")
            # self.explicit_wait(5, "XPATH", events_Read_Ini().tag_name_checkbox_list(), self.d)
            tag_name_checkbox_list = self.d.find_elements(By.XPATH, events_Read_Ini().checkbox_list_for_add_tag_to_event_by_xpath())
            self.logger.info(f"tagname: {tag_name}")
            time.sleep(web_driver.two_second)
            for i in range(len(tag_name_list)):
                if tag_name.upper() in tag_name_list[i].text:
                    self.logger.info(f"tag name displayed: {tag_name_list[i].text}")
                    self.status.append(True)

        except Exception as ex:
            self.logger.info(f"select_tag_to_add_to_event_for_verification ex: {ex.args}")

    def create_new_tag(self, tag_name):
        try:
            self.click_on_tags_submenu()
            action_dropdown = self.explicit_wait(5, "XPATH", events_Read_Ini().action_dropdown_in_events_tag(), self.d)
            self.logger.info(f"action dropdown is visible: {action_dropdown.is_displayed()}")
            if action_dropdown.is_displayed():
                action_dropdown.click()
            else:
                self.logger.info(f"action dropdown is not displayed.")
            self.click_on_create_tag_btn()
            self.verify_tag_details_panel_displayed()
            self.verify_tag_name_text_box_and_enter_tag_name(tag_name)
            time.sleep(web_driver.three_second)
            commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
            commit.is_displayed()
            # result.append(commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath())
            serious_event_checkbox = self.d.find_element(By.XPATH,
                                                         Read_Tags_Components().
                                                         get_serious_event_checkbox_by_xpath())
            serious_event_checkbox.click()
            time.sleep(web_driver.three_second)
            save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
            save.click()
            self.logger.info("save button is clicked")
            time.sleep(web_driver.one_second)
            # save_button = self.d.find_elements(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
            # self.logger.info(f"save btn visible: {save_button[0].is_displayed()}")
            # self.logger.info(f"save btn: {len(save_button)}")
            # time.sleep(web_driver.one_second)
            # if len(save_button) > 0:
            #     save_button[0].click()
            #     #self.verify_tag_created_success_message()
            self.close_all_panel_one_by_one()
        except Exception as ex:
            self.logger.info(f"create_new_tag ex: {ex.args}")

    def verify_tag_created_success_message(self):
        try:
            success_message = self.explicit_wait(5, "XPATH", events_Read_Ini().success_message_after_tag_creation_by_xpath(), self.d)
            self.logger.info(f"success message is displayed: {success_message.is_displayed()}")
            if success_message.is_displayed():
                self.status.append(True)
                self.logger.info(f"success msg: {success_message.text}")
            else:
                self.status.append(False)
                self.logger.info(f"success msg not displayed.")
        except Exception as ex:
            self.logger.info(f"verify_tag_created_success_message ex: {ex.args}")

    def verify_tag_name_text_box_and_enter_tag_name(self, tag_name):
        try:
            time.sleep(web_driver.three_second)
            name_test_box = self.explicit_wait(5, "XPATH", events_Read_Ini().tag_name_text_box_by_xpath(), self.d)
            self.logger.info(f"tag name textbox visible: {name_test_box.is_displayed()}")
            if name_test_box.is_displayed():
                name_test_box.send_keys(tag_name)
            else:
                self.logger.info("name text box is not displayed.")
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"verify_tag_name_text_box_and_enter_tag_name ex:{ex.args}")

    def verify_tag_details_panel_displayed(self):
        try:
            time.sleep(web_driver.two_second)
            tag_details_panel_heading = self.explicit_wait(5, "XPATH", events_Read_Ini().tag_details_panel_heading(), self.d)
            self.logger.info(f"tag details panel heading visible: {tag_details_panel_heading.is_displayed()}")
            if tag_details_panel_heading.is_displayed():
                self.logger.info(f"tag details panel heading: {tag_details_panel_heading.text}")
            else:
                self.logger.info("tag details panel is not displayed.")
        except Exception as ex:
            self.logger.info(f"verify_tag_details_panel_displayed ex: {ex.args}")

    def click_on_create_tag_btn(self):
        try:
            time.sleep(web_driver.three_second)
            create_tag_option = self.explicit_wait(5, "XPATH", events_Read_Ini().create_Tag_option_by_xpath(), self.d)
            self.logger.info(f"create tag option visible: {create_tag_option.is_displayed()}")
            if create_tag_option.is_displayed():
                create_tag_option.click()
                time.sleep(web_driver.one_second)
            else:
                self.logger.info("create tag option is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_create_tag_btn ex: {ex.args}")

    def click_on_tags_icon_on_first_event_enlisted(self):
        try:
            tags_icon_btn = self.explicit_wait(5, "XPATH", events_Read_Ini().tag_icon_list_on_events_panel_by_xpath(), self.d)
            self.logger.info(f"tag icon visible: {tags_icon_btn.is_displayed()}")
            if tags_icon_btn.is_displayed():
                tags_icon_btn.click()
            else:
                self.logger.info(f"tags icon is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_tags_icon_on_first_event_enlisted ex: {ex.args}")

    def verify_events_displayed_as_expected(self, eg_name):
        try:
            self.explicit_wait(5, "XPATH", events_Read_Ini().tags_attached_list_by_xpath(), self.d)
            tags_attached_list = self.d.find_elements(By.XPATH, events_Read_Ini().tags_attached_list_by_xpath())
            self.logger.info(f"tags attached list count: {len(tags_attached_list)}")
            tags_attached_names = []
            eg_names_input = events_Read_Ini().get_enrollment_group()
            eg_names_input_list = eg_names_input.split(',')
            serious_tags_input = events_Read_Ini().get_serious_tags()
            serious_tags_input_list = serious_tags_input.split(',')
            non_serious_tags_input = events_Read_Ini().get_non_serious_tags()
            non_serious_tags_input_list = non_serious_tags_input.split(',')
            for i in range(len(tags_attached_list)):
                tags_attached_names.append(tags_attached_list[i].text)

            if eg_names_input_list[1].upper() == eg_name.upper():
                tag_name = serious_tags_input_list[2].upper()
                if tag_name in tags_attached_names:
                    self.status.append(True)
                else:
                    self.status.append(False)
            elif eg_names_input_list[2].upper() == eg_name.upper():
                tag_name = serious_tags_input_list[1].upper()
                if tag_name in tags_attached_names:
                    self.status.append(True)
                else:
                    self.status.append(False)
            elif eg_names_input_list[0].upper() == eg_name.upper():
                tag_name = serious_tags_input_list[0].upper()
                if tag_name in tags_attached_names:
                    self.status.append(True)
                else:
                    self.status.append(False)
            elif eg_names_input_list[3].upper() == eg_name.upper():
                tag_name = non_serious_tags_input_list[0].upper()
                if tag_name in tags_attached_names:
                    self.status.append(True)
                else:
                    self.status.append(False)
            elif eg_names_input_list[4].upper() == eg_name.upper():
                tag_name = non_serious_tags_input_list[1].upper()
                if tag_name in tags_attached_names:
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"eg_name doesn't match, eg_name: {eg_name}")
                tag_name = None
                self.status.append(False)
        except Exception as ex:
            self.logger.info(f"verify_events_displayed_as_expected ex: {ex.args}")

    def select_tag_from_tag_list(self, eg_name):
        try:
            self.explicit_wait(5, "XPATH", events_Read_Ini().tag_name_list_by_xpath(), self.d)
            tag_name_list = self.d.find_elements(By.XPATH, events_Read_Ini().tag_name_list_by_xpath())
            self.explicit_wait(5, "XPATH", events_Read_Ini().tag_name_checkbox_list(), self.d)
            tag_name_checkbox_list = self.d.find_elements(By.XPATH, events_Read_Ini().tag_name_checkbox_list())
            eg_names_input = events_Read_Ini().get_enrollment_group()
            eg_names_input_list = eg_names_input.split(',')
            serious_tags_input = events_Read_Ini().get_serious_tags()
            serious_tags_input_list = serious_tags_input.split(',')
            non_serious_tags_input = events_Read_Ini().get_non_serious_tags()
            non_serious_tags_input_list = non_serious_tags_input.split(',')
            if eg_names_input_list[1].upper() == eg_name.upper():
                tag_name = serious_tags_input_list[2].upper()
                for i in range(len(tag_name_list)):
                    self.logger.info(f"tag name: {tag_name_list[i].text}")
                    if tag_name_list[i].text == tag_name:
                        tag_name_checkbox_list[i].click()
            elif eg_names_input_list[2].upper() == eg_name.upper():
                tag_name = serious_tags_input_list[1].upper()
                for i in range(len(tag_name_list)):
                    self.logger.info(f"tag name: {tag_name_list[i].text}")
                    if tag_name_list[i].text == tag_name:
                        tag_name_checkbox_list[i].click()
            elif eg_names_input_list[0].upper() == eg_name.upper():
                tag_name = serious_tags_input_list[0].upper()
                for i in range(len(tag_name_list)):
                    self.logger.info(f"tag name: {tag_name_list[i].text}")
                    if tag_name_list[i].text == tag_name:
                        tag_name_checkbox_list[i].click()
            elif eg_names_input_list[3].upper() == eg_name.upper():
                tag_name = non_serious_tags_input_list[0].upper()
                for i in range(len(tag_name_list)):
                    self.logger.info(f"tag name: {tag_name_list[i].text}")
                    if tag_name_list[i].text == tag_name:
                        tag_name_checkbox_list[i].click()
            elif eg_names_input_list[4].upper() == eg_name.upper():
                tag_name = non_serious_tags_input_list[1].upper()
                for i in range(len(tag_name_list)):
                    self.logger.info(f"tag name: {tag_name_list[i].text}")
                    if tag_name_list[i].text == tag_name:
                        tag_name_checkbox_list[i].click()
            else:
                self.logger.info(f"eg_name doesn't match, eg_name: {eg_name}")
                tag_name = None
            save_btn = self.explicit_wait(5, "XPATH", events_Read_Ini().save_btn_on_tag_selection_by_xpath(), self.d)
            save_btn.click()
        except Exception as ex:
            self.logger.info(f"select_tag_from_tag_list ex: {ex.args}")

    def click_on_tag_selection_btn(self):
        try:
            tag_selection_btn = self.explicit_wait(5, "XPATH", events_Read_Ini().tag_selection(), self.d)
            self.logger.info(f"tag selection btn: {tag_selection_btn.is_displayed()}")
            if tag_selection_btn.is_displayed():
                tag_selection_btn.click()
            else:
                self.logger.info("tag selection btn not displayed.")

        except Exception as ex:
            self.logger.info(f"click_on_tag_selection_btn ex: {ex.args}")

    def click_on_add_tags_to_selected_events_option_1(self):
        try:
            time.sleep(web_driver.three_second)
            add_tags_option = self.explicit_wait(5, "XPATH", events_Read_Ini().add_tags_to_event_option_in_event_tags_1(), self.d)
            self.logger.info(f"add tags to events option visible: {add_tags_option.is_displayed()}")
            if add_tags_option.is_displayed():
                add_tags_option.click()
                self.status.append(True)
            else:
                self.status.append(False)
                self.logger.info(f"add tags option is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_add_tags_to_selected_events_option ex: {ex.args}")

    def click_on_add_tags_to_selected_events_option(self):
        try:
            time.sleep(web_driver.three_second)
            add_tags_option = self.explicit_wait(5, "XPATH", events_Read_Ini().add_tags_to_event_option_in_event_tags_1(), self.d)
            self.logger.info(f"add tags to events option visible: {add_tags_option.is_displayed()}")
            if add_tags_option.is_displayed():
                add_tags_option.click()
                self.status.append(True)
            else:
                self.status.append(False)
                self.logger.info(f"add tags option is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_add_tags_to_selected_events_option ex: {ex.args}")

    def click_action_dropdown_on_event_tags_panel(self):
        try:
            action_dropdown = self.explicit_wait(5, "XPATH", events_Read_Ini().action_dropdown_on_event_tags_panel_by_xpath(), self.d)
            self.logger.info(f"action dropdown on event tags: {action_dropdown.is_displayed()}")
            if action_dropdown.is_displayed():
                action_dropdown.click()
            else:
                self.logger.info(f"action dropdown is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_action_dropdown_on_event_tags_panel ex: {ex.args}")

    def select_tags_to_add_to_events(self, eg_name):
        try:
            get_eg_names = events_Read_Ini().get_enrollment_group()
            get_eg_names_list = get_eg_names.split(',')
            serious_tag_name_input_data = events_Read_Ini().get_serious_tags()
            serious_tag_name_input_data_list = serious_tag_name_input_data.split(',')
            non_serious_tag_input_data = events_Read_Ini().get_non_serious_tags()
            non_serious_tag_input_data_list = non_serious_tag_input_data.split(',')
            if get_eg_names_list[1].upper() == eg_name.upper():
                tag_name = serious_tag_name_input_data_list[2].upper()  # ABE linked to THREAT
            elif get_eg_names_list[2].upper() == eg_name.upper():
                tag_name = serious_tag_name_input_data_list[1].upper()  # PTE Linked to PUSH CART
            elif get_eg_names_list[0].upper() == eg_name.upper():
                tag_name = serious_tag_name_input_data_list[0].upper()  # SOE Linked to ASSAULT
            elif get_eg_names_list[3].upper() == eg_name.upper():
                tag_name = non_serious_tag_input_data_list[0].upper()  # FRAUDE Linked to FRAUD
            elif get_eg_names_list[4].upper() == eg_name.upper():
                tag_name = non_serious_tag_input_data_list[1].upper()  # VIPE Linked to VIP
            else:
                self.logger.info(f"eg_name doesn't match, eg_name: {eg_name}")
                tag_name = None
            self.logger.info(f"eg: {eg_name}, tag: {tag_name}")
            if tag_name is not None:
                tag_name_list = self.d.find_elements(By.XPATH, events_Read_Ini().tags_names())
                tag_checkbox_list = self.d.find_elements(By.XPATH, events_Read_Ini().checkbox_number_twentyfour())

                if tag_name == serious_tag_name_input_data_list[2].upper():
                    tag_checkbox_list[0].click()
                    for i in range(len(tag_name_list)):
                        self.logger.info(f"tag names: {tag_name_list[i].text}")
                        if tag_name_list[i].text == tag_name:
                            tag_checkbox_list[i].click()
                elif tag_name == serious_tag_name_input_data_list[1].upper():
                    tag_checkbox_list[0].click()
                    for i in range(len(tag_name_list)):
                        self.logger.info(f"tag names: {tag_name_list[i].text}")
                        if tag_name_list[i].text == tag_name:
                            tag_checkbox_list[i].click()
                elif tag_name == serious_tag_name_input_data_list[0].upper():
                    tag_checkbox_list[0].click()
                    for i in range(len(tag_name_list)):
                        self.logger.info(f"tag names: {tag_name_list[i].text}")
                        if tag_name_list[i].text == tag_name:
                            tag_checkbox_list[i].click()
                elif tag_name == non_serious_tag_input_data_list[0].upper():
                    tag_checkbox_list[0].click()
                    for i in range(len(tag_name_list)):
                        self.logger.info(f"tag names: {tag_name_list[i].text}")
                        if tag_name_list[i].text == tag_name:
                            tag_checkbox_list[i].click()
                elif tag_name == non_serious_tag_input_data_list[1].upper():
                    tag_checkbox_list[0].click()
                    for i in range(len(tag_name_list)):
                        self.logger.info(f"tag names: {tag_name_list[i].text}")
                        if tag_name_list[i].text == tag_name:
                            tag_checkbox_list[i].click()
                else:
                    self.logger.info(f"tag name is not as expected.")
            else:
                self.logger.info(f"enrollment group name given is not as expected")
        except Exception as ex:
            self.logger.info(f"select_tags_to_add_to_events ex: {ex.args}")

    def click_on_tags_submenu(self):
        try:
            tags_menu = self.explicit_wait(5, "XPATH", events_Read_Ini().tags_menu_item_by_xpath(), self.d)
            self.logger.info(f"tags menu visible: {tags_menu.is_displayed()}")
            if tags_menu.is_displayed():
                tags_menu.click()
            else:
                self.logger.info("tags menu is not displayed")
        except Exception as ex:
            self.logger.info(f"click_on_tags_submenu ex: {ex.args}")

    def click_on_cloud_menu_btn(self):
        try:
            cloud_menu = self.explicit_wait(5, "XPATH", events_Read_Ini().get_cloud_menu(), self.d)
            self.logger.info(f"cloud menu visible: {cloud_menu.is_displayed()}")
            if cloud_menu.is_displayed():
                cloud_menu.click()
            else:
                self.logger.info("cloud menu is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_cloud_menu_btn ex: {ex.args}")

    def verify_all_Tags_available(self):
        try:
            tags_enlisted = self.d.find_elements(By.XPATH, events_Read_Ini().tags_list_enlisted_by_xpath())
            self.logger.info(f"tags list enlisted count: {len(tags_enlisted)}")
            if len(tags_enlisted) == 1:
                self.logger.info(f"tags enlisted did not have other tags ")

            else:
                self.logger.info("tags enlisted did have tags. creating tags")

        except Exception as ex:
            self.logger.info(f"verify_all_Tags_available ex: {ex.args}")

    def click_on_unlinked_tags_option_inside_filter_dropdown(self):
        try:
            unlinked_tags_option = self.explicit_wait(5, "XPATH", events_Read_Ini().unlinked_tags_by_xpath(), self.d)
            self.logger.info(f"unlinked tags option ex: {unlinked_tags_option.is_displayed()}")
            if unlinked_tags_option.is_displayed():
                unlinked_tags_option.click()
            else:
                self.logger.info(f"unlinked tags option is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_unlinked_tags_option_inside_filter_dropdown ex: {ex.args}")

    def click_on_linked_tags_option_inside_filter_dropdown(self):
        try:
            linked_tags_option = self.explicit_wait(5, "XPATH", events_Read_Ini().linked_tags_by_xpath(), self.d)
            self.logger.info(f"linked_tags_option: {linked_tags_option.is_displayed()}")
            if linked_tags_option.is_displayed():
                linked_tags_option.click()
            else:
                self.logger.info(f"unlinked tags option is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_unlinked_tags_option_inside_filter_dropdown ex: {ex.args}")

    def click_on_filter_dropdown_on_event_tags_panel(self):
        try:
            filter_dropdown = self.explicit_wait(5, "XPATH", events_Read_Ini().filter_dropdown_in_events_tag(), self.d)
            self.logger.info(f"filter dropdown in event tags visible: {filter_dropdown.is_displayed()}")
            if filter_dropdown.is_displayed():
                filter_dropdown.click()
            else:
                self.logger.info("filter dropdown is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_filter_dropdown_on_event_tags_panel ex: {ex.args}")

    def verify_probable_match_event_tags_panel_displayed(self):
        try:
            probable_match_event_tags_panel_heading = self.explicit_wait(5, "XPATH", events_Read_Ini().events_tags_panel_heading(), self.d)
            self.logger.info(f"verify_probable_match_event_tags_panel_displayed visible: {probable_match_event_tags_panel_heading.is_displayed()}")
            if probable_match_event_tags_panel_heading.is_displayed():
                return True
            else:
                self.logger.info(f"event tags panel not displayed.")
                return False
        except Exception as ex:
            self.logger.info(f"verify_probable_match_event_tags_panel_displayed ex: {ex.args}")

    def click_on_edit_tags_option_inside_action_dropdown(self):
        try:
            edit_tags_option = self.explicit_wait(5, "XPATH", events_Read_Ini().edit_tags_in_actiondropdown(), self.d)
            self.logger.info(f"edit tags option visible: {edit_tags_option.is_displayed()}")
            if edit_tags_option.is_displayed():
                edit_tags_option.click()
            else:
                self.logger.info("edit tags option is not displayed")
        except Exception as ex:
            self.logger.info(f"click_on_edit_tags_option_inside_action_dropdown ex: {ex.args}")

    def click_on_action_dropdown(self):
        try:
            action_dropdown = self.explicit_wait(5, "XPATH", events_Read_Ini().action_dropdown_in_events(), self.d)
            self.logger.info(f"action dropdown is visible: {action_dropdown.is_displayed()}")
            if action_dropdown.is_displayed():
                action_dropdown.click()
            else:
                self.logger.info("action dropdown is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_action_dropdown ex: {ex.args}")

    def click_on_select_all_checkbox(self):
        try:
            select_all_checkbox = self.explicit_wait(5, "XPATH", events_Read_Ini().select_all_checkbox(), self.d)
            self.logger.info(f"select all checkbox visible: {select_all_checkbox.is_displayed()}")
            if select_all_checkbox.is_displayed():
                select_all_checkbox.click()
            else:
                self.logger.info("select all checkbox is not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_select_all_checkbox ex: {ex.args}")

    def select_region_from_org_hierarchy(self):
        try:
            # self.explicit_wait(5, "XPATH", events_Read_Ini().regions_xpath(), self.d)
            time.sleep(web_driver.two_second)
            region_list = self.d.find_elements(By.XPATH, events_Read_Ini().regions_xpath())
            region_checkbox_list = self.d.find_elements(By.XPATH, events_Read_Ini().region_checkbox_xpath())

            self.logger.info(f"region length: {len(region_list)}")
            if len(region_list) > 0:
                for i in range(len(region_list)):
                    self.logger.info(f"region name: {region_list[i].text}")
                    if region_list[i].text == events_Read_Ini().edge_name():
                        region_checkbox_list[i].click()
            else:
                self.logger.info(f"region name list not displayed.")
            save_btn = self.explicit_wait(5, "XPATH", events_Read_Ini().save_zone_button_by_xpath(), self.d)
            if save_btn.is_displayed():
                self.logger.info(f"save btn is visible: {save_btn.is_displayed()}")
                save_btn.click()
            else:
                self.logger.info("save btn not displayed.")
        except Exception as ex:
            self.logger.info(f"select_region_from_org_hierarchy ex: {ex.args}")

    def click_on_org_hierarchy_selection_btn(self):
        try:
            org_hierarchy_btn = self.explicit_wait(5, "XPATH", events_Read_Ini().org_hierarchy_selection(), self.d)
            self.logger.info(f"org hierarchy selection btn visible: {org_hierarchy_btn.is_displayed()}")
            if org_hierarchy_btn.is_displayed():
                org_hierarchy_btn.click()
            else:
                self.logger.info(f"org hierarchy selection btn not displayed.")
        except Exception as ex:
            self.logger.info(f"click_on_org_hierarchy_selection_btn ex: {ex.args}")

    def click_on_event_menu(self):
        self.logger.info(f"clicking on events panel")
        time.sleep(web_driver.two_second)
        event_menu = self.d.find_element(By.XPATH,
                                         events_Read_Ini().menu_event_button_by_xpath())
        self.d.execute_script("arguments[0].click();", event_menu)
        time.sleep(web_driver.one_second)

    def click_on_search_button(self):
        time.sleep(web_driver.one_second)
        event_search_button = self.d.find_element(By.XPATH,
                                                  events_Read_Ini().event_search_button_by_xpath())
        event_search_button.click()
        time.sleep(web_driver.one_second)

    def click_on_start_date_checkbox(self):
        start_date_checkbox = self.d.find_element(By.XPATH,
                                                  events_Read_Ini().event_search_start_date_checkbox())
        start_date_checkbox.click()

    def click_on_end_date_checkbox(self):
        end_date_checkbox = self.d.find_element(By.XPATH,
                                                events_Read_Ini().event_search_end_date_checkbox())
        end_date_checkbox.click()

    def click_on_save_button(self):
        click_on_save_button = self.explicit_wait(5, "XPATH", events_Read_Ini().save_button_by_xpath(), self.d)
        self.logger.info(f"save btn visible: {click_on_save_button.is_displayed()}")
        if click_on_save_button.is_displayed():
            click_on_save_button.click()
        else:
            self.logger.info("save btn is not displayed.")

    def click_on_save_zone_button(self):
        click_on_save_zone_button = self.d.find_element(By.XPATH,
                                                        events_Read_Ini().save_zone_button_by_xpath())
        time.sleep(web_driver.one_second)
        self.d.execute_script("arguments[0].click();", click_on_save_zone_button)
        # click_on_save_zone_button.click()

    def click_on_save_tag_button(self):
        click_on_save_tag_button = self.d.find_element(By.XPATH,
                                                       events_Read_Ini().tags_save_button_by_xpath())
        click_on_save_tag_button.click()

    def click_on_event_filter_search_button(self):
        time.sleep(web_driver.one_second)
        self.explicit_wait(10, "XPATH", events_Read_Ini().event_filter_search_button_by_xpath(), self.d)
        click_on_event_filter_search_button = self.d.find_element(By.XPATH,
                                                                  events_Read_Ini().event_filter_search_button_by_xpath())
        click_on_event_filter_search_button.click()
        # wait_icon = self.d.find_element(By.XPATH, events_Read_Ini().wait_icon_xpath())

        time.sleep(web_driver.one_second)
        # while wait_icon.is_displayed():
        # time.sleep(web_driver.two_second)

    def click_on_enrollment_group(self):
        enrollment_group_selection = self.explicit_wait(5, "XPATH", events_Read_Ini().enrollment_group_drop_down(), self.d)
        self.logger.info(f"enrollment group visible: {enrollment_group_selection.is_displayed()}")
        if enrollment_group_selection.is_displayed():
            enrollment_group_selection.click()
        else:
            self.logger.info(f"enrollment group is not displayed.")
        # checkbox_list = self.d.find_elements(By.XPATH,
        #                                      events_Read_Ini().enrollment_group_checkbox_list())
        # group_text_list = self.d.find_elements(By.XPATH,
        #                                        events_Read_Ini().enrollment_group_name_list())
        # for i in group_text_list:
        #     self.logger.info(f"enrollment group list are {i.text}")
        #
        # try:
        #     for i in range(len(group_text_list) - 1):
        #         actual_enrollment_group_text = group_text_list.__getitem__(i).text
        #         self.logger.info(f"actual text: {actual_enrollment_group_text}")
        #         expected_enrollment_group_text = events_Read_Ini().get_enrollment_group()[i].upper()
        #         expected_en_group_list = expected_enrollment_group_text.split(',')
        #         self.logger.info(f"expected text: {expected_enrollment_group_text}")
        #         for x in expected_en_group_list:
        #             if actual_enrollment_group_text == x:
        #                 checkbox_list.__getitem__(i).click()
        #                 break
        # except Exception as ex:
        #     self.logger.info(ex.args)

    def select_enrollment_group(self, eg_name):
        try:
            checkbox_list = self.d.find_elements(By.XPATH, events_Read_Ini().enrollment_group_checkbox_list())
            group_text_list = self.d.find_elements(By.XPATH, events_Read_Ini().enrollment_group_name_list())
            for i in range(len(group_text_list)):
                self.logger.info(f"enrollment group list are {group_text_list[i].text}")
                actual_enrollment_group_text = group_text_list[i].text
                self.logger.info(f"actual text: {actual_enrollment_group_text}")
                self.logger.info(f"expected text: {eg_name.upper()}")
                # for x in expected_en_group_list:
                if eg_name.upper() in group_text_list[i].text:
                    checkbox_list[i].click()
                    break

        except Exception as ex:
            self.logger.info(f"select_enrollment_group ex: {ex.args}")

    def zone_selection(self):
        zone_selection = self.d.find_element(By.XPATH,
                                             events_Read_Ini().zone_selection_drop_down())
        self.d.execute_script("arguments[0].click();", zone_selection)
        # time.sleep(3)
        # root_selection = self.d.find_element(By.XPATH,
        #                                      events_Read_Ini().root_zone_validation())
        # assert root_selection.is_displayed()
        # self.d.execute_script("arguments[0].click();", root_selection)

        checkbox_list = self.d.find_elements(By.XPATH,
                                             events_Read_Ini().zones_checkbox_list())
        zone_text_list = self.d.find_elements(By.XPATH,
                                              events_Read_Ini().zones_text_list())
        try:

            for i in range(len(zone_text_list)):
                actual_zone_text = zone_text_list.__getitem__(i).text
                self.logger.info(f"actual zone: {actual_zone_text}")
                expected_zone_text = events_Read_Ini().get_zone()
                self.loggger.info(f"expected zone: {expected_zone_text}")
                if expected_zone_text.lower() in actual_zone_text.lower():
                    if checkbox_list.__getitem__(i).is_selected():
                        checkbox_list.__getitem__(i).click()
                    else:
                        checkbox_list.__getitem__(i).click()
                        #checkbox_list.__getitem__(i).click()
                    break
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(ex.args)

    def tags_selection(self):
        tags_selection = self.d.find_element(By.XPATH,
                                             events_Read_Ini().tag_selection_drop_down())
        # self.d.execute_script("arguments[0].click();", tags_selection)

        tags_selection.click()
        time.sleep(web_driver.one_second)

        checkbox_list = self.d.find_elements(By.XPATH,
                                             events_Read_Ini().tags_checkbox_list())
        tags_text_list = self.d.find_elements(By.XPATH,
                                              events_Read_Ini().tags_text_list())
        try:

            for i in range(len(tags_text_list) + 1):
                actual_tag_text = tags_text_list.__getitem__(i).text
                expected_tag_text = events_Read_Ini().get_tags().upper()
                if actual_tag_text == expected_tag_text:
                    checkbox_list.__getitem__(i).click()
        except Exception as ex:
            self.logger.info(ex.args)

    # validation methods

    def enrollment_group_search_result_validation(self):
        enrollment_group_search_validation = self.d.find_element(By.XPATH,
                                                                 events_Read_Ini().
                                                                 enrollment_group_search_result_validation())
        actual_text = enrollment_group_search_validation.text
        expected_text = events_Read_Ini().get_enrollment_group()
        time.sleep(web_driver.one_second)
        if actual_text.lower() == expected_text.lower():
            self.logger.info(f"actual text is {actual_text.lower()},{expected_text.lower()}")
            self.status.append(True)
        else:
            self.status.append(False)

    def zones_search_result_validation(self):
        zones_search_result_validation = self.d.find_element(By.XPATH,
                                                             events_Read_Ini().
                                                             zone_search_result_validation())
        actual_text = zones_search_result_validation.text.lower()
        expected_text = events_Read_Ini().get_zone().lower()
        time.sleep(web_driver.one_second)
        return expected_text in actual_text

    def tag_search_result_validation(self):
        tag_search_result_validation = self.d.find_element(By.XPATH,
                                                           events_Read_Ini().
                                                           tags_search_result_validation())
        actual_text = tag_search_result_validation.text
        expected_text = events_Read_Ini().get_tags().upper()
        time.sleep(web_driver.one_second)
        return actual_text == expected_text.upper()

    def verify_date(self, date, month, year, hour, minute, period):
        month_to_mm = {
            "January": "1",
            "February": "2",
            "March": "3",
            "April": "4",
            "May": "5",
            "June": "6",
            "July": "7",
            "August": "8",
            "September": "9",
            "October": "10",
            "November": "11",
            "December": "12"
        }
        mon = month_to_mm.get(month)

        exp_asser = "{mon}/{date}/{year} {hour}:{minu} {pe}"
        exp_asser = exp_asser.format(mon=mon, date=date, year=year, hour=int(hour), minu=minute, pe=period)
        time.sleep(3)

        ac_start_date = self.d.find_element(By.XPATH, events_Read_Ini().date_search_result_validation())
        print("Expected data = " + exp_asser)
        print("Actual data = " + ac_start_date)
        ac_ass_date = ac_start_date.text
        if exp_asser in ac_ass_date:
            return True
        else:
            return False

    # Calender method

    def handle_calender_pop_up(self, strategy, date, month, year, hour, minute, req_period):
        # click on the form calendar popup
        if strategy == "from":
            start_check_bx = self.d.find_element(By.XPATH,
                                                 events_Read_Ini().event_search_start_date_checkbox())
            start_check_bx.click()
            start_date_txt_bx = self.d.find_element(By.XPATH, events_Read_Ini().event_search_start_date_input())
            start_date_txt_bx.click()
        else:
            # click on the to calendar pop up
            end_check_bx = self.d.find_element(By.XPATH,
                                               events_Read_Ini().event_search_end_date_checkbox())
            end_check_bx.click()
            end_date_txt_bx = self.d.find_element(By.XPATH, events_Read_Ini().event_search_end_date_input())
            end_date_txt_bx.click()

        # click on the clock icon
        calender_clock = self.d.find_element(By.XPATH, events_Read_Ini().calender_timer_icon_by_xpath())
        calender_clock.click()

        time.sleep(web_driver.one_second)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, events_Read_Ini().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, events_Read_Ini().calender_tick_icon_by_xpath())
        tick_icon.click()

        if strategy == "from":
            start_date_txt_bx = self.d.find_element(By.XPATH, events_Read_Ini().start_date_by_xpath())
            start_date_txt_bx.click()
        else:
            # click on the to calendar pop up
            start_date_txt_bx = self.d.find_element(By.XPATH, events_Read_Ini().end_date_by_xpath())
            start_date_txt_bx.click()

        req_month = month
        req_year = year
        month_to_num = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        month_year = self.d.find_element(By.XPATH, events_Read_Ini().calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  events_Read_Ini().calender_back_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()

            month_year = self.d.find_element(By.XPATH,
                                             events_Read_Ini().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  events_Read_Ini().calender_forward_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()

            month_year = self.d.find_element(By.XPATH,
                                             events_Read_Ini().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the required date
        try:
            date = self.d.find_element(By.XPATH,
                                       "(//td[@class='day' or @class='day weekend' or @class='day active'])[" + str(
                                           date) + "]")
            date.click()
        except Exception as ex:
            self.logger.info(ex.args)

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, events_Read_Ini().calender_tick_icon_by_xpath())
        tick_icon.click()

    def calender_handle_hour_minute_to(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, events_Read_Ini().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, events_Read_Ini().hour_down_by_xpath())
            hour_down.click()
            current_hour_ele = self.d.find_element(By.XPATH,
                                                   events_Read_Ini().current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH,
                                              events_Read_Ini().current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_down_button = self.d.find_element(By.XPATH, events_Read_Ini()
                                                    .clock_min_down_button_by_xpath())
            clock_down_button.click()
            current_min_ele = self.d.find_element(By.XPATH, events_Read_Ini()
                                                  .current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, events_Read_Ini().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, events_Read_Ini().hour_down_by_xpath())
            hour_down.click()
            current_hour_ele = self.d.find_element(By.XPATH, events_Read_Ini()
                                                   .current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH, events_Read_Ini()
                                              .current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_up_button = self.d.find_element(By.XPATH, events_Read_Ini()
                                                  .clock_min_up_button_by_xpath())
            clock_up_button.click()
            current_min_ele = self.d.find_element(By.XPATH, events_Read_Ini()
                                                  .current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    # close tab and logout method

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    events_Read_Ini().close_all_panel_one_by_one())
            for i in close_panel_list:
                i.click()
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(ex.args)

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.one_second)
            logout_button = self.d.find_element(By.XPATH, events_Read_Ini().logout_btn_by_xpath())
            logout_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_logout_button_failed.png")
            self.logger.info(f"exception:  {ex.args}")
            return False













import time
from pathlib import Path
from selenium.webdriver.common.by import By
from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Event_Filter_Read_INI import read_event_filter_ini
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components


class Event_search_filter_combinations_POM:

    def __init__(self, logger):
        self.d = Base_Class.d
        self.log = logger
        self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"

    def login_before(self):
        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(Base_Class.one_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            time.sleep(Base_Class.one_second)
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            self.d.execute_script("arguments[0].click();", login_btn)
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\events_search_filter_login_failed.png")
            self.log.info(f"login_before:  {ex.args}")
            return False

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton()). \
                is_displayed():
            self.login_before()
            time.sleep(Base_Class.one_second)

    def click_on_event_menu(self):
        time.sleep(Base_Class.one_second)
        event_menu = self.d.find_element(By.XPATH,
                                         read_event_filter_ini().menu_event_button_by_xpath())
        self.d.execute_script("arguments[0].click();", event_menu)
        time.sleep(Base_Class.one_second)

    def click_on_search_button(self):
        time.sleep(Base_Class.one_second)
        event_search_button = self.d.find_element(By.XPATH,
                                                  read_event_filter_ini().event_search_button_by_xpath())
        event_search_button.click()
        time.sleep(Base_Class.one_second)

    def click_on_start_date_checkbox(self):
        start_date_checkbox = self.d.find_element(By.XPATH,
                                                  read_event_filter_ini().event_search_start_date_checkbox())
        start_date_checkbox.click()

    def click_on_end_date_checkbox(self):
        end_date_checkbox = self.d.find_element(By.XPATH,
                                                read_event_filter_ini().event_search_end_date_checkbox())
        end_date_checkbox.click()

    def click_on_save_button(self):
        click_on_save_button = self.d.find_element(By.XPATH,
                                                   read_event_filter_ini().save_button_by_xpath())
        click_on_save_button.click()

    def click_on_save_zone_button(self):
        click_on_save_zone_button = self.d.find_element(By.XPATH,
                                                        read_event_filter_ini().save_zone_button_by_xpath())
        time.sleep(Base_Class.one_second)
        self.d.execute_script("arguments[0].click();", click_on_save_zone_button)
        # click_on_save_zone_button.click()

    def click_on_save_tag_button(self):
        click_on_save_tag_button = self.d.find_element(By.XPATH,
                                                       read_event_filter_ini().tags_save_button_by_xpath())
        click_on_save_tag_button.click()

    def click_on_event_filter_search_button(self):
        time.sleep(Base_Class.one_second)
        click_on_event_filter_search_button = self.d.find_element(By.XPATH,
                                                                  read_event_filter_ini().
                                                                  event_filter_search_button_by_xpath())
        wait_icon = self.d.find_element(By.XPATH, read_event_filter_ini().wait_icon_xpath())
        click_on_event_filter_search_button.click()
        time.sleep(Base_Class.one_second)
        while wait_icon.is_displayed():
            time.sleep(Base_Class.two_second)

    def enrollment_group_selection(self):
        enrollment_group_selection = self.d.find_element(By.XPATH,
                                                         read_event_filter_ini().enrollment_group_drop_down())
        enrollment_group_selection.click()

        checkbox_list = self.d.find_elements(By.XPATH,
                                             read_event_filter_ini().enrollment_group_checkbox_list())
        group_text_list = self.d.find_elements(By.XPATH,
                                               read_event_filter_ini().enrollment_group_name_list())
        try:
            for i in range(len(group_text_list) - 1):
                actual_enrollment_group_text = group_text_list.__getitem__(i).text
                # self.log.info(f"actual text: {actual_enrollment_group_text}")
                expected_enrollment_group_text = read_event_filter_ini().get_enrollment_group().upper()
                # self.log.info(f"expected text: {expected_enrollment_group_text}")
                if actual_enrollment_group_text == expected_enrollment_group_text:
                    checkbox_list.__getitem__(i).click()
                    break
        except Exception as ex:
            self.log.info(ex.args)

    def zone_selection(self):
        zone_selection = self.d.find_element(By.XPATH,
                                             read_event_filter_ini().zone_selection_drop_down())
        self.d.execute_script("arguments[0].click();", zone_selection)
        # time.sleep(3)
        # root_selection = self.d.find_element(By.XPATH,
        #                                      read_event_filter_ini().root_zone_validation())
        # assert root_selection.is_displayed()
        # self.d.execute_script("arguments[0].click();", root_selection)

        checkbox_list = self.d.find_elements(By.XPATH,
                                             read_event_filter_ini().zones_checkbox_list())
        zone_text_list = self.d.find_elements(By.XPATH,
                                              read_event_filter_ini().zones_text_list())
        try:

            for i in range(len(zone_text_list)):
                actual_zone_text = zone_text_list.__getitem__(i).text
                self.log.info(f"actual zone: {actual_zone_text}")
                expected_zone_text = read_event_filter_ini().get_zone()
                self.log.info(f"expected zone: {expected_zone_text}")
                if expected_zone_text.lower() in actual_zone_text.lower():
                    if checkbox_list.__getitem__(i).is_selected():
                        checkbox_list.__getitem__(i).click()
                    else:
                        checkbox_list.__getitem__(i).click()
                        #checkbox_list.__getitem__(i).click()
                    break
                time.sleep(Base_Class.one_second)
        except Exception as ex:
            self.log.info(ex.args)

    def tags_selection(self):
        tags_selection = self.d.find_element(By.XPATH,
                                             read_event_filter_ini().tag_selection_drop_down())
        # self.d.execute_script("arguments[0].click();", tags_selection)

        tags_selection.click()
        time.sleep(Base_Class.one_second)

        checkbox_list = self.d.find_elements(By.XPATH,
                                             read_event_filter_ini().tags_checkbox_list())
        tags_text_list = self.d.find_elements(By.XPATH,
                                              read_event_filter_ini().tags_text_list())
        try:

            for i in range(len(tags_text_list) + 1):
                actual_tag_text = tags_text_list.__getitem__(i).text
                expected_tag_text = read_event_filter_ini().get_tags().upper()
                if actual_tag_text == expected_tag_text:
                    checkbox_list.__getitem__(i).click()
        except Exception as ex:
            self.log.info(ex.args)

    # validation methods

    def enrollment_group_search_result_validation(self):
        enrollment_group_search_validation = self.d.find_element(By.XPATH,
                                                                 read_event_filter_ini().
                                                                 enrollment_group_search_result_validation())
        actual_text = enrollment_group_search_validation.text
        expected_text = read_event_filter_ini().get_enrollment_group()
        time.sleep(Base_Class.one_second)
        return actual_text.lower() == expected_text.lower()

    def zones_search_result_validation(self):
        zones_search_result_validation = self.d.find_element(By.XPATH,
                                                             read_event_filter_ini().
                                                             zone_search_result_validation())
        actual_text = zones_search_result_validation.text.lower()
        expected_text = read_event_filter_ini().get_zone().lower()
        time.sleep(Base_Class.one_second)
        return expected_text in actual_text

    def tag_search_result_validation(self):
        tag_search_result_validation = self.d.find_element(By.XPATH,
                                                           read_event_filter_ini().
                                                           tags_search_result_validation())
        actual_text = tag_search_result_validation.text
        expected_text = read_event_filter_ini().get_tags().upper()
        time.sleep(Base_Class.one_second)
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

        ac_start_date = self.d.find_element(By.XPATH, read_event_filter_ini().date_search_result_validation())
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
                                                 read_event_filter_ini().event_search_start_date_checkbox())
            start_check_bx.click()
            start_date_txt_bx = self.d.find_element(By.XPATH, read_event_filter_ini().event_search_start_date_input())
            start_date_txt_bx.click()
        else:
            # click on the to calendar pop up
            end_check_bx = self.d.find_element(By.XPATH,
                                               read_event_filter_ini().event_search_end_date_checkbox())
            end_check_bx.click()
            end_date_txt_bx = self.d.find_element(By.XPATH, read_event_filter_ini().event_search_end_date_input())
            end_date_txt_bx.click()

        # click on the clock icon
        calender_clock = self.d.find_element(By.XPATH, read_event_filter_ini().calender_timer_icon_by_xpath())
        calender_clock.click()

        time.sleep(Base_Class.one_second)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, read_event_filter_ini().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, read_event_filter_ini().calender_tick_icon_by_xpath())
        tick_icon.click()

        if strategy == "from":
            start_date_txt_bx = self.d.find_element(By.XPATH, read_event_filter_ini().start_date_by_xpath())
            start_date_txt_bx.click()
        else:
            # click on the to calendar pop up
            start_date_txt_bx = self.d.find_element(By.XPATH, read_event_filter_ini().end_date_by_xpath())
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
        month_year = self.d.find_element(By.XPATH, read_event_filter_ini().calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  read_event_filter_ini().calender_back_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()

            month_year = self.d.find_element(By.XPATH,
                                             read_event_filter_ini().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  read_event_filter_ini().calender_forward_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()

            month_year = self.d.find_element(By.XPATH,
                                             read_event_filter_ini().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the required date
        try:
            date = self.d.find_element(By.XPATH,
                                       "(//td[@class='day' or @class='day weekend' or @class='day active'])[" + str(
                                           date) + "]")
            date.click()
        except Exception as ex:
            self.log.info(ex.args)

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, read_event_filter_ini().calender_tick_icon_by_xpath())
        tick_icon.click()

    def calender_handle_hour_minute_to(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, read_event_filter_ini().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, read_event_filter_ini().hour_down_by_xpath())
            hour_down.click()
            current_hour_ele = self.d.find_element(By.XPATH,
                                                   read_event_filter_ini().current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH,
                                              read_event_filter_ini().current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_down_button = self.d.find_element(By.XPATH, read_event_filter_ini()
                                                    .clock_min_down_button_by_xpath())
            clock_down_button.click()
            current_min_ele = self.d.find_element(By.XPATH, read_event_filter_ini()
                                                  .current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, read_event_filter_ini().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, read_event_filter_ini().hour_down_by_xpath())
            hour_down.click()
            current_hour_ele = self.d.find_element(By.XPATH, read_event_filter_ini()
                                                   .current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH, read_event_filter_ini()
                                              .current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_up_button = self.d.find_element(By.XPATH, read_event_filter_ini()
                                                  .clock_min_up_button_by_xpath())
            clock_up_button.click()
            current_min_ele = self.d.find_element(By.XPATH, read_event_filter_ini()
                                                  .current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    # close tab and logout method

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    read_event_filter_ini().close_all_panel_one_by_one())
            for i in close_panel_list:
                i.click()
                time.sleep(Base_Class.one_second)
        except Exception as ex:
            self.log.info(ex.args)

    def click_on_logout_button(self):
        try:
            time.sleep(Base_Class.one_second)
            logout_button = self.d.find_element(By.XPATH, read_event_filter_ini().logout_btn_by_xpath())
            logout_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\click_on_logout_button_failed.png")
            self.log.info(f"exception:  {ex.args}")
            return False

    ############################################# Business Method #####################################################

    def event_search_with_no_filter_combination(self):
        try:
            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            search_button = self.d.find_element(By.XPATH, read_event_filter_ini().event_filter_search_button_by_xpath())
            self.click_on_event_filter_search_button()
            if search_button.is_enabled():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_no_filter_combination_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_no_filter_combination_failed.png")
            self.log.info(f"event_search_with_no_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_tag_filter_combination(self):
        try:
            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.tags_selection()
            self.click_on_save_tag_button()
            self.click_on_event_filter_search_button()

            if self.tag_search_result_validation():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_tag_filter_combination_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_tag_filter_combination_failed.png")
            self.log.info(f"event_search_with_tag_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_org_Hierarchy_filter_combination(self):
        try:
            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.zone_selection()
            self.click_on_save_zone_button()

            self.click_on_event_filter_search_button()

            if self.zones_search_result_validation():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_org_Hierarchy_filter_"
                                       f"combination_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_org_Hierarchy_filter_"
                                   f"combination_failed.png")
            self.log.info(f"event_search_with_org_Hierarchy_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_tag_and_org_hierarchy_filter_combination(self):
        result = []
        try:
            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.zone_selection()
            self.click_on_save_zone_button()
            self.tags_selection()
            self.click_on_save_tag_button()

            self.click_on_event_filter_search_button()

            result.append(self.zones_search_result_validation())
            result.append(self.tag_search_result_validation())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_tag_and_org_hierarchy_filter_"
                                       f"combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_tag_and_org_hierarchy_filter_"
                                   f"combination_failed.png")
            self.log.info(f"event_search_with_tag_and_org_hierarchy_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_enrollmentGroup_filter_combination(self):
        try:
            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.enrollment_group_selection()
            self.click_on_save_button()

            self.click_on_event_filter_search_button()

            if self.enrollment_group_search_result_validation():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_enrollmentGroup_filter_"
                                       f"combination_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_enrollmentGroup_filter_combination_"
                                   f"failed.png")
            self.log.info(f"event_search_with_enrollmentGroup_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_enrollmentGroup_and_tag_filter_combination(self):
        result = []
        try:
            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.enrollment_group_selection()
            self.click_on_save_button()
            self.tags_selection()
            self.click_on_save_tag_button()

            self.click_on_event_filter_search_button()

            result.append(self.enrollment_group_search_result_validation())
            result.append(self.tag_search_result_validation())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_enrollmentGroup_and_tag_filter_"
                                       f"combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_enrollmentGroup_and_tag_filter_"
                                   f"combination_failed.png")
            self.log.info(f"event_search_with_enrollmentGroup_and_tag_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_enrollmentGroup_org_hierarchy_filter_combination(self):
        result = []
        try:
            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.enrollment_group_selection()
            self.click_on_save_button()
            self.zone_selection()
            self.click_on_save_zone_button()

            self.click_on_event_filter_search_button()

            result.append(self.enrollment_group_search_result_validation())
            result.append(self.zones_search_result_validation())
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\event_search_with_enrollmentGroup_org_hierarchy_filter_"
                    f"combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_enrollmentGroup_org_hierarchy_filter"
                                   f"_combination_failed.png")
            self.log.info(f"event_search_with_enrollmentGroup_org_hierarchy_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_enrollmentGroup_org_hierarchy_and_tag_filter_combination(self):
        result = []
        try:
            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.enrollment_group_selection()
            self.click_on_save_button()
            self.zone_selection()
            self.click_on_save_zone_button()
            self.tags_selection()
            self.click_on_save_tag_button()

            self.click_on_event_filter_search_button()

            result.append(self.enrollment_group_search_result_validation())
            result.append(self.zones_search_result_validation())
            result.append(self.tag_search_result_validation())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_enrollmentGroup_org_hierarchy_and_"
                                       f"tag_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_enrollmentGroup_org_hierarchy_and_"
                                   f"tag_filter_combination_failed.png")
            self.log.info(f"event_search_with_enrollmentGroup_org_hierarchy_and_tag_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_dateTimeRange_filter_combination(self):
        try:
            date = int(read_event_filter_ini().get_start_date())
            month = str(read_event_filter_ini().get_start_month())
            year = int(read_event_filter_ini().get_start_year())
            hour = str(read_event_filter_ini().get_start_hour())
            minute = int(read_event_filter_ini().get_start_minuet())
            period = str(read_event_filter_ini().get_start_am_pm_period())

            e_month = str(read_event_filter_ini().get_end_month())
            e_date = int(read_event_filter_ini().get_end_date())
            e_year = int(read_event_filter_ini().get_end_year())
            e_hour = str(read_event_filter_ini().get_end_hour())
            e_minute = int(read_event_filter_ini().get_end_minuet())
            e_period = str(read_event_filter_ini().get_end_am_pm_period())

            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.two_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                        e_period)

            search_button = self.d.find_element(By.XPATH, read_event_filter_ini().event_filter_search_button_by_xpath())
            self.click_on_event_filter_search_button()
            if search_button.is_enabled():
                return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_dateTimeRange_filter_combination"
                                   f"_failed.png")
            self.log.info(f"event_search_with_dateTimeRange_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_DateTimeRange_and_Tag_filter_combination(self):
        result = []
        try:
            date = int(read_event_filter_ini().get_start_date())
            month = str(read_event_filter_ini().get_start_month())
            year = int(read_event_filter_ini().get_start_year())
            hour = str(read_event_filter_ini().get_start_hour())
            minute = int(read_event_filter_ini().get_start_minuet())
            period = str(read_event_filter_ini().get_start_am_pm_period())

            e_month = str(read_event_filter_ini().get_end_month())
            e_date = int(read_event_filter_ini().get_end_date())
            e_year = int(read_event_filter_ini().get_end_year())
            e_hour = str(read_event_filter_ini().get_end_hour())
            e_minute = int(read_event_filter_ini().get_end_minuet())
            e_period = str(read_event_filter_ini().get_end_am_pm_period())

            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.two_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                        e_period)
            self.tags_selection()
            self.click_on_save_tag_button()

            self.click_on_event_filter_search_button()
            result.append(self.tag_search_result_validation())
            if False in result :
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_and_Tag_filter_"
                                       f"combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_and_Tag_filter_"
                                   f"combination_failed.png")
            self.log.info(f"event_search_with_DateTimeRange_and_Tag_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_DateTimeRange_and_org_Hierarchy_filter_combination(self):
        result = []
        try:
            date = int(read_event_filter_ini().get_start_date())
            month = str(read_event_filter_ini().get_start_month())
            year = int(read_event_filter_ini().get_start_year())
            hour = str(read_event_filter_ini().get_start_hour())
            minute = int(read_event_filter_ini().get_start_minuet())
            period = str(read_event_filter_ini().get_start_am_pm_period())

            e_month = str(read_event_filter_ini().get_end_month())
            e_date = int(read_event_filter_ini().get_end_date())
            e_year = int(read_event_filter_ini().get_end_year())
            e_hour = str(read_event_filter_ini().get_end_hour())
            e_minute = int(read_event_filter_ini().get_end_minuet())
            e_period = str(read_event_filter_ini().get_end_am_pm_period())

            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            time.sleep(Base_Class.one_second)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                        e_period)
            self.zone_selection()
            self.click_on_save_zone_button()

            self.click_on_event_filter_search_button()

            result.append(self.zones_search_result_validation())
            self.log.info(f"result status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_and_org_Hierarchy"
                                       f"_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_and_org_Hierarchy_filter"
                                   f"_combination_failed.png")
            self.log.info(f"event_search_with_DateTimeRange_and_org_Hierarchy_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_DateTimeRange_org_Hierarchy_and_Tag_filter_combination(self):
        result = []
        try:
            date = int(read_event_filter_ini().get_start_date())
            month = str(read_event_filter_ini().get_start_month())
            year = int(read_event_filter_ini().get_start_year())
            hour = str(read_event_filter_ini().get_start_hour())
            minute = int(read_event_filter_ini().get_start_minuet())
            period = str(read_event_filter_ini().get_start_am_pm_period())

            e_month = str(read_event_filter_ini().get_end_month())
            e_date = int(read_event_filter_ini().get_end_date())
            e_year = int(read_event_filter_ini().get_end_year())
            e_hour = str(read_event_filter_ini().get_end_hour())
            e_minute = int(read_event_filter_ini().get_end_minuet())
            e_period = str(read_event_filter_ini().get_end_am_pm_period())

            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                        e_period)
            self.zone_selection()
            self.click_on_save_zone_button()
            self.tags_selection()
            self.click_on_save_tag_button()

            self.click_on_event_filter_search_button()

            result.append(self.zones_search_result_validation())
            result.append(self.tag_search_result_validation())
            self.log.info(f"result status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_org_Hierarchy_and_Tag"
                                       f"_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_org_Hierarchy_and_Tag_"
                                   f"filter_combination_failed.png")
            self.log.info(f"event_search_with_DateTimeRange_org_Hierarchy_and_Tag_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_DateTimeRange_and_EnrollmentGroup_filter_combination(self):
        result =[]
        try:
            date = int(read_event_filter_ini().get_start_date())
            month = str(read_event_filter_ini().get_start_month())
            year = int(read_event_filter_ini().get_start_year())
            hour = str(read_event_filter_ini().get_start_hour())
            minute = int(read_event_filter_ini().get_start_minuet())
            period = str(read_event_filter_ini().get_start_am_pm_period())

            e_month = str(read_event_filter_ini().get_end_month())
            e_date = int(read_event_filter_ini().get_end_date())
            e_year = int(read_event_filter_ini().get_end_year())
            e_hour = str(read_event_filter_ini().get_end_hour())
            e_minute = int(read_event_filter_ini().get_end_minuet())
            e_period = str(read_event_filter_ini().get_end_am_pm_period())

            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                        e_period)
            self.enrollment_group_selection()
            self.click_on_save_button()

            self.click_on_event_filter_search_button()

            result.append(self.enrollment_group_search_result_validation())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_and_EnrollmentGroup_"
                                       f"filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_and_EnrollmentGroup_"
                                   f"filter_combination_failed.png")
            self.log.info(f"event_search_with_DateTimeRange_and_EnrollmentGroup_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_DateTimeRange_EnrollmentGroup_and_Tag_filter_combination(self):
        result = []
        try:
            date = int(read_event_filter_ini().get_start_date())
            month = str(read_event_filter_ini().get_start_month())
            year = int(read_event_filter_ini().get_start_year())
            hour = str(read_event_filter_ini().get_start_hour())
            minute = int(read_event_filter_ini().get_start_minuet())
            period = str(read_event_filter_ini().get_start_am_pm_period())

            e_month = str(read_event_filter_ini().get_end_month())
            e_date = int(read_event_filter_ini().get_end_date())
            e_year = int(read_event_filter_ini().get_end_year())
            e_hour = str(read_event_filter_ini().get_end_hour())
            e_minute = int(read_event_filter_ini().get_end_minuet())
            e_period = str(read_event_filter_ini().get_end_am_pm_period())

            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                        e_period)
            self.enrollment_group_selection()
            self.click_on_save_button()
            self.tags_selection()
            self.click_on_save_tag_button()

            self.click_on_event_filter_search_button()

            result.append(self.enrollment_group_search_result_validation())
            result.append(self.tag_search_result_validation())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_EnrollmentGroup_"
                                       f"and_Tag_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_EnrollmentGroup_and_"
                                   f"Tag_filter_combination_failed.png")
            self.log.info(f"event_search_with_DateTimeRange_EnrollmentGroup_and_Tag_filter_combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_DateTimeRange_EnrollmentGroup_and_Org_Hierarchy_filter_combination(self):
        result = []
        try:
            date = int(read_event_filter_ini().get_start_date())
            month = str(read_event_filter_ini().get_start_month())
            year = int(read_event_filter_ini().get_start_year())
            hour = str(read_event_filter_ini().get_start_hour())
            minute = int(read_event_filter_ini().get_start_minuet())
            period = str(read_event_filter_ini().get_start_am_pm_period())

            e_month = str(read_event_filter_ini().get_end_month())
            e_date = int(read_event_filter_ini().get_end_date())
            e_year = int(read_event_filter_ini().get_end_year())
            e_hour = str(read_event_filter_ini().get_end_hour())
            e_minute = int(read_event_filter_ini().get_end_minuet())
            e_period = str(read_event_filter_ini().get_end_am_pm_period())

            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                        e_period)
            self.enrollment_group_selection()
            self.click_on_save_button()
            self.zone_selection()
            self.click_on_save_zone_button()

            self.click_on_event_filter_search_button()

            result.append(self.enrollment_group_search_result_validation())
            result.append(self.zones_search_result_validation())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_EnrollmentGroup_and_"
                                       f"Org_Hierarchy_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_EnrollmentGroup_and_Org_"
                                   f"Hierarchy_filter_combination_failed.png")
            self.log.info(f"event_search_with_DateTimeRange_EnrollmentGroup_and_Org_Hierarchy_filter_"
                          f"combination failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def event_search_with_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tag_filter_combination(self):
        result = []
        try:
            date = int(read_event_filter_ini().get_start_date())
            month = str(read_event_filter_ini().get_start_month())
            year = int(read_event_filter_ini().get_start_year())
            hour = str(read_event_filter_ini().get_start_hour())
            minute = int(read_event_filter_ini().get_start_minuet())
            period = str(read_event_filter_ini().get_start_am_pm_period())

            e_month = str(read_event_filter_ini().get_end_month())
            e_date = int(read_event_filter_ini().get_end_date())
            e_year = int(read_event_filter_ini().get_end_year())
            e_hour = str(read_event_filter_ini().get_end_hour())
            e_minute = int(read_event_filter_ini().get_end_minuet())
            e_period = str(read_event_filter_ini().get_end_am_pm_period())

            self.login()
            self.click_on_event_menu()
            self.click_on_search_button()
            self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
            self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                        e_period)
            self.enrollment_group_selection()
            self.click_on_save_button()
            self.zone_selection()
            self.click_on_save_zone_button()
            self.tags_selection()
            self.click_on_save_tag_button()

            self.click_on_event_filter_search_button()

            result.append(self.enrollment_group_search_result_validation())
            result.append(self.zones_search_result_validation())
            result.append(self.tag_search_result_validation())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_EnrollmentGroup_Org"
                                       f"_Hierarchy_and_Tag_filter_combination_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\event_search_with_DateTimeRange_EnrollmentGroup_Org_"
                                   f"Hierarchy_and_Tag_filter_combination_failed.png")
            self.log.info(f"event_search_with_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tag_filter_combination"
                          f" failed:  {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()


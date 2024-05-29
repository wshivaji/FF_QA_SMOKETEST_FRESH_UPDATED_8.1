import os
import time
import datetime
from datetime import timedelta

import pandas as pd
import pyautogui
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

# from All_Config_Packages._16_Audit_Log_Report_Module_Config_Files.Audit_Log_Report_Read_INI import \
#     Audit_Log_Report_Components
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login, logout
from selenium.webdriver.common.by import By
from All_Config_Packages._12_Identify_and_Enroll_Config_Files.Identify_and_Enroll_Readd_INI import \
    Read_Identify_and_Enroll_Components

from pathlib import Path


class Identify_And_Enroll_POM(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    now = (datetime.datetime.now())
    DATE_IE = now.strftime('%m/%d/%Y')
    TIME_IE = now.strftime('%H%M')
    AM_PM_IE = now.strftime('%p')
    tomorrow = now + timedelta(2)

    expirationDATE_IE = tomorrow.strftime('%m/%d/%Y')
    expirationTIME_IE = now.strftime('%H%M')
    expirationAM_PM_IE = now.strftime('%p')

    def dateTimeAMPM(self, date_incident):
        self.logger.info(f" date : {self.DATE_IE}")
        # date_incident.click()
        # date_incident.clear()
        date_incident.send_keys(self.DATE_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(self.TIME_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(self.AM_PM_IE)
        time.sleep(web_driver.one_second)

    def expirirationdateTimeAMPM(self, date_incident):
        self.logger.info(f" tommorow date : {self.expirationDATE_IE}")
        date_incident.send_keys(self.expirationDATE_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(" " + self.TIME_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(" " + self.AM_PM_IE)
        time.sleep(web_driver.one_second)

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

    def upload_image_not_enrolled(self, img_path):

        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        file_path = img_path
        time.sleep(2)
        self.logger.info(f"image uploaded: {file_path}")
        # upload_image = self.explicit_wait(10, "NAME", "image", self.d)
        upload_image = self.d.find_element(By.NAME, "image")
        upload_image.send_keys(file_path)

    # def upload_image(self, file_path):
    #     """
    #     This function is usd to upload the image and click on the search button
    #     :return:
    #     """
    #     # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
    #     # file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\ab\\00076.png"
    #     self.logger.info(f"image uploaded: {file_path}")
    #     # upload_image = self.explicit_wait(10, "NAME", "image", self.d)
    #     upload_image = self.d.find_element(By.NAME, "image")
    #     upload_image.send_keys(file_path)

        self.logger.info("Photo Selected....")

    def load_portal_login_page_if_not_loaded(self):
        try:
            login_func = login()
            if self.d.current_url == login_func.local_url:
                pass
            else:
                login().login_to_cloud_if_not_done(self.d)
                self.status.clear()
        except Exception as ex:
            self.logger.error(ex)

    def Select_Enrollment_Group(self, i):
        try:
            i = int(i)
            self.logger.info(f"eg index: {i}")
            eg = Read_Identify_and_Enroll_Components().get_eg()
            enrollment_groups_list = eg.split(',')

            time.sleep(web_driver.two_second)
            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
            enrollment_group.click()
            select = Select(enrollment_group)
            self.logger.info(f"enrollment group: {enrollment_groups_list[i]}")
            enter_eg = enrollment_groups_list[i] + " (Serious Offender - None)"
            select.select_by_visible_text(enter_eg)
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
        except Exception as ex:
            print("select enrollment group exception: ", ex.args)

    def login_with_persona_user(self):
        try:
            x = Read_Identify_and_Enroll_Components().get_user_name_input_data()
            username = x.split(',')
            self.logger.info(f"username expected: {username[0]}")
        except Exception as ex:
            print(ex)

    def Create_New_Enrollment_using_Identify_and_Enroll(self):
        try:
            self.logger.info("************* test_TC_IE_00 started  **************")
            # # # # self.verify_portal_login()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\img4.png"
            self.upload_image(file_path)

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
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)
            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group(0)
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

            # action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().action_inpt_bx_by_xpath())
            # action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

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
            # save_btn.click()
            time.sleep(5)

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
            # ***************************************Enrollment Process end here**********************
            self.close_all_panel_one_by_one()
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

    def verify_portal_login(self):
        try:
            self.load_portal_login_page_if_not_loaded()
            logout_func = logout()
            logout_button = self.d.find_element(By.XPATH, logout_func.config.get("logout_locators", "logout_btn_by_xpath"))

            if logout_button.is_displayed():
                pass
            else:
                login_func = login()
                if self.d.current_url == login().cloud_url:
                    self.status.append(True)
                else:
                    self.status.append(False)
                    login().login_to_cloud_if_not_done(self.d)
                    self.status.clear()

            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(ex)

    def login_before(self):
        try:
            self.status.clear()
            self.d.get(Read_Identify_and_Enroll_Components().get_portal_url())
            self.d.maximize_window()
            username = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().get_portal_login_username_textbox_by_xpath())
            username.send_keys(Read_Identify_and_Enroll_Components().get_username_to_login())
            password = self.d.find_element(By.XPATH,Read_Identify_and_Enroll_Components().get_portal_login_password_textbox_by_xpath())
            password.send_keys(Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)
            login_btn = self.d.find_element(By.ID, Read_Identify_and_Enroll_Components().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info("login")
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                self.logger.info("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_failed_for_portal_menu_pg_03.png")
                return False

    def upload_image(self, img_path):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        file_path = img_path
        time.sleep(2)
        self.logger.info(f"image uploaded: {file_path}")
        upload_image_box = self.d.find_element(By.NAME, "image")
        upload_image_box.send_keys(file_path)
        self.logger.info("Photo Selected....")

    def upload_image_not_enrolled(self, img_path):

        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        upload_photo = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                              .upload_image_by_xpath(), self.d)
        upload_photo.click()
        self.logger.info(f"clicked on upload image icon")
        time.sleep(2)
        file_path = f"{self.ie_file_path}\\vip\\00096.png"
        # All_Test_Data\\Common_Test_Data\\dataset1\\vip\\00096.png
        pyautogui.write(img_path)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')

    def upload_image_enrollment_not_required(self):

        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        upload_photo = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                              .upload_image_by_xpath(), self.d)
        upload_photo.click()
        self.logger.info(f"clicked on upload image icon")
        time.sleep(2)
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\ENR.png"

        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')

    def enroll_person(self):
        """
        This function is used to enroll the person
        :return:
        """
        self.login_before()
        time.sleep(web_driver.two_second)

        link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                   .identify_and_enroll_link_by_xpath())
        self.d.execute_script("arguments[0].click();", link)
        self.logger.info(f"clicked on Identify and enroll link")
        time.sleep(web_driver.one_second)
        file_path = f"{self.ie_file_path}\\ab\\00076.png"
        self.upload_image(file_path)

        identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .identify_enroll_panel_identify_enroll_btn_by_xpath())

        self.d.execute_script("arguments[0].click();", identify_enroll_btn)

        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .identifying_photo_wait_by_xpath())
        count = 0
        while wait_icon.is_displayed():
            if count > 15:
                break
            time.sleep(web_driver.one_second)
            count += 1
            self.logger.info(f"waiting fir wait icon, count: {count}")

        enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(1)

        location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .location_store_inpt_bx_by_xpath())
        location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

        case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .case_subject_inpt_bx_by_xpath())
        case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

        reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .reported_loss_inpt_bx_by_xpath())
        reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

        date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .date_incident_inpt_bx_by_xpath())
        time.sleep(web_driver.two_second)
        self.dateTimeAMPM(date_incident)
        time.sleep(web_driver.two_second)
        action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .action_inpt_bx_by_xpath())
        action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

        save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .add_details_save_btn_by_xpath())
        assert save_btn.is_displayed()
        save_btn.click()
        self.logger.info("Enrollment details filled and save btn is clicked")
        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_success_loader())
        count = 0
        while wait_icon.is_displayed():
            if count > 15:
                break
            time.sleep(web_driver.one_second)
            count += 1
            self.logger.info(f"waiting fir wait icon, count: {count}")
        success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                          .enrollment_success_msg_xpath())
        assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
            enrollment_success_msg_validation().lower()

        title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                     add_details_panel_title_panel())
        for x in title:
            if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                    add_details_panel_validation().lower():
                assert False
        self.close_all_panel_one_by_one()
        self.click_on_logout_button()

    def add_details_enrollment(self):
        """
        This function is used to add details for the enrollment
        :return:
        """

        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .identifying_photo_wait_by_xpath())
        count = 0
        while wait_icon.is_displayed() or count == 120:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting for wait icon, count: {count}")

        time.sleep(web_driver.two_second)
        enrollment_basis = self.d.find_element(By.XPATH,
                                               Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath())
        select = Select(enrollment_basis)
        select.select_by_index(1)

        time.sleep(web_driver.two_second)
        enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(2)
        time.sleep(web_driver.one_second)
        region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
        time.sleep(web_driver.one_second)
        region_btn.click()
        time.sleep(web_driver.one_second)
        region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
        edge_name = Read_Identify_and_Enroll_Components().edge_name()
        for i in range(len(region_names)):
            if edge_name in region_names[i].text:
                region_names[i].click()
                break
        save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
        save_btn.click()
        time.sleep(web_driver.two_second)

        enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(1)

        location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .location_store_inpt_bx_by_xpath())
        location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

        case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .case_subject_inpt_bx_by_xpath())
        case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

        reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .reported_loss_inpt_bx_by_xpath())
        reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

        date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .date_incident_inpt_bx_by_xpath())
        time.sleep(web_driver.two_second)
        self.dateTimeAMPM(date_incident)
        time.sleep(web_driver.two_second)
        action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .action_inpt_bx_by_xpath())
        action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

        save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .add_details_save_btn_by_xpath())
        save_btn.click()
        self.logger.info("Enrollment details filled and save btn is clicked")
        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_success_loader())
        count = 0
        while wait_icon.is_displayed() or count == 120:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting for wait icon, count: {count}")

        self.close_all_panel_one_by_one()

    def delete_enrollment(self):
        try:

            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             cloud_menu_button_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            time.sleep(2)
            enrollment_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                 enrollment_menu_button_xpath())
            time.sleep(2)
            enrollment_btn.click()
            time.sleep(web_driver.three_second)
            time.sleep(2)

            checkbox = self.d.find_element(By.XPATH,Read_Identify_and_Enroll_Components().select_one_checkbox())
            checkbox.click()

            time.sleep(web_driver.one_second)
            time.sleep(web_driver.two_second)

            action_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             enrollment_panel_action_btn())
            time.sleep(2)
            action_btn.click()
            time.sleep(web_driver.one_second)

            delete_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             delete_enrollments_btn_xpath())
            time.sleep(2)
            delete_btn.click()
            time.sleep(web_driver.one_second)

            yes_delete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             yes_delete_btn_xpath())
            time.sleep(2)
            yes_delete_2 = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                               yes_delete_btn_xpath_2())
            time.sleep(2)
            if yes_delete.is_displayed():
                time.sleep(2)
                yes_delete.click()
                time.sleep(web_driver.one_second)
            else:
                time.sleep(2)
                yes_delete_2.click()
                time.sleep(web_driver.one_second)

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                self.logger.info("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\delete_enrollment_failed.png")
                return False

    def verify_Cloud_Menu_Local_Menu(self):
        try:
            self.logger.info("************* test_TC_IE_01 started  **************")
            # # # self.verify_portal_login()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().cloud_menu_by_xpath(), self.d)
            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().cloud_menu_by_xpath())
            if cloud_menu.is_displayed():
                self.logger.info("Cloud menu is visible...")
                self.status.append(True)
            else:
                self.logger.info("Cloud menu is not visible...")
                self.status.append(False)
            if cloud_menu.is_enabled():
                self.logger.info("Cloud menu is clickable...")
                self.status.append(True)
            else:
                self.logger.info("Cloud menu is not clickable...")
                self.status.append(False)
            cloud_menu.click()
            # self.click_on_logout_button()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_01_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_01_Failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"test_TC_IE_01 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_01_exception.png")
            return False


    def verify_three_buttons_faces_person_view_and_purge_Replace_are_visible(self):
        try:
            self.logger.info("************* test_TC_IE_07 started  **************")
            # # self.verify_portal_login()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{self.ie_file_path}\\ab\\1821_20220526-124517.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())
            if face_icon.is_displayed():
                self.logger.info("Face icon is visible...")
                self.status.append(True)
            else:
                self.logger.info("Face icon is not visible...")
                self.status.append(False)
            person_view = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .identify_results_person_view_icon_by_xpath())
            if person_view.is_displayed():
                self.logger.info("Person view is visible...")
                self.status.append(True)
            else:
                self.logger.info("Person view is visible...")
                self.status.append(False)
            purge_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_purge_replace_icon_by_xpath())
            if purge_icon.is_displayed():
                self.logger.info("purge icon is visible...")
                self.status.append(True)
            else:
                self.logger.info("Person view is not visible...")
                self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_07.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_07_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_07 got an exception as: {ex}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_07_exception.png")
            return False
        finally:
            self.click_on_logout_button()

    def close_all_panel_one_by_one(self):
        try:
            # close_panel_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().close_all_panel_one_by_one())
            time.sleep(web_driver.one_second)
            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().cloud_menu_by_xpath())
            cloud_menu.click()
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            close_all_panels_menu = self.d.find_elements(By.XPATH,
                                                         Read_Identify_and_Enroll_Components().close_all_panels_btn_by_xpath())
            time.sleep(web_driver.one_second)
            # web_driver.implicit_wait(self, web_driver.one_second, self.d)
            # web_driver.explicit_wait(self, web_driver.one_second, close_all_panels_menu, self.d)
            if len(close_all_panels_menu) > 0:
                close_all_panels_menu[0].click()
                time.sleep(web_driver.one_second)
                try:
                    self.d.switch_to.alert.accept()
                except Exception as ex:
                    self.logger.info(f"Alert handled {ex.args}")
            else:
                pass
            time.sleep(web_driver.one_second)

        except Exception as ex:
            self.logger.error(f"Exception crated: {ex.args}")
            self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\test_TC_IE_05_exception.png")
            return False

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.one_second)
            logout_func = logout()
            logout_button = self.d.find_element(By.XPATH,
                                                logout_func.config.get("logout_locators", "logout_btn_by_xpath"))
            time.sleep(web_driver.one_second)
            logout_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("logout")
        except Exception as ex:
            self.logger.error(f"Exception crated: {ex}")
            # self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
            return False


    #
    def verify_Success_message_is_displayed_below_warning_on_Identify_and_enroll_panel(self):
        try:
            self.logger.info("************* test_TC_IE_101 started  **************")
            # # self.verify_portal_login()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)
            img_path = f"{self.ie_file_path}\\vip\\00096.png"
            print(f"iamge_path : {img_path}")
            self.upload_image_not_enrolled(img_path)
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
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)

            self.Select_Enrollment_Group(0)
            # enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
            # select = Select(enrollment_group)
            # select.select_by_index(2)
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

            action_input = self.d.find_element(By.XPATH,
                                               Read_Identify_and_Enroll_Components().action_input_by_xpath())
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
            # time.sleep(web_driver.one_second)
            # date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_time())
            # time.sleep(web_driver.one_second)
            # date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_am_pm())
            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath(), self.d)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            # wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
            #                                 .enrollment_success_loader())
            # count = 0
            # while wait_icon.is_displayed() or count == 120:
            #     time.sleep(web_driver.two_second)
            #     count += 1
            #     self.logger.info(f"waiting fir wait icon, count: {count}")
            #
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
            #                    .enrollment_success_msg_xpath(), self.d)
            # success_msg = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
            #                                   .enrollment_success_msg_xpath(), self.d)
            # if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
            #         lower():
            #     self.status.append(True)
            # else:
            #     self.status.append(False)
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

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)
            time.sleep(2)
            self.delete_enrollment()
            time.sleep(2)
            # ***************************************Enrollment Process end here**********************
            self.close_all_panel_one_by_one()
            # ***************************************************************
            # self.click_on_logout_button()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_101.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_101_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_101 got an exception as: {ex}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_101_Exception.png")
            return False

    def click_on_close_all_panel_btn(self):
        panel_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().get_panel_by_xpath())
        if len(panel_list) > 0:
            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().cloud_menu_button_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            close_all_panel_btn = self.d.find_element(By.XPATH,
                                                      Read_Identify_and_Enroll_Components().get_close_all_panel_menu_item_by_xpath())
            close_all_panel_btn.click()
            time.sleep(web_driver.two_second)

    def click_on_enroll_for_already_enrolled(self):
        time.sleep(web_driver.two_second)
        enroll = self.d.find_element(By.XPATH, "//i[@class='fa fa-pencil']")
        # web_driver.explicit_wait(self, 10, enroll, self.d)
        if enroll.is_displayed():
            # enroll.click()
            self.d.execute_script("arguments[0].click();", enroll)
            self.logger.info("Re-enroll for already enrolled ")
            self.logger.info("clicked on enroll button")

    def get_img_file_list(self, folder_name):
        try:
            img_folder = f"{self.ie_file_path}\\{folder_name}"
            print(img_folder)
            files_list = os.listdir(img_folder)
            base_path = Path(img_folder)
            print(f"images path: {base_path}")
            files_in_base_path = base_path.iterdir()
            print(type(files_in_base_path))
            img_name_list = []
            for file in files_list[:-1]:
                for file_name in files_in_base_path:
                    img_name_list.append(file_name.name)
            return img_name_list
        except Exception as ex:
            self.logger.info(f"images list exception : {ex.args}")
    def Read_user_from_json(self):
        try:
            file_path = f'{Path(__file__).parent.parent.parent}\\All_Test_Data\\12_Identify_and_Enroll_Module\\Data_From_Json\\Enrollment_group.json'
            print(f"json file path: {file_path}")
            # users_dict = json.loads(file_path)
            # print(f"users dictionary: {users_dict["date_range"]}")
            Enrollment_details_pd = pd.read_json(file_path)
            print(f"user dict dataframe: {Enrollment_details_pd['Enrollment_details']}")
            return Enrollment_details_pd
        except Exception as ex:
            self.logger.info(f"readiing Enrollment  from json: {ex.args}" )

    def Identify_and_enroll_25_subjects_and_fill_the_required_fields_5_per_Enrollment_groups(self):
        try:
            self.logger.info("************* test_TC_IE_01 started  **************")
            
            self.enroll_5_images("ab")
            self.enroll_5_images("fraud")
            self.enroll_5_images("pt")
            self.enroll_5_images("so")
            self.enroll_5_images("vip")

            # ***************************************Enrollment Process end here**********************

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_01.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_01_failed.png")
                return False
            else:
                return True
        except Exception as ex:

            self.logger.error(f"test_TC_IE_00 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_01_Exception.png")
            return False

    def enroll_5_images(self, folder_name):
        try:
            ab_folder_list_of_images = self.get_img_file_list(folder_name)
            self.logger.info(f"ab folder image names list: {ab_folder_list_of_images}")
            for image in ab_folder_list_of_images:

                login().login_to_cloud_if_not_done_with_user_credentials(self.d,
                                                                         Read_Identify_and_Enroll_Components().get_operator_to_login(),
                                                                         Read_Identify_and_Enroll_Components().get_password_to_login())

                time.sleep(web_driver.two_second)
                link = self.explicit_wait(10, "XPATH",
                                          Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath(),
                                          self.d)
                self.d.execute_script("arguments[0].click();", link)
                self.logger.info(f"clicked on Identify and enroll link")
                time.sleep(web_driver.one_second)

                file_path = f"{self.ie_file_path}\\{folder_name}\\{image}"
                self.upload_image(file_path)

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
                Enrollment_details_dict = self.Read_user_from_json()
                Enrollment_details_dict_1 = []
                if Enrollment_details_dict["Enrollment_details"][0]["case_subject"] == folder_name:
                    Enrollment_details_dict_1 = Enrollment_details_dict["Enrollment_details"][0]

                elif Enrollment_details_dict["Enrollment_details"][1]["case_subject"] == folder_name:
                    Enrollment_details_dict_1 = Enrollment_details_dict["Enrollment_details"][1]

                elif Enrollment_details_dict["Enrollment_details"][2]["case_subject"] == folder_name:
                    Enrollment_details_dict_1 = Enrollment_details_dict["Enrollment_details"][2]

                elif Enrollment_details_dict["Enrollment_details"][3]["case_subject"] == folder_name:
                    Enrollment_details_dict_1 = Enrollment_details_dict["Enrollment_details"][3]

                elif Enrollment_details_dict["Enrollment_details"][4]["case_subject"] == folder_name:
                    Enrollment_details_dict_1 = Enrollment_details_dict["Enrollment_details"][4]

                elif Enrollment_details_dict["Enrollment_details"][5]["case_subject"] == folder_name:
                    Enrollment_details_dict_1 = Enrollment_details_dict["Enrollment_details"][5]

                self.logger.info(f"enrollment details : {Enrollment_details_dict_1}")
                
                    
                dictionary_length = len(Enrollment_details_dict_1)
                print("length of dictionary is", dictionary_length)

                enrollment_basis = self.explicit_wait(10, "XPATH",
                                                      Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(),
                                                      self.d)
                select = Select(enrollment_basis)
                select.select_by_visible_text(Enrollment_details_dict_1["Enrollment_basis"])
                time.sleep(web_driver.three_second)

                enrollment_group = self.d.find_element(By.XPATH,
                                                       Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
                self.logger.info("enrollment group selection")
                time.sleep(web_driver.three_second)
                select = Select(enrollment_group)
                select.select_by_visible_text(Enrollment_details_dict_1["Enrollment_group"])

                enrollment_group_selected = select.first_selected_option
                self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
                print(f"enrollment group selected: {enrollment_group_selected.text}")
                time.sleep(web_driver.one_second)

                region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
                time.sleep(web_driver.one_second)
                region_btn.click()
                self.logger.info("region btn clicked")
                time.sleep(web_driver.one_second)
                region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
                edge_name = Enrollment_details_dict_1["region_hierarchy"]
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

                # action_input = self.d.find_element(By.XPATH,
                #                                    Read_Identify_and_Enroll_Components().action_input_by_xpath())
                # action_input.send_keys(Enrollment_details_dict_1["Action"])

                time.sleep(web_driver.two_second)

                location_store = self.d.find_element(By.XPATH,
                                                     Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
                location_store.send_keys(Enrollment_details_dict_1["Location_store"])

                time.sleep(web_driver.one_second)

                case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .case_subject_inpt_bx_by_xpath())
                case_subject.send_keys(Enrollment_details_dict_1["case_subject"])


                date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .date_incident_inpt_bx_by_xpath())
                time.sleep(web_driver.two_second)
                self.dateTimeAMPM(date_incident)

                reported_loss = self.d.find_element(By.XPATH,
                                                    Read_Identify_and_Enroll_Components().reported_loss_inpt_bx_by_xpath())
                reported_loss.send_keys(Enrollment_details_dict_1["reported_loss"])

                action_input = self.d.find_element(By.XPATH,
                                                   Read_Identify_and_Enroll_Components().action_inpt_bx_by_xpath())
                action_input.send_keys(Enrollment_details_dict_1["Action"])

                save_btn = self.d.find_element(By.XPATH,
                                               Read_Identify_and_Enroll_Components().add_details_save_btn_by_xpath1())
                if save_btn.is_displayed():
                    self.logger.info(f"save btn displayed: {save_btn.is_displayed()}")
                    self.status.append(True)
                else:
                    self.logger.info(f"save btn displayed: {save_btn.is_displayed()}")
                    self.status.append(False)
                self.d.execute_script("arguments[0].click();", save_btn)
                self.logger.info("Enrollment details filled and save btn is clicked")
                # save_btn.click()
                time.sleep(web_driver.one_second)

                try:
                    success_msg = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .enrollment_success_msg_xpath(), self.d)
                    if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                            lower():
                        self.logger.info(f"Success msg is visible: {True}")
                        self.status.append(True)
                    else:
                        self.logger.info(f"Success msg is visible: {False}")
                        self.status.append(False)
                except Exception as ex:
                    self.d.refresh()
                title = self.d.find_elements(By.XPATH,
                                             Read_Identify_and_Enroll_Components().add_details_panel_title_panel())

                for x in title:
                    if x.text.strip().lower() == Read_Identify_and_Enroll_Components().add_details_panel_validation().lower():
                        self.status.append(False)

                time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
        except Exception as ex:
            self.logger.info(f"enroll 5 images exception: {ex.args}")

    def verify_user_able_approve_enrollment(self):
        try:
            self.logger.info("Identify_enroll_Tc_02_started")
            self.status.clear()
            login().login_to_cloud_if_not_done_with_user_credentials(self.d, Read_Identify_and_Enroll_Components().get_approver_to_login(), Read_Identify_and_Enroll_Components().get_password_to_login())
            time.sleep(web_driver.one_second)

            Enrollment_link = self.d.find_element(By.XPATH,Read_Identify_and_Enroll_Components().get_enrollment_link())
            Enrollment_link.click()
            self.logger.info(f"Enrollment link is clicked ")
            time.sleep(web_driver.one_second)

            Filter_dropdown = self.d.find_element(By.XPATH,Read_Identify_and_Enroll_Components().get_filter_dropdown())

            Filter_dropdown = web_driver.explicit_wait(self,5,"XPATH",Read_Identify_and_Enroll_Components().get_filter_dropdown(),self.d)
            Filter_dropdown.click()
            self.logger.info(f"filter dropdown link is clicked:")
            time.sleep(web_driver.two_second)

            pending_for_review = web_driver.explicit_wait(self,5,"XPATH",Read_Identify_and_Enroll_Components().
                                                          pending_for_review_option(), self.d)
            pending_for_review.click()
            self.logger.info(f"pending for review link is clicked:")
            time.sleep(web_driver.two_second)

            load_more_button = web_driver.explicit_wait(self,5,"XPATH", Read_Identify_and_Enroll_Components().get_load_more_button_by_xpath(),self.d)
            time.sleep(web_driver.two_second)
            load_more_button.click()
            self.logger.info(f"load more button is clicked: ")
            time.sleep(web_driver.one_second)

            checkboxes = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().get_checkboxes_by_xpath())
            self.logger.info(f"checkboxes length is: {len(checkboxes)}")
            check = len(checkboxes)
            print(check)
            for ch in checkboxes:
                ch.click()
                time.sleep(web_driver.one_second)

            Action_button = web_driver.explicit_wait(self,10,"XPATH",Read_Identify_and_Enroll_Components().Action_button_by_Xpath(), self.d)
            Action_button.click()
            time.sleep(web_driver.two_second)

            approve_enrollment_link = web_driver.explicit_wait(self,10,"XPATH",Read_Identify_and_Enroll_Components().approve_enrollment_link(),self.d)
            approve_enrollment_link.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicking on approve enrollment link")

            message_after_approving = web_driver.explicit_wait(self,10,"XPATH",Read_Identify_and_Enroll_Components().after_approving_message_to_user(),self.d)
            if message_after_approving.is_displayed():
                self.logger.info(f"message to the user: {message_after_approving.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logout_from_portal()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_02.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_02_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_00 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_02_Exception.png")
            return False
        finally:
            self.click_on_logout_button()

    def Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_cropping_the_same_and_adding_the_required_details_for_the_same(self):
        try:
            self.logger.info("************* test_TC_IE_03 started  **************")
            # # # # self.verify_portal_login()
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_approver_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())
            self.status.clear()

            time.sleep(web_driver.two_second)
            link = self.explicit_wait(10, "XPATH",
                                      Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\img1.png"
            self.upload_image(file_path)

            time.sleep(web_driver.two_second)
            image = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().image_Xpath())

            action = ActionChains(self.d)
            action.move_to_element(image)
            self.logger.info("image moved successfully")
            time.sleep(2)
            ActionChains(self.d).click_and_hold(image).move_by_offset(150, 110).release().perform()

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
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH",
                                                  Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(),
                                                  self.d)
            select = Select(enrollment_basis)
            select.select_by_index(2)
            time.sleep(web_driver.two_second)

            enrollment_group = self.d.find_element(By.XPATH,
                                                   Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
            self.logger.info("enrollment group selection")
            time.sleep(web_driver.three_second)
            select = Select(enrollment_group)
            select.select_by_index(1)

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
            # save_btn.click()
            time.sleep(5)

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
            # ***************************************Enrollment Process end here**********************
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_03.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_03_failed.png")
                return False
            else:
                return True
        except Exception as ex:

            self.logger.error(f"test_TC_IE_01 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_03_Exception.png")
            return False

        finally:
            self.click_on_logout_button()


    def Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_and_adding_the_required_details_for_the_same_along_with_expiry_date_and_time_range(self):
        try:

            self.logger.info("************* test_TC_IE_04 started  **************")
            login().login_to_cloud_if_not_done_with_user_credentials(self.d,Read_Identify_and_Enroll_Components().get_approver_to_login(),Read_Identify_and_Enroll_Components().get_password_to_login())

            self.status.clear()

            time.sleep(web_driver.two_second)
            link = self.explicit_wait(10, "XPATH",
                                      Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset2\\img2.png"
            self.upload_image(file_path)

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
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            expiration_date = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().get_expiration_date_xpath())
            time.sleep(web_driver.one_second)
            expiration_date.send_keys(Keys.CONTROL,'a')
            time.sleep(web_driver.one_second)
            expiration_date.send_keys(Keys.BACKSPACE)
            time.sleep(web_driver.one_second)
            self.expirirationdateTimeAMPM(expiration_date)



            enrollment_basis = self.explicit_wait(10, "XPATH",
                                                  Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(),
                                                  self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)
            time.sleep(web_driver.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(2)
            time.sleep(web_driver.two_second)


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


            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH,
                                                Read_Identify_and_Enroll_Components().reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)



            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
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
            # save_btn.click()
            time.sleep(5)

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
            # ***************************************Enrollment Process end here**********************
            # self.delete_enrollment()
            # self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_04.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_04_failed.png")
                return False
            else:
                return True
        except Exception as ex:

            self.logger.error(f"test_TC_IE_04 got an exception as: {ex}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_04_Exception.png")
            return False
        finally:
            self.click_on_logout_button()


    def verify_user_able_delete_again_enrolling_same(self):
        try:
                self.logger.info("************* test_TC_IE_06 started  **************")
                # self.verify_portal_login()
                login().login_to_cloud_if_not_done(self.d)
                self.status.clear()
                time.sleep(web_driver.two_second)
                self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                            .identify_and_enroll_link_by_xpath(), self.d)
                link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                            .identify_and_enroll_link_by_xpath(), self.d)
                self.d.execute_script("arguments[0].click();", link)
                self.logger.info(f"clicked on Identify and enroll link")
                time.sleep(web_driver.two_second)
                img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset2\\img8.png"
                self.upload_image_not_enrolled(img_path)
                self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
                identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

                self.d.execute_script("arguments[0].click();", identify_enroll_btn)
                self.logger.info(f"Clicked on Identify and Enroll button")
                wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .identifying_photo_wait_by_xpath())
                count = 0
                while wait_icon.is_displayed():
                        if count > 15:
                         break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
                # ***************************************Enrollment Process start here**********************
                time.sleep(web_driver.two_second)
                self.click_on_enroll_for_already_enrolled()
                enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                       .enrollment_basis_by_xpath(), self.d)
                select = Select(enrollment_basis)
                select.select_by_index(1)
                time.sleep(web_driver.two_second)
                # self.Select_Enrollment_Group(3)
                enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
                select = Select(enrollment_group)
                select.select_by_index(3)
                time.sleep(web_driver.two_second)
                region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
                time.sleep(web_driver.two_second)
                region_btn.click()
                time.sleep(web_driver.two_second)
                region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
                edge_name = Read_Identify_and_Enroll_Components().edge_name()
                for i in range(len(region_names)):
                    if edge_name in region_names[i].text:
                        region_names[i].click()
                        break
                save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
                save_btn.click()
                time.sleep(web_driver.two_second)

                location_store = self.d.find_element(By.XPATH,
                                                     Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
                location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

                case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .case_subject_inpt_bx_by_xpath())
                case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

                date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().date_incident_inpt_bx_by_xpath())
                time.sleep(web_driver.one_second)
                self.dateTimeAMPM(date_incident)

                time.sleep(web_driver.one_second)

                reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .reported_loss_inpt_bx_by_xpath())
                reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

                action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .action_inpt_bx_by_xpath())
                action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
                self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                .add_details_save_btn_by_xpath(), self.d)
                save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .add_details_save_btn_by_xpath())
                if save_btn.is_displayed():
                     self.status.append(True)
                else:
                     self.status.append(False)
                save_btn.click()
                self.logger.info("Enrollment details filled and save btn is clicked")
                time.sleep(web_driver.one_second)

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

                title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                             add_details_panel_title_panel())
                for x in title:
                     if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                             add_details_panel_validation().lower():
                         self.status.append(False)
                time.sleep(2)
                self.delete_enrollment()


            # ***************************************Enrollment Process end here**********************
                self.close_all_panel_one_by_one()
                self.click_on_logout_button()
                self.logger.info(f"status: {self.status}")
                if False in self.status:
                     self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_1.png")
                     self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_1_failed.png")
                     return False
                else:
                     return True
        except Exception as ex:
             self.logger.error(f"test_TC_IE_1 got an exception as: {ex}")
             self.d.save_screenshot(
                 f"{self.screenshots_path}\\test_TC_IE_1_Exception.png")
             return False

    def Verify_for_above_25_enrolled_subject_region_edges_are_properly_assigned(self):
        global region
        try:
            self.logger.info("enrollment module testcases started")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            Enrollment_link = self.d.find_element(By.XPATH,Read_Identify_and_Enroll_Components().Enrollment_link())
            Enrollment_link.click()
            self.logger.info("clicking on enrollment link")
            time.sleep(web_driver.one_second)

            region_names_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().region_names_by_xpath())
            expected_region_name = Read_Identify_and_Enroll_Components().read_region_data()
            for region in region_names_list:
                self.logger.info(f"actual region name is {region.text}")
                if region.text == expected_region_name:
                    self.logger.info("actual and expected regions are same")
                    self.status.append(True)
                else:
                    self.logger.info("actual and expected  regions are not same")
                    self.status.append(False)
                if False in self.status:
                    return False
                else:
                    return True
        except Exception as ex:
            print(ex.args)
        finally:
            logout().logout_from_core(self.d)

    def Verify_for_above_25_enrolled_subject_reported_loss_are_properly_assigned(self):
         try:
            self.logger.info("identify  enroll tc started")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)


            Enrollment_details_dict = self.Read_user_from_json()
            enrollment_link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().Enrollment_link())
            enrollment_link.click()

            x = Read_Identify_and_Enroll_Components().read_reported_loss_values_from_ini()
            enrollment_reported_loss = x.split(',')
            self.logger.info(f"eg list: {enrollment_reported_loss}")

            search_dropdown = self.d.find_element(By.XPATH,Read_Identify_and_Enroll_Components().search_dropdow_on_enrollment())
            search_dropdown.click()
            self.logger.info("search dropdown is clicked")
            time.sleep(web_driver.one_second)
            read_case_subject_from_ini = Read_Identify_and_Enroll_Components().case_subject_inpt_bx_by_xpath()
            read_case_sub = read_case_subject_from_ini.split(',')
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().case_subject_xpath())
            for i in read_case_subject_from_ini:
                case_subject.clear()
                case_subject.send_keys(i)
                time.sleep(web_driver.one_second)
                search_button = self.d.find_element(By.XPATH,Read_Identify_and_Enroll_Components().search_button())
                search_button.click()
                self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().list_of_enrollments_by_xpath(),self.d)
                en_list = self.d.find_elements(By.XPATH,Read_Identify_and_Enroll_Components().list_of_enrollments_by_xpath())
                for x in range(len(en_list)):

                    tribar_button = self.d.find_elements(By.XPATH,Read_Identify_and_Enroll_Components().select_tribar_button_on_enrollment_panel())
                    tribar_button[i].click()
                    self.logger.info("clicking on tribar button")
                    time.sleep(web_driver.one_second)
                    details_button = self.d.find_elements(By.XPATH,Read_Identify_and_Enroll_Components().details_button())
                    details_button[i].click()
                    self.logger.info("clicking on details button")
                    time.sleep(web_driver.one_second)
                    reported_loss = self.d.find_element(By.XPATH,Read_Identify_and_Enroll_Components().reported_loss_value_xpath())
                    rl=reported_loss.text
                    if rl == Enrollment_details_dict["Enrollment_details"][x]["case_subject"]:
                        self.status.append(True)
                    else:
                        self.status.append(False)
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

    def Verify_user_is_able_to_enroll_the_person_by_uploading_the_image_and_adding_the_required_details_for_the_same(self):
        try:
            self.logger.info("************* test_TC_IE_05 started  **************")
            # self.verify_portal_login()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset2\\img3.png"
            self.upload_image_not_enrolled(img_path)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting fir wait icon, count: {count}")
            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(2)
            time.sleep(web_driver.two_second)


            enrollment_group = self.d.find_element(By.XPATH,
                                                   Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(2)
            time.sleep(web_driver.two_second)

            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.two_second)
            region_btn.click()
            time.sleep(web_driver.two_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            date_incident = self.d.find_element(By.XPATH,
                                                Read_Identify_and_Enroll_Components().date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.one_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.one_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_details_save_btn_by_xpath(), self.d)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)

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

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)
            time.sleep(2)
            self.delete_enrollment()

            # ***************************************Enrollment Process end here**********************
            self.close_all_panel_one_by_one()
            # self.click_on_logout_button()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_5.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_5_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_5 got an exception as: {ex}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_5_Exception.png")
            return False
        finally:
            self.click_on_logout_button()

    def Verify_user_is_able_to_see_the_possible_ranked_match_index_when_uploading_the_above_same_image_with_or_without_crop(self):
        try:
            self.logger.info("************* test_TC_IE_06 started  **************")
            # # self.verify_portal_login()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            file_path = f"{self.ie_file_path}\\ab\\1821_20220526-124517.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            expected_ranked_match_index_txt = Read_Identify_and_Enroll_Components() \
                .identify_results_ranked_match_index_text_validation().lower()

            ranked_match_index_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .identify_results_ranked_match_index_by_xpath())
            time.sleep(web_driver.two_second)
            actual_ranked_match_index_txt = ranked_match_index_ele.text.lower()
            self.logger.info(f"Expected data = {expected_ranked_match_index_txt}")
            self.logger.info(f"Actual data = {actual_ranked_match_index_txt}")
            if expected_ranked_match_index_txt == actual_ranked_match_index_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            exclamation_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_exclamation_symbol_by_xpath())
            if exclamation_icon.is_displayed():
                self.logger.info(f"exclamation_icon is visible")
                self.status.append(True)
            else:
                self.logger.info(f"exclamation_icon is not visible")
                self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_06.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_06_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_06 got an exception as: {ex}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_06_exception.png")
            return False
        finally:
            self.click_on_logout_button()


    def Verify_user_is_able_enroll_the_person_which_is_delete_one_delete_and_enrolling_again_person_should_be_same(self):
        try:
            self.logger.info("************* test_TC_IE_08 started  **************")
            # # self.verify_portal_login()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset2\\img4.png"
            self.upload_image_not_enrolled(img_path)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting fir wait icon, count: {count}")
            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)
            time.sleep(web_driver.two_second)


            enrollment_group = self.d.find_element(By.XPATH,
                                                   Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(2)
            time.sleep(web_driver.two_second)

            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.two_second)
            region_btn.click()
            time.sleep(web_driver.two_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            date_incident = self.d.find_element(By.XPATH,
                                                Read_Identify_and_Enroll_Components().date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.one_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.one_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_details_save_btn_by_xpath(), self.d)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)

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

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)
            time.sleep(2)
            self.delete_enrollment()

            # ***************************************Enrollment Process end here**********************
            self.close_all_panel_one_by_one()

            self.Create_New_Enrollment_using_Identify_and_Enroll()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_08.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_08_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"test_TC_IE_08 got an exception as: {ex}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_08_Exception.png")
            return False
        finally:
           self.click_on_logout_button()


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































































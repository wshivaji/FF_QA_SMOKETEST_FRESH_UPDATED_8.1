import time
from pathlib import Path
import pyautogui
from selenium.webdriver.common.by import By
from All_Config_Packages._00_deployment_manager_config_file.deployment_manager_read_ini import DeploymentManager_Read_ini
from All_Config_Packages._1_Portal_Login_Module_Config_Files.Portal_Login_Page_Read_INI import Portal_login_page_read_ini
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.keys import Keys
from Base_Package.Login_Logout_Ops import login
import random

class Deployment_Manager_Page_Pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def clear_main(self, id_name):
        self.d.find_element("id", id_name).send_keys(Keys.CONTROL + "a")
        self.d.find_element("id", id_name).send_keys(Keys.DELETE)

    def dm_log_out(self):
        self.d.find_element("xpath", "(//*[name()='svg'][@role='presentation'])[2]").click()
        self.logger.info("logging out")
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "(//li[normalize-space()='Logout'])[1]").click()
        self.logger.info("logged out from dm")
        time.sleep(web_driver.two_second)

    def register_login_dm(self):
        if self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url()):
            # login().login_to_dm_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.logger.info("Register Login Status: Passed")
        else:
            # login().login_to_dm_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            self.logger.info("A user has been already registered")
            self.logger.info("Directed to login page")
            # click on login
            self.d.find_element(By.LINK_TEXT, "Login").click()
            self.register_login_dm_details()
            self.logger.info("Register Login Status: Passed")

    def register_login_dm_details(self):
        try:
            # login
            self.d.find_element("id", "username").send_keys(DeploymentManager_Read_ini().get_mail())
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "password").send_keys(Portal_login_page_read_ini().get_portal_login_password())
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "password").send_keys(Keys.ENTER)
            time.sleep(web_driver.two_second)
            self.d.get(DeploymentManager_Read_ini().get_reg_login_link_url())
            self.d.refresh()
            time.sleep(3)
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_02_exception_Login_Failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_02_exception_Login_Failed.png")
            self.logger.error(f"TC_DM_02_exception_Login_Failed got an exception as: {e}")

    def dm_mini_window(self):
        try:
            self.d.find_element(By.CLASS_NAME, "jss347").click()
            time.sleep(web_driver.two_second)
            self.logger.info("Mini Window Status: Passed")
        except Exception as e:
            self.logger.error(
                f"screenshot file path: {self.screenshots_path}\\TC_DM_exception_mini_window_status_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_exception_mini_window_status_failed.png")
            self.logger.error(f"TC_DM_exception_mini_window_status_failed got an exception as: {e}")

    def domain_license(self):
        # licences status
        self.d.find_element("xpath",
                                 "(.//*[normalize-space(text()) and normalize-space(.)='License Status'])[1]/following::*[name()='svg'][1]").click()
        # customer id
        time.sleep(web_driver.two_second)
        self.clear_main("customerId")
        self.d.find_element("id", "customerId").send_keys(DeploymentManager_Read_ini().get_licences())
        time.sleep(web_driver.two_second)
        # save
        self.d.find_element("xpath",
                                 "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::span[2]").click()
        self.explicit_wait(250, "XPATH", "(//div[@role='alertdialog'])[1]", self.d)
        self.logger.info("Licenses status: Passed")

    def domain_url(self):
        # domain status
        self.d.find_element("xpath",
                                 "(.//*[normalize-space(text()) and normalize-space(.)='Domain Status'])[1]/following::*[name()='svg'][1]").click()
        time.sleep(web_driver.two_second)
        if DeploymentManager_Read_ini().get_domain_id() == str(3):
            # edit
            self.d.find_element("xpath", "//div[@id='domain-menu']/div[2]/ul/li").click()
            time.sleep(web_driver.two_second)
            # domain name (recommended)
            self.d.find_element("xpath",
                                     "(.//*[normalize-space(text()) and normalize-space(.)='Domain Name (recommended)'])[1]/following::p[1]").click()
            time.sleep(web_driver.two_second)
            # click on domain name and select
            self.clear_main("domainName")
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "domainName").send_keys(DeploymentManager_Read_ini().get_domain_name())
            time.sleep(web_driver.two_second)
            # save
            self.d.find_element("xpath",
                                     "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::span[2]").click()
            # edit
            self.d.find_element("xpath", "(//*[name()='svg'][@role='presentation'])[8]").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//li[normalize-space()='Upload Custom Certificate'])[1]").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(// input[@ id='enabled'])[1]").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//span[normalize-space()='Upload Certificate'])[1]").click()
            time.sleep(web_driver.two_second)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(web_driver.two_second)
            self.d.find_element(By.ID, "certUpload").send_keys(DeploymentManager_Read_ini().get_domain_certificate())
            time.sleep(web_driver.two_second)
            self.clear_main("certPassword")
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "certPassword").send_keys(DeploymentManager_Read_ini().get_domain_certificate_password())
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, "(//span[normalize-space()='Upload'])[1]").click()
            time.sleep(web_driver.two_second)
            self.explicit_wait(250, "XPATH", "(//div[@role='alertdialog'])[1]", self.d)
        if DeploymentManager_Read_ini().get_domain_id() == str(2):
            # edit
            self.d.find_element("xpath", "//div[@id='domain-menu']/div[2]/ul/li").click()
            time.sleep(web_driver.two_second)
            # domain name (recommended)
            self.d.find_element("xpath",
                                     "(.//*[normalize-space(text()) and normalize-space(.)='Domain Name (recommended)'])[1]/following::p[1]").click()
            time.sleep(web_driver.two_second)
            # click on domain name and select
            self.clear_main("domainName")
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "domainName").send_keys(DeploymentManager_Read_ini().get_domain_name())
            time.sleep(web_driver.two_second)
            # save
            self.d.find_element("xpath",
                                     "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::span[2]").click()
            self.explicit_wait(250, "XPATH", "(//div[@role='alertdialog'])[1]", self.d)
        elif DeploymentManager_Read_ini().get_domain_id() == str(1):
            # edit
            self.d.find_element("xpath", "//div[@id='domain-menu']/div[2]/ul/li").click()
            time.sleep(web_driver.two_second)
            # IP address
            self.d.find_element("xpath",
                                     "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]").click()
            time.sleep(web_driver.two_second)
            # select IP
            self.d.find_element("xpath", "(//div[@id='select-ipAddress'])[1]").click()
            time.sleep(web_driver.two_second)
            # select IP
            self.d.find_element("xpath", "/html[1]/body[1]/div[3]/div[2]/ul[1]/li[1]").click()
            time.sleep(web_driver.two_second)
            # save
            self.d.find_element("xpath",
                                     "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::span[2]").click()
            self.explicit_wait(250, "XPATH", "(//div[@role='alertdialog'])[1]", self.d)
        else:
            self.logger.info("Please Select Valid Domain Settings")
        self.logger.info("Domain Status: Passed")

    def core_deployment(self):
        time.sleep(3)
        # deployment wizard
        self.d.find_element("xpath",
                            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[2]/a[1]/div[1]").click()
        # core
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath",
                            "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]").click()
        # next
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath",
                            "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/button[1]/span[1]").click()

        # select camera
        # next
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath",
                            "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/button[1]/span[1]").click()

        # enter portal settings
        # username
        time.sleep(web_driver.two_second)
        self.d.find_element("id", "standard-username").send_keys(Portal_login_page_read_ini().get_valid_login_username())
        # password
        time.sleep(web_driver.two_second)
        self.d.find_element("id", "standard-adornment-password").send_keys(Portal_login_page_read_ini().get_portal_login_password())
        # confirm password
        time.sleep(web_driver.two_second)
        self.d.find_element("id", "standard-adornment-password-confirmation").send_keys(Portal_login_page_read_ini().get_portal_login_password())
        # mail
        time.sleep(web_driver.two_second)
        self.d.find_element("id", "standard-email").send_keys(DeploymentManager_Read_ini().get_mail())
        # timezone
        time.sleep(web_driver.two_second)
        self.d.find_element("id", "select-timezone").click()
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "//div[@id='menu-timezone']/div[2]/ul/li[61]").click()
        # next
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "//div[@id='root']/div/main/div[2]/div[3]/div/button/span").click()

        # enter system settings
        time.sleep(web_driver.two_second)
        # # self.clear_main("name")
        # # self.d.find_element("xpath", "(//input[@id='name'])[1]").send_keys("Dmart_India")
        # time.sleep(web_driver.two_second)
        self.d.find_element("id", "select-timezone").click()
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "//div[@id='menu-timezone']/div[2]/ul/li[61]").click()
        # next
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "//div[@id='root']/div/main/div[2]/div[3]/div/button/span").click()

        # deploy
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath",
                            "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/button[1]").click()
        time.sleep(web_driver.two_second)
        self.explicit_wait(500, "XPATH", "(//h6[normalize-space()='Operational'])[1]", self.d)
        self.logger.info("Deployment Wizard status: Passed")

    def dashboard(self):
        # analytics/dashboard
        self.d.find_element("xpath", "(//button[@aria-label='Edit'])[4]").click()
        # # analytic enable
        # time.sleep(DELAY)
        # driver.find_element("id", "analyticsEnabled").click()
        # dashboard enable
        time.sleep(web_driver.two_second)
        self.d.find_element("id", "dashboardEnabled").click()
        # # include masked faces
        time.sleep(web_driver.two_second)
        self.d.find_element("id", "countMaskedFaces").click()
        # dashboard refresh interval
        time.sleep(web_driver.two_second)
        # self.d.find_element("id", "select-dashboardRefreshIntervalSelect").click()
        # time.sleep(web_driver.two_second)
        #
        # if DeploymentManager_Read_ini().get_dashboard_refresh_interval() == "30 Seconds":
        #     time.sleep(web_driver.two_second)
        #     self.d.find_element("xpath",
        #                         "//div[@id='menu-dashboardRefreshIntervalSelect']/div[2]/ul/li[{0}]".format(
        #                             int(1))).click()
        # elif DeploymentManager_Read_ini().get_dashboard_refresh_interval() == "1 minutes":
        #     time.sleep(web_driver.two_second)
        #     self.d.find_element("xpath",
        #                         "//div[@id='menu-dashboardRefreshIntervalSelect']/div[2]/ul/li[{0}]".format(
        #                             int(2))).click()
        # elif DeploymentManager_Read_ini().get_dashboard_refresh_interval() == "2 minutes":
        #     time.sleep(web_driver.two_second)
        #     self.d.find_element("xpath",
        #                         "//div[@id='menu-dashboardRefreshIntervalSelect']/div[2]/ul/li[{0}]".format(
        #                             int(3))).click()
        # elif DeploymentManager_Read_ini().get_dashboard_refresh_interval() == "3 minutes":
        #     time.sleep(web_driver.two_second)
        #     self.d.find_element("xpath",
        #                         "//div[@id='menu-dashboardRefreshIntervalSelect']/div[2]/ul/li[{0}]".format(
        #                             int(4))).click()
        # elif DeploymentManager_Read_ini().get_dashboard_refresh_interval() == "5 minutes":
        #     time.sleep(web_driver.two_second)
        #     self.d.find_element("xpath",
        #                         "//div[@id='menu-dashboardRefreshIntervalSelect']/div[2]/ul/li[{0}]".format(
        #                             int(5))).click()
        # elif DeploymentManager_Read_ini().get_dashboard_refresh_interval() == "10 minutes":
        #     time.sleep(web_driver.two_second)
        #     self.d.find_element("xpath",
        #                         "//div[@id='menu-dashboardRefreshIntervalSelect']/div[2]/ul/li[{0}]".format(
        #                             int(6))).click()
        # elif DeploymentManager_Read_ini().get_dashboard_refresh_interval() == "15 minutes":
        #     time.sleep(web_driver.two_second)
        #     self.d.find_element("xpath",
        #                         "//div[@id='menu-dashboardRefreshIntervalSelect']/div[2]/ul/li[{0}]".format(
        #                             int(7))).click()
        # else:
        #     self.logger.info("Please verify 'Dashboard Refresh Interval'")

        # visitor search time select
        time.sleep(web_driver.two_second)
        self.d.find_element("id", "select-visitorSearchTimeSelect").click()
        time.sleep(web_driver.two_second)
        if DeploymentManager_Read_ini().get_visitor_search_select() == "1 hour":
            self.d.find_element("xpath", "//div[@id='menu-visitorSearchTimeSelect']/div[2]/ul/li[{0}]".format(
                DeploymentManager_Read_ini().get_visitor_search_select().split()[0])).click()
        else:
            self.d.find_element("xpath", "//div[@id='menu-visitorSearchTimeSelect']/div[2]/ul/li[{0}]".format(
                DeploymentManager_Read_ini().get_visitor_search_select().split()[0])).click()
        time.sleep(web_driver.two_second)
        # save
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "/html[1]/body[1]/div[2]/div[2]/div[1]/div[3]/div[1]/button[1]").click()
        time.sleep(web_driver.two_second)
        self.d.refresh()
        self.d.refresh()
        self.explicit_wait(250, "XPATH", "(//div[@role='alertdialog'])[1]", self.d)
        self.explicit_wait(250, "XPATH", "(//*[name()='svg'][@title='Operational'])[1]", self.d)
        self.logger.info("Analytics/Dashboard Platform Setting status: Passed")

    def email_configure(self):
        # Email
        self.d.find_element("xpath", "(//button[@aria-label='Edit'])[6]").click()
        self.logger.info("email ")
        # enable
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "(//input[@id='enabled'])[1]").click()
        self.logger.info("Enabled ")
        # host
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "(//input[@id='host'])[1]").send_keys("smtp.office365.com")
        self.logger.info("host")
        # sender
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "(//input[@id='from'])[1]").send_keys("qanotifications@facefirst.com")
        self.logger.info("sender ")
        # subject
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "(//input[@id='subject'])[1]").send_keys("Events-Notification")
        self.logger.info("subject ")
        # enable crendentials
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "(//input[@id='useCredentials'])[1]").click()
        self.logger.info("enable credentials ")
        # smpt username
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "(//input[@id='smtpUsername'])[1]").send_keys("qanotifications@facefirst.com")
        self.logger.info("smtp username")
        # smpt password
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "(//input[@id='smtpPassword'])[1]").send_keys("QAT3$t!nd!@QA23")
        self.logger.info("smtp password")
        # FMC Body Template
        self.d.find_element("xpath", "//textarea[@id=\"fcmBodyTemplate\"]").click()
        self.d.find_element("xpath", "//textarea[@id=\"fcmBodyTemplate\"]").send_keys("ABC")
        self.logger.info("FMC Body Text")
        # save
        time.sleep(web_driver.two_second)
        self.d.find_element("xpath", "/html[1]/body[1]/div[2]/div[2]/div[1]/div[3]/div[1]/button[1]").click()
        self.logger.info("save btn")
        self.d.refresh()
        self.d.refresh()
        self.explicit_wait(250, "XPATH", "(//div[@role='alertdialog'])[1]", self.d)
        self.explicit_wait(250, "XPATH", "(//*[name()='svg'][@title='Operational'])[1]", self.d)
        self.logger.info("Email Platform Setting status: Passed")

    def visitor_log_retention(self):
        ## visitors
        try:
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//button[@aria-label='Edit'])[15]").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "//input[@value='']").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "//input[@value='']").click()
            # visitor clustering time
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "select-stitchingTimeSelect").click()
            time.sleep(web_driver.two_second)
            if DeploymentManager_Read_ini().get_visitor_clustering_time() == "1 minute":
                VISITOR_CLUSTERING_TIME_li = 1
                time.sleep(web_driver.two_second)
                self.d.find_element("xpath", "//div[@id='menu-stitchingTimeSelect']/div[2]/ul/li[{0}]".format(
                    VISITOR_CLUSTERING_TIME_li)).click()
            elif DeploymentManager_Read_ini().get_visitor_clustering_time() == "5 minutes":
                VISITOR_CLUSTERING_TIME_li = 2
                time.sleep(web_driver.two_second)
                self.d.find_element("xpath", "//div[@id='menu-stitchingTimeSelect']/div[2]/ul/li[{0}]".format(
                    VISITOR_CLUSTERING_TIME_li)).click()
            elif DeploymentManager_Read_ini().get_visitor_clustering_time() == "10 minutes":
                VISITOR_CLUSTERING_TIME_li = 3
                time.sleep(web_driver.two_second)
                self.d.find_element("xpath", "//div[@id='menu-stitchingTimeSelect']/div[2]/ul/li[{0}]".format(
                    VISITOR_CLUSTERING_TIME_li)).click()
            elif DeploymentManager_Read_ini().get_visitor_clustering_time() == "15 minutes":
                VISITOR_CLUSTERING_TIME_li = 4
                time.sleep(web_driver.two_second)
                self.d.find_element("xpath", "//div[@id='menu-stitchingTimeSelect']/div[2]/ul/li[{0}]".format(
                    VISITOR_CLUSTERING_TIME_li)).click()
            elif DeploymentManager_Read_ini().get_visitor_clustering_time() == "30 minutes":
                VISITOR_CLUSTERING_TIME_li = 5
                time.sleep(web_driver.two_second)
                self.d.find_element("xpath", "//div[@id='menu-stitchingTimeSelect']/div[2]/ul/li[{0}]".format(
                    VISITOR_CLUSTERING_TIME_li)).click()

            # visitor clustering threshold
            time.sleep(web_driver.two_second)
            self.clear_main("stitchingThreshold")
            self.d.find_element("id", "stitchingThreshold").send_keys(DeploymentManager_Read_ini().get_visitor_clustering_threshold())
            # visitor blurring
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//input[@type='checkbox'])[2]").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//input[@type='checkbox'])[2]").click()
            # visitor log retention
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "select-retentionSelect").click()
            time.sleep(web_driver.two_second)
            visitorlogretention = 19
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "//div[@id='menu-retentionSelect']/div[2]/ul/li[{0}]".format(
                visitorlogretention)).click()
            time.sleep(web_driver.two_second)
            # save
            self.d.find_element("xpath", "/html[1]/body[1]/div[2]/div[2]/div[1]/div[3]/div[1]/button[1]").click()
            self.d.refresh()
            self.d.refresh()
            time.sleep(web_driver.two_second)
            self.explicit_wait(250, "XPATH", "(//div[@role='alertdialog'])[1]", self.d)
            self.explicit_wait(250, "XPATH", "(//*[name()='svg'][@title='Operational'])[1]", self.d)
            self.logger.info("Visitors Platform Setting status: Passed")
        except Exception as ex:
            print(ex)
            self.logger.info(ex.args)


    def verify_user_directs_to_user_register_page_and_create_a_user_by_providing_details(self):
        try:
            self.logger.info("********** TC_DM_01 started ********")
            self.logger.info("verify_user_directs_to_user_register_page_and_create_a_user_by_providing_details")
            self.status.clear()
            self.d.get(DeploymentManager_Read_ini().get_register_url())
            self.d.maximize_window()
            for i in range(4):
                pyautogui.hotkey('ctrl', '-')
                time.sleep(0.5)
            time.sleep(web_driver.two_second)

            try:
                self.d.find_element("id", "name").send_keys(Portal_login_page_read_ini().get_valid_login_username())
                time.sleep(web_driver.two_second)
                self.d.find_element("id", "email").send_keys(DeploymentManager_Read_ini().get_mail())
                time.sleep(web_driver.two_second)
                self.d.find_element("id", "newPassword").send_keys(
                    Portal_login_page_read_ini().get_portal_login_password())
                time.sleep(web_driver.two_second)
                self.d.find_element("id", "passwordConfirmation").send_keys(
                    Portal_login_page_read_ini().get_portal_login_password())
                time.sleep(web_driver.two_second)
                self.d.find_element("xpath", "//div[@id='root']/div/main/div[2]/div/button/span").click()
                time.sleep(web_driver.two_second)
                # self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                # self.d.refresh()
                # time.sleep(3)
                self.logger.info("Register Status: Passed")
            except Exception as e:
                self.logger.info("Register Status: Failed (Duplicate Registration Not Allowed")

            self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
            self.d.refresh()
            time.sleep(3)
            login_msg = self.d.find_element("xpath", "(//h6[normalize-space()='Login'])[1]")
            print(login_msg.text)
            actual_login_text = login_msg.text
            expected_login_test = "Login"
            if actual_login_text == expected_login_test:
                self.status.append(True)
            else:
                self.status.append(False)

            if False in self.status:
                return False
            else:
                return True

        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_01_exception_register_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_01_exception_register_failed.png")
            self.logger.error(f"TC_DM_01_exception_register_failed got an exception as: {e}")

    def verify_user_login_to_deployment_manager_using_create_user_credentials(self):
        try:
            self.logger.info("********** TC_DM_02 started ********")
            self.logger.info("verify_user_login_to_deployment_manager_using_create_user_credentials")
            self.register_login_dm()
            self.dm_mini_window()
            home_msg = self.d.find_element("xpath", "(//h6[normalize-space()='Home'])[1]")
            print(home_msg.text)
            actual_home_text = home_msg.text
            expected_home_test = "Home"
            if actual_home_text == expected_home_test:
                self.status.append(True)
            else:
                self.status.append(False)
            self.dm_log_out()
            if False in self.status:
                return False
            else:
                return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_02_exception_register_login_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_02_exception_register_login_failed.png")
            self.logger.error(f"TC_DM_02_exception_register_login_failed got an exception as: {e}")

    def enter_license_under_license_status_in_deployment_manager_settings(self):
        try:
            self.logger.info("********** TC_DM_03 started ********")
            self.logger.info("enter_license_under_license_status_in_deployment_manager_settings")
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.domain_license()
            self.dm_log_out()
            return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_03_exception_license_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_03_exception_license_failed.png")
            self.logger.error(f"TC_DM_03_exception_license_failed got an exception as: {e}")

    def verify_configuring_the_domain_url_using_recommended_letsencrypt_or_ssl_certificate(self):
        try:
            self.logger.info("********** TC_DM_04 started ********")
            self.logger.info("verify_configuring_the_domain_url_using_recommended_letsencrypt_or_ssl_certificate")
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.domain_url()
            self.dm_log_out()
            return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_04_exception_domain_url_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_04_exception_domain_url_failed.png")
            self.logger.error(f"TC_DM_04_exception_domain_url_failed got an exception as: {e}")

    def verify_the_deployment_options_of_core_edges_from_deployment_wizard(self):
        try:
            self.logger.info("********** TC_DM_05 started ********")
            self.logger.info("verify_the_deployment_options_of_core_edges_from_deployment_wizard")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            time.sleep(web_driver.two_second)
            # deployment wizard
            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[2]/a[1]/div[1]").click()
            core_msg = self.d.find_element("xpath", "(//li[@class='jss138'])[1]//div//div//span")
            print(core_msg.text)
            actual_core = core_msg.text
            expected_core = "Core"
            if actual_core == expected_core:
                self.status.append(True)
            else:
                self.status.append(False)
            edge_msg = self.d.find_element("xpath", "(//li[@class='jss138'])[2]//div//div//span")
            print(edge_msg.text)
            actual_edge = edge_msg.text
            expected_edge = "Edge"
            if actual_edge == expected_edge:
                self.status.append(True)
            else:
                self.status.append(False)
            self.dm_log_out()
            if False in self.status:
                return False
            else:
                return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_05_exception_deployment_option_core_&_edge_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_05_exception_deployment_option_core_&_edge_failed.png")
            self.logger.error(f"TC_DM_05_exception_deployment_option_core_&_edge_failed got an exception as: {e}")

    def verify_deployment_of_core_by_providing_required_details_for_core_deployment(self):
        try:
            self.logger.info("********** TC_DM_06 started ********")
            self.logger.info("verify_deployment_of_core_by_providing_required_details_for_core_deployment")
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.core_deployment()
            self.dm_log_out()
            return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_06_exception_core_deployment_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_06_exception_core_deployment_failed.png")
            self.logger.error(f"TC_DM_06_exception_core_deployment_failed got an exception as: {e}")

    def verify_web_portal_url_and_login_to_web_portal_with_core_credentials_and_verify_login_successful(self):
        try:
            self.logger.info("********** TC_DM_07 started ********")
            self.logger.info("verify_web_portal_url_and_login_to_web_portal_with_core_credentials_and_verify_login_successful")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.d.find_element("xpath", "//span[contains(text(), 'Portal URL')]/parent::div/p/a").click()
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[1])
            self.d.find_element(By.ID, "login-username").send_keys(Portal_login_page_read_ini().get_valid_login_username())
            time.sleep(web_driver.two_second)
            self.d.find_element(By.ID, "login-password").send_keys(Portal_login_page_read_ini().get_portal_login_password())
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "login-password").send_keys(Keys.ENTER)
            time.sleep(5)
            login().accept_terms_and_conditions_for_login_for_new_user(self.d)
            time.sleep(2)
            cloud_msg = self.d.find_element("xpath", "(//div[@id='start-logo-container'])[1]//div//p")
            print(cloud_msg.text)
            actual_cloud_msg = cloud_msg.text
            expected_cloud_msg = "CLOUD MENU"
            if actual_cloud_msg == expected_cloud_msg:
                self.status.append(True)
                self.logger.info("Portal Login Status: Passed")
            else:
                self.status.append(False)
                self.logger.info("Portal Login Status: Failed")
            self.d.find_element("xpath", "(//div[@ng-click='logout()'])[1]").click()
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[0])
            self.dm_log_out()
            self.logger.info("Portal Login By Clicking On DM URL Status: Passed")
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                return False
            else:
                return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_07_exception_portal_login_by_click_on_dm_url_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_07_exception_portal_login_by_click_on_dm_url_failed.png")
            self.logger.error(f"TC_DM_07_exception_portal_login_by_click_on_dm_url_failed got an exception as: {e}")

    def verify_enable_disable_dashboard_enabled_should_make_appear_and_disappear_the_dashboard_on_web_portal(self):
        try:
            self.logger.info("********** TC_DM_08 started ********")
            self.logger.info("verify_enable_disable_dashboard_enabled_should_make_appear_and_disappear_the_dashboard_on_web_portal")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.dashboard()
            self.d.find_element("xpath", "//span[contains(text(), 'Portal URL')]/parent::div/p/a").click()
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[1])

            self.d.find_element(By.ID, "login-username").send_keys(
                Portal_login_page_read_ini().get_valid_login_username())
            time.sleep(web_driver.two_second)
            self.d.find_element(By.ID, "login-password").send_keys(
                Portal_login_page_read_ini().get_portal_login_password())
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "login-password").send_keys(Keys.ENTER)
            time.sleep(5)
            login().accept_terms_and_conditions_for_login_for_new_user(self.d)
            time.sleep(2)
            cloud_msg = self.d.find_element("xpath", "(//div[@id='start-logo-container'])[1]//div//p")
            print(cloud_msg.text)
            actual_cloud_msg = cloud_msg.text
            self.logger.info(f"actual msg: {actual_cloud_msg}")
            expected_cloud_msg = "CLOUD MENU"
            self.logger.info(f"expected msg: {expected_cloud_msg}")
            if actual_cloud_msg == expected_cloud_msg:
                self.status.append(True)
                self.logger.info("Portal Login Status: matched")
            else:
                self.status.append(False)
                self.logger.info("Portal Login Status: not matched")
            self.d.refresh()
            self.d.refresh()
            dashboard_msg = self.d.find_element("xpath", "(//p[normalize-space()='Insights Dashboard'])[1]")
            print(dashboard_msg.text)
            self.logger.info(f"dashboard msg: {dashboard_msg.text}")
            actual_dashboard_msg = dashboard_msg.text

            expected_dashboard_msg = "Insights Dashboard"
            self.logger.info(f"expected: {expected_dashboard_msg}")
            if actual_dashboard_msg == expected_dashboard_msg:
                self.status.append(True)
                self.logger.info("Insights Dashboard Disabled Status: Passed")
            else:
                self.status.append(False)
                self.logger.info("Insights Dashboard Disabled Status: Failed")

            self.d.find_element("xpath", "(//div[@ng-click='logout()'])[1]").click()
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[0])
            self.dashboard()

            self.d.find_element("xpath", "//span[contains(text(), 'Portal URL')]/parent::div/p/a").click()
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[1])
            self.d.find_element(By.ID, "login-username").send_keys(
                Portal_login_page_read_ini().get_valid_login_username())
            time.sleep(web_driver.two_second)
            self.d.find_element(By.ID, "login-password").send_keys(
                Portal_login_page_read_ini().get_portal_login_password())
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "login-password").send_keys(Keys.ENTER)
            time.sleep(5)
            cloud_msg = self.d.find_element("xpath", "(//div[@id='start-logo-container'])[1]//div//p")
            print(cloud_msg.text)
            actual_cloud_msg = cloud_msg.text

            self.logger.info(actual_cloud_msg)
            self.logger.info(expected_dashboard_msg)
            if actual_cloud_msg == expected_cloud_msg:
                self.status.append(True)
                self.logger.info("Portal Login Status: matched")
            else:
                self.status.append(False)
                self.logger.info("Portal Login Status: not matched")
            self.d.refresh()
            self.d.refresh()
            dashboard_msg = self.d.find_element("xpath", "(//p[normalize-space()='Insights Dashboard'])[1]")
            print(dashboard_msg.text)
            actual_dashboard_msg = dashboard_msg.text
            expected_dashboard_msg = "Insights Dashboard"
            # if actual_dashboard_msg == expected_dashboard_msg:
            #     self.status.append(True)
            #     self.logger.info("Insights Dashboard Status: matched")
            # else:
            #     self.status.append(False)
            #     self.logger.info("Insights Dashboard Status: not matched")

            self.d.find_element("xpath", "(//div[@ng-click='logout()'])[1]").click()
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[0])
            self.dm_log_out()
            self.logger.info("Enable & Disable Dashboard Status: Passed")
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                return False
            else:
                return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_08_exception_enable_disable_dashboard_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_08_exception_enable_disable_dashboard_failed.png")
            self.logger.error(f"TC_DM_08_exception_enable_disable_dashboard_failed got an exception as: {e}")

    def verify_notification_email_configuration_by_proving_host_and_sender_credentials(self):
        try:
            self.logger.info("********** TC_DM_09 started ********")
            self.logger.info("verify_notification_email_configuration_by_proving_host_and_sender_credentials")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.email_configure()
            self.d.refresh()
            self.d.refresh()
            time.sleep(web_driver.two_second)
            mail_msg = self.d.find_element("xpath", "(//div[@class='jss137 jss140 jss145 jss147'])[7]//div//p")
            print(mail_msg.text)
            self.logger.info(mail_msg.text)
            if mail_msg.text != "Disabled":
                self.status.append(True)
            else:
                self.status.append(False)
            self.dm_log_out()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                return False
            else:
                return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_09_exception_mail_configuration_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_09_exception_mail_configuration_failed.png")
            self.logger.error(f"TC_DM_09_exception_mail_configuration_failed got an exception as: {e}")

    def verify_visitor_log_retention_set_to_maximum_clustering_time_under_platform_settings(self):
        try:
            self.logger.info("********** TC_DM_10 started ********")
            self.logger.info("verify_visitor_log_retention_set_to_maximum_clustering_time_under_platform_settings")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.visitor_log_retention()
            retention_msg = self.d.find_element("xpath", "(//div[@class='jss158'])[22]//p")
            print(retention_msg.text)
            self.logger.info(f"actual: {retention_msg.text}")
            self.logger.info("expected: clustering at 0.8 every 5 minute(s), keep visitors for 13 weeks")
            if retention_msg.text == "clustering at 0.8 every 5 minute(s), keep visitors for 13 weeks":
                self.status.append(True)
            else:
                self.status.append(False)
            self.dm_log_out()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                return False
            else:
                return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_10_visitor_log_retention_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_10_visitor_log_retention_failed.png")
            self.logger.error(f"TC_DM_10_visitor_log_retention_failed got an exception as: {e}")

    def verify_enrollment_quality_guard_is_enable_with_proper_settings(self):
        try:
            self.logger.info("********** TC_DM_11 started ********")
            self.logger.info("verify_enrollment_quality_guard_is_enable_with_proper_settings")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.d.find_element("xpath", "(//button[@aria-label='Edit'])[7]").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//input[@id='enabled'])[1]").click()
            time.sleep(web_driver.two_second)
            self.clear_main("countEvents")
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "countEvents").send_keys(DeploymentManager_Read_ini().get_enrollment_quality_guard_count_events_method())
            time.sleep(web_driver.two_second)
            self.clear_main("duration")
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "duration").send_keys(DeploymentManager_Read_ini().get_enrollment_quality_guard_duration_method())
            time.sleep(web_driver.two_second)
            self.clear_main("countEdges")
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "countEdges").send_keys(DeploymentManager_Read_ini().get_enrollment_quality_guard_count_edges_method())
            time.sleep(web_driver.two_second)
            # save
            self.d.find_element("xpath", "/html[1]/body[1]/div[2]/div[2]/div[1]/div[3]/div[1]/button[1]").click()
            self.d.refresh()
            self.d.refresh()
            time.sleep(web_driver.two_second)
            self.explicit_wait(250, "XPATH", "(//div[@role='alertdialog'])[1]", self.d)
            self.explicit_wait(250, "XPATH", "(//*[name()='svg'][@title='Operational'])[1]", self.d)
            self.logger.info("Enrollment Quality Guard Platform Setting status: Passed")
            self.dm_log_out()
            return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_11_enrollments_quality_guard_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_11_enrollments_quality_guard_failed.png")
            self.logger.error(f"TC_DM_11_enrollments_quality_guard_failed got an exception as: {e}")

    def verify_session_time_is_set_to_maximum_value_under_platform_settings(self):
        try:
            self.logger.info("********** TC_DM_12 started ********")
            self.logger.info("verify_session_time_is_set_to_maximum_value_under_platform_settings")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.d.find_element("xpath", "(//button[@aria-label='Edit'])[13]").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//div[@id='select-inactivityTimeoutSelect'])[1]").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//li[normalize-space()='24 hours'])[1]").click()
            time.sleep(web_driver.two_second)
            # save
            self.d.find_element("xpath", "/html[1]/body[1]/div[2]/div[2]/div[1]/div[3]/div[1]/button[1]").click()
            self.d.refresh()
            self.d.refresh()
            time.sleep(web_driver.two_second)
            self.explicit_wait(250, "XPATH", "(//div[@role='alertdialog'])[1]", self.d)
            self.explicit_wait(250, "XPATH", "(//*[name()='svg'][@title='Operational'])[1]", self.d)
            self.logger.info("Session Time-Out Platform Setting status: Passed")
            self.dm_log_out()
            return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_12_session_timeout_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_12_session_timeout_failed.png")
            self.logger.error(f"TC_DM_12_session_timeout_failed got an exception as: {e}")

    def launch_swagger_and_click_on_authorize_btn_and_login_with_core_credentials(self):
        try:
            self.logger.info("********** TC_DM_EDGE_01 started ********")
            self.logger.info("launch_swagger_and_click_on_authorize_btn_and_login_with_core_credentials")
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            login().login_to_dm_if_not_done(self.d)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.d.execute_script("window.open()")
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[1])
            time.sleep(web_driver.two_second)
            # Swagger URL
            self.d.get(DeploymentManager_Read_ini().get_swagger_url_method())
            time.sleep(web_driver.two_second)
            # authorize
            self.d.find_element("xpath", "(//button[@class='btn authorize unlocked'])[1]").click()
            time.sleep(web_driver.two_second)
            # username
            self.d.find_element("xpath", "(//input[@name='username'])[1]").send_keys(Portal_login_page_read_ini().get_valid_login_username())
            time.sleep(web_driver.two_second)
            # password
            self.d.find_element("xpath", "(//input[@name='password'])[1]").send_keys(Portal_login_page_read_ini().get_portal_login_password())
            time.sleep(web_driver.two_second)
            # submit
            self.d.find_element("xpath", "(//button[@type='submit'])[1]").click()
            time.sleep(web_driver.two_second)
            # close
            self.d.find_element("xpath", "(//button[normalize-space()='Close'])[1]").click()
            time.sleep(web_driver.two_second)
            self.d.execute_script("window.close()")
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[0])
            time.sleep(web_driver.two_second)
            self.logger.info("JSON import Status: Passed")
            self.dm_log_out()
            return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_01_swagger_authorize_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_01_swagger_authorize_failed.png")
            self.logger.error(f"TC_DM_01_swagger_authorize_failed got an exception as: {e}")

    def upload_json_file_to_swagger_api_regions_to_create_org_hierarchy_structure(self):
        try:
            self.logger.info("********** TC_DM_EDGE_02 started ********")
            self.logger.info("upload_json_file_to_swagger_api_regions_to_create_org_hierarchy_structure")
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            # login().login_to_dm_if_not_done(self.d)
            self.register_login_dm_details()
            self.dm_mini_window()
            self.d.execute_script("window.open()")
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[1])
            time.sleep(web_driver.two_second)
            # Swagger URL
            self.d.get(DeploymentManager_Read_ini().get_swagger_url_method())
            time.sleep(web_driver.two_second)
            # authorize
            self.d.find_element("xpath", "(//button[@class='btn authorize unlocked'])[1]").click()
            time.sleep(web_driver.two_second)
            # username
            self.d.find_element("xpath", "(//input[@name='username'])[1]").send_keys(Portal_login_page_read_ini().get_valid_login_username())
            time.sleep(web_driver.two_second)
            # password
            self.d.find_element("xpath", "(//input[@name='password'])[1]").send_keys(Portal_login_page_read_ini().get_portal_login_password())
            time.sleep(web_driver.two_second)
            # submit
            self.d.find_element("xpath", "(//button[@type='submit'])[1]").click()
            time.sleep(web_driver.two_second)
            # close
            self.d.find_element("xpath", "(//button[normalize-space()='Close'])[1]").click()
            time.sleep(web_driver.two_second)
            # try it out
            self.d.find_element("xpath", "//span[@data-path=\"/api/Regions/import\"]/parent::div/parent::button").click()
            time.sleep(web_driver.two_second)
            # choose file
            self.d.find_element("xpath", "(//button[normalize-space()='Try it out'])[1]").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//input[@type='file'])[1]").clear()
            # time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//input[@type='file'])[1]").send_keys(f'{Path(__file__).parent.parent.parent}\\{DeploymentManager_Read_ini().get_swagger_json_file_method()}')
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//button[normalize-space()='Execute'])[1]").click()
            time.sleep(10)
            jstatus = self.d.find_element("xpath", "(//td[@class='response-col_status'])[1]")
            expected1 = "Undocumented"
            expected = "200"
            if expected1 == jstatus.text:
                print("Please import the JSON file")
                self.logger.info("Please import the JSON file")
            elif expected == jstatus.text:
                print("Imported the JSON successfuly")
                self.logger.info("Imported the JSON successfuly")
                self.logger.info("JSON import Status: Passed")
            else:
                print(jstatus.text)
                self.logger.info(jstatus.text)
            time.sleep(web_driver.two_second)
            self.d.execute_script("window.close()")
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[0])
            time.sleep(web_driver.two_second)
            self.dm_log_out()
            return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_02_upload_json_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_02_upload_json_failed.png")
            self.logger.error(f"TC_DM_02_upload_json_failed got an exception as: {e}")

    def enter_one_of_edge_name_in_search_filter_textbox_and_verify_that_edge_name_is_filtering_below_it(self):
        try:
            self.logger.info("********** TC_DM_EDGE_03 started ********")
            self.logger.info("enter_one_of_edge_name_in_search_filter_textbox_and_verify_that_edge_name_is_filtering_below_it")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            # login().login_to_dm_if_not_done(self.d)
            self.register_login_dm_details()
            self.dm_mini_window()
            # system edge name place
            self.d.find_element("xpath", "(//input[@placeholder='Search'])[1]").send_keys(DeploymentManager_Read_ini().get_search_filter_text_box_method())
            time.sleep(web_driver.two_second)
            # system search
            self.d.find_element("xpath", "(//img[@class='btn'])[2]").click()
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            edge_msg = self.d.find_element("xpath", "(//a[@role='button'])[1]//div//ul//li[1]")
            print(edge_msg.text)
            actual_edge = edge_msg.text
            expected_edge = DeploymentManager_Read_ini().get_search_filter_text_box_method()
            self.logger.info(f"actual: {actual_edge}")
            self.logger.info(f"expected: {expected_edge}")
            if actual_edge == expected_edge:
                self.status.append(True)
            else:
                self.status.append(False)
            self.dm_log_out()
            self.logger.info("Enter one of edge name in search filter textbox and verify that edge name is filtering below it Status: Passed")
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                return False
            else:
                return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_03_enter_one_of_edge_name_in_search_filter_textbox_and_verify_that_edge_name_is_filtering_below_it_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_03_enter_one_of_edge_name_in_search_filter_textbox_and_verify_that_edge_name_is_filtering_below_it_failed.png")
            self.logger.error(f"TC_DM_03_enter_one_of_edge_name_in_search_filter_textbox_and_verify_that_edge_name_is_filtering_below_it_failed got an exception as: {e}")

    def before_deploying_all_edges_click_on_second_edge_which_is_to_be_deploy_go_to_diployment_wizards_and_verify_selected_edge_name_is_visible_for_deployment(self):
        try:
            self.logger.info("********** TC_DM_EDGE_04 started ********")
            self.logger.info("before_deploying_all_edges_click_on_second_edge_which_is_to_be_deploy_go_to_diployment_wizards_and_verify_selected_edge_name_is_visible_for_deployment")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            # login().login_to_dm_if_not_done(self.d)
            self.register_login_dm_details()
            self.dm_mini_window()
            # system edge name place
            self.d.find_element("xpath", "(//input[@placeholder='Search'])[1]").send_keys(DeploymentManager_Read_ini().get_2nd_edge_search_filter_text_box_method())
            time.sleep(web_driver.two_second)
            # system search
            self.d.find_element("xpath", "(//img[@class='btn'])[2]").click()
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            edge_msg = self.d.find_element("xpath", "(//a[@role='button'])[1]//div//ul//li[1]")
            print(edge_msg.text)
            # select the first edge
            self.d.find_element("xpath", "(//a[@role='button'])[1]").click()
            time.sleep(web_driver.two_second)
            # deployment wizard
            self.d.find_element("xpath", "//a[@href='/deploy']//div[@role='button']").click()
            time.sleep(web_driver.two_second)
            # edge
            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[2]/span[1]").click()
            time.sleep(web_driver.two_second)
            # next
            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/button[1]/span[1]").click()
            time.sleep(web_driver.two_second)
            # select system for edge
            self.explicit_wait(5, "XPATH", "(//input[@type='checkbox'])[1]", self.d)
            self.d.find_element("xpath", "(//input[@type='checkbox'])[1]").click()
            time.sleep(web_driver.two_second)
            # next
            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/button[1]/span[1]").click()
            time.sleep(web_driver.two_second)
            # select camera
            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/button[1]/span[1]").click()
            time.sleep(web_driver.two_second)
            # enter system settings
            # select region
            self.d.find_element("xpath", "(//span[normalize-space()='Edit'])[1]").click()
            time.sleep(web_driver.two_second)
            # search region hierarchy
            self.d.find_element("xpath", "(//input[@placeholder='Search'])[1]").click()
            self.d.find_element("xpath", "(//input[@placeholder='Search'])[1]").send_keys(DeploymentManager_Read_ini().get_single_edge_region_method())
            time.sleep(web_driver.two_second)
            regionHierarchy = self.d.find_elements("xpath", "(//div[@role='treeitem'])")
            for j in regionHierarchy:
                if DeploymentManager_Read_ini().get_single_edge_region_method() in j.text:
                    self.d.find_element("xpath", "(//span[normalize-space()='{0}'])[1]".format(j.text)).click()
                    time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "(//span[normalize-space()='Save'])[1]").click()
            time.sleep(web_driver.two_second)
            # timezone
            self.d.find_element("id", "select-timezone").click()
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "//div[@id='menu-timezone']/div[2]/ul/li[61]").click()
            time.sleep(web_driver.two_second)
            # next
            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/button[1]/span[1]").click()
            time.sleep(web_driver.two_second)
            # deploy
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "//button[@type=\"button\"]/span[contains(text(), 'Deploy')]").click()
            time.sleep(web_driver.two_second)
            self.explicit_wait(250, "XPATH", "(//h6[normalize-space()='Operational'])[1]", self.d)
            self.logger.info("Deployment Wizard For Single Edge Status: Passed")

            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]").click()
            # add manually
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "//div[@id='simple-menu']/div[2]/ul/li[{0}]".format(int(1))).click()
            # rtsp stream
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath",
                                "(.//*[normalize-space(text()) and normalize-space(.)='RS'])[1]/following::span[1]").click()
            # value
            time.sleep(web_driver.two_second)
            self.clear_main("rtsp")
            self.d.find_element("id", "rtsp").send_keys("rtsp://:" + DeploymentManager_Read_ini().get_single_edge_rtsp_port_method())
            # save
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath",
                                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::span[2]").click()
            self.explicit_wait(250, "XPATH", "(//div[@role='alertdialog'])[1]", self.d)
            self.logger.info("Add Camera Manually Status: Passed")

            # manual camera setting
            # 3 dot
            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/button[1]").click()
            # edit
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "/html[1]/body[1]/div[2]/div[2]/ul[1]/li[1]").click()
            # geolocation
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath",
                                "(.//*[normalize-space(text()) and normalize-space(.)='Basic Information'])[1]/following::span[4]").click()
            #
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys(
                Keys.CONTROL + "a")
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys(
                Keys.DELETE)
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath",
                                "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys(DeploymentManager_Read_ini().get_single_edge_camera_location_method())
            self.explicit_wait(250, "XPATH", "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/input[1]", self.d)
            # basic info
            self.d.find_element("xpath",
                                "(.//*[normalize-space(text()) and normalize-space(.)='Discovered By'])[1]/following::span[2]").click()
            # description
            time.sleep(web_driver.two_second)
            self.clear_main("description")
            self.d.find_element("id", "description").send_keys(DeploymentManager_Read_ini().get_single_edge_rtsp_port_method())
            self.logger.info(f"Description: {DeploymentManager_Read_ini().get_single_edge_rtsp_port_method()}")
            # enable camera
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath", "//input[@value='checkedA']/parent::span/parent::span").click()
            self.logger.info("clicked enable toggle btn")
            # save
            time.sleep(web_driver.two_second)
            self.d.find_element("xpath",
                                "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::span[2]").click()
            self.explicit_wait(250, "XPATH", "(//h6[normalize-space()='Warning'])[1]", self.d)
            self.logger.info("Camera Configured Status: Passed")

            self.dm_log_out()
            return True
        except Exception as e:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_DM_04_deployment_wizard_for_single_edge_failed.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_DM_04_deployment_wizard_for_single_edge_failed.png")
            self.logger.error(f"TC_DM_04_deployment_wizard_for_single_edge_failed got an exception as: {e}")

    def verify_user_able_click_on_manage_user_menu_add_user_screen_should_appears(self):
        try:
            self.logger.info("********** TC_DM_13 started ********")
            self.logger.info("verify_user_able_click_on_manage_user_menu_add_user_screen_should_appears")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            user_btn = self.explicit_wait(5, "XPATH", "//div[@title='Manage Users']/parent::div/parent::a", self.d)

            if user_btn.is_displayed():
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
                user_btn.click()
                time.sleep(web_driver.two_second)
                add_user_btn = self.explicit_wait(5, "XPATH", "//span[contains(text(), 'Add User')]/parent::button/parent::a", self.d)
                if add_user_btn.is_displayed():
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
                    self.status.append(True)
                else:
                    self.status.append(False)
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
            else:
                self.status.append(False)
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
            self.logger.info(f"status: {self.status}")
            self.dm_log_out()
            if False in self.status:
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\tc_dm_13.png")
            self.logger.error(f"tc_dm_13_verify_user_able_click_on_manage_user_menu_add_user_screen_should_appears got an exception as: {ex}")

    def on_add_user_screen_verify_add_user_button_is_visible_verify_text_on_the_button(self):
        try:
            self.logger.info("********** TC_DM_14 started ********")
            self.logger.info("on_add_user_screen_verify_add_user_button_is_visible_verify_text_on_the_button")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            user_btn = self.explicit_wait(5, "XPATH", "//div[@title='Manage Users']/parent::div/parent::a", self.d)

            if user_btn.is_displayed():
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
                user_btn.click()
                time.sleep(web_driver.two_second)
                add_user_btn = self.explicit_wait(5, "XPATH", "//span[contains(text(), 'Add User')]/parent::button/parent::a", self.d)
                if add_user_btn.is_displayed():
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
                    self.status.append(True)
                    self.logger.info(f"add user btn text: {add_user_btn.text}")
                    if add_user_btn.text == 'ADD USER':
                        self.status.append(True)
                    else:
                        self.status.append(False)
                else:
                    self.status.append(False)
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
            else:
                self.status.append(False)
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
            self.logger.info(f"status: {self.status}")
            self.dm_log_out()
            if False in self.status:
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\tc_dm_14.png")
            self.logger.error(f"TC_DM_14_on_add_user_screen_verify_add_user_button_is_visible_verify_text_on_the_button got an exception as: {ex}")

    def create_a_user_by_filling_all_fields(self):
        try:
            self.logger.info("********** TC_DM_15 started ********")
            self.logger.info("create_a_user_by_filling_all_fields")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            user_btn = self.explicit_wait(5, "XPATH", "//div[@title='Manage Users']/parent::div/parent::a", self.d)
            username = f"user{random.randint(1, 100)}"
            if user_btn.is_displayed():
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
                user_btn.click()
                time.sleep(web_driver.two_second)
                add_user_btn = self.explicit_wait(5, "XPATH", "//span[contains(text(), 'Add User')]/parent::button/parent::a", self.d)
                if add_user_btn.is_displayed():
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
                    self.status.append(True)
                    self.logger.info(f"add user btn text: {add_user_btn.text}")
                    add_user_btn.click()
                    time.sleep(web_driver.two_second)
                    new_user_details_panel = self.explicit_wait(5, "XPATH", "//h6[contains(text(), 'Fill out the form below to create a new user')]", self.d)
                    if new_user_details_panel.is_displayed():
                        self.status.append(True)
                        self.logger.info(f"new user details panel heading: {new_user_details_panel.is_displayed()}")
                        name = self.explicit_wait(5, "XPATH", "//input[@id='name']", self.d)
                        email = self.explicit_wait(5, "XPATH", "//input[@id='email']", self.d)
                        password = self.explicit_wait(5, "XPATH", "//input[@id='newPassword']", self.d)
                        confirm_pass = self.explicit_wait(5, "XPATH", "//input[@id='passwordConfirmation']", self.d)
                        name.send_keys(f'{username}')
                        email.send_keys(f'{username}@gmail.com')
                        password.send_keys('Right_1r1s')
                        confirm_pass.send_keys('Right_1r1s')
                        time.sleep(web_driver.two_second)
                        create_user_btn = self.explicit_wait(5, "XPATH", "//span[contains(text(), 'Create User')]/parent::button", self.d)
                        if create_user_btn.is_displayed():
                            self.logger.info(f"create user btn visible: {create_user_btn.is_displayed()}")
                            self.status.append(True)
                            create_user_btn.click()
                            time.sleep(web_driver.two_second)
                            list_of_users = self.d.find_elements(By.XPATH, "//tr/th")
                            if len(list_of_users) > 0:
                                self.logger.info(f"user list count: {len(list_of_users)}")
                                for x in list_of_users:
                                    self.logger.info(f"user name: {x.text}")
                                    if x.text == username:
                                        self.status.append(True)

                            else:
                                self.status.append(False)
                                self.logger.info(f"user list count: {len(list_of_users)}")
                        else:
                            self.status.append(False)
                            self.logger.info(f"create user btn visible: {create_user_btn.is_displayed()}")
                    else:
                        self.status.append(False)
                        self.logger.info(f"new user details panel heading: {new_user_details_panel.is_displayed()}")

                else:
                    self.status.append(False)
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
            else:
                self.status.append(False)
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
            self.logger.info(f"status: {self.status}")
            self.dm_log_out()
            if False in self.status:
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\tc_dm_15.png")
            self.logger.error(f"TC_DM_15_create_a_user_by_filling_all_fields got an exception as: {ex}")

    def verify_created_user_should_be_visible_on_add_user_screen(self):
        try:
            self.logger.info("********** TC_DM_16 started ********")
            self.logger.info("verify_created_user_should_be_visible_on_add_user_screen")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            user_btn = self.explicit_wait(5, "XPATH", "//div[@title='Manage Users']/parent::div/parent::a", self.d)
            username = f"user{random.randint(1, 100)}"
            if user_btn.is_displayed():
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
                user_btn.click()
                time.sleep(web_driver.two_second)
                add_user_btn = self.explicit_wait(5, "XPATH", "//span[contains(text(), 'Add User')]/parent::button/parent::a", self.d)
                if add_user_btn.is_displayed():
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
                    self.status.append(True)
                    self.logger.info(f"add user btn text: {add_user_btn.text}")
                    add_user_btn.click()
                    time.sleep(web_driver.two_second)
                    new_user_details_panel = self.explicit_wait(5, "XPATH", "//h6[contains(text(), 'Fill out the form below to create a new user')]", self.d)
                    if new_user_details_panel.is_displayed():
                        self.status.append(True)
                        self.logger.info(f"new user details panel heading: {new_user_details_panel.is_displayed()}")
                        name = self.explicit_wait(5, "XPATH", "//input[@id='name']", self.d)
                        email = self.explicit_wait(5, "XPATH", "//input[@id='email']", self.d)
                        password = self.explicit_wait(5, "XPATH", "//input[@id='newPassword']", self.d)
                        confirm_pass = self.explicit_wait(5, "XPATH", "//input[@id='passwordConfirmation']", self.d)
                        name.send_keys(f'{username}')
                        email.send_keys(f'{username}@gmail.com')
                        password.send_keys('Right_1r1s')
                        confirm_pass.send_keys('Right_1r1s')
                        time.sleep(web_driver.two_second)
                        create_user_btn = self.explicit_wait(5, "XPATH", "//span[contains(text(), 'Create User')]/parent::button", self.d)
                        if create_user_btn.is_displayed():
                            self.logger.info(f"create user btn visible: {create_user_btn.is_displayed()}")
                            self.status.append(True)
                            create_user_btn.click()
                            time.sleep(web_driver.two_second)
                            list_of_users = self.d.find_elements(By.XPATH, "//tr/th")
                            if len(list_of_users) > 0:
                                self.logger.info(f"user list count: {len(list_of_users)}")
                                for x in list_of_users:
                                    self.logger.info(f"user name: {x.text}")
                                    if x.text == username:
                                        self.status.append(True)

                            else:
                                self.status.append(False)
                                self.logger.info(f"user list count: {len(list_of_users)}")
                        else:
                            self.status.append(False)
                            self.logger.info(f"create user btn visible: {create_user_btn.is_displayed()}")
                    else:
                        self.status.append(False)
                        self.logger.info(f"new user details panel heading: {new_user_details_panel.is_displayed()}")

                else:
                    self.status.append(False)
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
            else:
                self.status.append(False)
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
            self.logger.info(f"status: {self.status}")
            self.dm_log_out()
            if False in self.status:
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\tc_dm_16.png")
            self.logger.error(f"TC_DM_16_verify_created_user_should_be_visible_on_add_user_screen got an exception as: {ex}")

    def verify_after_filling_all_valid_inputs_create_user_button_is_enabled(self):
        try:
            self.logger.info("********** TC_DM_17 started ********")
            self.logger.info("verify_after_filling_all_valid_inputs_create_user_button_is_enabled")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            user_btn = self.explicit_wait(5, "XPATH", "//div[@title='Manage Users']/parent::div/parent::a", self.d)
            username = f"user{random.randint(1, 100)}"
            if user_btn.is_displayed():
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
                user_btn.click()
                time.sleep(web_driver.two_second)
                add_user_btn = self.explicit_wait(5, "XPATH", "//span[contains(text(), 'Add User')]/parent::button/parent::a", self.d)
                if add_user_btn.is_displayed():
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
                    self.status.append(True)
                    self.logger.info(f"add user btn text: {add_user_btn.text}")
                    add_user_btn.click()
                    time.sleep(web_driver.two_second)
                    new_user_details_panel = self.explicit_wait(5, "XPATH", "//h6[contains(text(), 'Fill out the form below to create a new user')]", self.d)
                    if new_user_details_panel.is_displayed():
                        self.status.append(True)
                        self.logger.info(f"new user details panel heading: {new_user_details_panel.is_displayed()}")
                        name = self.explicit_wait(5, "XPATH", "//input[@id='name']", self.d)
                        email = self.explicit_wait(5, "XPATH", "//input[@id='email']", self.d)
                        password = self.explicit_wait(5, "XPATH", "//input[@id='newPassword']", self.d)
                        confirm_pass = self.explicit_wait(5, "XPATH", "//input[@id='passwordConfirmation']", self.d)
                        name.send_keys(f'{username}')
                        email.send_keys(f'{username}@gmail.com')
                        password.send_keys('Right_1r1s')
                        confirm_pass.send_keys('Right_1r1s')
                        time.sleep(web_driver.two_second)
                        create_user_btn = self.explicit_wait(5, "XPATH", "//span[contains(text(), 'Create User')]/parent::button", self.d)
                        if create_user_btn.is_enabled():
                            self.logger.info(f"create user btn enabled: {create_user_btn.is_enabled()}")

                            self.status.append(True)
                            # # create_user_btn.click()
                            # # time.sleep(web_driver.two_second)
                            # # list_of_users = self.d.find_elements(By.XPATH, "//tr/th")
                            # # if len(list_of_users) > 0:
                            # #     self.logger.info(f"user list count: {len(list_of_users)}")
                            # #     for x in list_of_users:
                            # #         self.logger.info(f"user name: {x.text}")
                            # #         if x.text == username:
                            # #             self.status.append(True)
                            #
                            # else:
                            #     self.status.append(False)
                            #     self.logger.info(f"user list count: {len(list_of_users)}")
                        else:
                            self.status.append(False)
                            self.logger.info(f"create user btn enabled: {create_user_btn.is_enabled()}")
                    else:
                        self.status.append(False)
                        self.logger.info(f"new user details panel heading: {new_user_details_panel.is_displayed()}")

                else:
                    self.status.append(False)
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
            else:
                self.status.append(False)
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
            self.logger.info(f"status: {self.status}")
            self.dm_log_out()
            if False in self.status:
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\tc_dm_17.png")
            self.logger.error(f"TC_DM_17_verify_after_filling_all_valid_inputs_create_user_button_is_enabled got an exception as: {ex}")

    def verify_login_to_deployment_maanger_using_newely_created_dm_users(self):
        try:
            self.logger.info("********** TC_DM_16 started ********")
            self.logger.info("verify_created_user_should_be_visible_on_add_user_screen")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
            user_btn = self.explicit_wait(5, "XPATH", "//div[@title='Manage Users']/parent::div/parent::a", self.d)
            username = f"user{random.randint(1, 100)}"
            if user_btn.is_displayed():
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
                user_btn.click()
                time.sleep(web_driver.two_second)
                add_user_btn = self.explicit_wait(5, "XPATH", "//span[contains(text(), 'Add User')]/parent::button/parent::a", self.d)
                if add_user_btn.is_displayed():
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
                    self.status.append(True)
                    self.logger.info(f"add user btn text: {add_user_btn.text}")
                    add_user_btn.click()
                    time.sleep(web_driver.two_second)
                    new_user_details_panel = self.explicit_wait(5, "XPATH", "//h6[contains(text(), 'Fill out the form below to create a new user')]", self.d)
                    if new_user_details_panel.is_displayed():
                        self.status.append(True)
                        self.logger.info(f"new user details panel heading: {new_user_details_panel.is_displayed()}")
                        name = self.explicit_wait(5, "XPATH", "//input[@id='name']", self.d)
                        email = self.explicit_wait(5, "XPATH", "//input[@id='email']", self.d)
                        password = self.explicit_wait(5, "XPATH", "//input[@id='newPassword']", self.d)
                        confirm_pass = self.explicit_wait(5, "XPATH", "//input[@id='passwordConfirmation']", self.d)
                        name.send_keys(f'{username}')
                        email.send_keys(f'{username}@gmail.com')
                        password.send_keys('Right_1r1s')
                        confirm_pass.send_keys('Right_1r1s')
                        time.sleep(web_driver.two_second)
                        create_user_btn = self.explicit_wait(5, "XPATH", "//span[contains(text(), 'Create User')]/parent::button", self.d)
                        if create_user_btn.is_displayed():
                            self.logger.info(f"create user btn visible: {create_user_btn.is_displayed()}")
                            self.status.append(True)
                            create_user_btn.click()
                            time.sleep(web_driver.two_second)
                            list_of_users = self.d.find_elements(By.XPATH, "//tr/th")
                            if len(list_of_users) > 0:
                                self.logger.info(f"user list count: {len(list_of_users)}")
                                for x in list_of_users:
                                    self.logger.info(f"user name: {x.text}")
                                    if x.text == username:
                                        self.status.append(True)

                            else:
                                self.status.append(False)
                                self.logger.info(f"user list count: {len(list_of_users)}")
                        else:
                            self.status.append(False)
                            self.logger.info(f"create user btn visible: {create_user_btn.is_displayed()}")
                    else:
                        self.status.append(False)
                        self.logger.info(f"new user details panel heading: {new_user_details_panel.is_displayed()}")

                else:
                    self.status.append(False)
                    self.logger.info(f"add user btn is visible: {add_user_btn.is_displayed()}")
            else:
                self.status.append(False)
                self.logger.info(f"users btn on dm visible: {user_btn.is_displayed()}")
            self.logger.info(f"status: {self.status}")
            self.dm_log_out()
            self.verify_new_user_login_successful(f'{username}@gmail.com', 'Right_1r1s')
            self.verify_dm_home_page()
            self.dm_log_out()
            if False in self.status:
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\tc_dm_16.png")
            self.logger.error(f"TC_DM_16_verify_created_user_should_be_visible_on_add_user_screen got an exception as: {ex}")

    def verify_new_user_login_successful(self, email_username, password):
        try:
            self.d.find_element("id", "username").send_keys(email_username)
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "password").send_keys(password)
            time.sleep(web_driver.two_second)
            self.d.find_element("id", "password").send_keys(Keys.ENTER)
            time.sleep(web_driver.two_second)
            self.d.get(DeploymentManager_Read_ini().get_reg_login_link_url())
            self.d.refresh()
            time.sleep(3)
        except Exception as ex:
            print(ex.args)

    def verify_dm_home_page(self):
        try:
            time.sleep(web_driver.two_second)
            home_page_title = self.explicit_wait(5, "XPATH", "//h6[@id='appBarTitle']", self.d)
            if home_page_title.is_displayed():
                self.logger.info(f"home page title visible: {home_page_title.is_displayed()}")
                self.status.append(True)
            else:
                self.logger.info(f"home page title visible: {home_page_title.is_displayed()}")
                self.status.append(False)
        except Exception as ex:
            print(ex.args)

    def verify_user_able_to_receive_account_login_id_password_setting_link_credentials_to_registed_email_to_sign_in_on_ispring_portal(self):
        try:
            self.d.switch_to.new_window()
            self.d.get(DeploymentManager_Read_ini().ispring_login_url())
            time.sleep(web_driver.one_second)
            username_text_box = self.explicit_wait(5, "XPATH", "//input[@id='loginField']", self.d)
            if username_text_box.is_displayed():
                self.logger.info(f"uername textbox is visible: {username_text_box.is_displayed()}")
                username_text_box.send_keys(DeploymentManager_Read_ini().get_mail())
            else:
                self.logger.info(f"uername textbox is visible: {username_text_box.is_displayed()}")
            password_text_box = self.explicit_wait(5, "XPATH", "//input[@id='passwordField']", self.d)
            if password_text_box.is_displayed():
                self.logger.info(f"password textbox is visible: {password_text_box.is_displayed()}")
                password_text_box.send_keys("Right_1r1s")
            else:
                self.logger.info(f"password textbox is visible: {password_text_box.is_displayed()}")
            login_btn = self.explicit_wait(5, "XPATH", "//input[@type='submit']", self.d)
            if login_btn.is_displayed():
                self.logger.info(f"login btn visible: {login_btn.is_displayed()}")
                login_btn.click()
            else:
                self.logger.info(f"login btn visible: {login_btn.is_displayed()}")
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            got_it_btn = self.explicit_wait(5, "XPATH", "//button[@class='_jwZrnS _puUSrc _o8aqb0 _irpium _ONKU2Z _n_Vogz _wsTb6U _DdKph6']", self.d)
            if got_it_btn.is_displayed():
                self.logger.log(f"got it btn visible: {got_it_btn.is_displayed()}")
                got_it_btn.click()
            else:
                self.logger.log(f"got it btn visible: {got_it_btn.is_displayed()}")
        except Exception as ex:
            print(ex.args)

    def verify_on_deployment_manger_under_platform_settings_a_new_setting_training_system_settings_is_visible(self):
        try:
            self.logger.info("********** TC_DM_training_01 started ********")
            self.logger.info("verify_on_deployment_manger_under_platform_settings_a_new_setting_training_system_settings_is_visible")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
        except Exception as ex:
            print(ex.args)

    def verify_beside_training_system_settings_pencil_icon_is_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_DM_training_02 started ********")
            self.logger.info("verify_beside_training_system_settings_pencil_icon_is_visible_and_clickable")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
        except Exception as ex:
            print(ex.args)

    def click_on_pencil_icon_annual_training_system_access_window_should_appear(self):
        try:
            self.logger.info("********** TC_DM_training_03 started ********")
            self.logger.info("click_on_pencil_icon_annual_training_system_access_window_should_appear")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
        except Exception as ex:
            print(ex.args)

    def verify_training_acknowledgement_required_label_and_its_toggle_button_is_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_DM_training_04 started ********")
            self.logger.info("verify_training_acknowledgement_required_label_and_its_toggle_button_is_visible_and_clickable")
            self.status.clear()
            if not DeploymentManager_Read_ini().get_register_login_link_from_register_url() == self.d.current_url:
                self.d.get(DeploymentManager_Read_ini().get_register_login_link_from_register_url())
                time.sleep(web_driver.two_second)
            self.register_login_dm_details()
            self.dm_mini_window()
        except Exception as ex:
            print(ex.args)

    def login_to_facefirst_ispring_portal_with_valid_credentials(self):
        try:
            self.logger.info("********** TC_DM_training_02 started ********")
            self.logger.info("login_to_facefirst_ispring_portal_with_valid_credentials")
            self.d.switch_to.new_window()
            self.d.get(DeploymentManager_Read_ini().ispring_login_url())
            time.sleep(web_driver.one_second)
            username_text_box = self.explicit_wait(5, "XPATH", "//input[@id='loginField']", self.d)
            if username_text_box.is_displayed():
                self.logger.info(f"uername textbox is visible: {username_text_box.is_displayed()}")
                username_text_box.send_keys(DeploymentManager_Read_ini().get_mail())
            else:
                self.logger.info(f"uername textbox is visible: {username_text_box.is_displayed()}")
            password_text_box = self.explicit_wait(5, "XPATH", "//input[@id='passwordField']", self.d)
            if password_text_box.is_displayed():
                self.logger.info(f"password textbox is visible: {password_text_box.is_displayed()}")
                password_text_box.send_keys("Right_1r1s")
            else:
                self.logger.info(f"password textbox is visible: {password_text_box.is_displayed()}")
            login_btn = self.explicit_wait(5, "XPATH", "//input[@type='submit']", self.d)
            if login_btn.is_displayed():
                self.logger.info(f"login btn visible: {login_btn.is_displayed()}")
                login_btn.click()
            else:
                self.logger.info(f"login btn visible: {login_btn.is_displayed()}")
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            got_it_btn = self.explicit_wait(5, "XPATH", "//button[@class='_jwZrnS _puUSrc _o8aqb0 _irpium _ONKU2Z _n_Vogz _wsTb6U _DdKph6']", self.d)
            if got_it_btn.is_displayed():
                self.logger.log(f"got it btn visible: {got_it_btn.is_displayed()}")
                got_it_btn.click()
            else:
                self.logger.log(f"got it btn visible: {got_it_btn.is_displayed()}")
        except Exception as ex:
            print(ex.args)

    def verify_and_complete_the_courses_are_enlisted_on_facefirst_ispring_portal(self):
        try:
            self.logger.info("********** TC_DM_training_02 started ********")
            self.logger.info("login_to_facefirst_ispring_portal_with_valid_credentials")
            self.d.switch_to.new_window()
            self.d.get(DeploymentManager_Read_ini().ispring_login_url())
            time.sleep(web_driver.one_second)
            username_text_box = self.explicit_wait(5, "XPATH", "//input[@id='loginField']", self.d)
            if username_text_box.is_displayed():
                self.logger.info(f"uername textbox is visible: {username_text_box.is_displayed()}")
                username_text_box.send_keys(DeploymentManager_Read_ini().get_mail())
            else:
                self.logger.info(f"uername textbox is visible: {username_text_box.is_displayed()}")
            password_text_box = self.explicit_wait(5, "XPATH", "//input[@id='passwordField']", self.d)
            if password_text_box.is_displayed():
                self.logger.info(f"password textbox is visible: {password_text_box.is_displayed()}")
                password_text_box.send_keys("Right_1r1s")
            else:
                self.logger.info(f"password textbox is visible: {password_text_box.is_displayed()}")
            login_btn = self.explicit_wait(5, "XPATH", "//input[@type='submit']", self.d)
            if login_btn.is_displayed():
                self.logger.info(f"login btn visible: {login_btn.is_displayed()}")
                login_btn.click()
            else:
                self.logger.info(f"login btn visible: {login_btn.is_displayed()}")
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            got_it_btn = self.explicit_wait(5, "XPATH", "//button[@class='_jwZrnS _puUSrc _o8aqb0 _irpium _ONKU2Z _n_Vogz _wsTb6U _DdKph6']", self.d)
            if got_it_btn.is_displayed():
                self.logger.log(f"got it btn visible: {got_it_btn.is_displayed()}")
                got_it_btn.click()
            else:
                self.logger.log(f"got it btn visible: {got_it_btn.is_displayed()}")
        except Exception as ex:
            print(ex.args)


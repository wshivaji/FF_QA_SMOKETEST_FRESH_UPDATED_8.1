import configparser
from pathlib import Path

file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\1_Portal_Login_Module\\Data_From_INI\\Portal_Login_Page.ini"
print("configure filepath: ", file_path)
common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"


class Portal_login_page_read_ini:
    def __init__(self):
        self.config = configparser.RawConfigParser()

        self.common_test_data_config = configparser.RawConfigParser()
        self.common_test_data_config.read(common_test_data_ini_file_path)
        try:
            self.config.read(file_path)
        except Exception as ex:
            print(ex)

    def get_portal_url(self):
        try:
            portal_url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
            print("portal page url: ", portal_url)
            return portal_url
        except Exception as ex:
            print(ex)

    def get_dm_url(self):
        try:
            dm_login_url = self.common_test_data_config.get("Login_Logout_Data", "dm_login_url")
            print("DM page url: ", dm_login_url)
            return dm_login_url
        except Exception as ex:
            print(ex)

    def get_dm_username_txtbx_by_xpath(self):
        try:
            dm_username_txtbx_by_xpath = self.common_test_data_config.get("Login_Logout_Data", "dm_username_txtbx_by_xpath")
            print("DM page username txt box: ", dm_username_txtbx_by_xpath)
            return dm_username_txtbx_by_xpath
        except Exception as ex:
            print(ex)

    def get_dm_password_txtbx_by_xpath(self):
        try:
            dm_password_txtbx_by_xpath = self.common_test_data_config.get("Login_Logout_Data",
                                                                          "dm_password_txtbx_by_xpath")
            print("DM page password txt box: ", dm_password_txtbx_by_xpath)
            return dm_password_txtbx_by_xpath
        except Exception as ex:
            print(ex)

    def get_login_btn_on_dm_by_xpath(self):
        try:
            login_btn_on_dm_by_xpath = self.common_test_data_config.get("Login_Logout_Data",
                                                                          "login_btn_on_dm_by_xpath")
            print("login_btn_on_dm_by_xpath: ", login_btn_on_dm_by_xpath)
            return login_btn_on_dm_by_xpath
        except Exception as ex:
            print(ex)

    def get_edge_system_by_xpath(self):
        try:
            edge_system_by_xpath = self.common_test_data_config.get("Login_Logout_Data",
                                                                          "edge_system_by_xpath")
            print("edge_system_by_xpath: ", edge_system_by_xpath)
            return edge_system_by_xpath
        except Exception as ex:
            print(ex)

    def get_edit_link_by_xpath(self):
        try:
            edit_link_by_xpath = self.common_test_data_config.get("Login_Logout_Data",
                                                                          "edit_link_by_xpath")
            print("edit_link_by_xpath: ", edit_link_by_xpath)
            return edit_link_by_xpath
        except Exception as ex:
            print(ex)

    def get_root_region_name_on_dm_by_xpath(self):
        try:
            root_region_name_on_dm_by_xpath = self.common_test_data_config.get("Login_Logout_Data",
                                                                          "root_region_name_on_dm_by_xpath")
            print("root_region_name_on_dm_by_xpath: ", root_region_name_on_dm_by_xpath)
            return root_region_name_on_dm_by_xpath
        except Exception as ex:
            print(ex)

    def get_close_btn_on_welcome_dialog_by_xpath(self):
        try:
            close_btn_on_welcome_dialog_by_xpath = self.common_test_data_config.get("Login_Logout_Data",
                                                                          "close_btn_on_welcome_dialog_by_xpath")
            print("close_btn_on_welcome_dialog_by_xpath: ", close_btn_on_welcome_dialog_by_xpath)
            return close_btn_on_welcome_dialog_by_xpath
        except Exception as ex:
            print(ex)

    def get_portal_title(self):
        try:
            portal_title = self.common_test_data_config.get("Login_Logout_Data", "portal_title")
            print("portal title: ", portal_title)
            return portal_title
        except Exception as ex:
            print(ex)

    def get_advance_btn_by_xpath(self):
        try:
            advance_btn_by_xpath = self.common_test_data_config.get("Login_Logout_Data", "advance_btn_by_xpath")
            print("portal title: ", advance_btn_by_xpath)
            return advance_btn_by_xpath
        except Exception as ex:
            print(ex)

    def get_proceed_link_by_xpath(self):
        try:
            proceed_link_by_xpath = self.common_test_data_config.get("Login_Logout_Data", "proceed_link_by_xpath")
            print("portal title: ", proceed_link_by_xpath)
            return proceed_link_by_xpath
        except Exception as ex:
            print(ex)

    def get_face_first_company_logo_by_xpath(self):
        try:
            face_first_company_logo = self.config.get("Portal_Login_Page", "face_first_company_logo_by_xpath")
            print("face first logo on portal login page: ", face_first_company_logo)
            return face_first_company_logo
        except Exception as ex:
            print(ex)

    def get_dashboard_menu_by_xpath(self):
        try:
            dashboard_menu_by_xpath = self.config.get("Portal_Login_Page", "dashboard_menu_by_xpath")
            print("dashboard menu: ", dashboard_menu_by_xpath)
            return dashboard_menu_by_xpath
        except Exception as ex:
            print(ex)

    def get_portal_login_username_textbox_by_xpath(self):
        try:
            portal_login_username_texbox = self.config.get("Portal_Login_Page",
                                                           "portal_login_username_textbox_by_xpath")
            print("portal username textbox: ", portal_login_username_texbox)
            return portal_login_username_texbox
        except Exception as ex:
            print(ex)

    def get_valid_login_username(self):
        try:
            valid_login_username = self.common_test_data_config.get("Login_Logout_Data", "username")
            print("username: ", valid_login_username)
            return valid_login_username
        except Exception as ex:
            print(ex)

    def get_portal_login_username(self):
        try:
            portal_login_username = self.common_test_data_config.get("Login_Logout_Data", "username_for_blocking")
            print("username: ", portal_login_username)
            return portal_login_username
        except Exception as ex:
            print(ex)

    def get_portal_login_invalid_username(self):
        try:
            portal_login_invalid_username = self.common_test_data_config.get("Portal_Login_module_data", "portal_login_invalid_username")
            print("invalid username: ", portal_login_invalid_username)
            return portal_login_invalid_username
        except Exception as ex:
            print(ex)

    def get_portal_login_invalid_password(self):
        try:
            portal_login_invalid_password = self.common_test_data_config.get("Portal_Login_module_data", "portal_login_invalid_password")
            print("invalid password: ", portal_login_invalid_password)
            return portal_login_invalid_password
        except Exception as ex:
            print(ex)

    def get_portal_login_password_textbox_by_xpath(self):
        try:
            portal_login_password_textbox = self.config.get("Portal_Login_Page", "portal_login_password_textbox_by_xpath")
            print("portal password textbox: ", portal_login_password_textbox)
            return portal_login_password_textbox
        except Exception as ex:
            print(ex)

    def get_portal_login_password(self):
        try:
            portal_login_password = self.common_test_data_config.get("Login_Logout_Data", "password")
            print("password: ", portal_login_password)
            return portal_login_password
        except Exception as ex:
            print(ex)

    def get_cloud_menu_on_dashboard_by_xpath(self):
        try:
            dashboard_menu_container = self.config.get("Portal_Login_Page", "cloud_menu_on_dashboard_by_xpath")
            print("dashboard menu container: ", dashboard_menu_container)
            return dashboard_menu_container
        except Exception as ex:
            print(ex)

    def get_cloud_login_button_on_portal_by_xpath(self):
        try:
            cloud_login_button_on_portal = self.config.get("Portal_Login_Page", "cloud_login_button_on_portal_by_xpath")
            print("cloud login button on portal: ", cloud_login_button_on_portal)
            return cloud_login_button_on_portal
        except Exception as ex:
            print(ex)

    def get_face_first_copyright_text_by_xpath(self):
        try:
            face_first_copyright_text = self.config.get("Portal_Login_Page", "face_first_copyright_text_by_xpath")
            print("face first copyright text: ", face_first_copyright_text)
            return face_first_copyright_text
        except Exception as ex:
            print(ex)

    def get_expected_copyright_text(self):
        try:
            expected_copyright_text = self.common_test_data_config.get("Portal_Login_module_data", "copyright_text")
            print("expected copyright text: ", expected_copyright_text)
            return expected_copyright_text
        except Exception as ex:
            print(ex)

    def get_copyright_on_display_version_page(self):
        try:
            copyright_on_display_version_page = self.config.get("Portal_Login_Page", "copyright_on_display_version_page_by_xpath")
            print("copyright on version display page: ", copyright_on_display_version_page)
            return copyright_on_display_version_page
        except Exception as ex:
            print(ex)

    def get_WebAPI_text_on_version_info_by_xpath(self):
        try:
            WebAPI_text_on_version_info = self.config.get("Portal_Login_Page", "WebAPI_text_on_version_info_by_xpath")
            print("webapi text on version info: ", WebAPI_text_on_version_info)
            return WebAPI_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_expected_webapi_text_on_version_info(self):
        try:
            webapi_text_on_version_info = self.common_test_data_config.get("Portal_Login_module_data", "webapi_text_on_version_info")
            print("expected webapi text on version info: ", webapi_text_on_version_info)
            return webapi_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_Server_text_on_version_info_by_xpath(self):
        try:
            Server_text_on_version_info = self.config.get("Portal_Login_Page", "Server_text_on_version_info_by_xpath")
            print("server text on version info: ", Server_text_on_version_info)
            return Server_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_expected_server_text_on_version_info(self):
        try:
            server_text_on_version_info = self.common_test_data_config.get("Portal_Login_module_data", "server_text_on_version_info")
            print("expected server text on version info: ", server_text_on_version_info)
            return server_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_webapi_version_info_by_xpath(self):
        try:
            webapi_version_info = self.config.get("Portal_Login_Page", "webapi_version_info_by_xpath")
            print("webapi version info: ", webapi_version_info)
            return webapi_version_info
        except Exception as ex:
            print(ex)

    def get_expected_webapi_version_number(self):
        try:
            webapi_version_number = self.common_test_data_config.get("Portal_Login_Page_Data", "webapi_version_number")
            print("expected webapi version number: ", webapi_version_number)
            return webapi_version_number
        except Exception as ex:
            print(ex)

    def get_portal_version_number_by_xpath(self):
        try:
            actual_portal_version_number = self.config.get("Portal_Login_Page", "portal_version_number_by_xpath")
            print("portal version number: ", actual_portal_version_number)
            return actual_portal_version_number
        except Exception as ex:
            print(ex)

    def get_expected_portal_version_number(self):
        try:
            portal_version_number = self.common_test_data_config.get("Portal_Login_Page_Data", "portal_version_number")
            print("expected portal version number: ", portal_version_number)
            return portal_version_number
        except Exception as ex:
            print(ex)

    def get_close_button_on_version_info_by_xpath(self):
        try:
            close_button_on_version_info = self.config.get("Portal_Login_Page", "close_button_on_version_info_by_xpath")
            print("close button on version info: ", close_button_on_version_info)
            return close_button_on_version_info
        except Exception as ex:
            print(ex)

    def get_invalid_username_text_on_alert_by_xpath(self):
        try:
            invalid_username_text_on_alert = self.config.get("Portal_Login_Page", "invalid_username_text_on_alert_by_xpath")
            print("invalid username text on alert: ", invalid_username_text_on_alert)
            return invalid_username_text_on_alert
        except Exception as ex:
            print(ex)

    def get_expected_invalid_username_error_text(self):
        try:
            expected_invalid_username_error_text = self.common_test_data_config.get("Portal_Login_module_data", "expected_invalid_username_error_text")
            print("invalid username error msg: ", expected_invalid_username_error_text)
            return expected_invalid_username_error_text
        except Exception as ex:
            print(ex)

    def get_expected_invalid_password_error_text(self):
        try:
            expected_invalid_password_error_text = self.common_test_data_config.get("Portal_Login_module_data", "expected_invalid_password_error_text")
            print("invalid password error msg: ", expected_invalid_password_error_text)
            return expected_invalid_password_error_text
        except Exception as ex:
            print(ex)

    def get_close_invalid_username_alert_by_xpath(self):
        try:
            close_invalid_username_alert = self.config.get("Portal_Login_Page", "close_invalid_username_alert_by_xpath")
            print("close invalid username alert: ", close_invalid_username_alert)
            return close_invalid_username_alert
        except Exception as ex:
            print(ex)

    def get_invalid_password_text_on_alert_by_xpath(self):
        try:
            invalid_password_text_on_alert = self.config.get("Portal_Login_Page", "invalid_password_text_on_alert_by_xpath")
            print("invalid password text on alert: ", invalid_password_text_on_alert)
            return invalid_password_text_on_alert
        except Exception as ex:
            print(ex)

    def get_close_invalid_password_alert_by_xpath(self):
        try:
            close_invalid_password_alert = self.config.get("Portal_Login_Page", "close_invalid_password_alert_by_xpath")
            print("close invalid password alert: ", close_invalid_password_alert)
            return close_invalid_password_alert
        except Exception as ex:
            print(ex)

    def get_account_blocked_message_after_entering_invalid_password_six_times(self):
        try:
            account_blocked_message_after_entering_invalid_password_six_times = self.common_test_data_config.get("Portal_Login_module_data", "account_blocked_message_after_entering_invalid_password_six_times")
            print("account blocked message: ", account_blocked_message_after_entering_invalid_password_six_times)
            return account_blocked_message_after_entering_invalid_password_six_times
        except Exception as ex:
            print(ex)

    def get_logout_button_on_portal_by_xpath(self):
        try:
            logout_button_on_portal = self.config.get("Portal_Login_Page", "logout_button_on_portal_by_xpath")
            print("logout button on portal: ", logout_button_on_portal)
            return logout_button_on_portal
        except Exception as ex:
            print(ex)

    def get_expected_password_not_match(self):
        try:
            expected_password_not_match = self.common_test_data_config.get("Portal_Login_module_data", "expected_password_not_match")
            print(f"expected_password_not_match: {expected_password_not_match}")
            return expected_password_not_match
        except Exception as ex:
            print(ex.args)

Portal_login_page_read_ini().get_portal_url()
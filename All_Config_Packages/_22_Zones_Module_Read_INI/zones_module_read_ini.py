import configparser
from pathlib import Path


class zones_Read_Ini:
    def __init__(self):
        try:
            self.file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\22_Zones_Module\\Data_From_ini\\zones.ini"
            self.config=configparser.RawConfigParser()
            print("ini file path: ", self.file_path)
            self.config.read(self.file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
           print(ex)

    def zones_menu_item(self):
        zones_menu_item = self.config.get("zones_locators", "zones_menu_item")
        print("zones_menu_item :", zones_menu_item)
        return zones_menu_item

    def zones_panel_heading_by_xpath(self):
        zones_panel_heading_by_xpath = self.config.get("zones_locators", "zones_panel_heading_by_xpath")
        print("zones_panel_heading_by_xpath :", zones_panel_heading_by_xpath)
        return zones_panel_heading_by_xpath

    def zone_list_by_xpath(self):
        zone_list_by_xpath = self.config.get("zones_locators", "zone_list_by_xpath")
        print("zone_list_by_xpath :", zone_list_by_xpath)
        return zone_list_by_xpath

    def zone_name_list_by_xpath(self):
        zone_name_list_by_xpath = self.config.get("zones_locators", "zone_name_list_by_xpath")
        print("zone_name_list_by_xpath :", zone_name_list_by_xpath)
        return zone_name_list_by_xpath

    def zone_details_btn_list_by_xpath(self):
        zone_details_btn_list_by_xpath = self.config.get("zones_locators", "zone_details_btn_list_by_xpath")
        print("zone_details_btn_list_by_xpath :", zone_details_btn_list_by_xpath)
        return zone_details_btn_list_by_xpath

    def zone_checkbox_list_by_xpath(self):
        zone_checkbox_list_by_xpath = self.config.get("zones_locators", "zone_checkbox_list_by_xpath")
        print("zone_checkbox_list_by_xpath :", zone_checkbox_list_by_xpath)
        return zone_checkbox_list_by_xpath

    def action_dropdown_by_xpath(self):
        action_dropdown_by_xpath = self.config.get("zones_locators", "action_dropdown_by_xpath")
        print("action_dropdown_by_xpath :", action_dropdown_by_xpath)
        return action_dropdown_by_xpath

    def options_list_under_action_dropdown_by_xpath(self):
        options_list_under_action_dropdown_by_xpath = self.config.get("zones_locators", "options_list_under_action_dropdown_by_xpath")
        print("options_list_under_action_dropdown_by_xpath :", options_list_under_action_dropdown_by_xpath)
        return options_list_under_action_dropdown_by_xpath

    # *********************************** Common Data read ini ***************************************

    def zone_names(self):
        zone_names = self.common_test_data_config.get("Login_Logout_Data", "zone_names")
        print("zone_names :", zone_names)
        return zone_names

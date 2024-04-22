import pytest
from All_POM_Packages.Account_module_POM.Account_pom import account_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=20)
class Test_account_testcases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Account_Module (Order - 19) Begin ********")
    print("******** Account_Module (Order - 19) Begin ********")


    # @pytest.mark.p1
    # def test_account_TC_001(self):
    #     if account_pom().Launching_login_page():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_account_TC_002(self):
    #     if account_pom().logo_username_texbox_password_textbox_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_account_TC_003(self):
    #     if account_pom().verify_on_cloud_menu_after_login():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p1
    # def test_account_TC_004(self):
    #     if account_pom().verify_account_is_visible_in_dashboard_items():
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.system
    def test_account_TC_001(self):
        if account_pom().save_account_panel_details_before_execution():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_account_TC_002(self):
        if account_pom().save_account_panel_details_after_execution():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_account_TC_034(self):
        if account_pom().click_on_image_sources_and_check_theplanel_heading_of_Account_Image_sources_is_displayed():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_account_TC_036(self):
        if account_pom().click_on_location_on_View_dropdown_map_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_account_TC_038(self):
        if account_pom().click_on_regions_button_verify_panel_heading():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_account_TC_040(self):
        if account_pom().click_on_detailsbutton_verify_imagesource_panel_heading_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_account_TC_042(self):
        if account_pom().click_on_viewlocation_button_on_imagesource_verify_location():
            assert True
        else:
            assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_005(self):
    #     if account_pom().verify_panel_heading_of_Account():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_006(self):
    #     if account_pom().verify_Account_Details_banner_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_account_TC_007(self):
    #     if account_pom().verify_Enabled_true_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_008(self):
    #     if account_pom().verify_Enrollments_and_its_number_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_009(self):
    #     if account_pom().verify_Users_Created_and_its_number_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_010(self):
    #     if account_pom().verify_Max_Investigation_Length_along_withits_number_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_011(self):
    #     if account_pom().verify_Enrollment_Groups_along_with_its_number_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_012(self):
    #     if account_pom().verify_Notification_Groups_along_its_number_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_013(self):
    #     if account_pom().verify_Stations_along_its_number_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_014(self):
    #     if account_pom().verify_First_Name_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_015(self):
    #     if account_pom().verify_Middle_Name_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_Tc_016(self):
    #     if account_pom().verify_Last_Name_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_017(self):
    #     if account_pom().verify_Company_and_its_name_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_018(self):
    #     if account_pom().verify_Department_and_its_name_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_019(self):
    #     if account_pom().verify_Title_and_its_name_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_020(self):
    #     if account_pom().verify_Email_and_its_emailid_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_021(self):
    #     if account_pom().verify_Work_Phone_and_its_number_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_022(self):
    #     if account_pom().verify_Home_Phone_and_its_number_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_023(self):
    #     if account_pom().verify_Fax_Number_and_its_number_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_024(self):
    #     if account_pom(). verify_Address_and_its_address_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_025(self):
    #     if account_pom().verify_Address2_and_its_details_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_026(self):
    #     if account_pom().verify_city_name_of_cityis_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_027(self):
    #     if account_pom().verify_State_and_its_nameis_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_028(self):
    #     if account_pom().verify_Zip_Code_and_its_number_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_029(self):
    #     if account_pom().verify_Timezone_Asia_Kolkata_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_030(self):
    #     if account_pom().verify_Case_TTL_and_its_seconds_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_031(self):
    #     if account_pom().verify_subscription_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_account_TC_032(self):
    #     if account_pom().click_on_subscription_button_verify_account_subscription_banner_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_033(self):
    #     if account_pom().verify_Image_sources_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_account_TC_034(self):
    #     if account_pom().click_on_image_sources_and_check_theplanel_heading_of_Account_Image_sources_is_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_035(self):
    #     if account_pom().verify_view_dropdown_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_account_TC_036(self):
    #     if account_pom().click_on_location_on_View_dropdown_map_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_037(self):
    #     if account_pom().verify_regions_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_account_TC_038(self):
    #     if account_pom().click_on_regions_button_verify_panel_heading():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_039(self):
    #     if account_pom().verify_details_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_account_TC_040(self):
    #     if account_pom().click_on_detailsbutton_verify_imagesource_panel_heading_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_account_TC_041(self):
    #     if account_pom().on_image_source_panel_verify_view_location_button_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_account_TC_042(self):
    #     if account_pom().click_on_viewlocation_button_on_imagesource_verify_location():
    #         assert True
    #     else:
    #         assert False
    #



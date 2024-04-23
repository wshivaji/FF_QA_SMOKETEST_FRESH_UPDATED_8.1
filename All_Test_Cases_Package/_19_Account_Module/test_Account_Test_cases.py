import pytest
from All_POM_Packages.Account_module_POM.Account_pom import account_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=20)
class Test_account_testcases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Account_Module (Order - 19) Begin ********")
    print("******** Account_Module (Order - 19) Begin ********")

    @pytest.mark.system
    def test_account_TC_001(self):
        if account_pom().Verify_account_panel_details_before_execution():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_account_TC_002(self):
        if account_pom().Verify_account_panel_details_after_execution():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_account_TC_034(self):
        if account_pom().click_on_image_sources_and_check_theplanel_heading_of_Account_Image_sources_is_displayed():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_account_TC_036(self):
        if account_pom().click_on_location_on_View_dropdown_map_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_account_TC_038(self):
        if account_pom().click_on_regions_button_verify_panel_heading():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_account_TC_040(self):
        if account_pom().click_on_detailsbutton_verify_imagesource_panel_heading_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_account_TC_042(self):
        if account_pom().click_on_viewlocation_button_on_imagesource_verify_location():
            assert True
        else:
            assert False

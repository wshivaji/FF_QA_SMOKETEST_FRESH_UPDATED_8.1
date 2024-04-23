import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.SSPR_Module_POM.Sspr_POM import SSPR_pom
from All_POM_Packages.Zones_Module_POM.Zones_Module_POM import Zones_pom


@pytest.mark.run(order=22)
class Test_Zones_Module_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** ZONES_Module (Order - 22) Begin ********")
    print("******** ZONES_Module (Order - 22) Begin ********")

    @pytest.mark.system
    def test_Zones_TC_001(self):
        if Zones_pom().open_zones_panel_and_verify_zones_panel_displayed():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_zones_TC_002(self):
        if Zones_pom().verify_zone_list_enlisted_and_zone_names_displayed_as_expected():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_zones_TC_003(self):
        if Zones_pom().verify_zone_list_enlisted_and_zone_details_btn_displayed_as_expected():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_zones_TC_004(self):
        if Zones_pom().verify_zone_list_enlisted_and_zone_select_checkbox_displayed_as_expected():
            assert True
        else:
            assert False

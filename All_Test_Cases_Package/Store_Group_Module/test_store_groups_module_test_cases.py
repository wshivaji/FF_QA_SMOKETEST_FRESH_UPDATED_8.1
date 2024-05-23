import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.Store_Groups_Module_POM.Store_Groups_Module_POM import Store_Groups_Module_pom


class Test_Portal_Smoke_Test_Cases(web_driver, web_logger):
    logger = web_logger.logger_obj()

    def test_TC_SG_01(self):
        if Store_Groups_Module_pom().create_three_store_groups_for_different_stores():
            assert True
        else:
            assert False

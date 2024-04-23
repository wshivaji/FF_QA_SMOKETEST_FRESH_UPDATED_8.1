
import pytest
# from All_POM_Packages.tags_module_POM.Tags_Module_POM import Tags_Module_pom
from All_POM_Packages.tags_module_POM.Tags_Module_POM import Tags_Module_pom
from Base_Package.Web_Logger import web_logger
from Base_Package.Web_Driver import web_driver


@pytest.mark.run(order=7)
class Test_Tags_Module(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Tags_Module (Order - 7) Begin ********")
    print("******** Tags_Module (Order - 7) Begin ********")

    @pytest.mark.system
    def test_TC_TAG_01(self):
        self.logger.info("test_TC_TAG_01 execution started..")
        if Tags_Module_pom().create_tags_for_serious_event():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_01.png")
            self.logger.info("test_TC_TAG_01 fail")
            assert False

    @pytest.mark.system
    def test_TC_TAG_02(self):
        self.logger.info("test_TC_TAG_02 execution started..")
        if Tags_Module_pom().create_tags_for_non_serious_event():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_02.png")
            self.logger.info("test_TC_TAG_02 fail")
            assert False

    @pytest.mark.system
    def test_TC_TAG_03(self):
        self.logger.info("test_TC_TAG_03 execution started..")
        if Tags_Module_pom().Verify_total_tags_are_n_including_default_Deterred_tag():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_TC_TAG_04(self):
        self.logger.info("test_TC_TAG_04 execution started..")
        if Tags_Module_pom().tags_search_functionality():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_04.png")
            self.logger.info("test_TC_TAG_04 fail")
            assert False

    @pytest.mark.p3
    def test_TC_TAG_05(self):
        self.logger.info("test_TC_TAG_05 execution started..")
        if Tags_Module_pom().filter_serious_event_tags_varify_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_05.png")
            self.logger.info("test_TC_TAG_05 fail")
            assert False

    @pytest.mark.p3
    def test_TC_TAG_06(self):
        self.logger.info("test_TC_TAG_06 execution started..")
        if Tags_Module_pom().filter_non_serious_event_tags_varify_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_06.png")
            self.logger.info("test_TC_TAG_06 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_07(self):
        self.logger.info("test_TC_TAG_07 execution started..")
        if Tags_Module_pom().duplicate_tags_not_create_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_07.png")
            self.logger.info("test_TC_TAG_07 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_08(self):
        self.logger.info("test_TC_TAG_08 execution started..")
        if Tags_Module_pom().edit_serious_event_tag_name():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_08.png")
            self.logger.info("test_TC_TAG_08 fail")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_09(self):
        self.logger.info("test_TC_TAG_09 execution started..")
        if Tags_Module_pom().delete_all_tags():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_09.png")
            self.logger.info("test_TC_TAG_09 fail")
            assert False

    @pytest.mark.p2
    def test_TC_TAG_10(self):
        self.logger.info("test_TC_TAG_10 execution started..")
        if Tags_Module_pom().verify_deterred_tag_is_present_at_first():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_10.png")
            self.logger.info("test_TC_TAG_10 fail")
            assert False

    @pytest.mark.p3
    def test_TC_TAG_11(self):
        self.logger.info("test_TC_TAG_011 execution started..")
        if Tags_Module_pom().close_panel_and_discard_changes_verify():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_11.png")
            self.logger.info("test_TC_TAG_11 fail")
            assert False





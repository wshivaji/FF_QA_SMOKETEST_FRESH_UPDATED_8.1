import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.Visitor_Seach_Jobs_Module_POM.Visitor_Search_Jobs_Module_POM import Visitor_Search_Jobs_Module_pom


@pytest.mark.run(order=6)
class Test_Visitor_Search_Jobs_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Visitor_Search_Jobs (Order - 6) Begin ********")
    print("******** Visitor_Search_Jobs (Order - 6) Begin ********")

    @pytest.mark.portal
    def test_VSJ_01(self):
        self.logger.info("Visitor search jobs module = test_VSJ_01 execution started..")
        if Visitor_Search_Jobs_Module_pom().verify_the_visitor_search_job_contains_user_performs_visitor_search_with_date_and_org_selection():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_01.png")
            self.logger.info("test_VSJ_01 execution failed..")
            assert False

    @pytest.mark.portal
    def test_VSJ_02(self):
        self.logger.info("Visitor search jobs module = test_VSJ_02 execution started..")
        if Visitor_Search_Jobs_Module_pom().Verify_visitor_search_status_banner_is_visible_visitor_search_jobs_on_VSJ_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_02.png")
            self.logger.info("test_VSJ_02 execution failed..")
            assert False

    @pytest.mark.portal
    def test_VSJ_03(self):
        self.logger.info("Visitor search jobs module = test_VSJ_03 execution started..")
        if Visitor_Search_Jobs_Module_pom().verify_when_user_click_on_View_Results_button_of_VSJ_should_display_visitor_search_results_panel():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_03.png")
            self.logger.info("test_VSJ_03 execution failed..")
            assert False

    @pytest.mark.portal
    def test_VSJ_04(self):
        self.logger.info("Visitor search jobs module = test_VSJ_04 execution started..")
        if Visitor_Search_Jobs_Module_pom().Verify_the_visitor_search_job_contains_the_selected_threshold_visitors_in_date_range_and_belongs_to_search_Org_Hierarchy_Selection_when_user_performs_a_visitor_search_with_Date_Org():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_04.png")
            self.logger.info("test_VSJ_04 execution failed..")
            assert False

    @pytest.mark.portal
    def test_VSJ_05(self):
        self.logger.info("Visitor search jobs module = test_VSJ_05 execution started..")
        if Visitor_Search_Jobs_Module_pom().verify_user_able_to_delete_VS_jobs():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_05.png")
            self.logger.info("test_VSJ_05 execution failed..")
            assert False

    @pytest.mark.portal
    def test_VSJ_06(self):
        self.logger.info("Visitor search jobs module = test_VSJ_06 execution started..")
        if Visitor_Search_Jobs_Module_pom().Verify_VSJ_filtering_with_date_range_selection_should_list_VSJ_in_the_selected_date_range_only():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_06.png")
            self.logger.info("test_VSJ_06 execution failed..")
            assert False

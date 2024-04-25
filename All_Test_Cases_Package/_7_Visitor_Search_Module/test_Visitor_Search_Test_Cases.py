import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.Visitor_Search_Module_POM.Visitor_Search_Module_POM import Visitor_Search_Module_pom


@pytest.mark.run(order=5)
class Test_Visitor_Search_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Visitor_Search (Order - 5) Begin ********")
    print("******** Visitor_Search (Order - 5) Begin ********")

    @pytest.mark.portal
    def test_TC_VS_01(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_metadata_Date_and_Org_Hierarchy_Selection_should_yield_visitor_results_within_selected_search_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_01.png")
            self.logger.info("test_TC_VS_01 execution failed..")
            assert False

    @pytest.mark.portal
    def test_TC_VS_02(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_image_only_should_list_the_matching_visitors_with_image():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_02.png")
            self.logger.info("test_TC_VS_02 execution failed..")
            assert False

    @pytest.mark.portal
    def test_TC_VS_03(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_Image_and_metadata_should_list_the_matched_visitors_with_search_image_from_selected_Org_Hierarchy_Selection_within_date_range():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_03.png")
            self.logger.info("test_TC_VS_03 execution failed..")
            assert False

    # @pytest.mark.portal
    # def test_TC_VS_04(self):
    #     if Visitor_Search_Module_pom().Verify_org_hierarchy_selection_root_name_should_be_able_to_match_with_DM_core_name():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_04.png")
    #         self.logger.info("test_TC_VS_04 execution failed..")
    #         assert False
    #
    # @pytest.mark.portal
    # def test_TC_VS_05(self):
    #     if Visitor_Search_Module_pom().Verify_warning_message_when_user_is_dropping_the_image_which_is_clicked_on_live_or_file_image_on_events_panel_able_to_perform_image_with_meta_data_idealy_it_should_not_with_larger_image_able_to_perform():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_05.png")
    #         self.logger.info("test_TC_VS_05 execution failed..")
    #         assert False

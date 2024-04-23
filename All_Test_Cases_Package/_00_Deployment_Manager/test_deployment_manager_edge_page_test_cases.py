import pytest
from All_POM_Packages._00_Deployment_Manager_POM.Deployment_Manager_Page_POM import Deployment_Manager_Page_Pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


class Test_Deployment_Manager_Edge_Page_Test_Cases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Deployment Manager Edge Page (Order - 0) Begin ********")
    print("******** Deployment Manager Edge Page (Order - 0) Begin ********")

    @pytest.mark.edge
    def test_dm_edge_tc01(self):
        if Deployment_Manager_Page_Pom().launch_swagger_and_click_on_authorize_btn_and_login_with_core_credentials():
            assert True
        else:
            assert False

    @pytest.mark.edge
    def test_dm_edge_tc02(self):
        if Deployment_Manager_Page_Pom().upload_json_file_to_swagger_api_regions_to_create_org_hierarchy_structure():
            assert True
        else:
            assert False

    @pytest.mark.edge
    def test_dm_edge_tc03(self):
        if Deployment_Manager_Page_Pom().enter_one_of_edge_name_in_search_filter_textbox_and_verify_that_edge_name_is_filtering_below_it():
            assert True
        else:
            assert False

    @pytest.mark.edge
    def test_dm_edge_tc04(self):
        if Deployment_Manager_Page_Pom().before_deploying_all_edges_click_on_second_edge_which_is_to_be_deploy_go_to_diployment_wizards_and_verify_selected_edge_name_is_visible_for_deployment():
            assert True
        else:
            assert False


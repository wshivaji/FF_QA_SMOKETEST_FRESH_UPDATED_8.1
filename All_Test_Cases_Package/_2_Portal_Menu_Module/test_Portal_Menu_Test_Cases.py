import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.Portal_Menu_Module_POM.Portal_Menu_Module_POM import Portal_Menu_Module_pom


@pytest.mark.run(order=18)
class Test_Portal_Menu_Test_Cases(web_driver, web_logger):
    d = web_driver.d
    logger = web_logger.logger_obj()
    logger.info(" ******** Portal_Menu (Order - 18) Begin ********")
    print("******** Portal_Menu (Order - 18) Begin ********")

    @pytest.mark.portal
    def test_TC_PM_1(self):
        if Portal_Menu_Module_pom().Verify_all_submenus_are_visible_and_clickable_on_Cloud_Menu():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_PM_2(self):
        if Portal_Menu_Module_pom().Verify_for_Operator_user_PME_Tags_IE_DF_Enrollments_EG_VS_VSJ_Notes_Loc_Zones_Reporting_IDB_Notifier_these_menus_are_visible_on_the_cloud_menu_items():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_PM_3(self):
        if Portal_Menu_Module_pom().Verify_for_Responder_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_PM_4(self):
        if Portal_Menu_Module_pom().Verify_for_Approver_or_supervisor_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_PM_5(self):
        if Portal_Menu_Module_pom().Verify_for_Executive_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Account_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_PM_6(self):
        if Portal_Menu_Module_pom().Verify_for_IT_Admin_user_PME_Tags_IE_DF_Enrollments_EG_NG_VS_VSJ_Notes_Loc_US_UR_Zones_Account_Reporting_IDB_Notifier_ALR_these_menus_are_visible_on_the_cloud_menu_items():
            assert True
        else:
            assert False

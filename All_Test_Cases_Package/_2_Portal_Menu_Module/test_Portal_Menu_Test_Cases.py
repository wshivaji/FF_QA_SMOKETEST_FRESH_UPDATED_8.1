import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._2_Portal_Menu_Module_POM.Portal_Menu_Module_POM import Portal_Menu_Module_pom


@pytest.mark.run(order=2)
class Test_Portal_Menu_Test_Cases(web_driver, web_logger):
    d = web_driver.d
    logger = web_logger.logger_obj()
    logger.info(" ******** Portal_Menu (Order - 2) Begin ********")
    print("******** Portal_Menu (Order - 2) Begin ********")

    @pytest.mark.p1
    def test_TC_PM_1(self):
        if Portal_Menu_Module_pom().Verify_all_submenus_are_visible_and_clickable_on_Cloud_Menu():
            assert True
        else:
            assert False

    # @pytest.mark.p1
    # def test_TC_PM_2(self):
    #     if Portal_Menu_Module_pom().Verify_tags_menu_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_PM_3(self):
    #     if Portal_Menu_Module_pom().Verify_Identify_and_Enroll_menu_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_PM_4(self):
    #     if Portal_Menu_Module_pom().Verify_Detect_Faces_menu_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_PM_5(self):
    #     if Portal_Menu_Module_pom().Verify_Enrollments_menu_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_PM_6(self):
    #     if Portal_Menu_Module_pom().Verify_Enrollment_Groups_menu_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False


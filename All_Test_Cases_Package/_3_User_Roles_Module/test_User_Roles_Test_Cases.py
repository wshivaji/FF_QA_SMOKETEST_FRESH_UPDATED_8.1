from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.User_Roles_Module_POM.User_Roles_Module_POM import user_roles_module_pom
import pytest


@pytest.mark.run(order=4)
class Test_User_Roles_Test_Cases(web_driver, web_logger):
    # d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** User_Roles (Order - 3) Begin ********")
    print("******** User_Roles (Order - 3) Begin ********")

    @pytest.mark.p2
    def test_TC_UR_01(self):
        self.logger.info("***************** test_TC_UR_01 *****************")
        if user_roles_module_pom().Verify_new_user_roles_operator_responder_approver_executive_and_it_admin_are_visible():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_TC_UR_02(self):
        self.logger.info("***************** test_TC_UR_02 *****************")
        if user_roles_module_pom().Verify_total_user_roles_are_6_including_default_user_role():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_TC_UR_03(self):
        self.logger.info("***************** test_TC_UR_03 *****************")
        if user_roles_module_pom().Verify_user_able_to_create_a_new_users_role_by_filling_all_the_fields():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_UR_04(self):
        self.logger.info("***************** test_TC_UR_04 *****************")
        if user_roles_module_pom().verify_user_able_to_edit_user_roles_detaild_description_with_disabled_enrollment_review_permissions():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_UR_05(self):
        self.logger.info("***************** test_TC_UR_05 *****************")
        if user_roles_module_pom().Verify_details_and_all_permission_of_default_it_admin():
            assert True
        else:
            assert False\

    @pytest.mark.p1
    def test_TC_UR_06(self):
        self.logger.info("***************** test_TC_UR_06 *****************")
        if user_roles_module_pom().Verify_User_role_deletion_functionality_by_deleting_one_user_role():
            assert True
        else:
            assert False









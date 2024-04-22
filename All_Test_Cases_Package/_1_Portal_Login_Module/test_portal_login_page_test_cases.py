import pytest
from All_POM_Packages.Portal_Login_Module_POM.Portal_Login_Page_POM import Portal_Login_Page_Pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=1)
class Test_Portal_Login_Page_Test_Cases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Portal_Login_Page (Order - 1) Begin ********")
    print("******** Portal_Login_Page (Order - 1) Begin ********")

    @pytest.mark.system
    def test_Portal_Login_TC01(self):
        if Portal_Login_Page_Pom().open_portal_url_and_verify_expected_url_is_visible_verify_expected_page_title_is_visible_and_verify_face_first_logo_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_Portal_Login_TC02(self):
        if (Portal_Login_Page_Pom().
                verify_user_login_with_valid_credentials_and_click_on_cloud_login_and_verify_it_is_navigating_to_cloud_menu_panel()):
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_Portal_Login_TC03(self):
        if Portal_Login_Page_Pom().verify_face_first_copy_rights_is_visible_and_clickable_click_on_copyrights_and_verify_versions_of_webapi_and_server_both_are_visible_verify_latest_version_of_webapi_and_server_is_appeared():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_Portal_Login_TC04(self):
        if Portal_Login_Page_Pom().Verify_user_login_to_webportal_should_fail_with_invalid_credentials():
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_Portal_Login_TC05(self):
        if Portal_Login_Page_Pom().\
               verify_user_account_blocked_for_30_min_if_user_enter_wrong_password_for_6_times_verify_message_warning():
            assert True
        else:
            assert False

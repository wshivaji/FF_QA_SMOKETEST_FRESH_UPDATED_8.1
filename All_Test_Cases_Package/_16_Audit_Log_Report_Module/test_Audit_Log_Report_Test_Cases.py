
import pytest
# from All_POM_Package.Audit_Log_Reports.Audit_Log_Reports_POM import Audit_log_report_pom
from All_POM_Packages.Audit_Log_Report_Module_POM.Audit_Log_Report_Module_POM import Audit_log_report_pom
# from All_Test_Cases_Package.conftest import Base_Class
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=14)
class Test_Audit_Log_Report_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Audit_Log_Report (Order - 14) Begin ********")

    @pytest.mark.portal
    def test_TC_ALR_001(self):
        self.logger.info("Audit Log Report = test_TC_ALR_001 execution started..")
        if Audit_log_report_pom().\
                Verify_user_is_able_to_generate_report_for_Approver_enrollments_and_download_excel_file():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_ALR_002(self):
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_user_enrollments_and_download_excel_file():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_ALR_003(self):
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_log_in_log_out_and_download_excel_file():
            assert True
        else:
            assert False

    @pytest.mark.portal
    def test_TC_ALR_004(self):
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_Threshold_changes_and_download_excel_file():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_ALR_05(self):
        if Audit_log_report_pom().Verify_user_with_all_permissions_enrolled_mask_subject_should_be_in_Disable_status_for_user_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_ALR_06(self):
        if Audit_log_report_pom().Verify_core_should_be_able_to_enable_above_mask_subject_and_verify_Enabled_status_and_action_by_core_for_user_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_ALR_07(self):
        if Audit_log_report_pom().Verify_for_above_enable_mask_subject_status_is_Enabled_in_Approver_Enrollments_too():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_ALR_008(self):
        if Audit_log_report_pom().Verify_user_with_2FA_enrolled_subject_should_be_able_to_see_Pending_status_for_user_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_ALR_09(self):
        if Audit_log_report_pom().Verify_user_with_2FA_enrolled_subject_approved_by_core_admin_should_be_able_to_see_Accepted_status_and_action_by_core_for_user_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_ALR_10(self):
        if Audit_log_report_pom().Verify_user_with_2FA_enrolled_subject_approved_by_core_admin_should_be_able_to_see_Accepted_status_for_approver_enrollments():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_ALR_11(self):
        if Audit_log_report_pom().Verify_Threshold_changes_report_with_user_modified_enrolment_group_details_should_be_displayed_on_the_report_with_ip_address():
            assert True
        else:
            assert False

    @pytest.mark.system
    def test_TC_ALR_12(self):
        if Audit_log_report_pom().Verify_Login_Logout_report_with_one_of_the_user_login_and_user_logout_with_minimum_delay_of_1_min():
            assert True
        else:
            assert False

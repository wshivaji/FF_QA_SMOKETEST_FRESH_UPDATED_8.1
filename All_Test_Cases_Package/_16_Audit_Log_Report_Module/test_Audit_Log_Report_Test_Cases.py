
import pytest
# from All_POM_Package.Audit_Log_Reports.Audit_Log_Reports_POM import Audit_log_report_pom
from All_POM_Packages._16_Audit_Log_Report_Module_POM.Audit_Log_Report_Module_POM import Audit_log_report_pom
# from All_Test_Cases_Package.conftest import Base_Class
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=17)
class Test_Audit_Log_Report_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Audit_Log_Report (Order - 16) Begin ********")

    @pytest.mark.p1
    def test_TC_ALR_001(self):
        self.logger.info("Audit Log Report = test_TC_ALR_001 execution started..")
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_Approver_enrollments_and_download_excel_file():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_002(self):
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_user_enrollments_and_download_excel_file():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_003(self):
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_log_in_log_out_and_download_excel_file():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_004(self):
        if Audit_log_report_pom().Verify_user_is_able_to_generate_report_for_Threshold_changes_and_download_excel_file():
            assert True
        else:
            assert False

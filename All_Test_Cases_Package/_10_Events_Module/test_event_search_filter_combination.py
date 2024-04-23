from pathlib import Path
import pytest
from All_POM_Package.Events_Module.Event_search_filter_combinations_POM import Event_search_filter_combinations_POM
from All_Test_Cases_Package.conftest import Base_Class


@pytest.mark.run(order=16)
class Test_event_search_filter_combination(Base_Class):
    logger = Base_Class.logger_obj()

    def setup_method(self):
        try:
            self.d = Base_Class.d
            self.d.maximize_window()
            self.d.set_page_load_timeout(50)
            self.d.set_script_timeout(30)
            self.d.implicitly_wait(30)
            self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"
        except Exception as ex:
            print("\nException in Test_event_search_filter_combination/setup_method: ", ex.args)

    @pytest.mark.p1
    def test_TC_ESFC_01(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_01 execution started..")
        if Event_search_filter_combinations_POM(self.logger).event_search_with_no_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_01.png")
            self.logger.info("test_TC_ESFC_01 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_02(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_02 execution started..")
        if Event_search_filter_combinations_POM(self.logger).event_search_with_tag_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_02.png")
            self.logger.info("test_TC_ESFC_02 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_03(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_03 execution started..")
        if Event_search_filter_combinations_POM(self.logger).event_search_with_org_Hierarchy_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_03.png")
            self.logger.info("test_TC_ESFC_03 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_04(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_04 execution started..")
        if Event_search_filter_combinations_POM(self.logger).event_search_with_tag_and_org_hierarchy_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_04.png")
            self.logger.info("test_TC_ESFC_04 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_05(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_05 execution started..")
        if Event_search_filter_combinations_POM(self.logger).event_search_with_enrollmentGroup_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_05.png")
            self.logger.info("test_TC_ESFC_05 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_06(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_06 execution started..")
        if Event_search_filter_combinations_POM(self.logger).event_search_with_enrollmentGroup_and_tag_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_06.png")
            self.logger.info("test_TC_ESFC_06 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_07(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_07 execution started..")
        if Event_search_filter_combinations_POM(self.logger).event_search_with_enrollmentGroup_org_hierarchy_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_07.png")
            self.logger.info("test_TC_ESFC_07 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_08(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_08 execution started..")
        if Event_search_filter_combinations_POM(self.logger).\
                event_search_with_enrollmentGroup_org_hierarchy_and_tag_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_08.png")
            self.logger.info("test_TC_ESFC_08 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_09(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_09 execution started..")
        if Event_search_filter_combinations_POM(self.logger).event_search_with_dateTimeRange_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_09.png")
            self.logger.info("test_TC_ESFC_09 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_010(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_010 execution started..")
        if Event_search_filter_combinations_POM(self.logger).event_search_with_DateTimeRange_and_Tag_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_010.png")
            self.logger.info("test_TC_ESFC_010 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_011(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_011 execution started..")
        if Event_search_filter_combinations_POM(self.logger).\
                event_search_with_DateTimeRange_and_org_Hierarchy_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_011.png")
            self.logger.info("test_TC_ESFC_011 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_012(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_012 execution started..")
        if Event_search_filter_combinations_POM(self.logger).\
                event_search_with_DateTimeRange_org_Hierarchy_and_Tag_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_012.png")
            self.logger.info("test_TC_ESFC_012 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_013(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_013 execution started..")
        if Event_search_filter_combinations_POM(self.logger).\
                event_search_with_DateTimeRange_and_EnrollmentGroup_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_013.png")
            self.logger.info("test_TC_ESFC_013 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_014(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_014 execution started..")
        if Event_search_filter_combinations_POM(self.logger).\
                event_search_with_DateTimeRange_EnrollmentGroup_and_Tag_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_014.png")
            self.logger.info("test_TC_ESFC_014 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_015(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_015 execution started..")
        if Event_search_filter_combinations_POM(self.logger).\
                event_search_with_DateTimeRange_EnrollmentGroup_and_Org_Hierarchy_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_015.png")
            self.logger.info("test_TC_ESFC_015 fail")
            assert False

    @pytest.mark.p1
    def test_TC_ESFC_016(self):
        self.logger.info("Event Search Filter Combination = test_TC_ESFC_016 execution started..")
        if Event_search_filter_combinations_POM(self.logger).\
                event_search_with_DateTimeRange_EnrollmentGroup_Org_Hierarchy_and_Tag_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ESFC_016.png")
            self.logger.info("test_TC_ESFC_016 fail")
            assert False


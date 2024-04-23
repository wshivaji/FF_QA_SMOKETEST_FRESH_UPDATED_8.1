from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.Notifier_Module_POM.Notifier_POM import Notifier_pom
import pytest


@pytest.mark.run(order=18)
class Test_Notifier_Module_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Notifier (Order - 17) Begin ********")
    print("******** Notifier (Order - 17) Begin ********")

    @pytest.mark.p2
    def test_TC_Notifier_01(self):
        if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_TC_Notifier_02(self):
        if Notifier_pom().Verify_events_appears_with_live_and_probable_match_image_upon_event_generation_with_sound():
            assert True
        else:
            assert False

    @pytest.mark.p3
    def test_TC_Notifier_03(self):
        if Notifier_pom().Verify_org_hierarchy_selection_features_collapse_all_expand_all_select_all_and_unselect_all():
            assert True
        else:
            assert False

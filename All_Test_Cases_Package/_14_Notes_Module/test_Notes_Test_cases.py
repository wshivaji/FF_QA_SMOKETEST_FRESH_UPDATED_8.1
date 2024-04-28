import pytest
from All_POM_Packages._6_Notes_Module_POM.Notes_pom import notes_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=15)
class Test_notes_page_testcases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Notes_Module (Order - 14) Begin ********")
    print("******** Notes_Module (Order - 14) Begin ********")

    @pytest.mark.p1
    def test_NOTES_TC_1(self):
        if notes_pom().verify_user_able_create_notes_successfully():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_NOTES_TC_2(self):
        if notes_pom().verify_user_able_to_edit_details_by_selecting_details_icon():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_NOTES_TC_3(self):
        if notes_pom().verify_user_is_able_to_select_any_one_note_and_click_on_location_icon():
            assert True
        else:
            assert False

    def test_NOTES_TC_04(self):
        if notes_pom().verify_user_is_able_to_select_any_one_note_and_click_on_location_in_view_dropdown():
            assert True
        else:
            assert False

    def test_NOTES_TC_05(self):
        if notes_pom().verify_user_is_able_to_see_the_enrollment_associated_to_particular_note():
            assert True
        else:
            assert False

    def test_NOTES_TC_06(self):
        if notes_pom().Verify_user_is_able_to_add_photo_when_image_icon_is_clicked():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_NOTES_TC_07(self):
        if notes_pom().verify_user_able_to_delete_notes_successfully():
            assert True
        else:
            assert False

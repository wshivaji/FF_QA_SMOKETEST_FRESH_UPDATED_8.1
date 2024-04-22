from pathlib import Path
import configparser


class DeploymentManager_Read_ini:

    def __init__(self):
        self.file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\00_Deployment_Manager_Data\\Data_From_INI\\dm_data.ini"
        print(f"INI Data File Path: {self.file_path}")
        self.config = configparser.RawConfigParser()
        self.config.read(self.file_path)
        common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
        self.common_test_data_config = configparser.RawConfigParser()
        self.common_test_data_config.read(common_test_data_ini_file_path)

    def get_register_url(self):
        try:
            reg_url = self.common_test_data_config.get("dm_login_urls", "RegisterURL")
            print("Register page url: ", reg_url)
            return reg_url
        except Exception as ex:
            print(ex)

    def get_register_login_link_from_register_url(self):
        try:
            reg_login_link_from_reg_url = self.common_test_data_config.get("dm_login_urls", "Reg_login_link_from_reg")
            print("Register login link from register page url: ", reg_login_link_from_reg_url)
            return reg_login_link_from_reg_url
        except Exception as ex:
            print(ex)

    def get_reg_login_link_url(self):
        try:
            reg_login_link_url = self.common_test_data_config.get("dm_login_urls", "Reg_login_link")
            print("Register Login link page url: ", reg_login_link_url)
            return reg_login_link_url
        except Exception as ex:
            print(ex)

    def get_mail(self):
        try:
            dm_mail = self.common_test_data_config.get("Login_Logout_Data", "mail")
            print("Register Mail: ", dm_mail)
            return dm_mail
        except Exception as ex:
            print(ex)

    def get_licences(self):
        try:
            dm_mail = self.common_test_data_config.get("Login_Logout_Data", "licence")
            print("Licence: ", dm_mail)
            return dm_mail
        except Exception as ex:
            print(ex)

    def get_domain_id(self):
        try:
            dm_domain_id = self.common_test_data_config.get("domain_settings", "domain_id")
            print("Domian ID: ", dm_domain_id)
            return dm_domain_id
        except Exception as ex:
            print(ex)

    def get_domain_name(self):
        try:
            dm_domain_name = self.common_test_data_config.get("domain_settings", "domain_name")
            print("Domain Name: ", dm_domain_name)
            return dm_domain_name
        except Exception as ex:
            print(ex)

    def get_domain_certificate(self):
        try:
            dm_domain_certificate = self.common_test_data_config.get("domain_settings", "domain_certificate")
            print("Domain Certificate: ", dm_domain_certificate)
            return dm_domain_certificate
        except Exception as ex:
            print(ex)

    def get_domain_certificate_password(self):
        try:
            dm_domain_certificate_password = self.common_test_data_config.get("domain_settings", "domain_certificate_password")
            print("Domain Certificate Password: ", dm_domain_certificate_password)
            return dm_domain_certificate_password
        except Exception as ex:
            print(ex)

    def get_alert_threshold(self):
        try:
            dm_alert_threshold = self.common_test_data_config.get("platform_settings", "alert_threshold")
            print("Alert Threshold: ", dm_alert_threshold)
            return dm_alert_threshold
        except Exception as ex:
            print(ex)

    def get_mask_alert_threshold(self):
        try:
            dm_mask_alert_threshold = self.common_test_data_config.get("platform_settings", "mask_alert_threshold")
            print("Mask Alert Threshold: ", dm_mask_alert_threshold)
            return dm_mask_alert_threshold
        except Exception as ex:
            print(ex)

    def get_dashboard_refresh_interval(self):
        try:
            dashboard_refresh_interval = self.common_test_data_config.get("platform_settings", "dashboard_refresh_interval")
            print("Dashboard Refresh Interval: ", dashboard_refresh_interval)
            return dashboard_refresh_interval
        except Exception as ex:
            print(ex)

    def get_visitor_search_select(self):
        try:
            visitor_search_select = self.common_test_data_config.get("platform_settings", "visitor_search_select")
            print("Visitor Search Select: ", visitor_search_select)
            return visitor_search_select
        except Exception as ex:
            print(ex)

    def get_inactivity_timeout(self):
        try:
            inactivity_timeout = self.common_test_data_config.get("platform_settings", "inactivity_timeout")
            print("Inactivity Timeout: ", inactivity_timeout)
            return inactivity_timeout
        except Exception as ex:
            print(ex)

    def get_face_detection_quality_threshold(self):
        try:
            face_detection_quality_threshold = self.common_test_data_config.get("platform_settings", "face_detection_quality_threshold")
            print("Face Detection Quality Threshold: ", face_detection_quality_threshold)
            return face_detection_quality_threshold
        except Exception as ex:
            print(ex)

    def get_face_detection_masked_threshold(self):
        try:
            face_detection_masked_threshold = self.common_test_data_config.get("platform_settings", "face_detection_masked_threshold")
            print("Face Detection Masked Threshold: ", face_detection_masked_threshold)
            return face_detection_masked_threshold
        except Exception as ex:
            print(ex)

    def get_visitor_clustering_time(self):
        try:
            visitor_clustering_time = self.common_test_data_config.get("platform_settings", "visitor_clustering_time")
            print("Visitor Clustering Time: ", visitor_clustering_time)
            return visitor_clustering_time
        except Exception as ex:
            print(ex)

    def get_visitor_clustering_threshold(self):
        try:
            visitor_clustering_threshold = self.common_test_data_config.get("platform_settings", "visitor_clustering_threshold")
            print("Visitor Clustering Threshold: ", visitor_clustering_threshold)
            return visitor_clustering_threshold
        except Exception as ex:
            print(ex)

    def get_visitor_search_method(self):
        try:
            visitor_search_method = self.common_test_data_config.get("platform_settings", "visitor_search_method")
            print("Visitor Search Method: ", visitor_search_method)
            return visitor_search_method
        except Exception as ex:
            print(ex)

    def get_enrollment_quality_guard_count_events_method(self):
        try:
            enrollment_quality_guard_count_events = self.common_test_data_config.get("platform_settings", "eqg_count_events")
            print("Enrollment Quality Guard Count Events: ", enrollment_quality_guard_count_events)
            return enrollment_quality_guard_count_events
        except Exception as ex:
            print(ex)

    def get_enrollment_quality_guard_duration_method(self):
        try:
            enrollment_quality_guard_duration_method = self.common_test_data_config.get("platform_settings", "eqg_duration")
            print("Enrollment Quality Guard Duration: ", enrollment_quality_guard_duration_method)
            return enrollment_quality_guard_duration_method
        except Exception as ex:
            print(ex)

    def get_enrollment_quality_guard_count_edges_method(self):
        try:
            enrollment_quality_guard_count_edges_method = self.common_test_data_config.get("platform_settings", "eqg_count_edges")
            print("Enrollment Quality Guard Duration: ", enrollment_quality_guard_count_edges_method)
            return enrollment_quality_guard_count_edges_method
        except Exception as ex:
            print(ex)

    def get_swagger_url_method(self):
        try:
            swagger_url_method = self.common_test_data_config.get("swagger", "swagger_url")
            print("Swagger URL: ", swagger_url_method)
            return swagger_url_method
        except Exception as ex:
            print(ex)

    def get_swagger_json_file_method(self):
        try:
            swagger_json_file_method = self.common_test_data_config.get("swagger", "swagger_json")
            print("Swagger URL: ", swagger_json_file_method)
            return swagger_json_file_method
        except Exception as ex:
            print(ex)

    def get_search_filter_text_box_method(self):
        try:
            search_filter_text_box_method = self.common_test_data_config.get("dm_edge", "search_filter_text_box")
            print("Search Filter Text Box Edge: ", search_filter_text_box_method)
            return search_filter_text_box_method
        except Exception as ex:
            print(ex)

    def get_2nd_edge_search_filter_text_box_method(self):
        try:
            edge_2nd_search_filter_text_box_method = self.common_test_data_config.get("dm_edge", "edge_2nd_search_filter_text_box")
            print("Second Edge Search Filter Text Box Edge: ", edge_2nd_search_filter_text_box_method)
            return edge_2nd_search_filter_text_box_method
        except Exception as ex:
            print(ex)

    def get_single_edge_region_method(self):
        try:
            single_edge_region_method = self.common_test_data_config.get("dm_edge", "single_edge_region")
            print("Single Edge Region Method: ", single_edge_region_method)
            return single_edge_region_method
        except Exception as ex:
            print(ex)

    def get_single_edge_rtsp_port_method(self):
        try:
            single_edge_rtsp_port_method = self.common_test_data_config.get("dm_edge", "single_edge_rtsp_port")
            print("Single Edge RTSP Port Method: ", single_edge_rtsp_port_method)
            return single_edge_rtsp_port_method
        except Exception as ex:
            print(ex)

    def get_single_edge_camera_location_method(self):
        try:
            single_edge_camera_location_method = self.common_test_data_config.get("dm_edge", "single_edge_camera_location")
            print("Single Edge Camera Location Method: ", single_edge_camera_location_method)
            return single_edge_camera_location_method
        except Exception as ex:
            print(ex)
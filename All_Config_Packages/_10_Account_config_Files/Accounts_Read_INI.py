import configparser
from pathlib import Path


class account_Read_Ini:
    def __init__(self):
        try:
            self.file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\10_Account_Module\\Data_From_INI\\Account_Module.ini"
            self.config=configparser.RawConfigParser()
            print("ini file path: ", self.file_path)
            self.config.read(self.file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
           print(ex)

    def get_Launching_url(self):
        url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
        print("launching webportal login page", url)
        return url

    def get_expecting_title_webportal_login(self):
        expected_title = self.common_test_data_config.get("Login_Logout_Data", "portal_title")
        print("expected title of webportal login page", expected_title)
        return expected_title

    def get_logo_is_visible_on_login_page(self):
        logo = self.config.get("login_locators", "logo_image_by_xpath")
        print("logo of webportal login page", logo)
        return logo

    def get_username_textbox(self):
        username = self.config.get("login_locators", "username_textbox_by_xpath")
        print("username texbox", username)
        return username

    def get_password_textbox(self):
        password = self.config.get("login_locators", "password_textbox_by_xpath")
        print("password textbox", password)
        return password

    def get_cloudlogin_button(self):
        cloud_menu = self.config.get("login_locators", "cloudlogin_button_by_xpath")
        print("cloud menu button",cloud_menu)
        return cloud_menu

    def get_valid_username(self):
        valid_username = self.common_test_data_config.get("Login_Logout_Data", "username")
        print("valid username is",valid_username)
        return valid_username

    def get_valid_password(self):
        valid_password = self.common_test_data_config.get("Login_Logout_Data", "password")
        print("valid password is", valid_password)
        return valid_password

    def get_username_after_successfull_login(self):
        afterlogin_username = self.config.get("login_locators", "after_successful_login_username_is_visible")
        print("after successfull login username is displayed on footer section", afterlogin_username)
        return afterlogin_username

    def get_cloud_menu(self):
        cloud_menu=self.config.get("login_locators", "cloud_menu")
        print("cloud menu is displayed", cloud_menu)
        return cloud_menu

    def get_logout(self):
        logout=self.config.get("login_locators","logout")
        print("logout is",logout)
        return logout

    def get_afterlogin_cloud_menu_is_visible(self):
        cloud_menu_after_login = self.config.get("account_locators","After_login_cloud_menu")
        print("after login cloud menu is visible",cloud_menu_after_login)
        return cloud_menu_after_login

    def account_in_dashboarditems(self):
        account=self.config.get("account_locators","account_in_dashboard_items")
        print("account present in dashboard items",account)
        return account

    def Account_panel_heading(self):
        account_panel_heading=self.config.get("account_locators", "Account_panel_heading")
        print("accounts panel heading is", account_panel_heading)
        return account_panel_heading

    def Account_details_banner(self):
        Account_details_banner=self.config.get("account_locators", "account_details_banner")
        print("account details banners is", Account_details_banner)
        return Account_details_banner
    def get_enabled_text(self):
        enabled=self.config.get("account_locators", "Enabled_text")
        print("enabled text is on accounts page", enabled)
        return enabled

    def read_enabled(self):
        enabled=self.common_test_data_config.get("Account_Module_Data", "Enabled")
        print("reading text  enabled:", enabled)
        return enabled

    def read_true(self):
        true = self.common_test_data_config.get("Account_Module_Data", "true")
        print("reading text  true:", true)
        return true

    def get_true_text(self):
        true_text=self.config.get("account_locators", "true_text")
        print("true text along with enabled", true_text)
        return true_text

    def get_Enrollments_text(self):
        enrollment_text = self.config.get("account_locators", "Enrollment")
        print("Enrollment text is", enrollment_text)
        return enrollment_text

    def get_number_of_enrollment_text(self):
        enrollment_number_text=self.config.get("account_locators", "Enrollments_number")
        print("no of enrollments text is", enrollment_number_text)
        return enrollment_number_text

    def read_enrollment_number(self):
        enrollment_number=self.common_test_data_config.get("Account_Module_Data", "Enrollments_number_text")
        print("reading enrollment number ", enrollment_number)
        return enrollment_number

    def get_usercreated_text(self):
        users_created=self.config.get("account_locators","users_created")
        print("users created text is ",users_created)
        return users_created

    def get_number_of_usercreated(self):
        usercreated_number=self.config.get("account_locators", "users_created_number")
        print("users created number is", usercreated_number)
        return usercreated_number

    def read_number_of_usercreated_text(self):
        userscreated_number = self.common_test_data_config.get("Account_Module_Data", "users_created_number_text")
        print("users created number is", userscreated_number)
        return userscreated_number

    def get_maximum_investigation_length(self):
        maximum_investigation=self.config.get("account_locators","Maximum_investigation_length")
        print("maximum investigation length ",maximum_investigation)
        return maximum_investigation

    def get_number_of_maximum_investigation(self):
        maximum_investigation_number=self.config.get("account_locators","maximum_investigation_number")
        print("maximum investigation number is",maximum_investigation_number)
        return maximum_investigation_number

    def read_number_of__maximum_investigation(self):
        maximum_investigation_number = self.common_test_data_config.get("Account_Module_Data", "maximum_investigation_number_text")
        print("gives maximum investigation number",maximum_investigation_number)
        return maximum_investigation_number

    def enrollment_groups(self):
        enrollment_groups=self.config.get("account_locators", "Enrollment_groups")
        print("enrollment group is", enrollment_groups)
        return enrollment_groups
    def number_enrollment_groups(self):
        enrollment_groups_number=self.config.get("account_locators","Enrollment_group_number")
        print("enrollments number is ",enrollment_groups_number)
        return enrollment_groups_number

    def number_enrollment_group_text(self):
        enrollment_group_number=self.config.get("Account_Module_Data", "Enrollment_group_number_text")
        print("enrollment group number text is", enrollment_group_number)
        return  enrollment_group_number

    def notification_group(self):
        notification_group = self.config.get("account_locators", "notification_groups_number")
        print("notification group number is", notification_group)
        return notification_group

    def number_of_notification_groups(self):
        number_of_notiification_groups=self.config.get("account_locators","notification_groups_number")
        print("number of notification groups is",number_of_notiification_groups)
        return number_of_notiification_groups
    def get_stations(self):
        stations = self.config.get("account_locators","stations")
        print("stations in accounts ",stations)
        return stations
    def number_of_stations(self):
        number_of_stations = self.config.get("account_locators","number_of_stations")
        print("number of stations",number_of_stations)
        return  number_of_stations
    def get_firstname(self):
        firstname = self.config.get("account_locators","first_name")
        print("getting firstname",firstname)
        return firstname
    def get_comapny_text(self):
        company_text = self.config.get("account_locators","company_text")
        print("company is  firstname",company_text)
        return company_text
    def get_middle_name(self):
        middle_name = self.config.get("account_locators","middle_name")
        print("middle name is ",middle_name)
        return middle_name
    def name_of_middle_name(self):
        name_of_middlename= self.config.get("account_locators","name_of_middlename")
        print("middle name is",name_of_middlename)
        return name_of_middlename
    def get_last_name(self):
        last_name=self.config.get("account_locators","name_of_last_name")
        print("lastname is ",last_name)
        return last_name
    def name_of_lastname(self):
        name_of_lastname=self.config.get("account_locators","name_of_last_name")
        print("name of lastname",name_of_lastname)
        return name_of_lastname
    def get_company(self):
        comapny=self.config.get("account_locators","comapany")
        print("comapny name is ",comapny)
        return comapny
    def name_of_company(self):
        name_of_company = self.config.get("account_locators","name_of_comapny")
        print("name of company is ",name_of_company)
        return name_of_company
    def get_department(self):
        department = self.config.get("account_locators","Department")
        print("deparment is ",department)
        return department
    def name_of_department(self):
        name_of_department=self.config.get("account_locators","name_of_Department")
        print("name of department is ",name_of_department)
        return name_of_department
    def get_title(self):
        title= self.config.get("account_locators","title")
        print("title is ",title)
        return title
    def name_of_title(self):
        name_of_title = self.config.get("account_locators","name_of_title")
        print("name of title is ", name_of_title)
        return name_of_title
    def get_Email(self):
        email = self.config.get("account_locators","Email")
        print("email is ",email)
        return email
    def email_id(self):
        email_id =self.config.get("account_locators","Email_id")
        print("email id is ",email_id)
        return email_id
    def Home_phone(self):
        Home_phone = self.config.get("account_locators","Home_phone")
        print("home phone is ",Home_phone)
        return Home_phone
    def number_of_home_phone(self):
        number_of_home_phone = self.config.get("account_locators","number_of_Home_phone")
        print("number of home phone is ",number_of_home_phone)
        return number_of_home_phone
    def work_phone(self):
        work_phone = self.config.get("account_locators","work_phone")
        print("work phone is ",work_phone)
        return work_phone
    def work_phone_number(self):
        work_phone_number=self.config.get("account_locators","work_phone_number")
        print("work phone number is ",work_phone_number)
        return work_phone_number
    def get_fax(self):
        fax = self.config.get("account_locators","Fax")
        print("fax is ",fax)
        return fax
    def fax_number(self):
        fax_number = self.config.get("account_locators","Fax_number")
        print("fax number is ",fax_number)
        return fax_number
    def get_Address(self):
        Address = self.config.get("account_locators","Address")
        print("address is ",Address)
        return Address
    def Address_name(self):
        address_name=self.config.get("account_locators","address_text")
        print("address details are",address_name)
        return address_name
    def get_address2(self):
        address2 = self.config.get("account_locators","address2")
        print("address 2 is ",address2)
        return address2
    def address2_details(self):
        address2_details = self.config.get("account_locators","address2_details")
        print("address2 details are",address2_details)
        return address2_details
    def get_city(self):
        city=self.config.get("account_locators","city")
        print("city is ",city)
        return city
    def city_name(self):
        city_name = self.config.get("account_locators","name_of_city")
        print("city name is ",city_name)
        return city_name
    def get_state(self):
        state = self.config.get("account_locators","state")
        print("state name is ",state)
        return state
    def state_name(self):
        state_name = self.config.get("account_locators","name_of_state")
        print("name of state is ",state_name)
        return state_name
    def get_zipcode(self):
        zip_code=self.config.get("account_locators","zip_code")
        print("zipcode is ",zip_code)
        return zip_code
    def zipcode_number(self):
        zipcode_number=self.config.get("account_locators","Zipcode_number")
        print("zipcode number is ",zipcode_number)
        return zipcode_number
    def get_timezone(self):
        timezone=self.config.get("account_locators","timezone")
        print("timezone is ",timezone)
        return timezone
    def timezone_by_xpath(self):
        timezone_by_xpath = self.config.get("account_locators","timezone_by_xpath")
        print("timezone by xpath",timezone_by_xpath)
        return timezone_by_xpath
    def get_case_TTL(self):
        case_ttl = self.config.get("account_locators","case_TTL")
        print("case ttl is ",case_ttl)
        return case_ttl
    def case_ttl_seconds(self):
        case_ttl_seconds = self.config.get("account_locators","case_TTL_seconds")
        print("case ttl second is ",case_ttl_seconds)
        return case_ttl_seconds
    def get_subscription(self):
        subscriptions = self.config.get("account_locators","subscription")
        print("subscription is ",subscriptions)
        return subscriptions
    def account_subscription(self):
        account_subscription = self.config.get("account_locators","account_subscription")
        print("account subscription is ",account_subscription)
        return account_subscription
    def view_Image_source_button(self):
        image_source = self.config.get("account_locators","Image_source_button")
        print("image source is ",image_source)
        return image_source
    def account_image_sources_panel_heading(self):
        account_image_sources=self.config.get("account_locators","account_imagesources_panel_heading")
        print("account image sources panel heading",account_image_sources)
        return account_image_sources
    def view_dropdown(self):
        view_dropdown = self.config.get("account_locators","view_dropdown")
        print("view dropdown is ",view_dropdown)
        return view_dropdown
    def location_in_viewdropdown(self):
        location = self.config.get("account_locators","location_in_viewdropdown")
        print("location in view dropdown ",location)
        return location
    def select_checkbox(self):
        checkbox=self.config.get("account_locators","checkbox")
        print("checkbox is ",checkbox)
        return checkbox
    def get_map(self):
        map=self.config.get("account_locators","map")
        print("map is visible",map)
        return map
    def regions_button(self):
        regions=self.config.get("account_locators","regions")
        print("regions is",regions)
        return regions
    def zones_panel_heading(self):
        zones_panel=self.config.get("account_locators","zones_panel_heading")
        print("zones panel heading is",zones_panel)
        return zones_panel
    def details_button(self):
        details=self.config.get("account_locators","Details_button")
        print("details button is ",details)
        return details
    def image_source_panel_heading(self):
        image_source_panel=self.config.get("account_locators","image_source_panel_heading")
        print("image source panel heading is ",image_source_panel)
        return image_source_panel
    def view_location_button(self):
        view_location=self.config.get("account_locators","viewlocation_button_in_imagesource")
        print("view location button is ",view_location)
        return view_location
    def events_location_panel_heading(self):
        events_location=self.config.get("account_locators","events_location_panel_heading")
        print("events location panel heading is ",events_location)
        return events_location

    def get_facefirst_logo_in_map(self):
        facefirst_logo = self.config.get("account_locators","facefirst_logo")
        print("facefirst logo is visible in map",facefirst_logo)
        return facefirst_logo

    def account_details_table_data_list_by_xpath(self):
        account_details_table_data_list_by_xpath = self.config.get("account_locators","account_details_table_data_list_by_xpath")
        print("account_details_table_data_list_by_xpath",account_details_table_data_list_by_xpath)
        return account_details_table_data_list_by_xpath

    def enabled_status_text(self):
        enabled_status_text = self.common_test_data_config.get("Account_Module_Data", "enabled_status_text")
        print("enabled_status_text", enabled_status_text)
        return enabled_status_text

    def enrollments_text(self):
        enrollments_text = self.common_test_data_config.get("Account_Module_Data", "enrollments_text")
        print("enrollments_text", enrollments_text)
        return enrollments_text

    def users_text(self):
        users_text = self.common_test_data_config.get("Account_Module_Data", "users_text")
        print("users_text", users_text)
        return users_text

    def max_investigation_length_text(self):
        max_investigation_length_text = self.common_test_data_config.get("Account_Module_Data", "max_investigation_length_text")
        print("max_investigation_length_text", max_investigation_length_text)
        return max_investigation_length_text

    def enrollment_groups_text(self):
        enrollment_groups_text = self.common_test_data_config.get("Account_Module_Data", "enrollment_groups_text")
        print("enrollment_groups_text", enrollment_groups_text)
        return enrollment_groups_text

    def notification_groups_text(self):
        notification_groups_text = self.common_test_data_config.get("Account_Module_Data", "notification_groups_text")
        print("notification_groups_text", notification_groups_text)
        return notification_groups_text

    def stations_text(self):
        stations_text = self.common_test_data_config.get("Account_Module_Data", "stations_text")
        print("stations_text", stations_text)
        return stations_text

    def first_name_text(self):
        first_name_text = self.common_test_data_config.get("Account_Module_Data", "first_name_text")
        print("first_name_text", first_name_text)
        return first_name_text

    def middle_name_text(self):
        middle_name_text = self.common_test_data_config.get("Account_Module_Data", "middle_name_text")
        print("middle_name_text", middle_name_text)
        return middle_name_text

    def last_name_text(self):
        last_name_text = self.common_test_data_config.get("Account_Module_Data", "last_name_text")
        print("last_name_text", last_name_text)
        return last_name_text

    def company_text(self):
        company_text = self.common_test_data_config.get("Account_Module_Data", "company_text")
        print("company_text", company_text)
        return company_text

    def department_text(self):
        department_text = self.common_test_data_config.get("Account_Module_Data", "department_text")
        print("department_text", department_text)
        return department_text

    def title_text(self):
        title_text = self.common_test_data_config.get("Account_Module_Data", "title_text")
        print("title_text", title_text)
        return title_text

    def email_text(self):
        email_text = self.common_test_data_config.get("Account_Module_Data", "email_text")
        print("email_text", email_text)
        return email_text

    def home_phone_text(self):
        home_phone_text = self.common_test_data_config.get("Account_Module_Data", "home_phone_text")
        print("home_phone_text", home_phone_text)
        return home_phone_text

    def work_phone_text(self):
        work_phone_text = self.common_test_data_config.get("Account_Module_Data", "work_phone_text")
        print("work_phone_text", work_phone_text)
        return work_phone_text

    def fax_number_text(self):
        fax_number_text = self.common_test_data_config.get("Account_Module_Data", "fax_number_text")
        print("fax_number_text", fax_number_text)
        return fax_number_text

    def address_text(self):
        address_text = self.common_test_data_config.get("Account_Module_Data", "address_text")
        print("address_text", address_text)
        return address_text

    def address_2_text(self):
        address_2_text = self.common_test_data_config.get("Account_Module_Data", "address_2_text")
        print("address_2_text", address_2_text)
        return address_2_text

    def city_text(self):
        city_text = self.common_test_data_config.get("Account_Module_Data", "city_text")
        print("city_text", city_text)
        return city_text

    def state_text(self):
        state_text = self.common_test_data_config.get("Account_Module_Data", "state_text")
        print("state_text", state_text)
        return state_text

    def zip_code_text(self):
        zip_code_text = self.common_test_data_config.get("Account_Module_Data", "zip_code_text")
        print("zip_code_text", zip_code_text)
        return zip_code_text

    def timezone_text(self):
        timezone_text = self.common_test_data_config.get("Account_Module_Data", "timezone_text")
        print("timezone_text", timezone_text)
        return timezone_text

    def case_TTL_text(self):
        case_TTL_text = self.common_test_data_config.get("Account_Module_Data", "case_TTL_text")
        print("case_TTL_text", case_TTL_text)
        return case_TTL_text

    def start_enrollments_count(self):
        start_enrollments_count = self.common_test_data_config.get("Account_Module_Data", "start_enrollments_count")
        print("start_enrollments_count", start_enrollments_count)
        return start_enrollments_count

    def end_enrollments_count(self):
        end_enrollments_count = self.common_test_data_config.get("Account_Module_Data", "end_enrollments_count")
        print("end_enrollments_count", end_enrollments_count)
        return end_enrollments_count

    def start_users_count(self):
        start_users_count = self.common_test_data_config.get("Account_Module_Data", "start_users_count")
        print("start_users_count", start_users_count)
        return start_users_count

    def user_accounts_number(self):
        user_accounts_number = self.common_test_data_config.get("common_data", "user_accounts_number")
        print("user_accounts_number", user_accounts_number)
        return user_accounts_number

    def end_users_count(self):
        end_users_count = self.common_test_data_config.get("Account_Module_Data", "end_users_count")
        print("end_users_count", end_users_count)
        return end_users_count

    def start_max_investigation_length_count(self):
        start_max_investigation_length_count = self.common_test_data_config.get("Account_Module_Data", "start_max_investigation_length_count")
        print("start_max_investigation_length_count", start_max_investigation_length_count)
        return start_max_investigation_length_count

    def end_max_investigation_length_count(self):
        end_max_investigation_length_count = self.common_test_data_config.get("Account_Module_Data", "end_max_investigation_length_count")
        print("end_max_investigation_length_count", end_max_investigation_length_count)
        return end_max_investigation_length_count

    def start_enrollment_groups_count(self):
        start_enrollment_groups_count = self.common_test_data_config.get("Account_Module_Data", "start_enrollment_groups_count")
        print("start_enrollment_groups_count", start_enrollment_groups_count)
        return start_enrollment_groups_count

    def end_enrollment_groups_count(self):
        end_enrollment_groups_count = self.common_test_data_config.get("Account_Module_Data", "end_enrollment_groups_count")
        print("end_enrollment_groups_count", end_enrollment_groups_count)
        return end_enrollment_groups_count

    def start_notification_groups_count(self):
        start_notification_groups_count = self.common_test_data_config.get("Account_Module_Data", "start_notification_groups_count")
        print("start_notification_groups_count", start_notification_groups_count)
        return start_notification_groups_count

    def end_notification_groups_count(self):
        end_notification_groups_count = self.common_test_data_config.get("Account_Module_Data", "end_notification_groups_count")
        print("end_notification_groups_count", end_notification_groups_count)
        return end_notification_groups_count

    def start_stations_count(self):
        start_stations_count = self.common_test_data_config.get("Account_Module_Data", "start_stations_count")
        print("start_stations_count", start_stations_count)
        return start_stations_count

    def end_stations_count(self):
        end_stations_count = self.common_test_data_config.get("Account_Module_Data", "end_stations_count")
        print("start_stations_count", end_stations_count)
        return end_stations_count

    def start_email(self):
        start_email = self.common_test_data_config.get("Account_Module_Data", "start_email")
        print("start_email", start_email)
        return start_email

    def end_email(self):
        end_email = self.common_test_data_config.get("Account_Module_Data", "end_email")
        print("end_email", end_email)
        return end_email

    def no_enrollments_message_by_xpath(self):
        no_enrollments_message_by_xpath = self.config.get("account_locators", "count_of_enrollments_by_xpath")
        print("no_enrollments_message_by_xpath", no_enrollments_message_by_xpath)
        return no_enrollments_message_by_xpath

    def count_of_users_by_xpath(self):
        count_of_users_by_xpath = self.config.get("account_locators", "count_of_users_by_xpath")
        print("count_of_users_by_xpath", count_of_users_by_xpath)
        return count_of_users_by_xpath

    def count_of_enrollment_groups_by_xpath(self):
        count_of_enrollment_groups_by_xpath = self.config.get("account_locators", "count_of_enrollment_groups_by_xpath")
        print("count_of_enrollment_groups_by_xpath", count_of_enrollment_groups_by_xpath)
        return count_of_enrollment_groups_by_xpath

    def count_of_notification_groups_by_xpath(self):
        count_of_notification_groups_by_xpath = self.config.get("account_locators", "count_of_notification_groups_by_xpath")
        print("count_of_notification_groups_by_xpath", count_of_notification_groups_by_xpath)
        return count_of_notification_groups_by_xpath

    def count_of_stations_by_xpath(self):
        count_of_stations_by_xpath = self.config.get("account_locators", "count_of_stations_by_xpath")
        print("count_of_stations_by_xpath", count_of_stations_by_xpath)
        return count_of_stations_by_xpath

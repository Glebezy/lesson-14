import os

from allure import step
from selene import browser, be, have

from pages.page import open_page

CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
FILE = os.path.join(DIRECTORY, "..", "resources")


class RegistrationPage:

    def open(self):
        with step("open browser"):
            open_page('/automation-practice-form')
        return self

    def fill_first_name(self, first_name):
        browser.element('[id="firstName"]').clear().type(first_name)

    def fill_last_name(self, last_name):
        browser.element('[id="lastName"]').clear().type(last_name)

    def fill_email(self, email):
        browser.element('[id="userEmail"]').clear().type(email)

    def choose_gender(self, gender):
        browser.element(f'//label[text()="{gender}"]').click()

    def fill_phone(self, phone):
        browser.element('[id="userNumber"]').clear().type(phone)

    def choose_date_of_birth(self, date_of_birth):
        split_date_of_birth = date_of_birth.split()
        day = split_date_of_birth[0]
        month = split_date_of_birth[1].split(',')[0]
        year = split_date_of_birth[1].split(',')[1]

        browser.element('[id="dateOfBirthInput"]').click()

        (browser.element('.react-datepicker__month-select').should(be.visible)
         .element(f'//*[text()="{month}"]').click())
        (browser.element('.react-datepicker__year-select').should(be.visible)
         .element(f'option[value="{year}"]').click())
        (browser.element('.react-datepicker__day').should(be.visible)
         .element(f'//*[text()="{day}"]').click())

    def fill_subjects(self, subjects):
        browser.element('[id="subjectsInput"]').clear()
        for subject in subjects:
            browser.element('[id="subjectsInput"]').type(subject)
            browser.element('[id="react-select-2-option-0"]').click()

    def choose_hobbies(self, hobbies):
        for hobby in hobbies:
            browser.element(f'//label[text()="{hobby}"]').click()

    def upload_picture(self, picture):
        browser.element('[id="uploadPicture"]').send_keys(os.path.abspath(f'{FILE}/{picture}'))

    def fill_address(self, address):
        browser.element('[id="currentAddress"]').clear().type(address.split(',')[0])

        browser.element('[id="state"]').click()
        browser.element(f'//*[contains(text(), "{address.split()[-2]}")]').click()

        browser.element('[id="city"]').click()
        browser.element(f'//*[contains(text(), "{address.split()[-1]}")]').click()

    def submit_form(self):
        with step("submit form"):
            browser.element('[id="submit"]').click()
            return self

    def register(self, user):
        with step("Fill form"):
            self.fill_first_name(user.first_name)
            self.fill_last_name(user.last_name)
            if user.email:
                self.fill_email(user.email)
            self.choose_gender(user.gender)
            self.fill_phone(user.phone_number)
            if user.date_of_birth:
                self.choose_date_of_birth(user.date_of_birth)
            if user.subjects:
                self.fill_subjects(user.subjects)
            if user.hobbies:
                self.choose_hobbies(user.hobbies)
            if user.picture:
                self.upload_picture(user.picture)
            if user.address:
                self.fill_address(user.address)
        self.submit_form()

        return self

    def should_have_registered(self, user):
        with step("Check registration"):
            browser.element("//td[contains(text(), 'Student Name')]/following-sibling::td").should(
                have.text(user.first_name + ' ' + user.last_name))
            if user.email:
                browser.element("//td[contains(text(), 'Student Email')]/following-sibling::td").should(
                    have.text(user.email))
            browser.element("//td[contains(text(), 'Gender')]/following-sibling::td").should(
                have.text(user.gender))
            browser.element("//td[contains(text(), 'Mobile')]/following-sibling::td").should(
                have.text(user.phone_number))

            if user.date_of_birth:
                browser.element("//td[contains(text(), 'Date of Birth')]/following-sibling::td").should(
                    have.text(user.date_of_birth))
            if user.subjects:
                browser.element("//td[contains(text(), 'Subjects')]/following-sibling::td").should(
                    have.text(', '.join(user.subjects)))
            if user.hobbies:
                browser.element("//td[contains(text(), 'Hobbies')]/following-sibling::td").should(
                    have.text(', '.join(user.hobbies)))
            if user.picture:
                browser.element("//td[contains(text(), 'Picture')]/following-sibling::td").should(
                    have.text(user.picture))
            if user.address:
                browser.element("//td[contains(text(), 'Address')]/following-sibling::td").should(
                    have.text(user.address.split(', ')[0]))
                browser.element("//td[contains(text(), 'State and City')]/following-sibling::td").should(
                    have.text(user.address.split(', ')[1]))

    def should_validation_visible(self):
        with step("check validation"):
            browser.element('#firstName').should(have.css_property('border-color', value='rgb(220, 53, 69)'))
            browser.element('#lastName').should(have.css_property('border-color', value='rgb(220, 53, 69)'))
            browser.element('[for^="gender-radio"]').should(have.css_property('border-color', value='rgb(220, 53, 69)'))
            browser.element('#userNumber').should(have.css_property('border-color', value='rgb(220, 53, 69)'))

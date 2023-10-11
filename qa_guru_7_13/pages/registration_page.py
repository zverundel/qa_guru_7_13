import allure
import os.path
from selene import browser, be, by, have
import tests


class RegistrationPage:

    @allure.step("Переход на форму")
    def open(self):
        browser.open('/automation-practice-form')

    @allure.step("Ввод имени")
    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    @allure.step("Ввод фамилиия")
    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    @allure.step("Ввод электронной почты")
    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    @allure.step("Выбор пола")
    def select_gender(self, value):
        browser.element(f'[value={value}] + label').click()
        return self

    @allure.step("Ввод номера телефона")
    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    @allure.step("Выбор года рождения")
    def fill_date_of_birth_year(self, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(year)).click()
        return self

    @allure.step("Ввод месяца рождения")
    def fill_date_of_birth_month(self, month):
        browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(month)).click()
        return self

    @allure.step("Ввод дня рождения")
    def fill_date_of_birth_day(self, day):
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    @allure.step("Выбор предметов")
    def fill_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        return self

    @allure.step("Выбор хобби")
    def fill_hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()
        return self

    @allure.step("Загрузка фото")
    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f"resources/{value}")
            ))
        return self

    @allure.step("Ввод адреса")
    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    @allure.step("Выбор штата")
    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    @allure.step("Выбор города")
    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    @allure.step("Отправка формы")
    def submit(self):
        browser.element('#submit').click()

    @allure.step("Регистрация пользователя")
    def register_user(self, user):
        (
            self
            .fill_first_name(user.first_name)
            .fill_last_name(user.last_name)
            .fill_user_email(user.email)
            .select_gender(user.gender)
            .fill_user_number(user.user_number)
            .fill_date_of_birth_year(user.date_of_birth.strftime('%Y'))
            .fill_date_of_birth_month(user.date_of_birth.strftime('%B'))
            .fill_date_of_birth_day(user.date_of_birth.strftime('%d'))

            .fill_subject(user.subject)
            .fill_hobby(user.hobby)

            .upload_picture(user.upload_picture)

            .fill_current_address(user.current_address)
            .fill_state(user.state)
            .fill_city(user.city)

            .submit()
        )

    @allure.step("Проверка данных")
    def should_register_user(self, user):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.user_number,
                f"{user.date_of_birth.strftime('%d')} {user.date_of_birth.strftime('%B')},{user.date_of_birth.strftime('%Y')}",
                user.subject,
                user.hobby,
                user.upload_picture,
                user.current_address,
                f'{user.state} {user.city}',
            )
        )
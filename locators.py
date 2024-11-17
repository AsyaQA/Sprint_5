from selenium.webdriver.common.by import By


class TestLocators:
    BUTTON_LOGIN_TO_ACCOUNT =  By.XPATH, "//*[text()='Войти в аккаунт']" # Кнопка "Войти в аккаунт"
    REGISTRATION_LINK = By.XPATH, "//*[text()='Зарегистрироваться']" # Ссылка на регистрацию
    ENTRY_FIELD_NAME = By.XPATH, "//fieldset[1]//input[@class='text input__textfield text_type_main-default']" # Поле ввода "Имя"
    ENTRY_FIELD_EMAIL = By.XPATH, "//fieldset[2]//input[@class='text input__textfield text_type_main-default']" # Поле ввода "Email"
    ENTRY_FIELD_PASSWORD = By.XPATH, "//fieldset[3]//input[@class='text input__textfield text_type_main-default']" # Поле ввода "Пароль"
    REGISTER_BUTTON = By.XPATH, "//*[text()='Зарегистрироваться']" # Кнопка "Зарегистрироваться"
    LOGIN_BUTTON = By.XPATH, "//*[text()='Войти']" # Кнопка "Войти"
    PASSWORD_ERROR = By.XPATH, "//*[text()='Некорректный пароль']" # Ошибка "Некорректный пароль"
    ENTRY_FIELD_EMAIL_FOR_LOGIN = By.XPATH, "//fieldset[1]//input[@class='text input__textfield text_type_main-default']" # Поле ввода "Email" на странице входа
    ENTRY_FIELD_PASSWORD_FOR_LOGIN = By.XPATH, "//fieldset[2]//input[@class='text input__textfield text_type_main-default']" # Поле ввода "Пароль" на странице входа
    PLACE_ORDER_BUTTON = By.XPATH, "//*[text()='Оформить заказ']" # Кнопка "Оформить заказ"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and @href='/account']" # Кнопка "Личный кабинет"
    LINK_TO_RESET_PASSWORD = By.XPATH, "//*[text()='Восстановить пароль']" # Ссылка "Восстановить пароль"
    SAVE_BUTTON = By.XPATH, "//*[text()='Сохранить']" # Кнопка "Сохранить"
    LINE_OF_TEXT = By.XPATH, "//*[text()='В этом разделе вы можете изменить свои персональные данные']" # Строка текста в личном кабинете
    BUTTON_CONSTRUCTOR = By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and @href='/']" # Кнопка "Конструктор"
    STELLAR_BURGERS_LOGO = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a" # Логотип Stellar Burgers
    EXIT_BUTTON = By.XPATH, "//*[text()='Выход']" # Кнопка "Выход"
    FILLING_SECTION = By.XPATH, "//*[text()='Начинки']" # Переход "Начинки"
    SAUCES_SECTION = By.XPATH, "//*[text()='Соусы']" # Переход "Соусы"
    BUNS_SECTION = By.XPATH, "//*[text()='Булки']" # Переход "Булки"
    FILLING_SECTION_PARENT = By.XPATH, "//*[text()='Начинки']/parent::div" # Узел-родитель "Начинки"
    SAUCES_SECTION_PARENT = By.XPATH, "//*[text()='Соусы']/parent::div"  # Узел-родитель "Соусы"
    BUNS_SECTION_PARENT = By.XPATH, "//*[text()='Булки']/parent::div"  # Узел-родитель "Булки"







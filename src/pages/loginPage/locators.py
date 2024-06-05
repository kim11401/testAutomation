class LoginPageLocators:
    URL = "/login/login.pang"
    LOCATORS = {
        "USERNAME_INPUT": '//*[@id="login-email-input"]',
        "PASSWORD_INPUT": '//*[@id="login-password-input"]',
        "LOGIN_BUTTON": "button[text()='로그인']",
    }

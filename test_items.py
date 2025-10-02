from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    try:
        add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form button")

        assert add_to_basket_button.is_displayed(), \
            "Кнопка добавления в корзину не найдена на странице или не видна."

        print(f"\nКнопка найдена. Текст кнопки: {add_to_basket_button.text}")

    except Exception as e:
        assert False, f"Тест провален: кнопка добавления в корзину не найдена. Ошибка: {e}"



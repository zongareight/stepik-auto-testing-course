"""
To start by 'pytest --language=es test_items.py'
"""


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_page_have_a_button_for_adding_to_the_basket(browser):
    browser.get(link)
    text = browser.find_element_by_css_selector('.btn.btn-add-to-basket').text
    assert text == 'Añadir al carrito'

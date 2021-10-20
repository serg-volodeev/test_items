link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_found_btn_add_to_basket(browser):
    browser.get(link)
    selector = ".btn-add-to-basket"
    elems = browser.find_elements_by_css_selector(selector)
    assert len(elems) != 0, f"Not found element by css selector '{selector}'"
    assert len(elems) == 1, f"Many elements found by css selector '{selector}'"

from collections import Counter
from utils import Herokuapp


def test_double_pict():
    case = Herokuapp()
    img_list = case.visit_page1()
    img_url = []
    for item in img_list:
        img_url.append(item.get_attribute("src"))
    # print(len(Counter(img_url).values()))
    assert len(Counter(img_url).values()) == 2


def test_upload_file():
    case = Herokuapp()
    case.load_file()
    # print(case.driver.find_element_by_id("uploaded-files").text)
    # print(case.driver.find_element_by_tag_name("h3").text)
    assert case.driver.find_element_by_id("uploaded-files").text == "test_text.txt"
    assert case.driver.find_element_by_tag_name("h3").text == "File Uploaded!"

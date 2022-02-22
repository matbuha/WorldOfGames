from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
CD_Path = "C:/Users/REL/Desktop/devops/chromedriver_win32/chromedriver.exe"


def test_scores_service():
    """it’s purpose is to test our web service. It will get the application
    URL as an input, open a browser to that URL, select the score element in our web page,
    check that it is a number between 1 to 1000 and return a boolean value if it’s true or not."""
    my_driver = webdriver.Chrome(ChromeDriverManager().install())
    my_driver.get("http://127.0.0.1:5000/")
    my_score = my_driver.find_element_by_xpath("/html/body/main/div/div[1]/table/tbody/tr/td[2]").text
    my_int_score = int(my_score)
    print(my_int_score.__bool__())
    return 0 < my_int_score < 1000


test_scores_service()


def main_function():
    """call our tests function. The main function will return -1 as an OS exit
    code if the tests failed and 0 if they passed."""
    if test_scores_service():
        return exit(0)
    else:
        return exit(-1)


main_function()

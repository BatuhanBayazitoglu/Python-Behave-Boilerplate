# Python - Behave - Boilerplate

####Tools and Frameworks
[Selenium Webdriver](https://www.seleniumhq.org/projects/webdriver/), [Python 3.6](https://www.python.org/), [Behave](https://behave.readthedocs.io/en/latest/)

## Requirements and Running Project
######Requirements
Please follow steps in order for running the project without an issue

1. pip must be upgraded and virtual env must be created. More details;
[Installing packages using pip and virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
2. Make sure all requirements are install
```
pip install -r requirements.txt 

```
3. You may need to redownload chromedriver according to the your chrome version.

######Running Project 

1. To run your code on terminal
```
behave features/shoppingCart.feature
```
2. To run responsive test; width and height parameters(in pixel) must be added. Default value is 1920x1080
```
behave -D width=1920 -D height=1080
behave -D width=414 -D height=736
```


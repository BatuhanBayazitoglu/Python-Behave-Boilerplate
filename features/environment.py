from selenium import webdriver

def before_all(context):
    print("Executing before all")
    #Get screen size from userdata(paramaters from cmd)
    context.screen_width = int(context.config.userdata.get("width"))
    context.screen_height = int(context.config.userdata.get("height"))

def before_feature(context, feature):
    driver = webdriver.Chrome(executable_path='venv/chromedriver73')
    context.browser = driver
    context.browser.set_window_size(context.screen_width, context.screen_height)
    print("Before feature\n")

def before_scenario(context,scenario):
    print("Before scenario\n")

def after_scenario(context,scenario):
    print("After scenario\n")

def after_feature(context,feature):
    context.browser.quit()
    print("After feature\n")

def after_all(context):
     print("Executing after all")


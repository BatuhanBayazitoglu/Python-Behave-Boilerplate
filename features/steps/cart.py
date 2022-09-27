from behave import *
import time
from features.helper import helper

use_step_matcher("re")

@given('I go to website "(.*)"')
def step_impl(context, p1="p1",):
    #URL from feature
    context.browser.get(p1)

@when('I search for "(.*)"')
def step_impl(context, p1="p1"):
    #ID for responsive
    if(context.screen_width < 768):
        search_id = "search_word_mobile"
        submit_id = "header-mobile-search-find"
    else:
        search_id = "search_word"
        submit_id = "header_find_button"
    #Searching keywords via search input
    context.browser.find_element_by_id(search_id).send_keys(p1)
    element = context.browser.find_element_by_id(submit_id)
    context.browser.execute_script("arguments[0].click();", element)

@step('I click page "(.*)" and item "(.*)"')
def step_impl(context, p1 = "p1", p2 = "p2"):
    #Changing page if needed and for responsive
    if (context.screen_width < 768):
        for i in range(1, int(p1)):
            element = context.browser.find_element_by_link_text("Sonraki")
            context.browser.execute_script("arguments[0].click();", element)
    else:
        element = context.browser.find_element_by_link_text(p1)
        context.browser.execute_script("arguments[0].click();", element)
    #Getting the right item on the catalog
    product_list = context.browser.find_elements_by_class_name("catalog-seem-cell")
    product_id = str(product_list[int(p2)-1].get_attribute("product-id"))
    product = context.browser.find_element_by_id("item-info-block-" + product_id)
    context.browser.execute_script("arguments[0].click();", product)

@step('I save price for "(.*)"')
def step_impl(context, p1="p1"):
    #Get prices for products
    temp_price = context.browser.find_element_by_css_selector("li.posr > div:nth-child(3) > div:nth-child(1) > strong:nth-child(1)")
    if(p1 == "televizyon"):
        context.tv_price = helper.tl_to_float(str(temp_price.text))
    elif(p1 == "iphone"):
        context.iphone_price = helper.tl_to_float(str(temp_price.text))

@step('I click "(.*)" id "(.*)" without Fixpack')
def step_impl(context, p1 = "p1", p2 = "p2"):
    element = context.browser.find_element_by_id(p2)
    context.browser.execute_script("arguments[0].click();", element)
    #Skip Fixpack if dekstop resolution
    if (context.screen_width > 767):
        element = context.browser.find_element_by_id("ContinueToBasket")
        element.click()

@then("I confirm television_price equals to cart_price")
def step_impl(context):
    # Getting cart price of TV
    temp_price = context.browser.find_element_by_css_selector(".total-price > strong:nth-child(1)")
    context.cart_price = helper.tl_to_float(str(temp_price.text))

    assert (context.tv_price == context.cart_price)

@then("I confirm total_price equals to tv plus iphone")
def step_impl(context):
    total_product = context.iphone_price + context.tv_price
    temp_price = context.browser.find_element_by_class_name("new-price")
    total_cart = helper.tl_to_float(str(temp_price.text))

    assert (total_product == total_cart)

@when('I delete "(.*)"')
def step_impl(context, p1="p1"):
    #Deleting requried(p1) item as needed
    if (context.screen_width > 767):
        product_list = context.browser.find_elements_by_class_name("btn-delete")
    else:
        product_list = context.browser.find_elements_by_class_name("btn-delete-m")
    if(p1 == "televizyon"):
        product = product_list[1]
    else:
        product = product_list[0]
    #Adding a sleep to make sure product is set specially for mobile
    time.sleep(1)
    context.browser.execute_script("arguments[0].click();", product)


@then("I confirm total_price equals to iphone")
def step_impl(context):
    temp_price = context.browser.find_element_by_class_name("new-price")
    total_cart = helper.tl_to_float(str(temp_price.text))

    assert (total_cart == context.iphone_price)

@when("I clear Shopping Cart")
def step_impl(context):
    element = context.browser.find_element_by_class_name("btn-remove-item ")
    context.browser.execute_script("arguments[0].click();", element)
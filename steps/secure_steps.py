from behave import *


@then('secure : I verify that the secure URL is correct')
def step_impl(context):
    context.secure_page.assert_secure_page()

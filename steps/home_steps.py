from behave import *

# given!, when!, and, but, then! - sintaxa gherkin
# given - seteaza situatia initiala
# when - pasii din test
# then - verificarea din test
#
#
@given('home: I am a user on herokuapp home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()


@when('home : I click on  the form_auth button')
def step_impl(context):
    context.home_page.click_form_auth()


@when('home : I click on  the checkboxes button')
def step_impl(context):
    context.home_page.click_checkboxes()


@when('home : I click on  the forgot password button')
def step_impl(context):
    context.home_page.click_forgot_password()
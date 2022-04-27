from behave import *

# given!, when!, and, but, then! - sintaxa gherkin
# given - seteaza situatia initiala
# when - pasii din test
# then - verificarea din test


@given('login: I am a user on herokuapp login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('login: I set my username "{username}"')
def step_impl(context, username):
    context.login_page.insert_username(username)


@when('login: I set my password "{password}"')
def step_impl(context, password):
    context.login_page.insert_password(password)


@when('login: I click on login button')
def step_impl(context):
    context.login_page.click_login_btn()


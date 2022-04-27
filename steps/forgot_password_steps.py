from behave import *


@given('forgot_password: I am a user on herokuapp forgot password page')
def step_impl(context):
    context.forgot_password_page.navigate_to_forgot_password_page()


@when('forgot_password: I set my email "{email}"')
def step_impl(context, email):
    context.forgot_password_page.insert_email(email)


@when('forgot_password: I click on retrieve password button')
def step_impl(context):
    context.forgot_password_page.click_retrieve_password_btn()


@then('forgot_password_page: I see the error message')
def step_impl(context):
    context.forgot_password_page.display_error_message()

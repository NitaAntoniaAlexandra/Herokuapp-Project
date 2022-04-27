Feature: Herokuapp error message displayed

    Background:
      #se ruleaza inainte de fiecare test, se pun in general given-urile
      Given home: I am a user on herokuapp home page
      When home : I click on  the forgot password button



    @herokuapp
    Scenario: error message is displayed
      When forgot_password: I set my email "email"
      When forgot_password: I click on retrieve password button
      Then forgot_password_page: I see the error message


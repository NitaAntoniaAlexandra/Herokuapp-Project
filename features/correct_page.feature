Feature: Herokuapp correct_URL tests

    Background:
      #se ruleaza inainte de fiecare test, se pun in general given-urile
      Given home: I am a user on herokuapp home page
      When home : I click on  the form_auth button


    @herokuapp
    Scenario: correct_URL
      When login: I set my username "tomsmith"
      When login: I set my password "SuperSecretPassword!"
      When login: I click on login button
      Then secure : I verify that the secure URL is correct

    @herokuapp
    Scenario Outline: correct_URL with table data
      When login: I set my username "<username>"
      When login: I set my password "<password>"
      When login: I click on login button
      Then secure : I verify that the secure URL is correct
      Examples:
        | username  | password             |
        | abcde@com | 133                  |
        | tomsmith  | SuperSecretPassword! |
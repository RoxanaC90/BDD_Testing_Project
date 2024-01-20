Feature: Test the functionality of the Login Page

  Background: Open Login Page
    Given I am on the Home Page going to Login Page



@Login1
    Scenario: Check that the greetings message is displayed on the login page
      When I click on the Contul meu
      When I click on Intra in cont button
      When The message "Salut!" is displayed
      Then The greeting message contains "Salut!" message

@Login2
    Scenario: Check that the Logo eMAG is displayed
      When I click on the Contul meu - Scenario 2
      When I click on Intra in cont button - Scenario 2
      Then The Logo "eMAG" is displayed
      Then The Logo message contains "eMAG" message

@Login3

   Scenario: Check an email without @
     When I click on the Contul meu - Scenario 3
     When I click on Intra in cont button - Scenario 3
     When I insert an unregistered email in the mail input - Scenario 3
     Then I click Continue button


@Login4

   Scenario: Check "Câmp obligatoriu" message is displayed when the user tries to login without providing an email
     When I click on the Contul meu - Scenario 4
     When I click on Intra in cont button - Scenario 4
     When I click on the Continue button - Scenario 4
     Then Email error text contains message is displayed - Scenario 4
     Then Email error text contains "Câmp obligatoriu" message - Scenario 4

@Test_url_login_page
    Scenario: Check the functionality of the redirection to the Login Page "https://auth.emag.ro/user/login"
     When I click on the Contul meu - Scenario 5
     When I click on Intra in cont button - Scenario 5
     Then I am redirected to the Login Page "https://auth.emag.ro/user/login"


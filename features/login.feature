Feature: Test the functionality of the Login Page

  Background: Open Login Page
    Given I am on the Home Page going to Login Page



@Login1
    Scenario: Check that the greetings message is displayed on the login page
      When I click on the Contul meu
      When I click on Intra in cont button
      When The message Salut! is displayed
      Then The greeting message contains Salut! message

@Login2
    Scenario: Check that the Logo eMAG is displayed
      When I click on the Contul meu
      When I click on Intra in cont button
      Then The Logo eMAG is displayed
      Then The Logo message contains eMAG message

@Login3

   Scenario: Check that an error message is displayed when the user enters an mail without @
     When I click on the Contul meu
     When I click on Intra in cont button
     When I insert an unregistered email in the mail input
     When I click Continue button
     Then The error meesage is displayed


@Login4

   Scenario: Check "Câmp obligatoriu" message is displayed when the user tries to login without providing an email
     When I click on the Contul meu
     When I click on Intra in cont button
     When I click on the Continue button
     Then Email error text contains message is displayed
     Then Email error text contains "Câmp obligatoriu" message

@Test_url_login_page
    Scenario: Check the functionality of the redirection to the Login Page https://auth.emag.ro/user/login
     When I click on the Contul meu
     When I click on Intra in cont button
     Then I am redirected to the Login Page https://auth.emag.ro/user/login


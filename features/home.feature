Feature:Test the functionality of the Home Page and of the associated functions

  Background: Open Home Page
    Given I am on the Home Page


@Search1
   Scenario: Check that you get at least 10 results when you search for ”Monitoare Gaming”
     When I click on the Search bar
     When I search "Monitoare Gaming" in the Search Bar
     When I click Search button
     Then At least 10 products are displayed


@Search2
  Scenario Outline: Test the search functionality
    When I click on the Search bar
    When I search after "<product_name>"
    When I click Search button
    Then I verify that results contain search "<product_name>"
  Examples:
    | product_name |
    | samsung      |
    | xiaomi       |

  @Filter
   Scenario: Check the functionality of the Filter feature
     When I click on the Search bar
     When I search "Monitoare Gaming" in the Search Bar
     When I click Search button
     When I click the checkbox Diagonala at 23-25 inch
     When I click the checkbox Brand to LG
     When I click the checkbox Brand to Samsung
     When I click the checkbox Pret intre 500 si 1000
     Then All products displayed are between 500 and 1000 lei




@Test_URL
   Scenario: Check the functionality of the redirection to the Cart Page "https://www.emag.ro/cart/products?ref=cart"
     When I click on the Cart button
     Then I am redirected to the Cart Page https://www.emag.ro/cart/products?ref=cart



@Newsletter1
   Scenario: Check "Email incorect" message is displayed when the user tries to subscribe without @ in the contain of the mail subscription(at the end of the page)
   When I set name as "Ion" in the name subscription input box
   When I set email as "test_emag1.itfactory.ro" in the email subscription input box
   When I click aboneaza-ma
   Then The error message "Email incorect" is displayed
   Then The error message contains "Email incorect" message




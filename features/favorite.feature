Feature: Test the functionality of the Favourite page
  Background: Open "I am on the "Robot de bucatarie Bosch MCM3100W, 800 W, bol 2.3 l, 2 viteze, alb/ gri" page
    Given I am on the product page

 @Favorite1
 Scenario: Check the functionality of the "Favourite page"
   When I click Adauga la favorite button
   When I click the favourite button
   Then I verify that the product is in favorite page
   Then I verify the favorite page url
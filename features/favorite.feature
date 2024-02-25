Feature: Test the functionality of the Favourite page
  Background: Open Home Page
    Given I am on the Home Page

 @Favorite1
 Scenario: Check the functionality of the "Favourite page"
   When I click on the Search bar
   When I search "Robot de bucatarie Bosch MCM3100W" in the Search Bar
   When I click Search button
   When I click Adauga la favorite button
   When I click the favourite button
   Then I verify that the product "Robot de bucatarie Bosch MCM3100W" is in favorite page
   Then I verify the favorite page url
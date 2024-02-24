Feature: Test the functionality of the Cart Page

  Background: Open Home Page
    Given I am on the Home Page

   @Cart1
   Scenario: Check the functionality of the "COS"
     When I click on the Search bar
     When I search "Multifunctional inkjet color CANON PIXMA TR4650" in the Search Bar
     When I click Search button
     When I click on the Adauga in cos button
     When I click on the Vezi detalii cos button
     Then The cart must contain "Multifunctional Inkjet" product
     Then I click the button Sterge
     Then "Cosul tau de cumparaturi nu contine produse. Pentru a adauga produse in cos te rugam sa te intorci in magazin." message is displayed

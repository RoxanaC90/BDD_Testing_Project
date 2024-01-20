Feature: Test the functionality of the Cart Page

  Background: Open "Multifunctional inkjet color CANON PIXMA TR4650" printer product Page
    Given I am on the "Multifunctional inkjet color CANON PIXMA TR4650" Page

   @Cart1
   Scenario: Check the functionality of the "COS"
     When I click on the "Adauga in cos" button
     When I click on the "Vezi detalii cos" button
     Then The cart must contain "Multifunctional inkjet color CANON PIXMA TR4650" product
     Then I click the button "Sterge"
     Then "Cosul tau de cumparaturi nu contine produse. Pentru a adauga produse in cos te rugam sa te intorci in magazin." message is displayed

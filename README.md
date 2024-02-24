# BDD_Testing_Project
## Site tested: eMAG.ro

**Design pattern used: Page Object Model(POM)**

**Methodology: behavior driven development (BDD)**

## What I tested on the site eMAG.ro?

The evaluation of the Search Bar, Cart Page, Favourite Page, Login Page and Home Page was my main concern.

## Structure of the project

The project has a structure consisting of a series of files and directories. We find settings for opening Chrome, maximizing the window and a default wait of three seconds in the **"driver"** file. We have the structure of the pages tested in the **"environment". "features", "pages" and "steps"** are the three directories that make up the general structure. The test scenarios are written in Gherkin syntax and can be found in the "features" category. We have general methods for actions such as clicking, finding the element, typing, etc. defined in "pages". The other files contain locators and specific methods for the suggested scenarios. The Gherkin syntax defines the functions of the "steps" directory. This structure organizes the code for automated tests.

## Language, IDE, Libraries and Plugins

I choose testing using **Python programming language with Pycharm IDE**. I used the Selenium, webdriver-manager, behave and behave-html-formatter libraries to automate the interaction with eMAG.ro. The libraries needed for testing were installed from the terminal using the command "pip install".

The plugins needed for running the project are **Cucumber+, Gherkin and INI**. They can be installed fom File-> Settings-> Plugins-> Search.

## The importance of Automating Testing

Automated testing is crucial in software development and brings forth a range of significant advantages, namely: swift error detection, increased developer efficiency, time and resource savings, and early identification of performance issues.

## Methodology: behavior driven development (BDD)

The chosen methodology for this project is BDD (Behavior-Driven Development), which is a software development methodology that can be successfully integrated into automated testing. 

The advantages of using BDD include: facilitating efficient communication among team members; focusing on transforming BDD scenarios into automated tests; automatically documenting functionalities and requirements; and emphasizing customer needs and quality.

## Installation and Execution of the Project

Using the project starts by cloning it from GitHub. Access the project, press the green **"Code"** button, and it is downloaded by accessing the **Download zip.** Then you will have to extract it.
In the final, you can run the project by using the command **"behave -f html -o behave-report.html"** in the terminal. To view the generated report, open the "behave-report.html" file in Chrome.

## Scenarios

Test scenarios chosen for evaluation include:

- Check the functionality of the "COS"

- Check the functionality of the "Favourite page"

- Check that you get at least 10 results when you search for "Monitoare Gaming"

- Test the search functionality

- Check the functionality of the redirection to the Cart Page "https://www.emag.ro/cart/products?ref=cart"

- Check "Email incorect" message is displayed when the user tries to subscript without @ in the contain of the mail subscription(at the end of the page)

- Check that the greetings message is displayed on the login page

- Check that the Logo "eMAG" is displayed

- Check that an error message is displayed when the user enters an mail without @

- Check "Camp obligatoriu" message is displayed when the user tries to log in without providing an email
- Check the functionality of the redirection to the Login Page "https://auth.emag.ro/user/login"

These scenarios cover a variety of situations to ensure that the key functionalities of the application are tested exhaustively and that errors can be identified and handled accordingly.

Happy testing, 

Roxana
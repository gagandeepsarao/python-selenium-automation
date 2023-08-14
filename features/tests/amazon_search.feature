Feature: Tests for amazon search

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for table
    Then Verify search result is correct

  Scenario: Verify that clicking Orders takes to signin
    Given Open Amazon page
    When Click Orders
    Then Verify sign in page opened



  Scenario: Verify that clicking Returns & Orders takes to signin
    Given Open Amazon page
    When Click Returns & Orders
    Then Verify Sign in page opened
      And Verify email input field is present


  Scenario: Verify that clicking on cart icon shows empty cart
    Given Open Amazon page
    When Click cart icon
    Then Verify cart is empty
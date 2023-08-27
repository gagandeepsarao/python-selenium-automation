Feature: Tests for Main page UI

  Scenario: Verify that footer has correct amount of links
    Given Open Amazon page
    Then Verify footer has 36 links

  Scenario: Verify that footer has many links
    Given Open Amazon page
    Then Verify many links are shown in the footer

    #HOMEWORK7 QUESTION1
  Scenario: Verify cart empty text present
    Given Open Amazon page
    When Click on cart icon
    Then Verify Your Amazon Cart is empty text present
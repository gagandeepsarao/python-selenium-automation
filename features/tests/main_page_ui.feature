Feature: Tests for Main page UI

  Scenario: Verify that footer has correct amount of links
    Given Open Amazon page
    Then Verify footer has 36 links

  Scenario: Verify that footer has many links
    Given Open Amazon page
    Then Verify many links are shown in the footer


#Homework 4 Question 1
    Scenario: Verify that Best Sellers page has 5 links
      Given Open Amazon page
      When Click on Best Sellers
      Then Verify 5 links are shown on the top of the page


#Homework 4 Question 2
    Scenario: Verify that added item is present in the cart
      Given Open Amazon page
      When Click on Best Sellers
        And Click on the first product
        And Click on Add to cart button
      Then Verify "Added to Cart" text is displayed on the page
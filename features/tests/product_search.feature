Feature: Test Scenarios for Search functionality

#  Scenario: User can search for a product
#    Given Open Google page
#    When Input Car into search field
#    And Click on search icon
#    Then Product results for Car are shown


  #Homework 5 Test Scenario, step definition is in product_page_steps.py
  Scenario: Verify that a user can click through different colors and chosen a color for a product.
    Given Open Amazon product <product_id> page
    When Click on each color
    Then Verify that one color has been selected
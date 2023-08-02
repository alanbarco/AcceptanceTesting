from behave import given, when, then
from dining import *

@given('the system has meals with prices and topics')
def step_given_system_has_meals(context):
    global meals, prices, topics
    meals, prices, topics = {}, {}, {}
    for row in context.table:
        meal = row['Meal']
        meals[meal] = meal
        prices[meal] = float(row['Price'])
        topics[meal] = row['Topic']

@when('the user displays the menu')
def step_when_user_displays_menu(context):
    print_menu()

@then('the output should contain all meals with prices and topics')
def step_then_output_should_contain_all_meals(context):
    for row in context.table:
        meal = row['Meal']
        price = float(row['Price'])
        topic = row['Topic']
        assert meal in meals
        assert price == prices[meal]
        assert topic == topics[meal]

@given('the system has meals with topics')
def step_given_system_has_meals_topics(context):
    global meals, topics
    meals, topics = {}, {}
    for row in context.table:
        meal = row['Meal']
        meals[meal] = meal
        topics[meal] = row['Topic']

@then('the output should list meals under their correct topics')
def step_then_output_should_list_meals_under_their_correct_topics(context):
    for row in context.table:
        meal = row['Meal']
        topic = row['Topic']
        assert meal in meals
        assert topic == topics[meal]

@given('the user selects a meal')
def step_given_user_selects_a_meal(context):
    global client_order
    client_order = {}
    for row in context.table:
        meal = row['Meal']
        qty = int(row['Quantity'])
        client_order[meal] = qty

@when('the system calculates the total cost')
def step_when_system_calculates_total_cost(context):
    context.total_cost = calc_final_total_cost(client_order)

@then('the total cost should be {expected_total_cost}')
def step_then_total_cost_should_be(context, expected_total_cost):
    assert context.total_cost == float(expected_total_cost)

@given('the user selects multiple meals')
def step_given_user_selects_multiple_meals(context):
    global client_order
    client_order = {}
    for row in context.table:
        meal = row['Meal']
        qty = int(row['Quantity'])
        client_order[meal] = qty

@when('the system generates the order summary')
def step_when_system_generates_order_summary(context):
    display_order_summary(client_order)



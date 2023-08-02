from behave import given, when, then
import dining


@given(u'the system has a meal "{meal}"')
def step_given_system_has_meal(context, meal):
    assert meal in dining.meals, f"{meal} not found in meals list."


@when(u'the user enters a quantity "{quantity}" for the meal')
def step_when_user_enters_quantity_for_meal(context, quantity):
    context.quantity = int(quantity)


@then(u'the system should accept the quantity')
def step_then_system_should_accept_quantity(context):
    try:
        dining.validate_qty(context.quantity)
    except ValueError:
        assert False, f"System did not accept valid quantity: {context.quantity}"
    else:
        assert True


@then(u'the system should not accept the quantity and display an error message')
def step_then_system_should_not_accept_quantity_and_display_error(context):
    try:
        dining.validate_qty(context.quantity)
    except ValueError:
        assert True
    else:
        assert False, f"System incorrectly accepted invalid quantity: {context.quantity}"


@when(u'the user orders a total quantity of "{total_quantity}" meals')
def step_when_user_orders_total_quantity_meals(context, total_quantity):
    context.total_quantity = int(total_quantity)
    context.client_order = {"Pizza familiar": context.total_quantity}


@then(u'the system should apply a "{discount}" percent discount to the total cost')
def step_then_system_should_apply_discount_to_total_cost(context, discount):
    expected_discount = float(discount) / 100
    base_total_cost = dining.calc_base_total_cost(context.client_order)
    actual_discount = dining.calc_qty_discount(
        context.client_order, base_total_cost) / base_total_cost
    assert actual_discount == expected_discount, f"Expected {expected_discount} but got {actual_discount}"


@when(u'the user orders "{quantity}" of the meal')
def step_when_user_orders_quantity_of_meal(context, quantity):
    context.meal_quantity = int(quantity)


@then(u'the system should calculate the total cost as "{total_cost}"')
def step_then_system_should_calculate_total_cost(context, total_cost):
    expected_total_cost = float(total_cost)
    actual_total_cost = dining.calc_meal_total_cost(
        "Pizza familiar", context.meal_quantity)
    assert actual_total_cost == expected_total_cost, f"Expected {expected_total_cost} but got {actual_total_cost}"


@when(u'the user enters a total quantity "{total_quantity}" for the order')
def step_when_user_enters_total_quantity_for_order(context, total_quantity):
    context.total_quantity = int(total_quantity)
    context.client_order = {"Pizza familiar": context.total_quantity}


@then(u'the system should not accept the total quantity and display an error message')
def step_then_system_should_not_accept_total_quantity_and_display_error(context):
    try:
        dining.validate_amount(context.client_order)
    except ValueError:
        assert True
    else:
        assert False, f"System incorrectly accepted invalid total quantity: {context.total_quantity}"

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

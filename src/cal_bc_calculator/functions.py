from numpy import polyfit, polyval

from xlcalculator.xlfunctions import xl
from xlcalculator.xlfunctions.xl import func_xltypes


@xl.register()
@xl.validate_args
# =TREND(known_y's, [known_x's], [new_x's], [const])
def TREND(
    known_ys: func_xltypes.Array,
    known_xs: func_xltypes.Array,
    new_x: func_xltypes.Array,
) -> func_xltypes.Array:
    coefficients = polyfit(
        [n[0].value for n in known_xs.values.tolist()],
        [n[0].value for n in known_ys.values.tolist()],
        1,
    )

    if not isinstance(new_x, func_xltypes.Array):
        predicted_y_for_given_x = polyval(coefficients, [new_x])

        return predicted_y_for_given_x[0]
    else:
        predicted_y_for_given_x = polyval(
            coefficients, [n[0].value for n in new_x.values.tolist()]
        )

        return func_xltypes.Array(predicted_y_for_given_x)

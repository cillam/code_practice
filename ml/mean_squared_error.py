# Track: ML/DS coding
# Problem: Mean Squared Error (MSE)
# Difficulty: Easy warmup
# Approach:
# Time:   |  Space:
#
# MSE is the most common regression loss. Given two equal-length sequences
# of numbers -- `y_true` (the actual values) and `y_pred` (the model's
# predictions) -- return the mean of the squared differences:
#
#     MSE = (1/n) * sum( (y_true_i - y_pred_i)^2 )
#
# Write it in PLAIN PYTHON first (no numpy): a loop or a zip, sum, len.
# numpy IS available in this environment, so once the plain version passes,
# there's a stretch goal at the bottom.
#
# Examples:
#   mse([1, 2, 3], [1, 2, 3])       -> 0.0
#   mse([1, 2, 3], [2, 2, 2])       -> 0.6666666666666666   # (1 + 0 + 1)/3
#   mse([0.5, 1.0], [1.0, 1.0])     -> 0.125                 # (0.25 + 0)/2
#   mse([3], [5])                   -> 4.0

def mse(y_true, y_pred):
    sum = 0
    for true, pred in zip(y_true, y_pred):
        diff_squared = (true - pred)**2
        sum += diff_squared
    return sum / len(y_true)


# STRETCH (optional): once the plain version works, write the vectorized
# numpy one-liner. ML/DS interviews usually expect numpy fluency, so it's
# worth doing both.
#
def mse_np(y_true, y_pred):
    import numpy as np
    return np.mean((np.array(y_true)-np.array(y_pred))**2)


def _close(a, b, tol=1e-9):
    return abs(a - b) < tol


if __name__ == "__main__":
    assert _close(mse([1, 2, 3], [1, 2, 3]), 0.0)
    assert _close(mse([1, 2, 3], [2, 2, 2]), 2/3)
    assert _close(mse([0.5, 1.0], [1.0, 1.0]), 0.125)
    assert _close(mse([3], [5]), 4.0)
    print("passed")

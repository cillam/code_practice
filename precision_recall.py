# Track: ML/DS coding
# Problem: Precision & Recall
# Difficulty: Easy warmup (with a small twist)
# Approach:
# Time:   |  Space:
#
# Two of the most important classification metrics. You're given two
# equal-length lists of 0/1 labels:
#   y_true -- the actual labels (1 = positive, 0 = negative)
#   y_pred -- the model's predicted labels
#
# Return (precision, recall) as a tuple of floats.
#
# Definitions (in terms of the confusion-matrix counts):
#   TP = predicted 1 AND actually 1   (true positive)
#   FP = predicted 1 BUT actually 0   (false positive)
#   FN = predicted 0 BUT actually 1   (false negative)
#
#   precision = TP / (TP + FP)   -- of everything I flagged positive, how much was right?
#   recall    = TP / (TP + FN)   -- of all the real positives, how many did I catch?
#
# The twist: those denominators can be ZERO (e.g. the model predicts no
# positives at all -> TP+FP = 0). Division by zero will crash. By convention,
# return 0.0 for a metric whose denominator is 0.
#
# Write it in plain Python first. numpy vectorized version is the stretch.
#
# Examples:
#   precision_recall([1,1,0,0], [1,0,0,1])  -> (0.5, 0.5)   # TP=1, FP=1, FN=1
#   precision_recall([1,1,1],   [1,1,1])    -> (1.0, 1.0)   # TP=3, FP=0, FN=0
#   precision_recall([0,0],     [0,0])      -> (0.0, 0.0)   # no positives anywhere
#   precision_recall([1,0,1,0], [1,1,1,1])  -> (0.5, 1.0)   # TP=2, FP=2, FN=0

def precision_recall(y_true, y_pred):
    tp_count = 0
    fp_count = 0
    fn_count = 0
    for true, pred in zip(y_true, y_pred):
        if true == 1 and pred == 1:
            tp_count += 1
        if true == 0 and pred == 1:
            fp_count += 1
        if true == 1 and pred == 0:
            fn_count += 1
    if (tp_count + fp_count) != 0:
        precision = tp_count / (tp_count + fp_count)
    else:
        precision = 0.0
    if (tp_count + fn_count) != 0:
        recall = tp_count / (tp_count + fn_count)
    else:
        recall = 0.0
    return (precision, recall)


import numpy as np

def precision_recall_numpy(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    true_positives = np.sum((y_pred == 1) & (y_true == 1))
    false_positives = np.sum((y_pred == 1) & (y_true == 0))
    false_negatives = np.sum((y_pred == 0) & (y_true == 1))

    if (true_positives + false_positives) != 0:
        precision = true_positives / (true_positives + false_positives)
    else:
        precision = 0.0
    if (true_positives + false_negatives) != 0:
        recall = true_positives / (true_positives + false_negatives)
    else:
        recall = 0.0

    return (precision, recall)

def _close(a, b, tol=1e-9):
    return abs(a - b) < tol


if __name__ == "__main__":
    p, r = precision_recall_numpy([1,1,0,0], [1,0,0,1]); assert _close(p,0.5) and _close(r,0.5), (p,r)
    p, r = precision_recall_numpy([1,1,1],   [1,1,1]);   assert _close(p,1.0) and _close(r,1.0), (p,r)
    p, r = precision_recall_numpy([0,0],     [0,0]);     assert _close(p,0.0) and _close(r,0.0), (p,r)
    p, r = precision_recall_numpy([1,0,1,0], [1,1,1,1]); assert _close(p,0.5) and _close(r,1.0), (p,r)
    print("passed")

    p, r = precision_recall([1,1,0,0], [1,0,0,1]); assert _close(p,0.5) and _close(r,0.5), (p,r)
    p, r = precision_recall([1,1,1],   [1,1,1]);   assert _close(p,1.0) and _close(r,1.0), (p,r)
    p, r = precision_recall([0,0],     [0,0]);     assert _close(p,0.0) and _close(r,0.0), (p,r)
    p, r = precision_recall([1,0,1,0], [1,1,1,1]); assert _close(p,0.5) and _close(r,1.0), (p,r)
    print("passed")
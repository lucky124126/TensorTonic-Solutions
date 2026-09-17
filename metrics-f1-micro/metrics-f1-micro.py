def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    tp = sum(t == p for t, p in zip(y_true, y_pred))
    fp = sum(t != p for t, p in zip(y_true, y_pred))
    fn = fp

    if 2 * tp + fp + fn == 0:
        return 0.0

    f1 = (2 * tp) / (2 * tp + fp + fn)

    return round(float(f1), 4)
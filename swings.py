def swing_points(df, n):
    """Подтверждённые swing-точки: экстремум среди n свечей слева и справа."""
    h, l = df.high.values, df.low.values
    highs, lows = [], []
    for i in range(n, len(df) - n):
        if h[i - n:i + n + 1].argmax() == n:
            highs.append((i, h[i]))
        if l[i - n:i + n + 1].argmin() == n:
            lows.append((i, l[i]))
    return highs, lows


def trend_break(df, highs, lows):
    if len(highs) < 2 or len(lows) < 2:
        return 0
    close = df.close.iloc[-1]
    if lows[-1][1] > lows[-2][1] and close > highs[-1][1]:
        return 1
    if highs[-1][1] < highs[-2][1] and close < lows[-1][1]:
        return -1
    return 0


def trend_of(highs, lows):
    if len(highs) < 2 or len(lows) < 2:
        return 0
    (_, h1), (_, h2) = highs[-2], highs[-1]
    (_, l1), (_, l2) = lows[-2], lows[-1]
    if h2 > h1 and l2 > l1:
        return 1
    if h2 < h1 and l2 < l1:
        return -1
    return 0

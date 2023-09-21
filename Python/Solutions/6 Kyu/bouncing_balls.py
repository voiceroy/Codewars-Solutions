def bouncing_ball(h: float, bounce: float, window: float) -> int:
    if 0 < bounce < 1 and window < h:
        count = 1
        ball_height = h * bounce

        while ball_height > window:
            ball_height *= bounce
            count += 2

        return count
    else:
        return -1

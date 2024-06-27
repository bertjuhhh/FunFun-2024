def color_wheel(position):
    if position < 85:
        return (int(position * 3), int(255 - position * 3), 0)
    elif position < 170:
        position -= 85
        return (int(255 - position * 3), 0, int(position * 3))
    else:
        position -= 170
        return (0, int(position * 3), int(255 - position * 3))

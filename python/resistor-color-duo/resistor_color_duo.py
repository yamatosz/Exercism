def value(colors: list):
    _colors = ['black', 'brown', 'red', 'orange', 'yellow',
               'green', 'blue', 'violet', 'grey', 'white']
    return int(f'{_colors.index(colors[0])}{_colors.index(colors[1])}')

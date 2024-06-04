def reduced(s: dict, av: str):
    red = av[av.find('*'):av.find('^')]
    res = ''

    for k, v in s.items():
        if v > 0 and k is not min(s.keys()) :
            res += ' + '
        if v.is_integer():
            s[k] = int(v)
        else:
            s[k] = round(v, 1)
        if v < 0:
            res += ' - ' + str(s[k] * -1) + red + '^' + str(k)
            s[k] = v * -1
        else:
            res += str(s[k]) + ' ' + red + '^' + str(k)
    print(f'Reduced form: {res} = 0')
    return (s)
    
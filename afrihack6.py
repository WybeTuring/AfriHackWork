def nb_year(p0, percent, aug, p):
    i = 0
    while (p0 < p):
        i += 1;
        p0 = p0 + (p0 * (percent/100)) + aug;
    return i
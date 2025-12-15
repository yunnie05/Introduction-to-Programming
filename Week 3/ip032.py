def approximate_sqrt(x, max_error):
    y0= x/2
    yn= 1/2*(y0+(x/y0))
    while (abs(yn-y0)>max_error):
        y0= yn
        yn= 1/2*(y0+(x/y0))
    return yn

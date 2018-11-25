program rotateTest;
var parabola p1;
    hyperbola h1;
    ellipse e1;
# Simple parabola graphing program!
{
    p1 ~ "y = 4x^2 + 2x + 1";
    h1 ~ "-x ^ 2 / 4  + y ^ 2 / 4 = 1";
    e1 ~ "x ^ 2 / 8  + y ^ 2 / 4 = 1";
    # rotate(h1);
    # rotate(h1);
    # plot(h1, green);
    # rotate(e1);
    # rotate(e1);
    
    rotate(p1);
    plot(p1, purple);
}
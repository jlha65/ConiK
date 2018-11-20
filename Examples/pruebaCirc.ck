program circleTest;
var int j;
    circle c1;
    ellipse e1;
    parabola p1;
    hyperbola h1;

{
    j = 1;
    c1 ~ "x^2 + y^2 = 4";
    e1 ~ "x ^ 2/ 5 + y ^ 2 / 10 = 1";
    p1 ~ "y = 4x^2 + x + 1";
    h1 ~ "+x^2 / 16 - y^2 / 12 = 1";
    plot(c1, purple);
    plot(e1, red);
    plot(p1, black);
    plot(h1, green);
    print(c1);
}
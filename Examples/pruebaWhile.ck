program pruebaWhile;
var int i;
    int j;
    float c;
    float b[10];
{
    i = 0;
    j = 10;
    c = 1.4;
    #c = 1;

    
    while(i<j)
    {
        b[i] = c;
        print(b[i]);
        i = i + 1;
        c = c + 1.3;
    }
    print("sale del while");
}
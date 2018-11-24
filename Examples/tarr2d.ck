program bubble;
var int i;
    int j;
    #int a[10];
    int b[4][4];

{
    i = 0;
    j = 0;

    for(i = 0; i < 4; i = i + 1)
    {
        for(j = 0; j < 4; j = j + 1)
        {
            b[i][j] = i*4 + j;
        }
    }

    #print array
    #for(i = 0; i < 4; i = i + 1)
    #{
    #    for(j = 0; j < 4; j = j + 1)
    #    {
    #        #print(i*4 + j);
    #        print(b[i][j]);
    #    }
    #}
    #b[3][3] = 69;
    print("i=");
    print(i);
    print(b[2][3]);
}
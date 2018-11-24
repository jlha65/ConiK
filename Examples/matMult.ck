program bubble;
var int i;
    int j;
    int k;
    int aux;
    int aux1;
    int aux2;
    int aux3;
    int aux4;
    int a[2][3];
    int b[3][2];
    int c[2][2];

{
    #init a
    a[0][0] = 3;
    a[0][1] = -2;
    a[0][2] = 5;
    a[1][0] = 3;
    a[1][1] = 0;
    a[1][2] = 4;

    #init b
    b[0][0] = 2;
    b[0][1] = 3;
    b[1][0] = -9;
    b[1][1] = 0;
    b[2][0] = 0;
    b[2][1] = 4;

    #init c
    c[0][0] = 0;
    c[0][1] = 0;
    c[1][0] = 0;
    c[1][1] = 0;

    print("#######################a:");
    for(i = 0; i < 2; i = i + 1)
    {
        for(j = 0; j < 3; j = j + 1)
        {
            print(a[i][j]);
        }
    }

    print("########################b:");
    for(i = 0; i < 3; i = i + 1)
    {
        for(j = 0; j < 2; j = j + 1)
        {
            print(b[i][j]);
        }
    }

    #rows 1st
    for(i = 0; i < 2; i = i + 1)
    {
        #cols 2nd
        for(j = 0; j < 2; j = j + 1)
        {
            #cols 1st
            for(k = 0; k < 3; k = k + 1)
            {
                aux = a[i][k];
                aux1 = b[k][j];
                aux2 = aux * aux1;
                aux3 = c[i][j];
                aux4 = aux2 + aux3;
                c[i][j] = aux4;
            }
        }
    }

    print("######################c:");
    for(i = 0; i < 2; i = i + 1)
    {
        for(j = 0; j < 2; j = j + 1)
        {
            print(c[i][j]);
        }
    }

}
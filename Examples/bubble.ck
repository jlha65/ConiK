program bubble;
var int i;
    int j;
    float temp;
    float a[10];

{
    a[0] = 13.1;
    a[1] = 2.4;
    a[2] = 25.55;
    a[3] = -66.8;
    a[4] = 27.2;
    a[5] = 1.1;
    a[6] = -7.11;
    a[7] = 0.234;
    a[8] = 55.76;
    a[9] = 21.9;

    print("Before sort: ");

    for(i = 0; i < 10; i = i + 1)
    {
        print(a[i]);
    }

    for(i = 1; i < 10; i = i + 1)
    {
        for(j = 0; j < 10-i; j = j + 1)
        {
            if(a[j] > a[j+1])
            {
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }

    print("After sort: ");

    for(i = 0; i < 10; i = i + 1)
    {
        print(a[i]);
    }
}
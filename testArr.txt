program bubble;
var int i;
    int j;
    int temp;
    int temp2;
    int z;
    int a[10];

{
    a[0] = 13;
    a[1] = 2;
    a[2] = 25;
    a[3] = 66;
    a[4] = 27;
    #a[5] = 1;
    #a[6] = 7;
    #a[7] = 33;
    #a[8] = 55;
    #a[9] = 21;

    j=2;
    temp = 0;

    z = a[4];
    temp = a[j];
    a[j] = a[j+1];
    a[9] = 5;
    print(a[-0]);
    #z = j + 1;
    #temp2 = a[j+1];
    #temp2 = a[z];
    #a[j] = temp2;
    a[j+1] = temp;
    #a[z] = temp;

    #print(a[0]);
    print(a[1]);
    print(temp);
    print(a[j+1]);
    print(a[j]);

}
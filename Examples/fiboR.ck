program fibo;
var int a[7];
    #int b[5][7];
    int c;
    int d;

papa(int n1,int n2, int cont, int stop)
var int n3;
{
    if(cont == 1)
    {
        print("0");
        if(cont < stop)
        {
            proc papa(n1,n2,cont+1,stop);
        }
    }
    else
    {
        if(cont == 2)
        {
            print("1");
            if(cont < stop)
            {
                proc papa(n1,n2,cont+1,stop);
            }
        }
        else
        {
            if(cont > 2)
            {
	        n3 = n1+n2;
                print(n3);
                if(cont < stop)
                {
                    proc papa(n2,n3,cont+1,stop);
                }
            }
        }
    }
}
{
    proc papa(0,1,1,10);
    a[4] = 2;
    #b[3][4] = 5;
    #print(b[3][4]);
}
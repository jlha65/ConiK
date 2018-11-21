program fiboR;
var int c;
    int d;

fibo(int n1,int n2, int cont, int stop)
var int n3;
{
    if(cont == 1)
    {
        print("0");
        if(cont < stop)
        {
            proc fibo(n1,n2,cont+1,stop);
        }
    }
    else
    {
        if(cont == 2)
        {
            print("1");
            if(cont < stop)
            {
                proc fibo(n1,n2,cont+1,stop);
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
                    proc fibo(n2,n3,cont+1,stop);
                }
            }
        }
    }
}
#Main
{
    proc fibo(0,1,1,10);
}
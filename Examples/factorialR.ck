program factorialR;

proc void papa(int x, int cont, int stop)
{
    print(x);
    if(cont < stop)
    {
        proc papa(x*cont,cont+1,stop);
    }
}

{
    proc papa(1,1,50);
}
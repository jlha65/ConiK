program factR2;
var int a;
    #int aux;

#Funcion factorial
proc int factorial(int i)
var int aux;
    int j;
{
    if(i==1)
    {
        return 1;
    }
    print(i * i);
    proc factorial(i-1);
    return 19204*i;
}

#Main
{
    a = proc factorial(10);
    print(a);
}
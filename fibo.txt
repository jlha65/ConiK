program fibo;
var int n;
    int t1;
    int t2;
    int nextTerm;
    int i;

{
    n = 10;
    t1 = 0;
    t2 = 1;
    nextTerm = 0;

    for(i = 1; i < n + 1; i = i + 1){
        if(i == 1) {
            print(t1);
        }
        
        if(i == 2){
            print(t2);
        }

        if(i > 2) {
            nextTerm = t1 + t2;
            t1 = t2;
            t2 = nextTerm;
            print(nextTerm);
        }
    }
}


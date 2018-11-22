program rt;
var int v1;

proc int a(int i1, int i2){
    i1 = i1 * i2;
    if(i1 > 0) {
        return i1;
    }
    return i1 / i2;
}

{
    print(proc a(2, 2));
}
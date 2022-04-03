class Stat{
    public static void main(String args[]){
        Stat1.multi(200,400);
        System.out.println("Multiplication="+m);

    }
}
class Stat1{
    static int m;
    static int multi(int p,int q){
        m=p*q;
        return(m);
    }
}
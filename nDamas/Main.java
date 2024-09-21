
public class Main {



    public static void main(String[] args) {



        //Tablero: matriz de nxn caracteres

        //D dama
        /*
        * D dama
        * 0 nada
        * * amenaza por dama
        *
        *
        * */

        int n = 10;

        Tablero tablero = new Tablero(n);
        Busqueda busqueda = new Busqueda(tablero);

        boolean b = false;


        if(n < 4 && n != 1)
            throw new IllegalArgumentException ("Imposible resolver para n < 4");




        long tini1 = System.currentTimeMillis();
        b = busqueda.busquedaFBruta();
        long tfin1 = System.currentTimeMillis();

        if(b){
            tablero.reset();

            tablero.imprimirTablero();
        }
        else {
            System.out.println("Imposible resolver");
        }

        System.out.println('\n');

        long tini2 = System.currentTimeMillis();
        b = busqueda.busquedaBacktracking();
        long tfin2 = System.currentTimeMillis();

        if(b){
            tablero.reset();

            tablero.imprimirTablero();
        }
        else {
            System.out.println("Imposible resolver");
        }


        System.out.println("Tiempo utilizando fuerza bruta: " + (tfin1 - tini1) + " milisegundos");

        System.out.println("Tiempo utilizando backtracking: " + (tfin2 - tini2) + " milisegundos");
    }
}
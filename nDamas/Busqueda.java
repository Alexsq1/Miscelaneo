public class Busqueda {

    private static Tablero tablero;
    private static int[] arrayBusqueda;

    public Busqueda(Tablero tablero){
        this.tablero = tablero;

        arrayBusqueda = new int[tablero.n + 1];


    }

    public static boolean busquedaFBruta(){
        for(int i = 0; i < arrayBusqueda.length; i++)
            arrayBusqueda[i] = i;
        return busquedaFBrutaRec(tablero.n + 1);
    }

    public static boolean busquedaFBrutaRec(int n){

        //bucle:
        /*
        bucle (algoritmo de Heap, combinatorio)
        avanzar dama

        comprobar
        * */

        boolean b = false;

        if(n == 1){

            for(int i = 1; i < arrayBusqueda.length; i++)
                tablero.casillasDama[i][1] = arrayBusqueda[i];

            return comprobar();
        }
        else {
            for (int i = 1; !b && i < n; i++){

                b = b || busquedaFBrutaRec(n - 1);

                if(n % 2 == 0){

                    int tmp = arrayBusqueda[i];
                    arrayBusqueda[i] = arrayBusqueda[n - 1];
                    arrayBusqueda[n - 1] = tmp;

                }
                else {

                    int tmp = arrayBusqueda[1];
                    arrayBusqueda[1] = arrayBusqueda[n - 1];
                    arrayBusqueda[n - 1] = tmp;
                }
            }
        }
        return b;
    }

    public static boolean comprobar(){

        boolean b = true;

        //Damas consecutivas
        for(int i = 1; b && i < tablero.n; i++){
            if(Math.abs(tablero.casillasDama[i][1] - tablero.casillasDama[i + 1][1]) <= 1)
                b = false;
        }

        //Resto de damas
        for(int i = 1; b && i < tablero.n - 1; i++){

            for(int j = i + 2; b && j <= tablero.n; j++){
                b = !colisionan(i, j);
            }
        }
        return b;
    }

    public static boolean busquedaBacktracking(){


        for(int i = 1; i <= tablero.n; i++){
            arrayBusqueda[i] = 0;
        }

        boolean b = false;
        int damasAjustadas = 0;
        //long iters = 0;
        //long maxIters = factorial(tablero.n);



        while (!b){

            int damaAjustar = damasAjustadas + 1;
            int pre = arrayBusqueda[damaAjustar];

            arrayBusqueda[damaAjustar] = 0;
            volcado();
            tablero.reset();


            arrayBusqueda[damaAjustar] = pre + 1;
            //arrayBusqueda[damaAjustar]++;

            int colProbando = arrayBusqueda[damaAjustar];

            while (arrayBusqueda[damaAjustar] <= tablero.n &&
                    tablero.tablero[damaAjustar][colProbando] != '0'){

                //Idea usar el resumen anterior

                arrayBusqueda[damaAjustar]++;
                colProbando++;
            }

            if(arrayBusqueda[damaAjustar] > tablero.n){

                //Si me he pasado (probado todas las opciones y sin futuro)
                // : descarto y volver para atrás

                arrayBusqueda[damaAjustar] = 0;
                damasAjustadas--;
            }
            else {

                //Si no, reviso si esta posición tiene futuro

                volcado();
                int[] libres = tablero.reset();
                int[] resumen = minLibres(libres);

                if (resumen[1] != 0) {//posición sin futuro

                    //Creo que caso innecesario
                    damasAjustadas++;

                }

                if (damasAjustadas == tablero.n) {
                    b = comprobar();
                }
            }
        }


        return b;
    }

    public static boolean busquedaBackTrackingR(int n){

        return true;
    }

    private static int[] minLibres(int[] libres){

        //De las damas que quedan por poner, mira los huecos
        //libres donde podría ir
        int[] par = new int[2];
        //(fila, valor)
        par[1] = tablero.n + 1;

        for(int i = 1; i < libres.length; i++){
            if(arrayBusqueda[i] == 0 && libres[i] < par[1]){
                par[0] = i;
                par[1] = libres[i];
            }
        }
        return par;
    }

    public static void volcado(){

        for(int i = 1; i < arrayBusqueda.length; i++)
            tablero.casillasDama[i][1] = arrayBusqueda[i];
    }


    public static boolean colisionan(int i, int j){

        return Math.abs(i - j) == Math.abs(tablero.casillasDama[i][1] - tablero.casillasDama[j][1]);
    }

    public static int factorial(int n){
        if(n == 1)
            return n;
        else
            return n * factorial(n - 1);
    }
}

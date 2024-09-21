public class Tablero {

    public static int n;
    public static char[][] tablero;
    public static int[][] casillasDama;

    public Tablero(int n){

        this.n = n;
        tablero = new char[n + 1][n + 1];
        casillasDama = new int[n + 1][2];

        for(int i = 0; i <= n; i++) {
            casillasDama[i][0] = i;
            casillasDama[i][1] = i;
        }
    }

    public int[] reset(){

        //Resetea y devuelve el número de
        //columnas libres de cada fila

        int[] libres = new int[n + 1];

        for(int i = n; i > 0; i--){
            for(int j = 1; j <= n; j++){


                if(casillasDama[i][1] == j)
                    tablero[i][j] = 'D';
                else if(damaAmenaza(i, j))
                    tablero[i][j] = '*';
                else{
                    tablero[i][j] = '0';
                    libres[i]++;
                }
            }
        }
        return libres;
    }

    public static boolean damaAmenaza(int fc, int cc){

        boolean b = false;

        if(casillasDama[fc][1] != 0)
            b = true;

        for(int i = 1; i <= n && !b; i++){

            if(casillasDama[i][1] != 0){

                if(casillasDama[i][1] == cc || Math.abs(fc - i) == Math.abs(cc - casillasDama[i][1]))
                    b = true;
            }
        }
        return b;
    }

    public void imprimirTablero(){

        for(int i = n; i > 0; i--){
            for(int j = 1; j <= n; j++){
                System.out.print(tablero[i][j] + " ");
            }
            System.out.println();
        }
    }
}

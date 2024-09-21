public class Main {
    static int[][] tablero = new int[9][9];
    //Fila/columna 0 no usar
    public static void main(String[] args) {

        find();

    }
    public static void find(){
        if(findR(1, 8, 1))
            imprimirTablero();
    }

    public static boolean findR(int i, int j, int n){

        tablero[i][j] = n;

        if(n == 64){

            return true;
        }

        int[][] casillasSaltoCaballo = saltoCaballo(i, j);

        if(casillasSaltoCaballo[0][0] == 0) {

            tablero[i][j] = 0;
            return false;
        }

        boolean var = false;

        for(int k = 0; casillasSaltoCaballo[0][k] != 0 && !var; k++){

            var = findR(casillasSaltoCaballo[0][k], casillasSaltoCaballo[1][k], n + 1);
        }

        if(!var)
            tablero[i][j] = 0;

        return var;
    }

    public static int[][] saltoCaballo(int i, int j){

        int[] dif1 = {1, -1};
        int[] dif2 = {2, -2};

        int[][] casillas = new int[2][8];
        int k = 0;

        for(int casx = 0; casx < 2; casx++){
            for(int casy = 0; casy < 2; casy++){

                int i2 = i + dif1[casx];
                int j2 = j + dif2[casy];


                int i3 = i + dif2[casy];
                int j3 = j + dif1[casx];
/*
                if(esquina(i2, j2) && tablero[j][i] != 0) {
                    i2 = 0;
                    j2 = 0;
                }

                if(esquina(i3, j3) && tablero[j][i] != 0) {
                    i3 = 0;
                    j3 = 0;
                }


 */
                if(enRango(i2, j2) && tablero[i2][j2] == 0){

                    casillas[0][k] = i2;
                    casillas[1][k] = j2;
                    k++;
                }
                if(enRango(i3, j3) && tablero[i3][j3] == 0){

                    casillas[0][k] = i3;
                    casillas[1][k] = j3;
                    k++;
                }
            }
        }

        return casillas;


    }

    public static boolean enRango(int i, int j){

        return i > 0 && i < 9 && j > 0 && j < 9;
    }

    public static void imprimirTablero(){

        for(int i = 1; i < 9; i++) {
            for (int j = 8; j > 0; j--) {

                if (tablero[i][j] < 10)
                    System.out.print(" ");

                System.out.print(tablero[i][j] + "  ");
            }
            System.out.println();
        }
    }

    public static void imprimirMatriz(int matriz[][]){

        for(int i = 1; i < matriz.length; i++) {
            for (int j = 1; j < matriz[0].length; j++) {

                if(matriz[i][j] < 10)
                    System.out.print(" ");
                System.out.print(matriz[i][j] + "  ");

            }
            System.out.println();
        }
    }

    public static boolean esquina(int i, int j){

        return (i == 0 || i == 8) && (j == 0 || j == 8);
    }
}
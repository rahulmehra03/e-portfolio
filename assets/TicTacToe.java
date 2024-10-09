import java.util.Scanner;
import java.util.Random;

public class TicTacToe {
    static char[][] board = {
        {'1', '2', '3'},
        {'4', '5', '6'},
        {'7', '8', '9'}
    };
    static char player = 'X';
    static char computer = 'O';
    static Random random = new Random();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int moves = 0;
        boolean gameWon = false;

        while (!gameWon && moves < 9) {
            printBoard();
            if (moves % 2 == 0) {  // Player's turn
                System.out.println("Your turn! Enter a number (1-9) to make your move:");
                int move = scanner.nextInt();
                if (isValidMove(move)) {
                    makeMove(move, player);
                    moves++;
                    if (checkWin(player)) {
                        gameWon = true;
                        printBoard();
                        System.out.println("You win!");
                    }
                } else {
                    System.out.println("Invalid move, try again.");
                    continue;
                }
            } else {  // Computer's turn
                int move = getRandomMove();
                makeMove(move, computer);
                System.out.println("Computer chose: " + move);
                moves++;
                if (checkWin(computer)) {
                    gameWon = true;
                    printBoard();
                    System.out.println("Computer wins!");
                }
            }
        }
        
        if (!gameWon) {
            printBoard();
            System.out.println("It's a draw!");
        }

        scanner.close();
    }

    public static void printBoard() {
        System.out.println("-------------");
        for (int i = 0; i < 3; i++) {
            System.out.print("| ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " | ");
            }
            System.out.println();
            System.out.println("-------------");
        }
    }

    public static boolean isValidMove(int move) {
        int row = (move - 1) / 3;
        int col = (move - 1) % 3;
        return (move >= 1 && move <= 9) && (board[row][col] != 'X' && board[row][col] != 'O');
    }

    public static void makeMove(int move, char symbol) {
        int row = (move - 1) / 3;
        int col = (move - 1) % 3;
        board[row][col] = symbol;
    }

    public static int getRandomMove() {
        int move;
        do {
            move = random.nextInt(9) + 1;
        } while (!isValidMove(move));
        return move;
    }

    public static boolean checkWin(char symbol) {
        // Check rows and columns
        for (int i = 0; i < 3; i++) {
            if ((board[i][0] == symbol && board[i][1] == symbol && board[i][2] == symbol) ||
                (board[0][i] == symbol && board[1][i] == symbol && board[2][i] == symbol)) {
                return true;
            }
        }

        // Check diagonals
        if ((board[0][0] == symbol && board[1][1] == symbol && board[2][2] == symbol) ||
            (board[0][2] == symbol && board[1][1] == symbol && board[2][0] == symbol)) {
            return true;
        }

        return false;
    }
}
#include <iostream>
#include <ncurses.h>
#include "paddle.cpp"
#include "ball.cpp"

int board_length=20, board_height=10;
int player1_x=1, player2_x=(board_length - 2);
int paddle_size=((3 * board_height) / board_height);


class Board{
private:
  int length, height;
  Paddle player1, player2;
  Ball ball;
  bool left_board;              //signals the ball leaving the board
public:
  Board() : length(board_length), height(board_height), player1(player1_x, paddle_size),
            player2(player2_x, paddle_size), ball(), left_board(false) {
    initscr(); cbreak(); keypad(stdscr, true); draw();}
  void input(){                  //input part
    int key = getch();
    switch (key) {
      case KEY_UP: player2.moveUp(); break;
      case KEY_DOWN: player2.moveDown(); break;
      case 'z': player1.moveUp(); break;
      case 's': player1.moveDown(); break;
    }
  }
  void update() {            //logic part
    switch (ball.getX()) {
      case 1: {
        if (ball.getY() <= player1.getY() && player1.getY() <= ball.getY()+2) ball.paddleBounce(player1.getY());
        else {left_board = true;} break;
      }
      case 18: {
        if (ball.getY() <= player2.getY() && player2.getY() <= ball.getY()+2) ball.paddleBounce(player2.getY());
        else {left_board = true;} break;
      }
    }
    switch (ball.getY()) {
      case 0: ball.wallBounce(); break;
      case 9: ball.wallBounce(); break;
    }
    ball.update();
  }
  void draw() {                  //UI part
    erase();
    mvaddch(ball.getX(), ball.getY(), 'o');
    for (int i=0; i<3; ++i){
      mvaddch(player1.getX(), player1.getY()+i, '-');
      mvaddch(player2.getX(), player2.getY()+i, '-');
    }
  }
  // void restartGame() {};
  void runGame() {
    while (!left_board) { input(); update(); draw();}
    // restartGame();
    endwin();
  }
};

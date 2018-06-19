#include <iostream>
#include <ncurses.h>
#include "paddle.cpp"
#include "ball.cpp"


class Board{
private:
  int length, height;
  Paddle player1, player2;
  Ball ball;
  bool left_board;              //signals the ball leaving the board
public:
  Board() : length(20), height(10), ball(), player1(1), player2(18), left_board(false) {
    initscr(); cbreak(); noecho(); keypad(stdscr, true); draw();}
  void input(){                  //input part
    int key = getch();
    switch (key) {
      case KEY_UP: player2.moveUp(); break;
      case KEY_DOWN: player2.moveDown(); break;
      case 'z': player1.moveUp(); break;
      case 's': player1.moveDown(); break;
      default: std::cout << "Wrong key" << std::endl;
    }
  }
  void ballUpdate() {            //logic part
    switch (ball.getX()) {
      case 1: {
        if (ball.getY() <= player1.getY() <= ball.getY()+2) ball.paddleBounce(player1.getY());
        else {left_board = true;} break;
      }
      case 18: {
        if (ball.getY() < player2.getY() < ball.getY()+2) ball.paddleBounce(player2.getY());
        else {left_board = true;} break;
      }
      // default: std::cout << "still moving to the side" << std::endl;
    }
    switch (ball.getY()) {
      case 0: ball.wallBounce(); break;
      case 9: ball.wallBounce(); break;
      // default: std::cout << "still moving up and down" << std::endl;
    }
    ball.update();
  }
  void draw() {                  //UI part
    erase();
    mvaddch(ball.getX(), ball.getY(), 'o');
    for (unsigned i=0; i<3; ++i){
      mvaddch(player1.getX(), player1.getY()+i, '-');
      mvaddch(player2.getX(), player2.getY()+i, '-');
    }
  }
  // void restartGame() {};
  void runGame() {
    while (!left_board) { input(); ballUpdate(); draw();}
    // restartGame();
    endwin(); refresh();
  }
};

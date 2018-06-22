#include <iostream>
#include <cstdlib>

enum Directions {UPRIGHT=0, UPLEFT=1, DOWNRIGHT=2, DOWNLEFT=3, RIGHT=4, LEFT=5};


class Ball{
private:
  int x, y, direction;
public:
  Ball() : x(9), y(4), direction(1) {
    int modifier = rand() % 2; x = x + modifier;
    modifier = rand() % 2; y = y + modifier;
    modifier = rand() % 4; direction = direction + modifier;
  }
  int getX(){return x;}
  int getY(){return y;}
  // int getSpeed(){return speed;}
  int getDirection(){return direction;}
  void update(){
    switch(direction){
      case RIGHT: ++x; break;
      case UPRIGHT: ++x; ++y; break;
      case UPLEFT: --x; ++y; break;
      case DOWNRIGHT: ++x; --y; break;
      case DOWNLEFT: --x; --y; break;
      case LEFT: --x; break;
      // default: std::cout << "Wrong direction code" << std::endl;
    }
  }
  // void speedUp(){if (speed < 5) ++speed;} //speed up with time too
  void paddleBounce(int paddleY){
    if (x == 1) {                         //player1 side
      if (y == paddleY+1) direction = 4;  //go RIGHT
      else --direction;                   //3 -> 2 or 1 -> 0
    }
    else {                                //player2 side
      if (y == paddleY+1) direction = 5;  //go LEFT
      else ++direction;                   //0 -> 1 or 2 -> 3
    }
  }
  void wallBounce(){
    direction = (direction + 2)%4;        //0 <-> 2 or 1 <-> 3
  }
};

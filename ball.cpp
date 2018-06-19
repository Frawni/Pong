#include <iostream>
#include <cstdlib>

enum Directions {RIGHT, UPRIGHT, UPLEFT, DOWNRIGHT, DOWNLEFT, LEFT};


class Ball{
private:
  int x, y, direction;
  bool bouncing;
public:
  Ball() : x(9), y(4), direction(1), bouncing(false) {
    int modifier = rand() % 2; x = x + modifier;
    modifier = rand() % 2; y = y + modifier;
    modifier = rand() % 4; direction = direction + modifier;
  }
  int getX(){return x;}
  int getY(){return y;}
  // int getSpeed(){return speed;}
  int getDirection(){return direction;}
  bool isBouncing(){return bouncing;}
  void update(){
    if (bouncing) {
      std::cout << bouncing << std::endl;
      bouncing = false;         //passes for a timeframe to bounce on surface
    }
    else {
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
  }
  // void speedUp(){if (speed < 5) ++speed;} //speed up with time too
  void paddleBounce(int paddleY){
    bouncing = true;
    if (x == 1) {                         //player1 side
      if (y == paddleY+1) direction = 0;  //go RIGHT
      else --direction;                   //4 -> 3 or 2 -> 1
    }
    else {                                //player2 side
      if (y == paddleY+1) direction = 5;  //go LEFT
      else ++direction;                   //1 -> 2 or 3 -> 4
    }
  }
  void wallBounce(){
    bouncing = true;
    direction = (direction + 2)/5;        //1 <-> 4 or 3 <-> 5
  }
};

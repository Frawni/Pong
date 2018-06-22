#include <iostream>


class Paddle{
private:
  int x, y, size;
public:
  // Paddle() : x(), y(), size() x{}
  Paddle(int x_) : x(x_), y(3), size(3) {}
  int getX() {return x;}
  int getY() {return y;}
  void moveUp() {if (y < 7) ++y;}
  void moveDown() {if (y > 0) --y;}
};

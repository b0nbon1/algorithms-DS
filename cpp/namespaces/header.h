#ifndef FILE
#define FILE

struct Rectangle
{
  double width;
  double length;
};

namespace utilz
{
  double area(double length, double width);

  double area(double length);

  double area(Rectangle rectangle);

  double pow(double base, int pow);
}

#endif

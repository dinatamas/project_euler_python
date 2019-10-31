//#include "stdio.h"
#include <cstdint>
#include <iostream>

int main()
{
  int64_t toplen = 1;
  int64_t top = 1;
  int64_t counter, n;

  for (int64_t i = 500000; i < 999999; ++i) {
    counter = 0;
    n = i;
    while (n != 1) {
      if (n & 1) {
        n = (n * 3 + 1) / 2;
        counter += 2;
      }
      else {
        n = n / 2;
        counter += 1;
      }
    }
    if (counter > toplen) {
      toplen = counter;
      top = i;
      //printf("%d -> %d\n", top, toplen);
      std::cout << top << " -> " << toplen << std::endl;
    }
  }

  return 0;
}

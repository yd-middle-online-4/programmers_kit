#include <stdio.h>

void func (int y)
{
    y = 10;
}
int main(void)
{
    int x = 5;
    func(x);
    printf("%i\n", x);
}

using System;

namespace Practice_C_sharp
{
    class Program
    {
        public static void Main(string[] args)
        {
            for (int a = 1; a <= 1000; a++)
            {
                for (int b = 1; b <= 1000; b++)
                {
                    int c = 1000 - a - b;

                    if (a * a + b * b == c * c)
                    {
                        Console.WriteLine(a * b * c);
                        return;
                    }
                }
            }
        }
    }
}

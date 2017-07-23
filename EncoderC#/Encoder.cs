using System;

public class RomanConvert
{
    int x;
    String ans = ""; 

    String[] numerals = new String[] {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    int[] values = new int[] {1000,900,500,400,100,90,50,40,10,9,5,4,1};

    public static string Solution(int n)
    {
        do
        {
            for (i = 0; i < numerals.Length; i++)
            {
                x = n / values[i];

                for (j = 0; j < x; j++)
                {
                    ans += numerals[i];
                }
                n -= x * values[i];
            }
        } while (n > 0);
        return ans;
    }
}

//1
/*using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");
    }
}*/

//2
/*using System;

class Program
{
    static void Main()
    {
        int a = 10;
        double b = 10.5;
        char c = 'A';
        bool d = true;

        Console.WriteLine(a);
        Console.WriteLine(b);
        Console.WriteLine(c);
        Console.WriteLine(d);
    }
} 
*/
//3
/*using System;
class Program 
{
    static void Main()
    {
        int num = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("You entered: " + num);
    }
}*/

//4

/*using System;

class Program
{
    static void Main()
    {
        int a = Convert.ToInt32(Console.ReadLine());
        int b = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine(a + b);
    }
} */


//5

/*using System;

class Program
{
    static void Main()
    {
        double celsius = Convert.ToDouble(Console.ReadLine());

        double fahrenheit = (celsius * 9 / 5) + 32;

        Console.WriteLine(fahrenheit);
    }
}  */

//6

/*using System;

class Program
{
    static void Main()
    {
        int a = 10;
        int b = 20;
        int temp;

        temp = a;
        a = b;
        b = temp;

        Console.WriteLine(a);
        Console.WriteLine(b);
    }
} */

//7
/*using System;

class Program
{
    static void Main()
    {
        int a = 10;
        int b = 20;

        a = a + b;
        b = a - b;
        a = a - b;

        Console.WriteLine(a);
        Console.WriteLine(b);
    }
} */


//8

/*using System;

class Program
{
    static void Main()
    {
        Console.WriteLine(sizeof(int));
        Console.WriteLine(sizeof(double));
        Console.WriteLine(sizeof(float));
    }
}*/

//9 implicit conversion

/*using System;

class Program
{
    static void Main()
    {
        int a = 10;

        double b = a;

        Console.WriteLine(b);
    }
} */

//10 explicit conversion

/*using System;

class Program
{
    static void Main()
    {
        double a = 10.75;

        int b = (int)a;

        Console.WriteLine(b);
    }
} */

//11

/*using System;

class Program
{
    static void Main()
    {
        double radius = Convert.ToDouble(Console.ReadLine());

        double area = Math.PI * radius * radius;

        Console.WriteLine(area);
    }
} */

//12

/*using System;

class Program
{
    static void Main()
    {
        double p = 1000;
        double r = 5;
        double t = 2;

        double si = (p * r * t) / 100;

        Console.WriteLine(si);
    }
} */

//13

/*using System;

class Program
{
    static void Main()
    {
        int n = Convert.ToInt32(Console.ReadLine());

        if (n % 2 == 0)
            Console.WriteLine("Even");
        else
            Console.WriteLine("Odd");
    }
} */

//14

/*using System;

class Program
{
    static void Main()
    {
        int a = 10;
        int b = 20;

        if (a > b)
            Console.WriteLine(a);
        else
            Console.WriteLine(b);
    }
} */

//15

/*using System;

class Program
{
    static void Main()
    {
        int a = 10;
        int b = 30;
        int c = 20;

        if (a > b && a > c)
            Console.WriteLine(a);
        else if (b > c)
            Console.WriteLine(b);
        else
            Console.WriteLine(c);
    }
}*/

//16

/*using System;

class Program
{
    static void Main()
    {
        double num = 2;
        double power = 3;

        double result = Math.Pow(num, power);

        Console.WriteLine(result);
    }
} */

//17

/*using System;

class Program
{
    static void Main()
    {
        double num = 25;

        double result = Math.Sqrt(num);

        Console.WriteLine(result);
    }
} */

//18

/*using System;

class Program
{
    static void Main()
    {
        Random rand = new Random();

        Console.WriteLine(rand.Next(1, 101));
    }
} */

//19

/*using System;

class Program
{
    static void Main()
    {
        int num = Convert.ToInt32(Console.ReadLine());

        if (num % 5 == 0 && num % 11 == 0)
            Console.WriteLine("Divisible");
        else
            Console.WriteLine("Not divisible");
    }
} */

//20

/*using System;

class Program
{
    static void Main()
    {
        int a = 20;
        int b = 3;

        Console.WriteLine("Quotient = " + a / b);
        Console.WriteLine("Remainder = " + a % b);
    }
} */

//21

/*using System;

class Program
{
    static void Main()
    {
        string text = Console.ReadLine();

        Console.WriteLine(text.Length);
    }
} */

//22

/*using System;

class Program
{
    static void Main()
    {
        string text = Console.ReadLine();

        Console.WriteLine(text.ToUpper());
        Console.WriteLine(text.ToLower());
    }
} */

//23

/*using System;

class Program
{
    static void Main()
    {
        string text = "I love C Sharp";

        if (text.Contains("love"))
            Console.WriteLine("Found");
        else
            Console.WriteLine("Not found");
    }
} */

//24

/*using System;

class Program
{
    static void Main()
    {
        string text = Console.ReadLine();

        for (int i = text.Length - 1; i >= 0; i--)
        {
            Console.Write(text[i]);
        }
    }
} */

//25

/*using System;

class Program
{
    static void Main()
    {
        string str1 = "Hello";
        string str2 = "Hello";

        if (str1 == str2)
            Console.WriteLine("Equal");
        else
            Console.WriteLine("Not equal");
    }
} */

//26

/*using System;

class Program
{
    static void Main()
    {
        string str = Console.ReadLine();

        string rev = "";

        for (int i = str.Length - 1; i >= 0; i--)
        {
            rev += str[i];
        }

        if (str == rev)
            Console.WriteLine("Palindrome");
        else
            Console.WriteLine("Not palindrome");
    }
} */

//27 count vowels

/*using System;

class Program
{
    static void Main()
    {
        string str = Console.ReadLine();

        int count = 0;

        foreach (char ch in str)
        {
            if (ch == 'a' || ch == 'e' || ch == 'i' ||
                ch == 'o' || ch == 'u')
            {
                count++;
            }
        }

        Console.WriteLine(count);
    }
} */

//28

/*using System;

class Program
{
    static void Main()
    {
        string str = Console.ReadLine();

        str = str.Replace(" ", "-");

        Console.WriteLine(str);
    }
}  */

//29

/*using System;

class Program
{
    static void Main()
    {
        string str = "Programming";

        Console.WriteLine(str.Substring(0, 5));
    }
} */

//30

/*using System;

class Program
{
    static void Main()
    {
        string firstName = "Nabil";
        string lastName = "Mahmud";

        string fullName = firstName + " " + lastName;

        Console.WriteLine(fullName);
    }
} */

//31

/*using System;

class Program
{
    static void Main()
    {
        int num = Convert.ToInt32(Console.ReadLine());

        if (num > 0)
            Console.WriteLine("Positive");
        else if (num < 0)
            Console.WriteLine("Negative");
        else
            Console.WriteLine("Zero");
    }
}   */

//32

/*using System;

class Program
{
    static void Main()
    {
        int age = Convert.ToInt32(Console.ReadLine());

        if (age >= 18)
            Console.WriteLine("Eligible");
        else
            Console.WriteLine("Not Eligible");
    }
} */

//33

/*using System;

class Program
{
    static void Main()
    {
        int year = Convert.ToInt32(Console.ReadLine());

        if ((year % 4 == 0 && year % 100 != 0) ||
            (year % 400 == 0))
        {
            Console.WriteLine("Leap Year");
        }
        else
        {
            Console.WriteLine("Not a Leap Year");
        }
    }
}   */

//34

/*
using System;

class Program
{
    static void Main()
    {
        int marks = Convert.ToInt32(Console.ReadLine());

        if (marks >= 80)
            Console.WriteLine("A+");
        else if (marks >= 70)
            Console.WriteLine("A");
        else if (marks >= 60)
            Console.WriteLine("A-");
        else if (marks >= 50)
            Console.WriteLine("B");
        else
            Console.WriteLine("Fail");
    }
} */

//35

/*using System;

class Program
{
    static void Main()
    {
        int a = 20;
        int b = 10;

        Console.WriteLine("1. Addition");
        Console.WriteLine("2. Subtraction");
        Console.WriteLine("3. Multiplication");
        Console.WriteLine("4. Division");

        int choice = Convert.ToInt32(Console.ReadLine());

        switch (choice)
        {
            case 1:
                Console.WriteLine(a + b);
                break;

            case 2:
                Console.WriteLine(a - b);
                break;

            case 3:
                Console.WriteLine(a * b);
                break;

            case 4:
                Console.WriteLine(a / b);
                break;

            default:
                Console.WriteLine("Invalid choice");
                break;
        }
    }
} */

//36

/*using System;

class Program
{
    static void Main()
    {
        int day = Convert.ToInt32(Console.ReadLine());

        switch (day)
        {
            case 1:
                Console.WriteLine("Sunday");
                break;

            case 2:
                Console.WriteLine("Monday");
                break;

            case 3:
                Console.WriteLine("Tuesday");
                break;

            case 4:
                Console.WriteLine("Wednesday");
                break;

            case 5:
                Console.WriteLine("Thursday");
                break;

            case 6:
                Console.WriteLine("Friday");
                break;

            case 7:
                Console.WriteLine("Saturday");
                break;

            default:
                Console.WriteLine("Invalid day");
                break;
        }
    }
} */

//37

/*using System;

class Program
{
    static void Main()
    {
        char ch = Convert.ToChar(Console.ReadLine());

        if (ch == 'a' || ch == 'e' || ch == 'i' ||
            ch == 'o' || ch == 'u')
        {
            Console.WriteLine("Vowel");
        }
        else
        {
            Console.WriteLine("Consonant");
        }
    }
}   */

//38

/*using System;

class Program
{
    static void Main()
    {
        int year = Convert.ToInt32(Console.ReadLine());

        if (year % 100 == 0)
            Console.WriteLine("Century Year");
        else
            Console.WriteLine("Not a Century Year");
    }
} */

//39

/*using System;

class Program
{
    static void Main()
    {
        int num = -15;

        Console.WriteLine(Math.Abs(num));
    }
} */

//40

/*using System;

class Program
{
    static void Main()
    {
        int age = Convert.ToInt32(Console.ReadLine());

        if (age < 10)
            Console.WriteLine("Ticket Price = 50");
        else if (age < 60)
            Console.WriteLine("Ticket Price = 100");
        else
            Console.WriteLine("Ticket Price = 70");
    }
} */

//41

/*using System;

class Program
{
    static void Main()
    {
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine(i);
        }
    }
} */

//42

/*using System;

class Program
{
    static void Main()
    {
        int i = 10;

        while (i >= 1)
        {
            Console.WriteLine(i);
            i--;
        }
    }
} */

//43

/*using System;

class Program
{
    static void Main()
    {
        int n = Convert.ToInt32(Console.ReadLine());

        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine(n + " x " + i + " = " + n * i);
        }
    }
} */

//44

/*using System;

class Program
{
    static void Main()
    {
        int n = Convert.ToInt32(Console.ReadLine());

        int sum = 0;

        for (int i = 1; i <= n; i++)
        {
            sum += i;
        }

        Console.WriteLine(sum);
    }
} */

//45

/*using System;

class Program
{
    static void Main()
    {
        int n = Convert.ToInt32(Console.ReadLine());

        int factorial = 1;

        for (int i = 1; i <= n; i++)
        {
            factorial *= i;
        }

        Console.WriteLine(factorial);
    }
} */



using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace AoCMD5
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines(@"..\..\input.txt");

            int[] inputArray = new int[lines.Length];
            inputArray = Array.ConvertAll(lines, int.Parse);

            Thread th = new Thread(() =>
            {
                Console.WriteLine(Puzzle1(inputArray, 0, 0));
            },
            0x10000000);
            th.Start();
            th.Join();
            Console.ReadLine();
        }

        private static double Puzzle1(int[] inputArray, int currentIndex, double jumps){
            if(currentIndex + inputArray[currentIndex] >= 0 && inputArray[currentIndex] + currentIndex < inputArray.Length){
                int next = inputArray[currentIndex];
                inputArray[currentIndex]++;
                jumps++;
                return (Puzzle1(inputArray, (currentIndex + next), jumps));
            }
                return jumps +1;
        }
    }
}

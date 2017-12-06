using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace AoCMD5
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines(@"..\..\input.txt");
            int[] inputArray = new int[lines.Length];
            inputArray = Array.ConvertAll(lines, int.Parse);

            Thread th = new Thread(() => { Console.WriteLine(Puzzle1(inputArray, 0, 0));}, 0x10000000);
            th.Start();
            th.Join();
            inputArray = Array.ConvertAll(lines, int.Parse);
            //Thread th2 = new Thread(() => { Console.WriteLine(Puzzle2(inputArray, 0, 0)); }, 0x10000000);
            //th2.Start();
            //th2.Join();

            Console.WriteLine(Puzzle2LessStackOverflow(inputArray));
            Console.ReadLine();
        }

        private static double Puzzle1(int[] inputArray, int currentIndex, double jumps){
            if (currentIndex + inputArray[currentIndex] >= 0 && inputArray[currentIndex] + currentIndex < inputArray.Length){
                int next = inputArray[currentIndex];
                inputArray[currentIndex]++;
                jumps++;
                return (Puzzle1(inputArray, (currentIndex + next), jumps));
            }else
                return jumps + 1;
        }

        private static double Puzzle2LessStackOverflow(int[] inputArray)
        {
            int currentIndex = 0;
            double jumps = 0;
            while (currentIndex + inputArray[currentIndex] >= 0 && inputArray[currentIndex] + currentIndex < inputArray.Length)
            {
                int next = inputArray[currentIndex];
                inputArray[currentIndex] += (inputArray[currentIndex] > 2) ? -1 : 1;
                jumps++;
                currentIndex += next;
            }
            return jumps+1;
        }



        //private static double Puzzle2(int[] inputArray, int currentIndex, double jumps)
        //{
        //    if (currentIndex + inputArray[currentIndex] >= 0 && inputArray[currentIndex] + currentIndex < inputArray.Length)
        //    {
        //        int next = inputArray[currentIndex];
        //        inputArray[currentIndex] += (inputArray[currentIndex] > 2) ? -1 : 1;
        //        jumps++;
        //        return (Puzzle2(inputArray, (currentIndex + next), jumps));
        //    }
        //    else
        //        return jumps + 1;
        //}


    }
}




    


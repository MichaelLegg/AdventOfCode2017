using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace AoCMD2
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines(@"..\..\input.txt");

            int[][] intVersion = new int[lines.Length][];

            for (int i = 0; i < lines.Length; i++)
            {
                intVersion[i] = lines[i].Split('\t').Select(Int32.Parse).ToArray();
            }

            Console.WriteLine(Puzzle1(intVersion));
            Console.WriteLine(Puzzle2(intVersion));
            Console.ReadLine();
        }

        private static int Puzzle1(int[][] intVersion)
        {
            int returnSum = 0;
            int curMax, curMin;
            for (int i = 0; i < intVersion.GetLength(0); i++) // for each array
            {
                curMax = 0;
                curMin = 0;
                for (int x = 0; x < intVersion[i].Length; x++) // for each item in that array
                {
                    if (intVersion[i][x] > curMax)
                        curMax = intVersion[i][x];
                    if (intVersion[i][x] < curMin || curMin == 0)
                        curMin = intVersion[i][x];                       
                }
                returnSum += (curMax - curMin);
            }
            return returnSum;
        }

        private static int Puzzle2(int[][] intVersion)
        {
            int returnSum = 0;
            for (int i = 0; i < intVersion.GetLength(0); i++)
            {
                bool foundFlag = false;
                for (int x = 0; x < intVersion[i].Length; x++)
                {
                    if (foundFlag)
                        break;
                    for (int y = 0; y < intVersion[i].Length; y++)
                    {
                        if (x==y)
                            continue;
                        int checkVal = intVersion[i][x];
                        if (checkVal % intVersion[i][y] == 0)
                        {
                            returnSum += checkVal / intVersion[i][y];
                            foundFlag = true;
                            break;
                        }
                    }
                }
            }
            return (returnSum);
        }
    }
}

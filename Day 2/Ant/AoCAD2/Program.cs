using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace AoCAD2
{
    class Program
    {
        static void Main(string[] args)
        {
            /// I will code this better
            /// I will code this better
            /// I will code this better 
            /// I will code this better
            /// I will code this better
            /// I will code this better
            /// I will code this better

            string[] fileLines = File.ReadAllLines(@"..\..\DATA.txt");  // Load in das file
            int[,] data = new int[16,fileLines.Count()]; //I know this only works if there are 16 items in the list but.. meh
            int[] lineNums = new int[16];
            int curCol;
            int curLine = 0;
            foreach (string line in fileLines) // Lets split up the lines shall we!
            {
                string currentValue = "";
                curCol = 0;
                char[] lineChar = line.ToCharArray();
                for (int i = 0; i < line.Length; i++)
                {
                    if(lineChar[i].Equals('\t'))
                    {
                        //write number to array
                        data[curCol, curLine] = Int32.Parse(currentValue);
                        curCol++;
                        currentValue = "";
                    }
                    else
                    {
                        currentValue += lineChar[i].ToString();
                    }
                }
                data[curCol, curLine] = Int32.Parse(currentValue);
                curLine++;
            }
            Console.WriteLine("Welcome.... DATA LOADED!");
            Console.WriteLine(partOne(data, fileLines.Count()));
            Console.WriteLine(partTwo(data, fileLines.Count()));
            Console.ReadLine(); // Pause init
        }

        static string partOne(int[,] data, int lines)
        {
            int[] lineCheckSum = new int[lines];
            int curLow = 99999;
            int curHigh = -1;

            // loop for each line
            for (int i = 0; i < lines; i++)
            {
                //Loop for each column
                for (int x = 0; x < 16; x++)
                {
                    if (data[x,i] > curHigh)
                    {
                        curHigh = data[x, i];
                    }
                    if(data[x,i] < curLow)
                    {
                        curLow = data[x, i];
                    }
                }
                //Get checksum value
                lineCheckSum[i] = curHigh - curLow;
                
                // Reset the values
                curLow = 99999;
                curHigh = -1;
            }
            // reuse curHigh as why not
            curHigh = 0;
            foreach(int value in lineCheckSum)
            {
                curHigh += value;
            }            

            return "Part 1 answer is : " + curHigh.ToString();
        }

        static string partTwo(int[,] data, int lines)
        {
            int answer = 0;
            bool found = false;
            int[,] devNumbers = new int[2, lines];

            //3 loops 
            // loop 1 - each line
            //    loop 2 - each number 1 
            //        loop 3 - each number 2 
            //              check if they divide easily
            //                     Yes! - save them to variables and break out
            //                     Add them all up and then return!

            for (int a = 0; a < lines; a++) //Loop 1
            {
                for (int b = 0; b < 16; b++) //Loop 2
                {
                    if (found == false)
                    {
                        for (int c = 0; c < 16; c++) //Loop 3
                        {
                            if (found == false)
                            {
                                if (data[b, a] % data[c, a] == 0)//if no remainder...
                                {
                                    if(data[b, a] != data[c, a])
                                    {
                                        found = true;
                                        devNumbers[0, a] = data[b, a];
                                        devNumbers[1, a] = data[c, a];
                                    }
                                }
                            }
                        }
                    }
                }
                found = false;
            }
            // now devide each pair and add up all answers!
            for(int x = 0; x < lines; x++)
            {
                answer += (devNumbers[0, x] / devNumbers[1, x]);
            }
            return "Part 1 answer is : " + answer.ToString();// return the result!
        }
    }
}

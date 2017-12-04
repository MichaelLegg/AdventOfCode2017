using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoCMD4
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines(@"..\..\input.txt");

            string[][] stringArray = new string[lines.Length][];

            for (int i = 0; i < lines.Length; i++)
            {
                stringArray[i] = lines[i].Split(' ').ToArray();
            }

            Console.WriteLine(Puzzle1(stringArray));
            Console.WriteLine(Puzzle2(stringArray));
            Console.ReadLine();
        }

        private static int Puzzle1(string[][] stringArray)
        {
            int validCount = 0;
            for (int i = 0; i < stringArray.GetLength(0); i++) // for each passphrase
            {
                bool duplicateFound = false;
                for (int x = 0; x < stringArray[i].Length && !duplicateFound; x++) // for each word in the passphrase
                {
                    for (int y = x + 1; y < stringArray[i].Length; y++) // check each other word in the passphrase
                    {
                        if (stringArray[i][x] == stringArray[i][y])
                        {
                            duplicateFound = true;
                            break;
                        }
                    }                  
                }
                if (!duplicateFound)
                    validCount++;
            }
            return validCount;
        }

        private static int Puzzle2(string[][] stringArray)
        {
            for (int i = 0; i < stringArray.GetLength(0); i++) // for each passphrase
            {
                List<List<string>> stringsByLength = new List<List<string>>();
                stringArray[i] = stringArray[i].OrderByDescending(s => s.Length).ToArray(); // order them longest to shortest
                int currentLength = 1000;
                List<string> currentList = new List<string>();
                for (int x = 0; x < stringArray[i].Length; x++) // for each word in the passphrase
                {
                    if (stringArray[i][x].Length < currentLength)
                    {
                        currentLength = stringArray[i][x].Length;
                        if (currentList.Count != 0)
                        {
                            stringsByLength.Add(currentList);
                            currentList = new List<string>();
                        }                       
                        currentList.Add(stringArray[i][x]);
                    }
                    else
                    {
                        currentList.Add(stringArray[i][x]);
                    }                    
                }

                // now need to work out all possibly anagrams for each string in each string list in the list of strings
                foreach (List<string> stringList in stringsByLength)
                {
                    if (stringList.Count() == 1)
                        continue;
                    else

                }

                
            }
            return 1;
        }
    }
}

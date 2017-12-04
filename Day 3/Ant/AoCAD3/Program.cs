using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoCAD3
{
    class Program
    {
        static void Main(string[] args)
        {
            // Actually going to do todays... TODAY!!! OMG!!!
            // FUCK THIS!
            int[,] data = new int[101,101];
            int counter = 1;
            bool goLeft = false;
            bool goUp = false;
            int horTimes = 1;
            int curHorTimes = horTimes;
            int verTimes = 1;
            int curVerTimes = verTimes;
            int locationX = 51;
            int locationY = 51;
            bool turnVertical = true;

            // initalize the array with all -1's
            for (int x = 0; x < 101; x++)
            {
                for(int y = 0; y < 101; y++)
                {
                    data[x, y] = -1;
                }
            }
            // Start adding the numbers!
            
            while (counter <= 10201)
            {
                data[locationX,locationY] = counter;
                if(turnVertical == true)
                {
                    if (curHorTimes == 0)
                    {
                        turnVertical = !turnVertical;
                        verTimes++;
                        curVerTimes = verTimes;
                        // start off horiz movement
                        if (goLeft == true)
                        {
                            locationX--;
                            curVerTimes--;
                        }
                        else
                        {
                            locationX++;
                            curVerTimes--;
                        }
                    }
                    else
                    {
                        // y up or down
                        if (goUp == false)
                        {
                            locationY++;
                            curHorTimes--;
                        }
                        else
                        {
                            locationY--;
                            curHorTimes--;
                        }
                    }
                }
                else
                {
                    if (curVerTimes == 0)
                    {
                        turnVertical = !turnVertical;
                        horTimes++;
                        curHorTimes = horTimes;
                        // Start vertical movement
                        if (goUp == false)
                        {
                            locationY--;
                            curHorTimes--;
                        }
                        else
                        {
                            locationY++;
                            curHorTimes--;
                        }
                    }
                    else
                    {
                        // y left or right
                        if (goLeft == true)
                        {
                            locationX--;
                            curVerTimes--;
                        }
                        else
                        {
                            locationX++;
                            curVerTimes--;
                        }
                    }
                }
                counter++;
            }

            Console.WriteLine("all done!");
            Console.ReadLine();
        }
    }
}

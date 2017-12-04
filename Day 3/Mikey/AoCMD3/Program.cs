using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoCMD3
{
    class Program
    {
        static void Main(string[] args)
        {
            const int BIGGESTNUMBER = 361527;
            BuildArray(BIGGESTNUMBER);




            Console.ReadLine();
        }

        enum State
        {
            increasingX,
            increasingY,
            decreasingX,
            decreasingY
        }

        private static void BuildArray(double biggestNumber)
        {
            int dimension = (int)Math.Ceiling(Math.Sqrt(biggestNumber));
            dimension--; // since it's going to be 0 indexed

            // check if it's even or not
            if ((dimension % 2) == 0)  // this was the broken bit, need to make sure that the grid is created using an odd number in the x and y direction. So if there's a remainder of 0 just add 1 to it
            {
                dimension++;
            }

            int[,] builtArray = new int[dimension, dimension];

            int half = dimension / 2;

            int currentX = half;
            int currentY = half;

            bool maxSetFlag = false;

            State currentState = State.increasingX;

            // OK X AND Y ARE ACTUALLY THE WRONG WAY AROUND, IT'S ROWS AND COLUMNS RATHER THAN POSITIONS ON AN AXIS SO VARIABLE NAMES ARE WROOOOONG
            // ALSO, I PROBABLY REALLY DIDN'T NEED TO ACTUALLY BUILD A SPIRAL TO SOLVE THIS, BUT IT'S QUITE COOL AND NOW I KNOW HOW TO BUILD A SPIRAL...RIGHT?
            int currentValue = 1;
            do
            {
                Console.WriteLine("X=" + currentX + "Y=" + currentY + "Value Set:" + currentValue);
                builtArray[currentX, currentY] = currentValue;

                if (currentState == State.increasingX)
                {
                    currentX++;
                    if(currentX + 1 > dimension -1 || (builtArray[currentX+1, currentY] == 0) && builtArray[currentX, currentY-1] == 0){
                        currentState = State.decreasingY;
                    }
                }
                else if (currentState == State.increasingY)
                {
                    currentY++;
                    if(currentY + 1 > dimension - 1 || (builtArray[currentX, currentY+1] == 0) && builtArray[currentX + 1, currentY] == 0)
                    {
                        currentState = State.increasingX;
                    }
                }
                else if(currentState == State.decreasingX)
                {
                    currentX--;
                    if (currentX - 1 < 0 || (builtArray[currentX-1, currentY] == 0) && builtArray[currentX, currentY + 1] == 0)
                    {
                        currentState = State.increasingY;
                    }
                }
                else if(currentState == State.decreasingY)
                {
                    currentY--;
                    if (currentY - 1 < 0 || (builtArray[currentX, currentY-1] == 0) && builtArray[currentX - 1, currentY] == 0)
                    {
                        currentState = State.decreasingX;
                    }
                }
                if(currentValue == biggestNumber)
                    maxSetFlag = true;
                else
                    currentValue++;
                
            } while (!maxSetFlag); // do it until we've set the biggest value
            Console.WriteLine(Puzzle1(builtArray, dimension, biggestNumber));
        }
        
        private static int Puzzle1(int[,] builtArray, int dimension, double searchVal)
        {
            int half = dimension / 2;

            int searchX = 0;
            int searchY = 0;
            for (int x = (dimension-1); x != 1; x--)
            {                
                for (int y = dimension - 1; y != 1; y--)
                {
                    if(builtArray[x,y] == searchVal){
                        searchX = x;
                        searchY = y;
                        break;
                    }
                }
            }
            int sum = 0;
            // quick and dirty
            if (searchX > half)
                sum += searchX - half;
            else       
            
           (searchX - half) + (half -searchY);
            return sum;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
// ReSharper disable UnusedVariable
// ReSharper disable CollectionNeverQueried.Local
// ReSharper disable ConvertToLocalFunction
// ReSharper disable UseObjectOrCollectionInitializer

namespace ProgrammingMeeting1
{
    public static class Program
    {
        public static void Main()
        {
            Example example = ObjectExample(10);

            Example[] array = ArrayExample(10);

            List<Example> list = ListExample(10);

            InputExample();
        }

        /// <summary>
        /// Creates an instance of <see cref="Example"/>.
        /// </summary>
        /// <param name="value">
        /// The value with which the <see cref="Example"/> is created.
        /// </param>
        /// <returns>
        /// An <see cref="Example"/> object.
        /// </returns>
        public static Example ObjectExample(int value)
        {
            Example example = new Example(value);

            ExtendedExample extended = new ExtendedExample(value);

            example.IncreaseValue(2);

            extended.IncreaseValue(2);

            Console.WriteLine(example.Value);
            Console.WriteLine(extended.Value);

            return example;
        }

        /// <summary>
        /// Creates an array of <see cref="Example"/> objects.
        /// </summary>
        /// <param name="length">
        /// The length of the array.
        /// </param>
        /// <returns>
        /// An array of <see cref="Example"/>.
        /// </returns>
        public static Example[] ArrayExample(int length)
        {
            Example[] exampleArray = new Example[length];

            for (int i = 0; i < length; i++)
            {
                exampleArray[i] = new Example(i);
            }

            foreach (Example example in exampleArray)
            {
                example.IncreaseValue(1);
            }

            exampleArray[length - 1] = new Example(-1);

            IEnumerable<Example> decreaseCollection =
                exampleArray.Select(
                    x =>
                    {
                        x.IncreaseValue(-1);
                        return x;
                    });

            Func<Example, Example> function =
                x =>
                {
                    x.IncreaseValue(1);
                    return x;
                };

            IEnumerable<Example> increaseCollection = decreaseCollection.Select(function);

            foreach (Example example in decreaseCollection)
            {
                Console.WriteLine(example);
            }

            foreach (Example example in increaseCollection)
            {
                Console.WriteLine(example);
            }

            return exampleArray;
        }

        /// <summary>
        /// Creates a list of <see cref="Example"/> objects.
        /// </summary>
        /// <param name="length">
        /// The length of the list.
        /// </param>
        /// <returns>
        /// A list of <see cref="Example"/> objects.
        /// </returns>
        public static List<Example> ListExample(int length)
        {
            IEnumerable<Example> enumerableCollection =
                Enumerable.Range(0, length)
                          .Select(x => new Example(x));

            List<Example> exampleList = new List<Example>(enumerableCollection);

            exampleList[9] = new Example(10);

            exampleList.Add(new Example(11));

            return exampleList;
        }

        /// <summary>
        /// Ask the user for their name and age, then print to console.
        /// </summary>
        public static void InputExample()
        {
            Console.WriteLine("Enter your name:");

            string name = Console.ReadLine();

            Console.WriteLine($"Hello {name}! How old are you?");

            if (!int.TryParse(Console.ReadLine(), out int age))
            {
                Console.WriteLine("Unable to parse console input as an integer.");
            }
            else
            {
                Console.WriteLine($"You are {age} years old!");
            }
        }
    }
}
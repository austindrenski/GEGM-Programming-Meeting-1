using System;
using JetBrains.Annotations;

namespace ProgrammingMeeting1
{
    /// <summary>
    /// Represents a class that inherits from the <see cref="Example"/> class.
    /// </summary>
    [PublicAPI]
    public class ExtendedExample : Example
    {
        /// <summary>
        /// Constructs an <see cref="ExtendedExample"/> by passing the constructor argument down to the base class constructor.
        /// </summary>
        /// <param name="value">
        /// The value of the example.
        /// </param>
        public ExtendedExample(int value) : base(value)
        {
        }

        /// <summary>
        /// Overrides the base class virtual method with new behavior.
        /// </summary>
        /// <param name="amount">
        /// The amount -- now ignored.
        /// </param>
        /// <returns>
        /// True if the value is greater than zero; otherwise false.
        /// </returns>
        public override bool IncreaseValue(int amount)
        {
            base.IncreaseValue(1);
            return Value > 0;
        }

        /// <summary>
        /// Incrememnts the value and prints to console.
        /// </summary>
        public void IncrementAndPrintValue()
        {
            IncreaseValue(1);
            Console.WriteLine(Value);
        }
    }
}
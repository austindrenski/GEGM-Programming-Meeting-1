using JetBrains.Annotations;

namespace ProgrammingMeeting1
{
    /// <summary>
    /// Represents an example.
    /// </summary>
    [PublicAPI]
    public class Example
    {
        /// <summary>
        /// The value of this example.
        /// </summary>
        public int Value { get; set; }

        /// <summary>
        /// Constructs an example with the given value.
        /// </summary>
        /// <param name="value">
        /// The value for this example.
        /// </param>
        public Example(int value)
        {
            Value = value;
        }

        /// <summary>
        /// Increases the Value property by the specified amount.
        /// </summary>
        /// <param name="amount">
        /// The amount by which to increase the Value property.
        /// </param>
        /// <returns>
        /// True if the Value property is positive; otherwise false.
        /// </returns>
        public bool IncreaseValue(int amount)
        {
            Value += amount;

            return Value > 0;
        }
    }
}
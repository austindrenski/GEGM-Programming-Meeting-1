module Example

/// <summary>
/// Represents an example.
/// </summary>
type Example(amount : int) = 

    /// <summary>
    /// The value of this example.
    /// </summary>
    member val Value : int = amount with get, set

    /// <summary>
    /// Increases the Value property by the specified amount.
    /// </summary>
    /// <param name="amount">
    /// The amount by which to increase the Value property.
    /// </param>
    /// <returns>
    /// True if the Value property is positive; otherwise false.
    /// </returns>
    member this.IncreaseValue(amount : int) : bool = 
    this.Value <- this.Value + amount
    this.Value > 0
        
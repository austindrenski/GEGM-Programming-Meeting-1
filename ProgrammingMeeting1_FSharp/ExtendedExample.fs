module ExtendedExample

open Example

/// <summary>
/// Represents a class that inherits from the <see cref="Example"/> class.
/// </summary>
type ExtendedExample(value : int) = 
    inherit Example(value)

    /// <summary>
    /// Incrememnts the value and prints to console.
    /// </summary>
    member this.IncrementAndPrintValue() : unit =
        this.IncreaseValue(1) |> ignore
        printfn "%i" this.Value
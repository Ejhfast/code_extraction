# How to apply a function to every element in a list using Linq in C# like the method reduce() in python?
var list = Enumerable.Range(5, 3); // [5, 6, 7]
Console.WriteLine("Aggregation: {0}", list.Aggregate((a, b) =&gt; (a + b)));
// Result is "Aggregation: 18"

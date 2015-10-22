# Processing the string separated by ":" with C#
var st = "a:b:c";
foreach(var item in st.Split(':'))
   Console.WriteLine(item);

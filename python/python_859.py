# C# equivalent of rotating a list using python slice operation
var newlist = oldlist.Skip(1).Concat(oldlist.Take(1));

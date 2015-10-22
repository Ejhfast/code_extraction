# Python's xml.etree getiterator equivalent to C#
var xml = XDocument.Load(filename);
var res = from p in xml.Root.Elements("Class").Elements("ClassKeyName") select p.Value;

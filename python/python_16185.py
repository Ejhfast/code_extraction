# C# Parsing JSON Array(HTTPrequest Response) to display
JObject obj = JObject.Parse(File.ReadAllText("1.json"));
foreach (JToken o in obj["data"]["innerData"] as JArray)
    Console.WriteLine(o["dataInfo"]);

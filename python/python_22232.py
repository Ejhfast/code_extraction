# How to use process.StartInfo.Arguments in command prompt?
Process p = new Process();
   p.StartInfo = new ProcessStartInfo("cmd.exe", "/c notepad.exe");
   p.Start();

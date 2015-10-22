# How can one set up a thread in C# to only execute when CPU is idle?
Thread thread = Thread.CurrentThread;
thread.Priority = ThreadPriority.Lowest;

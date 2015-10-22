# Sending a string over Python server to C# client returns a number of the chars in the string
int numReceived = clientSock.Receive(buffer);
string msg = Encoding.ASCII.GetString(buffer, 0, numReceived);

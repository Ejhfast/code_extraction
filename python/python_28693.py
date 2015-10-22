# XOR decryption in c#
for (int c = 0; c &lt; text.Length; c+=2)
    result.Append((char)(Convert.ToUInt16(text.Substring(c, 2), 16) ^ (ushort)key[ (c/2) % key.Length]));

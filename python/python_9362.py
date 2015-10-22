# Python Base64 string shorter than Botan Base64 string
Pipe dec_pipe(new Base64_Decoder, get_cipher("AES-256/CBC/NoPadding", key, iv, Botan::DECRYPTION));

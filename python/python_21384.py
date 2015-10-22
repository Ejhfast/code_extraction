# Inconsistent PBKDF2 hashes in Python (django) and Javascript (crypto.js)
CryptoJS.PBKDF2('qwerty', 'qwerty', { iterations: 1, keySize: 256/32, hasher: CryptoJS.algo.SHA256 });

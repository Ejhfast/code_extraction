# SHA256 encoding in javascript
var signature = CryptoJS.HmacSHA256(message,API_SECRET).toString(CryptoJS.enc.Hex).toUpperCase();

# Decoding binary files stored inside a database after being uploaded from a browser
byte[] bytes = Files.readAllBytes(Paths.get("/test/test.pdf"));
String base64 = DatatypeConverter.printBase64Binary(bytes);
System.out.println(base64.substring(0, 10)); // JVBERi0xLj

# How to generate a list of given length in Java 8?
Stream.generate(this::generate).limit(length).collect(Collectors.toList());

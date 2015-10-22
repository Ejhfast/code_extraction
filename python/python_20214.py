# How do i convert a list of numbers into their corresponding chr()
intList = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
charList = [chr( intList[i] ) for i in range( 0, len( intList ) )]

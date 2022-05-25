# HyperionTHT

## Section A: Option 2

For the string reversal, this method looks good overall. It has a reliable exit condition to avoid stack overflows at line 23. I do suggest just printing the input string given from the argument of the method for the exit condition instead of noting that the input string is empty. Or better yet, just having an empty return statemtn altogether. It make the output look a bit tidier.

For the fibonacci method, I have several comments:

1. The name of the method is not clear enough to signify immediately what the method does. It is very generic,a nd anyone trying to use the method as part of a library would be confused as to what function(T maxNumber) does.
2. I don't see where the argument is used within the method. `maxNumber` is declared but is reassigned with an `int` type inside the method. Why not make the following change: `public static <T> void function(T maxNumber)` → `public static void fibonacci(int maxNumber)`. Then maxNumber won't have to be reassigned.
3. This method is dynamic, not recursive. Recursively, you could do the following:

- Take the position of the target fibonacci number as an argument (in our case, we already have maxNumber)
- Check if maxNumber is less than or equal to 1, in which case just print maxNumber out
- Otherwise print and return fibonacci(maxNumber - 1) + fibonacci(maxNumber - 2)

The dynamic method is faster as it has a complexity of O(n), but it is not recursive.

For the rest of the program, there are lots of empty line breaks. Removing these and limiting them to maybe one line break between blocks (if you really want to) can massively aid the readability of your program. The indentation is also very inconsistent, and can make following code blocks difficult. Think of indentation as hierarchy: if it's to the left of a code block, it is outside that block. If it is to the right of a block, it is inside the block. If it is on the same level as the block, then it is part of the block.


## Section B

This is an Android application I made many years ago. It is quite heavily commented and should still build, but was also tested on Android 8.0 (I believe 11 is the latest version). I now use an iPhone, so I haven't used the app in quite a long time.

[Here is a link to the app.](https://github.com/TrippyUnicorn420/SplitBill-Android)


## Secton C

I chose option 3. My source code is in the repository above this file. I created and tested it with Python 3.10.4 x64 on Windows 10.

# Problem Definition - Day 19 # [Hard]

<<<<<<< HEAD
This problem was asked by Google.

Suppose we represent out file system by a string in the following manner:

The string `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` represents:
```
dir
    subdir1
    subdir2
        file.ext
```

The directory `dir` contains an empty sub-directory `subdir1` and a sub-directory `subdir2` containing a file `file.ext`.

The string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` represents:
```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is `"dir/subdir2/subsubdir2/file2.ext"`, and its length is 32(not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system if there is no file in the system, return 0.

Note: The name of a file contains at least a period and an extension. The name of a directory or sub-directory will not contain a period.
=======
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters. 
For example, if N is 4, then there are 5 unique ways:
 - 1, 1, 1, 1
 - 2, 1, 1
 - 1, 2, 1
 - 1, 1, 2
 - 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if `X={1, 3, 5}`, you could climb 1, 3, or 5 steps at a time.

LinNote: this is a same problem as the coin change problem - day 13 problem. 
>>>>>>> c51c27fd1daf954573b8f27dfb6772c3a487d980

# Binmod

Binmod is a simple language I created that isn't really a language. It is kinda an esoteric computer language but it limits the size of binary files stored on your computer. \n

Documentation:
```
- <Number>: Number of digits of a pattern of either 1 then 0 or 0 then 1 wil take place - referred to as a term in speech
- ': Pattern of digits will start off with 1 instead of 0 - referred to as prime in speech
-  : A space seperates terms - referred to as space in speech
- .<Number><1 or 0>: a period is the most complex function in this language, the number following the period will be the number of times either a 1 or 0 will be repeated, which digit  will be repeated is determined as the last character of the term - referred to as "<Number> mult <1 or 0>" in speech
```

Example Code:
```
2, 4', .111
```
The program will return 2 digits of 1 then 0. \n
The program will then return 4 digits of 0 and 1 \n
The program will then return 11 1s \n
Output:
```
01101011111111111
^^||||^^^^^^^^^^^
2  4'    11 1s
```

This language is incredibly simple and does not proove to be of much use. \n

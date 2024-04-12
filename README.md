# Binmod

Binmod is a simple language I created that isn't really a language. It is kinda an esoteric computer language but it reduces the size of binary files stored on your computer so I guess that it could theoretically be helpfull in some situations. Binmod stands for Binary Modulus. I got this idea because I realised that binary is a mod 2 language (it only has 2 values) which means that any series of repeating 1s and 0s or 0s and 1s could be represented as one non-0-or-1 number. The code is not hard to follow so no comments are present. It is configured to accept files with your Binmod code in it and it will turn the Binmod code back into Binary. I am currently working on a encoder to turn Binary into Binmod code.  


# Binmod to Binary decoder
Documentation:
```
- <Number>: Number of digits of a pattern of either 1 then 0 or 0 then 1 wil take place - referred to
            as a "term" in speech
- ': Pattern of digits will start off with 1 instead of 0 - referred to as "prime" in speech
-  : A space seperates terms - referred to as "space" in speech
- .<Number><1 or 0>: a period is the most complex function in this language, the number
                     following the period will be the number of times either a 1 or 0
                     will be repeated, which digit  will be repeated is determined as
                     the last character of the term - referred to as "<Number> mult <1 or 0>" in speech
```

Example Code:
```
2 4' .111
```
The program will return 2 digits of 0 then 1.  
The program will then return 4 digits of 1 and 0 
The program will then return 11 1s  
Output:
```
01101011111111111
^^||||^^^^^^^^^^^
2  4'    11 1s
```

# Binary to Binmod encoder coming soon

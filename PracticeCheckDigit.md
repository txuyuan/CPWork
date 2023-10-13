# CP Practice (29/8/2023)

## 1. 

### (a)

```
FUNCTION GenerateCheckDigit (ISB: STRING) RETURN CHAR
    DECLARE sum: INTEGER

    FOR i FROM 0 TO 10 
        DECLARE num: INTEGER
        num <- ISB[i]
        sum <- sum + num * (10 - i)
    
    DECLARE check: INTEGER
    check <- 11 - (sum % 11)

    IF check == 10
    THEN
        return 'X'
    ELSE
        return check % 11
```

### (b)

The purpose is to check for any human error in the transmission of a number.
A check digit can capture transposition errors. 



## 2.

### (a)

Output: 0011

### (b)

The given algorithm outputs the binary number backwards. Since each step of the recursive algorithm outputs increasingly large exponents of 2, the algorithm outputted 0011 instead of 1100 when given an input of 12 (base-10).

### (c)

```python

def HexaToDenary(HexaDecNum):
    hexChars = "0123456789abdcef"
    
    denaryAnswer = 0
    exp = len(HexaDecNum) - 1
    for c in HexaDecDum:
        denaryAnswer += hexChars.find(c) * 16 ** exp
        exp -= 1
    
    return denaryAnswer 

```



## 3. 

### (a)

218 (base-10) = 11011010 (base-2)

### (b)

685 (base-10) = 2ad (base-16)

### (c)

... = 57ba (base-16)

### (d)

```python
def binaryToDec(binaryNum):
    decAnswer = 0 

    exp = len(binaryNum) - 1 
    for c in binaryNum:
        decAnswer += int(c) * 2 ** exp 
        exp -= 1

    return decAnswer 
```

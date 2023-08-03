# How computers perform basic arithmetic

### how do machines add, subtract, multiply and divide?
* very good question; start with addition
* before that, learn about the base 2 counting system; this is 
the system that machines use. we, mostly, use base 10 in our day-to-day:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ... zer0 to nine (including nine) is 10 numbers,
which explains _base 10_ (and also the word _digit_). sometimes we use base 60;
60 secs in a minute, 60 mins in an hour (thanks to the Sumerians). zero, by the
way, is an Indian invention

#### how machines add
* say you want to add the numbers 0 and 1 in any combination as long as you add
    two numbers only (assume base 10)
    * option 1: 0 + 0 = 0
    * option 2: 0 + 1 = 1
    * option 3: 1 + 0 = 1
    * option 4: 1 + 1 = 2
* the first three match the truth table for `XOR`; see [0-logic_gates.md][def].
we can use the `XOR` gate to perform binary addition. in binary, there are only two
numbers: 0 and 1. they are called _bits_ (binary digits). values are calculated in
ascending powers of 2 (same way 10 is used in base 10); so 1 + 1 in binary is zero,
carry 1 (same as 5 + 5 in base 10 is zero, carry 1)
* the example above done in binary viz: 
    * option 1: 0 + 0 = 0
    * option 2: 0 + 1 = 1
    * option 3: 1 + 0 = 1
    * option 4: 1 + 1 = 10
* notice that the result in option 4 is 10, not 2; this is how to represent decimal 2
in binary. think about it this way: 10 = 1*2^1 + 0*2^0
* also, notice that the last bit of the sum matches the `XOR` truth table: we have found
a way to do addition, however, what about the carry?
* the carry bit, for the first three, is zero: 0 + 0 = 0 carry 0 and so on; it is 1 for
option 4. this matches the truth table for `AND`; see [0-logic_gates.md][def]. now we
_really_ have a way to perform addition
* how, you ask?
    * ea...sy! combine a `XOR` and `AND` gate in such a way that it is possible to "carry"

### this is not the aim of this project, therefore, this is it, folks

[def]: 0-logic_gates.md#logic-gates
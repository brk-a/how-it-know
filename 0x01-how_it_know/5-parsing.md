# Parsing

* the second of three steps a computer takes to convert source code to binary
    * the other two, in order, are: lexical analysis and interpretation
* here, the computer identifies patterns and associations in the array of
tokens from the first step (lexical analysis)
* example instruction `1 + 3`
    * output of lexical analysis step: 
        [Token(1, int), Token(+, op), Token(3, int)]
    * what the parser does:
        * id arr[0] -> Token(1, int) as the decimal `1` of type `int`
        * id arr[1] -> Token(+, op) as the sign `+` of type `op`
        * id arr[2] -> Token(3, int) as the decimal `3` of type `int`
* lexical analyser does not care about the syntax of the language; it, simply,
_tokenises_ all the input it receives
* parser cares about syntax; this is where syntax errors will be caught
    * parser has a set of rules;  expressions (collection/array of tokens) must
    conform to the rules (aka syntax), else, syntax error
* FrankenScript uses [BNF][def]
    * general form viz:
    
    ```
     <symbol> ::= __expression__
    ```

    * where:

        * `<symbol>` is a non-terminal (variable)
        * `__expression__` is one or more sequences of either terminal or non-terminal symbols
        * `::=` means that `symbol` on the left must be replaced with `expression` on the right.
            more sequences [of symbols] are separated by the vertical bar `|`, indicating a choice; the whole is a possible substitution for the `symbol` on the left
    * symbols that never appear on the right side are terminals; symbols that appear on a left side are non-terminals and are always enclosed between `<>`
    * example:
        
        ```
            <expr> ::= <term> + <expr> | <term> - <expr> | <term>
        ```

    * `<expr` is one of the following
        * `<term> + <expr>` 
        * `<term> - <expr>`
        * `<term>`
    * the first two contain `<expr>` on the RHS; why?
        * continuity
        * take 5 + 3 + 1. this expression falls in the first option because `+`. computer classifies
            5 as `<term>` and 3 + 1 as `<expr>`. next pass: 3 becomes `<term>` and 1 is `<expr>`. third pass: 1 is `<term>` (the last option, because there is nothing after 3). the whole
            thing viz:
            `<term> + <expr>` -> `<term> + <term> + <expr>` -> `<term> + <term> + <term>`
        * the recursive calls/passes allow the user and computer deal with one or more terms; you can perform 5 + 3 or 5 + 3 + 1 or 5 + 3 + 1 + 2 + 4 ...
    * terminals, non-terminals...?
        * consider the following

        ```
            <expr> ::= <term> + <expr> | <term> - <expr> | <term>
            <expr> ::= <term> * <expr> | <term> / <expr> | <term>
            <term> ::= <int>
            <int>  ::= 0|1|2|3|4|5|6|7|8|9
            <op>   ::= +|-|*|/
        ```

        * `<expr>` and `<term>` are non-terminals. they are derived from more basic data types/tokens 
        * `<int>`  and `op` are terminals. they are base tokens; singular, irreducible forms of data/tokens
        * notice that `<expr>` and `<term>` appear on the RHS as well. that is alright because recursion
        * another example: 3 + 5 * 2
            * first pass: `<term> 3` + `<expr>`
            * second pass: `<term> 3` + `<term> 5` * `<expr>`
            * third pass: `<term> 3` + `<term> 5` * `<term> 2`
            * but `<term>` is `<int>` so: `<int> 3` + `<int> 5` * `<int> 2`
            * however, `<int>` is \[0-9\] so: `<expr>` ::== `3` + `5` * `2` 



[def]: https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form
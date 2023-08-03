# Lexical Analysis

* aka tokenisation
* the first of three steps a computer takes to convert source code to binary
    * the other two, in order, are: parsing and interpretation
* our "proramming language" will be called _FrankenScript_ (see what I did
there?);  the interpreter will ingest FrankenScript
* lexical analysis is, simply, _lexical analysis_; the computer looks at the
    sequences of characters (words, whitespace, special chars etc) and breaks
    them into tokens
    * in this project, tokens have a value, a type or both
    * example `x = 5`: `x` is of type `int` and has value `5`
    * example `+`: type `op` and value `+`
* these _tokens_ will be stored sequentially in a Py list because we will use
Py to create FrankenScript
* the lexical analyser takes in the code typed by the user and passes its output
    to the parser
    * example output: instruction `1 + 3`
        * [Token(1, int), Token(+, op), Token(3, int)]
* lexical analyser does not care about the syntax of the language; it, simply,
_tokenises_ all the input it receives
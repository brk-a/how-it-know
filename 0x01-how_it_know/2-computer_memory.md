# How computers store data

* simple, actually: arrange a `NOT` and `OR` such that:
    *  their outputs are the inputs of an `AND` gate
    * the output of the `AND` gate is connected to one input of the `OR` gate
    * the output of the arrangement is the output of the `AND` gate; call it `O`
* name the input of the `NOT` gate `R` (reset)
* name the input of the `OR` gate that is not connected the output of the `AND`
gate `S` (set)
* how it works
    * turn on the `S` wire; leave the `R` off
        * output of `OR` is 1
        * output of `NOT` is 1
        * inputs of `AND` are 1 and 1
        * output of `AND` is 1
        * output of `AND` becomes input of `OR` (infinite loop)
        * output of arrangement is 1
    * turn off the `S` wire; leave the `R` off
        (recall: 1 has been stored in `O` and `O` is an input of `OR`)
        * output of `OR` is 1
        * output of `NOT` is 1
        * inputs of `AND` are 1 and 1
        * output of `AND` is 1
        * output of `AND` becomes input of `OR` (infinite loop)
        * output of arrangement is 1
        (the computer has "remembered" the state it was in before `S` was turned off;
        we have computer memory _ab initio_)
    * turn on the `R` wire; leave the `S` off
        (recall: 1 has been stored in `O` and `O` is an input of `OR`)
        * output of `OR` is 1
        * output of `NOT` is 0
        * inputs of `AND` are 0 and 1
        * output of `AND` is 0
        * output of `AND` becomes input of `OR` (infinite loop)
        * output of arrangement is 0
        (the computer has reset the state of the arrangement)
    * turn on the `R` and  `S` wires
        (recall: 0 has been stored in `O` and `O` is an input of `OR`)
        * output of `OR` is 1
        * output of `NOT` is 0
        * inputs of `AND` are 0 and 1
        * output of `AND` is 0
        * output of `AND` becomes input of `OR` (infinite loop)
        * output of arrangement is 0
        (the computer has stored zero)
* truth table viz:

|set|reset|output|effect|
|:---:|:---:|:---:|:---|
|1|0|1|store 1|
|0|0|1|recall 1|
|1|1|0|reset mem|
|0|1|0|store 0|

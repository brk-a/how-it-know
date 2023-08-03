# Logic  gates

* computers, at their core, are transistors meticulously arranged in a specific manner
* a transistor is, simply, a semi-conductor attached to to electrodes (or two electrodes
attached to a semi-conductor, if you like)
* a semi-conductor _semi-conducts_; that is, conducts electricity under specific conditions
and, sometimes, in a specific direction
* semi-conductor's input is called the _control wire_. electricity flows through the sc when
the control wire is on; the inverse is true
* let 1 represent the `ON` state of the control wire and 0 the `OFF` state
    * electricity flows to \[one of\] the electrodes via the sc when cw is 1
    * electricity does not flow to the electrodes via the sc when cw is 0
* take control wire as the `input` and any electrode as `output`
    * `output` is 1 when `input` is 1
    * `output` is 0 when `input` is 0
    * one can use these properties to construct _logic gates_
* a logic gate is  is an idealised or physical device that performs a boolean function
    * a boolean function is a logical operation performed on one or more binary inputs that produces a single binary output
    * some logic gates: NAND, AND, NOT, NOR, OR, XOR
    * `NOT` _not_\s; that is, it negates whatever it operates on. `NOT 1` evaluates to `0` and 
    vice versa
    * `NAND` is, simply, `NOT AND`; it _not_\s `AND`
    * `AND` compares two inputs and outputs 1 IFF both are 1, else 0
    * `OR` compares two inputs and outputs 0 IFF both are 0, else 1
    * `XOR` compares two inputs and outputs 1 IFF only one input is 1, else 0
* truth tables are tables/grids that show the _truthyness_ of output under a specific logic gate
    * truth table for `NOT`
    
    |input|output|
    |:---:|:---:|
    |1|0|
    |0|1|

    * truth table for `AND`

    |input1|input2|output|
    |:---:|:---:|:---:|
    |0|0|0|
    |0|1|0|
    |1|0|0|
    |1|1|1|

    * truth table for `NAND`

    |input1|input2|output `AND`|output `NAND`|
    |:---:|:---:|:---:|:---:|
    |0|0|0|1|
    |0|1|0|1|
    |1|0|0|1|
    |1|1|1|0|

    * truth table for `OR`

    |input1|input2|output|
    |:---:|:---:|:---:|
    |0|0|0|
    |0|1|1|
    |1|0|1|
    |1|1|1|

    * truth table for `NOR`

    |input1|input2|output `OR`|output `NOR`|
    |:---:|:---:|:---:|:---:|
    |0|0|0|1|
    |0|1|1|0|
    |1|0|1|0|
    |1|1|1|0|

    * truth table for `XOR`
    
    |input1|input2|output|
    |:---:|:---:|:---:|
    |0|0|0|
    |0|1|1|
    |1|0|1|
    |1|1|0|
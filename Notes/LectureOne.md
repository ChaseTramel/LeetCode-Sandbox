# 6.006, Lecture One, Intro to Algorithms

[Course Link](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | [Lecture Link](https://youtu.be/ZA-tUyM_y7s)

## What is this course about?

Solve computational problems
Prove correctness
Argue efficiency (better than other solutions)
Communicate these ideas to other people (may be doing a lot of writing)

## Defining terms

**Problem**: Inputs => Outputs. A relation between inputs and outputs.
We want to talk about large problems.
For solutions, we want an alogrithm that:
 - applies to different situations / inputs (generalized)
 - scales for larger inputs

*Aside: consider also taking Mathematics for CS. It is a prerec for 6.006*

**Alogorithm**: A fixed procedure that solves the problem with the correct output for the specified input.

**Correctness**: Through inductive reasoning
Inductive reasoning: Proving the algorithm sovles the problem with a small set of inputs, therefore proving that it solves the problem with a larger set of ouputs.
Can you communicate in a way that can be written as code?

*Aside: this inductive reasoning / proofs discussion is apparently discussed in Mathematics for CS.*

**Efficiency**: How fast does this algorithm run? How fast does this algorithm compare to other possible algorithms?
Instead of measuring time, count operations. We expect this to depend on the size of the input. We use N to represent the number of inputs.
Asymptotic Analysis: Big O, Omega, and Theta notation

Constant Time
Logarithmic Time
Linear
Log Linear
Quadraic Time
Polynomial Time
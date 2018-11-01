# Pinocchio for EthSnarks

This repository includes the [Pinocchio](https://eprint.iacr.org/2013/279.pdf) compiler, it translates a small and limited subset of the C language to the 'Pinocchio format' for defining Secure Function circuits. Unfortunately the initial Pinocchio compiler wasn't fully developed and is... academic quality. Subsequent work moved onto Geppetto which uses LLVM as a frontend rather than PyCParser.

The [Pequin](https://github.com/pepper-project/pequin) compiler should be used instead.

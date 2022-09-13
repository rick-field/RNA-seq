#!/bin/bash/

paste - - - - - - - - < Y_filamentosa_84_4W_NAWWY.fasta \
    | tee >(cut -f 1-4 | tr "\t" "\n" > Y_filamentosa_84_4W_NAWWY_R1.fq) \
    |       cut -f 5-8 | tr "\t" "\n" > Y_filamentosa_84_4W_NAWWY_R2.fq

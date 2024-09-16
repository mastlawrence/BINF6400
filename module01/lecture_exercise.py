"""
Module 01 Lesson 2 Exercise

Consider a set of sequences {S} where each sequence is 20 bases long. 
Consider a parameter k which is the minimum size of the overlap which
can be used to merge reads into a contig. 

If you assemble S into a single contig using parameter K with no ambiguity,
what does this tell you about the uniqueness of any sub-sequence length n
(where n = 0, 1, 2 ... k ... length).

"""
import sys
import random
import os

os.system('color')
random.seed(42)



GREEN = '\033[32M'


def main():

    ## Step 1: generate sample data
    data_set = generate_set(2, 4)
    seq1 = data_set[0]
    seq2 = data_set[1]

    print(seq1, seq2)

    ## Step 2: Look for overlap between the two sequences
    for i in range(len(seq1), 0, -1):
        detect_match(seq1, seq2, i)

def generate_set(n, l):
    """
    generates a set of 10 different 
    20-length reads
    """
    sequence_set = []

    for i in range(0,n):
        sequence = _generate_sequence(l)
        sequence_set.append(sequence)

    return sequence_set


def _generate_sequence(l):
    """
    generates sequence reads of l length
    """
    seq_data = []

    for i in range(1, l+1):
        bp = random.choice("ACGT")
        
        seq_data.append(bp)

    return "".join(seq_data)


def detect_match(seq1, seq2, merge_parameter):
    """
    test function for figuring out 
    how to merge and remove elements 
    from a list based on a match 
    parameter.
    """

    seq1_list = list(seq1)
    seq2_list = list(seq2)
    
    print("\n")
    
    print("matching +", merge_parameter, "of", seq1, "with -", merge_parameter, "of", seq2)
    print("-----------------------------------------------------------------------------")
    print(seq1_list[:merge_parameter])
    print(seq2_list[-merge_parameter:])

    match_f_seq1 = seq1_list[:merge_parameter]
    match_f_seq2 = seq2_list[-merge_parameter:]

    if match_f_seq1 == match_f_seq2:
        print("")
        print("match detected")

        combined_seq = seq2_list[:merge_parameter] + seq1_list
        combined_seq = "".join(combined_seq)

        print("Contig:", combined_seq)
        sys.exit("Contig found")

    print("\n")

    print("matching -", merge_parameter, "of", seq1, "with +", merge_parameter, "of", seq2)
    print("-----------------------------------------------------------------------------")
    print(seq1_list[-merge_parameter:])
    print(seq2_list[:merge_parameter])

    match_b_seq1 = seq1_list[-merge_parameter:]
    match_b_seq2 = seq2_list[:merge_parameter]

    if match_b_seq1 == match_b_seq2:
        print("")
        print(GREEN + "match detected")
        print("\n")



if __name__ == "__main__":
    main()

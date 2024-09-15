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

random.seed(42)


def main():

    ## Step 1: generate sample data
    data_set = generate_set(3)

    ## Step 2: By a greedy method, assemble the sequences
    assemble_reads(data_set)

    ## TODO: Test function to figure out how to merge and remove elements of a list
    merge_and_remove()


def generate_set(n):
    """
    generates a set of 10 different 
    20-length reads
    """
    sequence_set = []

    for i in range(0,n):
        sequence = _generate_sequence(4)
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


def assemble_reads(seq_data):
    """
    looks for matching reads
    """
    for i in range(0, len(seq_data)):
        print(seq_data[i])


def merge_and_remove():
    """
    test function for figuring out 
    how to merge and remove elements 
    from a list based on a match 
    parameter.
    """
    merge_parameter = int(input("merge parameters:"))
    seq1 = "AAGC"
    seq2 = "CCAA"

    seq1_list = list(seq1)
    seq2_list = list(seq2)
    
    print("matching +", merge_parameter, "of", seq1, "with -", merge_parameter, "of", seq2)
    print("-----------------------------------------------------------------------------")
    print(seq1_list[:merge_parameter])
    print(seq2_list[-merge_parameter:])

    match_f_seq1 = seq1_list[:merge_parameter]
    match_f_seq2 = seq2_list[-merge_parameter:]

    if match_f_seq1 == match_f_seq2:
        print("")
        print("match detected")

    print("\n")

    print("matching -", merge_parameter, "of", seq1, "with +", merge_parameter, "of", seq2)
    print("-----------------------------------------------------------------------------")
    print(seq1_list[-merge_parameter:])
    print(seq2_list[:merge_parameter])

    match_b_seq1 = seq1_list[-merge_parameter:]
    match_b_seq2 = seq2_list[:merge_parameter]

    if match_b_seq1 == match_b_seq2:
        print("")
        print("match detected")
        print("\n")









if __name__ == "__main__":
    main()

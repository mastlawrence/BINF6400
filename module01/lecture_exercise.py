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

random.seed(100)

def main():

    ## Step 1: generate sample data
    data_set = generate_set(3, 4)
    data_set = ['AAGCC', 'CCAAA','GGGGG', 'TAAACC', "GGGGT"]

    ## Step 2: Look for overlap between the two sequence
    contig_set = find_contigs(data_set, 2)




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


def find_contigs(data_set, merge_parameter):
    """
    assembles contigs within the sequence data
    stored within the list
    """
    contigs = []
    i = 1
    while i < len(data_set):
        combined_seq = _detect_match(data_set[0], data_set[i], merge_parameter)

        if combined_seq is None:
            combined_seq = False

        print(combined_seq)


        if combined_seq == False:
            if i == len(data_set) - 1:
                print("bottom found!")
            i = i + 1

        else:
            data_set = [x for x in data_set if x not in [data_set[0], data_set[i]]]
            data_set.insert(0, combined_seq)


    return data_set



def _detect_match(seq1, seq2, merge_parameter):
    """
    test function for figuring out 
    how to merge and remove elements 
    from a list based on a match 
    parameter.
    """

    seq1_list = list(seq1)
    seq2_list = list(seq2)


    match_f_seq1 = seq1_list[:merge_parameter]
    match_f_seq2 = seq2_list[-merge_parameter:]

    if match_f_seq1 == match_f_seq2:

        combined_seq = seq2_list[:-merge_parameter] + seq1_list
        combined_seq = "".join(combined_seq)
 
        return combined_seq


    match_b_seq1 = seq1_list[-merge_parameter:]
    match_b_seq2 = seq2_list[:merge_parameter]

    if match_b_seq1 == match_b_seq2:

        combined_seq = seq1_list[:-merge_parameter] + seq2_list
        combined_seq = "".join(combined_seq)

        return combined_seq

if __name__ == "__main__":
    main()

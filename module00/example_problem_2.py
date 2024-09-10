## Take two sequences as inputs and find the longest common subsequence between the two strings

## Approach problem by calculating k-mers, and finding the longest identical k-mer shared between 
## the two strings

## sequence 1: A T G C A T C
## sequence 2: A T G T G C A T T

import sys 

def main():
    """
    Business Logic
    """
    seq1 = "ATGCATC"
    seq2 = "ATGTGCATT"

    ## Step 1: Accept user input
    seq1, seq2 = accept_user_input()

    ## Step 2: Generate list of k-mers for each sequence
    seq1_list = list_kmers(seq1)
    seq2_list = list_kmers(seq2)

    ## Step 3: Generate list of set intersections between two kmer lists
    common_elements = generate_intersection(seq1_list, seq2_list)

    ## Step 4: Select the longest shared subsequence
    longest_subsequence = select_longest_subsequence(common_elements)
    print(longest_subsequence)

    ## Step 5: Output results
    print("the longest shared subsequence is:", longest_subsequence)


def accept_user_input():
    """
    accepts user input of two sequences
    """
    seq1 = input("input sequence 1:")
    seq2 = input("input sequence 2:")

    return seq1, seq2


def list_kmers(seq):
    """
    Generate list of k-mers for a given sequence
    """
    ## declare empty list
    kmer_list = list()

    for i in range(len(seq), 0, -1):
        kmer = i

        for i in range(0,len(seq) - kmer):
            subseq = seq[i:i+kmer]
            kmer_list.append(subseq)

    ## filter for unique kmers and sort
    kmer_list = set(kmer_list)
    kmer_list = list(kmer_list)
    kmer_list = sorted(kmer_list, key=len)

    return kmer_list


def generate_intersection(seq1, seq2):
    """
    Generate list of set intersections to store 
    shared kmers between the two sequences 
    """
    set1, set2 = set(seq1), set(seq2)
    common_elements = set1.intersection(set2)

    return common_elements


def select_longest_subsequence(shared_kmers):
    """
    selects the longest shared kmer from the 
    generated list.
    """
    try:
        return  max(sorted(shared_kmers, key = len), key = len)

    except ValueError:
        print("no sequence data submitted! Please submit sequence data.")
        sys.exit()



if __name__ == "__main__":
    main()


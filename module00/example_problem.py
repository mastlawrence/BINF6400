## Module 00 Warm-up Coding Exercise

## Write a python program to take two sequences as input and find the longest common 
## subsequences between these two strings

## TODO: Possible idea is to think about this in terms of k-mers. Build lists for both
##       and find the largest k-mer which matches between the two sequences. Build both
##       and compare performance.

## one way is to model this pattern of scanning:

## Seq1: A T G C A T G
## Seq2: A T G T G C A T T

## Seq1:   A T G C A T G
## Seq2: A T G T G C A T T

## Seq1:     A T G C A T G
## Seq2: A T G T G C A T T

## Shift the shorter one along the longer one and count how many in each shift match


def main():
    """
    Business Logic
    """

    seq1 = list("ATGCATC")
    seq2 = list("ATGTGCATT")

    ## Step 1: Determine the long and short sequence
    long_seq, short_seq = determine_length(seq1, seq2)

    ## Step 2: Compare each sequence and return an index
    compare_lists(short_seq, long_seq)




    






def determine_length(seq1, seq2):
    """
    Determines which sequence is the 'short' sequence and 
    which is the 'long' sequence
    """

    length_seq1 = len(seq1)
    length_seq2 = len(seq2)

    if length_seq1 > length_seq2:
        long_seq = seq1
        short_seq = seq2

    else:
        long_seq = seq2
        short_seq = seq1

    return (long_seq, short_seq)


def compare_lists(list1, list2):
    """
    compares both lists. Returns a list of the index where
    both lists match and where they did not.
    """
    match_index = list()
    list2 = list2[0:len(list1)]
    
    print("list1", list1)
    print("list2", list2)




if __name__ == "__main__":
    main()



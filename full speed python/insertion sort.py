def InsertionSort(seq):
    for sliceEnd in range(len(seq)):
        # Build longer and longer sorted slices
        # In each iteration seq[0:sliceEnd] already sorted
        # Move first element after sorted slice left
        # Till its in the correct place

        pos = sliceEnd
        while pos>0 and seq[pos] < seq[pos-1]:
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
            pos = pos-1
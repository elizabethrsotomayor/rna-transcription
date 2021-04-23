def to_rna(dna_strand):
    rna_string = ''
    for char in dna_strand:
        if char == 'G':
            rna_string += 'C'
        elif char == 'C':
            rna_string += 'G'
        elif char == 'T':
            rna_string += 'A'
        elif char == 'A':
            rna_string += 'U'
        else:
            break

    return rna_string

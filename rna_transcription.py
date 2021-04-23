def to_rna(dna_strand):
    translation = dna_strand.maketrans('GCTA', 'CGAU')
    rna_string = dna_strand.translate(translation)
    return rna_string

def DNA_strand(dna: str) -> str:
    return dna.translate(str.maketrans("ATCG", "TAGC"))

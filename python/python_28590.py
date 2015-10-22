# Python 2.7 - Identify Pathogenicity Islands - Calculate GC Content Across Sections of a String
def get_gc_across_sections(s):
    sections =  [s[i:i+5] for i in range(0, len(s), 5)]
    return [GCcont(section) for section in sections]

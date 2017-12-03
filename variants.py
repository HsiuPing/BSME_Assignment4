# project: BMSE Assignment 4
# filename: variant.py
# time: 201712
# editor: HsiuPing Lin

class Variant(object):

    def __init__(self, chromosome, location, reference, alternative, name=None):
        """ Create a Variant instance

        Create a new Variant object, AKA a Variant instance. This is used by the
        expression Variant(). The parameters chromosome, location, reference and alternative are required,
        while the parameter name is optional.

        Args:
             chromosome (:obj:`str`): the chromosome name, it should follows the USCS HG 38 genome database
             location (:obj:`int`): the location of the variant
             reference (:obj:'str'): the reference nucleotide
             alternative (:obj:'str'): the alternative nucleotide
             name (:obj:`str`, optional): the person who has this variant
        """
        from urllib.request import urlopen

        link = "http://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.chrom.sizes"
        file = urlopen(link)
        myfile = file.read()
        content = myfile.decode()
        contents = content.split(sep='\n')
        contents = contents[:-1]
        chr_dict = dict()
        for line in contents:
            chr = line.split('\t')
            chr_dict[chr[0]] = int(chr[1])

        DNA_list = ["A", "T", "C", "G"]

        if chromosome not in chr_dict.keys():
            raise NameError("The chromosome name should follows the USCS HG 38 genome database")

        #if not isinstance(location, int):
        #    raise ValueError("The location ({}) should be an integer.".format(location))

        if not location in range (1, chr_dict[chromosome] + 1):
            raise ValueError("The location ({}) in ({}) should be in the range 1 to ({}).".format
                             (location, chromosome, chr_dict[chromosome]))

        reference = str.upper(reference)
        alternative = str.upper(alternative)

        if reference not in DNA_list:
            raise NameError("The reference ({}) should be one of ({}).".format
                            (reference, DNA_list))

        if alternative not in DNA_list:
            raise NameError("The alternative ({}) should be one of ({}).".format
                            (alternative, DNA_list))

        if reference == alternative:
            raise NameError("The alternative should not be the same with the reference.")

        self.chromosome = chromosome
        self.location = location
        self.reference = reference
        self.alternative = alternative
        self.name = name

    def __str__(self):
        """ Provide a string representation of this variant
        """
        return "chromosome {}; location {}; reference {}; alternative {}".format(
            self.chromosome,
            self.location,
            self.reference,
            self.alternative)


Variant1 = Variant(chromosome='chr1', location=15, reference="T", alternative="A")

print(Variant1)

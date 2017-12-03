# project: BMSE Assignment 4
# filename: load.py
# time: 201712
# editor: HsiuPing Lin

class Loading():

    @staticmethod
    def load_people(path):
        from person import Person
        file_people = open(path, mode="r")
        contents = file_people.read()
        content = contents.split(sep='\n')
        people_data = dict()
        for data in content:
            info = data.split('\t')

            if info[2] == " ":
                info[2] = None
            if info[3] == " ":
                info[3] = None

            people_data[info[0]] = Person(name=info[0], gender=info[1], mother=info[2], father=info[3])

        m_dict = {}
        f_dict = {}

        for k, v in people_data.items():
            if v.mother in people_data.keys():
                v.set_mother(people_data[v.mother])
            elif v.mother is not None:
                m_dict[v.name] = v.mother
            if v.father in people_data.keys():
                v.set_father(people_data[v.father])
            elif v.father is not None:
                f_dict[v.name] = v.father

        for k, v in m_dict.items():
            people_data[v] = Person(name=v, gender='f')
            people_data[k].set_mother(people_data[v])

        for k, v in f_dict.items():
            people_data[v] = Person(name=v, gender='m')
            people_data[k].set_father(people_data[v])

        return people_data

    @staticmethod
    def load_variants(path):
        from variants import Variant
        file_variants = open(path, mode="r")
        contents = file_variants.read()
        content = contents.split(sep='\n')
        variants_data = dict()
        i = 1

        for data in content:
            info = data.split('\t')

            if info[4] == " ":
                info[4] = None

            v_name = 'variant_' + str(i)
            variants_data[v_name] = Variant(chromosome=info[0], location=int(float(info[1])),
                                            reference=info[2],alternative=info[3], name=info[4])
            i += 1
        return variants_data

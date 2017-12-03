# project: BMSE Assignment 4
# filename: person.py
# time: 201712
# editor: HsiuPing Lin

""" Person, with heredity and other characteristics

:Author: Arthur Goldberg <Arthur.Goldberg@mssm.edu>
:Date: 2017-10-12
:Copyright: 2017, Arthur Goldberg
:License: MIT
"""

class Person(object):
    """ Person
          
    Attributes:
        name (:obj:`str`): a person's name
        gender (:obj:`str`): a person's gender
        mother (:obj:`Person`): a person's mother
        father (:obj:`Person`): a person's father
        children (:obj:`set` of `Person`): a person's children
        variants (:obj:'list' of 'Variant'): a person's variants
    """

    def __init__(self, name, gender, mother=None, father=None):
        """ Create a Person instance

        Create a new Person object, AKA a Person instance. This is used by the
        expression Person(). The parameters name and gender are required, while   other parameters are
        optional.

        Args:
             name (:obj:`str`): the person's name
             gender (:obj:`str`): the person's gender
             mother (:obj:`Person`, optional): the person's mother
             father (:obj:`Person`, optional): the person's father
        """
        # TODO: standardize the representations of gender, so that M, m, and male are valid inputs
        # for male, but only one standard stored constant represents male, and similarly for female.

        gender_list= [("M", "m", "male"), ("F", "f", "female")]


        if gender in gender_list[0]:
            gender = "male"
            self.gender = gender
        elif gender in gender_list[1]:
            gender = "female"
            self.gender = gender
        else:
            raise NameError("The gender is not valid. It should be ({}) or ({})".format(
                gender_list[0], gender_list[1]))

        self.name = name
        self.mother = mother
        self.father = father
        self.children = set()
        self.variants = list()

    # TODO: add a data structure containing this person's variants, and methods that add a variant,
    # and list all variants

    # This method is to get variants from the input data, then collect this person's variants and put
    # them into variants attribute
    def get_variants(self):
        from load import Loading as ld
        variants_data = ld.load_variants('variants_input.txt')
        try:
            for k, v in variants_data.items():
                if v.name == self.name:
                    self.variants.append(v)
        except:
            print('Variant data loading error, or not found!')
        return self.variants

    # A method to list all variants
    def print_variants(self):
        for v in self.variants:
            print('\t', v)

    # a method created for adding a variant to this person's variants list.
    # The parameter 'variant' should be the object 'Variant'.
    def add_variant(self, variant):
        self.variants = self.variants.append(variant)
        return self.variants

    # a method annotated with '@staticmethod' is a 'static method' that does not receive an
    # implicit first argument. Rather, it is called C.m(), where the class C identifies the
    # class in which the method is defined.
    @staticmethod
    def get_persons_name(person):
        """ Get a person's name; if the person is not known, return 'NA'

        Returns:
            :obj:`str`: the person's name, or 'NA' if they're not known
        """
        if person is None:
            return 'NA'
        return person.name

    # TODO: write 'set_father' and 'set_mother' methods that set a person's father or mother,
    # and adds the person to the father's or mother's children. Replace all statements below
    # that set a person's father or mother attribute with these methods.

    def set_father(self, father):
        self.father = father
        father.children.add(self)

    def set_mother(self, mother):
        self.mother = mother
        mother.children.add(self)

    # TODO: remove the 'add_child' method and replace any statements that use it with a call to
    # 'set_father' or 'set_mother'

    # TODO: write 'remove_father' and 'remove_mother' methods that removes a person's father or mother,
    # and removes the person from the father's or mother's children. Test these methods.

    def remove_father(self):
        if self.father:
            self.father.children.remove(self)
            self.father = None

    def remove_mother(self):
        if self.mother:
            self.mother.children.remove(self)
            self.mother = None

    # TODO: create a 'siblings' method that returns a person's siblings, and write a 'half_siblings'
    # method that returns a person's half-siblings.

    def siblings(self):
        if (self.father) and (self.mother):
            children_from_father = self.father.children
            children_from_mother = self.mother.children
            siblings = set(children_from_father.intersection(children_from_mother))
            siblings.remove(self)
            return siblings
        else:
            siblings = None
        return siblings

    def half_siblings(self):
        if (self.father) and (self.mother):
            children_from_father = self.father.children
            children_from_mother = self.mother.children
            allchildren = set(children_from_father.union(children_from_mother))
            siblings = set(children_from_father.intersection(children_from_mother))
            half_siblings = allchildren - siblings
        elif (self.father) and (self.mother == None):
            half_siblings = self.father.children
            half_siblings.remove(self)
        elif (self.mother) and (self.father == None):
            half_siblings = self.mother.children
            half_siblings.remove(self)
        else:
            half_siblings = None
        return half_siblings

    def sons(self):
        """ Get this person's sons

        Returns:
            :obj:`list` of `Person`: the person's sons
        """
        sons = []
        for child in self.children:
            if child.gender == 'male':
                sons.append(child)
        return sons

    def __str__(self):
        """ Provide a string representation of this person
        """
        return "{}: gender {}; mother {}; father {}".format(
            self.name,
            self.gender,
            Person.get_persons_name(self.mother),
            Person.get_persons_name(self.father))

    def grandparents_structured(self):
        ''' Provide this person's grandparents

        Returns:
            :obj:`tuple`: the person's grandparents, in a 4-tuple:
            (maternal grandmother, maternal grandfather, paternal grandmother, paternal grandfather)
            Missing individuals are identified by None.
        '''
        grandparents = []
        if self.mother:
            grandparents.extend([self.mother.mother, self.mother.father])
        else:
            grandparents.extend([None, None])
        if self.father:
            grandparents.extend([self.father.mother, self.father.father])
        else:
            grandparents.extend([None, None])
        return tuple(grandparents)

    # TODO: EXTRA CREDIT: implement this descendants method, which has analogous semantics to the
    # ancestors method below. The implementation may use a while loop or be recursive. Use
    # your 'descendants' method to implement 'children', 'grand_children', and 'all_descendants'.
    def descendants(self, min_depth, max_depth=None):
        """ Return this person's descendants within a generational depth range

        Obtain descendants whose generational depth satisfies `min_depth` <= depth <= `max_depth`.
        E.g., this person's children would be obtained with `min_depth` = 1, and this person's
        grandchildren and great-grandchildren would be obtained with `min_depth` = 3 and
        `max_depth` = 3.

        Args:
            min_depth (:obj:`int`): the minimum depth of descendants which should be provided;
                this person's depth is 0, their children's depth is 1, etc.
            max_depth (:obj:`int`, optional): the minimum depth of descendants which should be
                provided; if `max_depth` is not provided, then `max_depth` == `min_depth` so that only
                descendants at depth == `min_depth` will be provided; a `max_depth` of infinity will
                obtain all descendants at depth >= `min_depth`.

        Returns:
            :obj:`set` of `Person`: this person's descendants

        Raises:
            :obj:`ValueError`: if `max_depth` < `min_depth`
        """
        if min_depth is not None:
            if max_depth < min_depth:
                    raise ValueError("max_depth ({}) cannot be less than min_depth ({})".format(
                        max_depth, min_depth))
        else:
            # collect just one depth
            max_depth = min_depth
        collected_descendants = set()
        return self._descendants(collected_descendants, min_depth, max_depth)

    def ancestors(self, min_depth, max_depth=None):
        """ Return this person's ancestors within a generational depth range

        Obtain ancestors whose generational depth satisfies `min_depth` <= depth <= `max_depth`. E.g.,
        a person's parents would be obtained with `min_depth` = 1, and this person's parents and
        grandparents would be obtained with `min_depth` = 1 and `max_depth` = 2.

        Args:
            min_depth (:obj:`int`): the minimum depth of ancestors which should be provided;
                this person's depth is 0, their parents' depth is 1, etc.
            max_depth (:obj:`int`, optional): the minimum depth of ancestors which should be
                provided; if `max_depth` is not provided, then `max_depth` == `min_depth` so that only
                ancestors at depth == `min_depth` will be provided; a `max_depth` of infinity will obtain
                all ancestors at depth >= `min_depth`.

        Returns:
            :obj:`set` of `Person`: this person's ancestors

        Raises:
            :obj:`ValueError`: if `max_depth` < `min_depth`
        """
        if max_depth is not None:
            if max_depth < min_depth:
                    raise ValueError("max_depth ({}) cannot be less than min_depth ({})".format(
                        max_depth, min_depth))
        else:
            # collect just one depth
            max_depth = min_depth
        collected_ancestors = set()
        return self._ancestors(collected_ancestors, min_depth, max_depth)

    def _descendants(self, collected_descendants, min_depth, max_depth):
        """ Obtain this person's descendants who lie within the generational depth [min_depth, max_depth]

        This is a private, recursive method that recurses through the ancestry via parent references.

        Args:
            collected_descendants (:obj:`set`): descendants collected thus far by this method
            min_depth (:obj:`int`): see `descendants()`
            max_depth (:obj:`int`): see `descendants()`

        Returns:
            :obj:`set` of `Person`: this person's descendants

        Raises:
            :obj:`ValueError`: if `max_depth` < `min_depth`
        """
        if min_depth <= 0:
            collected_descendants.add(self)
        if 0 < max_depth:
            for child in self.children:
                if self.children is not None:
                    child._descendants(collected_descendants, min_depth-1, max_depth-1)
        return collected_descendants

    def _ancestors(self, collected_ancestors, min_depth, max_depth):
        """ Obtain this person's ancestors who lie within the generational depth [min_depth, max_depth]

        This is a private, recursive method that recurses through the ancestry via parent references.

        Args:
            collected_ancestors (:obj:`set`): ancestors collected thus far by this method
            min_depth (:obj:`int`): see `ancestors()`
            max_depth (:obj:`int`): see `ancestors()`

        Returns:
            :obj:`set` of `Person`: this person's ancestors

        Raises:
            :obj:`ValueError`: if `max_depth` < `min_depth`
        """
        # TODO: EXTRA CREDIT: can a cycle in the ancestry graph will create an infinite loop?
        # if so, avoid this problem.
        if min_depth <= 0:
            collected_ancestors.add(self)
        if 0 < max_depth:
            for parent in [self.mother, self.father]:
                if parent is not None:
                    parent._ancestors(collected_ancestors, min_depth-1, max_depth-1)
        return collected_ancestors


    def parents(self):
        ''' Provide this person's parents

        Returns:
            :obj:`set`: this person's known parents
        '''
        return self.ancestors(1)

    def grandparents(self):
        ''' Provide this person's known grandparents, by using ancestors()

        Returns:
            :obj:`set`: this person's known grandparents
        '''
        return self.ancestors(2)

    def great_grandparents(self):
        return self.ancestors(3)

    def all_grandparents(self):
        ''' Provide all of this person's known grandparents, from their parents' parents on back 

        Returns:
            :obj:`set`: all of this person's known grandparents
        '''
        return self.ancestors(2, max_depth=float('inf'))

    def all_ancestors(self):
        ''' Provide all of this person's known ancestors

        Returns:
            :obj:`set`: all of this person's known ancestors
        '''
        return self.ancestors(1, max_depth=float('inf'))



import unicodedata


class NormalizedStr:
    '''
    By default, Python's str type stores any valid unicode string.
    This can result in unintuitive behavior.
    For example:
    >>> 'César' in 'César Chávez'
    True
    >>> 'César' in 'César Chávez'
    False
    The two strings to the right of the in keyword
    above are equal *semantically*,
    but not equal *representationally*.
    In particular, the first is in NFC form, and the second is in NFD form.
    The purpose of this class is to automatically normalize our strings for us,
    making foreign languages "just work" a little bit easier.
    '''

    def __init__(self, text, normal_form='NFC'):
        self.norm = normal_form
        self.text = unicodedata.normalize(self.norm, text)
        self.i = -1

    def __repr__(self):
        '''
        The string returned by the __repr__ function should
        be valid python code
        that can be substituted directly into the python
        interpreter to reproduce an equivalent object.
        '''
        return "NormalizedStr(\'{}\', \'{}\')".format(self.text, self.norm)

    def __str__(self):
        '''
        This functions converts the NormalizedStr
        into a regular string object.
        The output is similar, but not exactly
        the same, as the __repr__ function.
        '''
        return str(self.text)

    def __len__(self):
        '''
        Returns the length of the string.
        The expression `len(a)` desugars to a.__len__().
        '''
        return len(self.text)

    def __contains__(self, substr):
        '''
        Returns true if the `substr` variable is contained within `self`.
        The expression `a in b` desugars to `b.__contains__(a)`
        '''
        normalise = unicodedata.normalize(self.norm, substr)
        string1 = str(self.text)
        string2 = str(normalise)
        return string1.__contains__(string2)

    def __getitem__(self, index):
        '''
        Returns the character at position `index`.
        The expression `a[b]` desugars to `a.__getitem__(b)`.
        '''
        return self.text.__getitem__(index)

    def lower(self):
        '''
        Returns a copy in the same normalized form, but lower case.
        '''
        return self.text.lower()

    def upper(self):
        '''
        Returns a copy in the same normalized form, but upper case.
        '''
        return self.text.upper()

    def __add__(self, b):
        '''
        Returns a copy of `self` with `b` appended to the end.
        The expression `a + b` gets desugared into `a.__add__(b)`.
        '''
        filler = self.text + unicodedata.normalize(self.norm, str(b))
        word = unicodedata.normalize(self.norm, filler)
        return NormalizedStr(word, self.norm)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.text) - 1:
            raise StopIteration
        else:
            self. i += 1
            return self.text[self.i]


class NormalIter:
    def __init__(self, text):
        self.text = text
        self.i = -1

    def __next__(self):
        if self.i == len(self.text) - 1:
            raise StopIteration
        else:
            self.i += 1
            return self.text[self.i]

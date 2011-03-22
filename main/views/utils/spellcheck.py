import popen2

class Hunspell:
    def __init__(self):
        self._f = popen2.Popen3("hunspell -d ./en_US")
        self._f.fromchild.readline() #skip the credit line
    def suggest(self, words):
        if isinstance(words, basestring):
            words = words.split(' ')
        output = []
        for word in words:
            self._f.tochild.write(word+'\n')
            self._f.tochild.flush()
            s = self._f.fromchild\
            .readline()\
            .strip()\
            .lower()
            self._f.fromchild.readline() #skip the blank line
            if s == "*":
                output.append(None)
            elif s[0] == '#':
                output.append("No Suggestions")
            elif s[0] == '+':
                pass
            else:
                output.append(
                        s.split(':')[1]\
                        .strip()\
                        .split(', ')
                        )
        output = filter(
                lambda pair:
                    pair[1] is not None,
                zip(words, output)
                )
        return output
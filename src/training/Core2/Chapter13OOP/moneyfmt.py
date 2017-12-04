class MoneyFmt(object):
    'exercise 13-3 '
    def __init__(self, value=0.0):
        assert isinstance(value, float), "Value must be a float!"
        self.value = value


    def __repr__(self):
        return self.value


    def __str__(self):
        val = ''
        val2str = '%.2f' % self.value
        count = 0
        for i in range(-1, -(len(val2str)+1), -1):
            val = val + val2str[i]
            if val2str[i] == '.':
                count = 0
            else:
                count += 1
                if count % 3 == 0 and i != -len(val2str):
                    val = val + ','
        return '$' + val[::-1]

    def update(self, new_value):
        self.value = new_value

    def __nonzero__(self):
        return 0 == self.value

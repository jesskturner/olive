class Task(object):
    PRIORITY_OPTIONS = (
        (1, 'low'),
        (2, 'medium'),
        (3, 'high'),
        (4, 'highest'),
    )
    SIZE_OPTIONS = (
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large'),
        ('xl', 'extra large'),
    )

    def __init__(self, **kwargs):
        self.description = kwargs.get('description')
        self.priority = kwargs.get('priority')
        self.size = kwargs.get('size')
        self.tags = kwargs.get('tags')

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority):
        if priority not in [
            short_name for short_name, _ in self.PRIORITY_OPTIONS
        ]:
            self.__priority = 1
        else:
            self.__priority = priority

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size in [
            size_int for size_int, _ in self.SIZE_OPTIONS
        ]:
            self.__size = size
        else:
            self.__size = 's'

    def __repr__(self):
        return u'{} ({} {} {})'.format(
            self.description, self.priority, self.size, self.tags)

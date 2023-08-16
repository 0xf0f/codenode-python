class TestClass(A, B, C):
    def test_method(self, a, b, c, d=test):
        """
        This is an example docstring.
        This is another line.
        """
        # This is an example comment.
        # This is another line.


# class TestClass(A, B, C):
#     def test_method(self, a, b, c, d=test):
#         """
#         This is an example docstring.
#         This is another line.
#         """
#         # This is an example comment.
#         # This is another line.


def test_function(a, b, c=123):
    pass


test_function(a, b, c=123)


for i in range(10):
    pass
else:
    pass


while True:
    pass
else:
    pass


if True:
    pass
elif True:
    pass


match [1, 2]:
    case [x, y]:
        pass


try:
    pass
except (ValueError, TypeError) as error:
    pass
else:
    pass
finally:
    pass


try:
    pass
except* (ValueError, TypeError) as error:
    pass



import pathlib

cd = pathlib.Path(__file__).absolute().parent


def generate_code():
    import codenode

    from codenode_python import (
        Class,
        Function,
        Call,
        For,
        While,
        If,
        Match,
        Try,
        DocString,
        Comment,
        commented,
    )

    test_class = Class('TestClass', 'A', 'B', 'C')
    test_method = test_class.add_method('test_method', 'a', 'b', 'c', d='test')
    test_method.add_child(
        DocString('This is an example docstring.\nThis is another line.')
    )
    test_method.add_child(
        Comment('This is an example comment.\nThis is another line.')
    )

    commented_test_class = commented(test_class)

    function = Function('test_function', 'a', 'b', c='123')
    function_call = Call('test_function', 'a', 'b', c='123')

    for_loop = For('i in range(10)')
    for_else = for_loop.add_else()

    while_loop = While('True')
    while_else = while_loop.add_else()

    if_check = If('True')
    elif_check = if_check.add_elif('True')

    match_statement = Match('[1, 2]')
    match_case = match_statement.add_case('[x, y]')

    try_block = Try()
    except_block = try_block.add_except(
        ('ValueError', 'TypeError'), 'error', False
    )
    else_block = try_block.add_else()
    finally_block = try_block.add_finally()

    try_block_2 = Try()
    except_group_block = try_block_2.add_except(
        ('ValueError', 'TypeError'), 'error', True
    )

    block = [
        test_class,
        codenode.empty_lines(2),
        commented_test_class,
        codenode.empty_lines(2),
        function,
        codenode.empty_lines(2),
        function_call,
        codenode.empty_lines(2),
        for_loop,
        codenode.empty_lines(2),
        while_loop,
        codenode.empty_lines(2),
        if_check,
        codenode.empty_lines(2),
        match_statement,
        codenode.empty_lines(2),
        try_block,
        codenode.empty_lines(2),
        try_block_2,
        codenode.empty_lines(2),
    ]

    return codenode.dumps(block)


def basic_test():
    with open(cd / 'example_code.py') as file:
        code = file.read()

    generated_code = generate_code()
    assert code == generated_code
    compile(generated_code, '<code>', 'exec')


if __name__ == '__main__':
    basic_test()

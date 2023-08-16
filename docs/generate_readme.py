import codenode
import pathlib
import string

from docs.generation_utilities import (
    functions, classes, variables,
    AttributeDocumentation, FunctionDocumentation
)

cd = pathlib.Path(__file__).absolute().parent
template_path = cd / 'readme_template.md'
output_path = cd.parent / 'README.md'

contents = (
    *classes((
        'codenode_python.node.Node',
        'codenode_python.Function',
        'codenode_python.Class',
        'codenode_python.method.Method',
        'codenode_python.If',
        'codenode_python.conditional.Elif',
        'codenode_python.conditional.Else',
        'codenode_python.For',
        'codenode_python.While',
        'codenode_python.Try',
        'codenode_python.try_except.Except',
        'codenode_python.try_except.Finally',
        'codenode_python.With',
        'codenode_python.Match',
        'codenode_python.match_statement.Case',
        'codenode_python.DocString',
        'codenode_python.Comment',
    )),

    FunctionDocumentation('codenode_python.commented'),
)


def reference_contents():
    for item in contents:
        yield codenode.line(f'- [{item.path}](#{item.get_link()})')


def reference():
    for item in contents:
        yield codenode.line('---')
        yield item


if __name__ == '__main__':
    with open(template_path) as file:
        template = string.Template(file.read())

    with open(output_path, 'w') as file:
        file.write(
            template.safe_substitute(
                {
                    'reference_contents': codenode.dumps(reference_contents(), debug=True),
                    'reference': codenode.dumps(reference(), debug=True),
                }
            )
        )

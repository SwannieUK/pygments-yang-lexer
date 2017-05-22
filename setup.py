from setuptools import setup, find_packages

setup (
    name='pygments_yang_lexer',
    version = "0.0.2",
    author = "Carl Moberg",
    description = ("A pygments lexer for Yang."),
    long_description=read('README.md'),
    packages=find_packages(),
    entry_points =
    """
    [pygments.lexers]
    yang = pygments_yang_lexer.yang:YangLexer
    """,
)
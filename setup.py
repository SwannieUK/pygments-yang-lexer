from setuptools import setup, find_packages

setup (
    name='pygments_yang_lexer',
    packages=find_packages(),
    entry_points =
    """
    [pygments.lexers]
    yang = pygments_yang_lexer.yang:YangLexer
    """,
)
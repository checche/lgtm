import click


@click.command()
def cli():
    """LGTM生成ツール"""
    lgtm()
    click.echo('lgtm')


def lgtm():
    pass

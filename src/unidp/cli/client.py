import os
import click
from pathlib import Path
from unidp.version import __version__
from unidp.utils.cli_parser import arg_parse
from loguru import logger
from unidp.cli.common import doc_suffixes,image_suffixes, do_parse

@click.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.pass_context
@click.version_option(__version__,
                      '--version',
                      '-v',
                      help='display the version and exit')
@click.option(
    '-p',
    '--path',
    'input_path',
    type=click.Path(exists=True),
    # required=True,
    help='local filepath or directory. support pdf, png, jpg, jpeg files',
)
@click.option(
    '-o',
    '--output',
    'output_dir',
    type=click.Path(),
    # required=True,
    help='output local directory',
)
def main(ctx, input_path, output_dir, **kwargs):

    kwargs.update(arg_parse(ctx))

# def main(input_path,output_dir):
    os.makedirs(output_dir, exist_ok=True)

    def parse_doc(input_file_path_list: list[Path]):
        try:
            logger.info('----- parse docx started -----')
            do_parse(input_file_path_list, output_dir, parse_method='paddleocr')
            logger.info('----- parse docx finished -----')
        except Exception as e:
            logger.exception(e)

    if os.path.isdir(input_path):
        doc_path_list = []
        for doc_path in Path(input_path).glob('*'):
            if doc_path.suffix in doc_suffixes+image_suffixes:
                doc_path_list.append(doc_path)
        parse_doc(doc_path_list)
    else:
        parse_doc([Path(input_path)])


if __name__=='__main__':
    input_path=r"F:\my-home\1-ai-code\16-data-process\data_process\data\input"
    output_dir=r"F:\my-home\1-ai-code\16-data-process\data_process\data\output"
    
    from click.testing import CliRunner
    runner = CliRunner()
    result = runner.invoke(main, ['-p', input_path,'-o', output_dir])
    # main(input_path= input_path, output_dir= output_dir)
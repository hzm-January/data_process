
from loguru import logger
from pathlib import Path
from docling_core.types.doc import ImageRefMode, PictureItem, TableItem

doc_suffixes = [".pdf",".docx"]
image_suffixes = [".png", ".jpeg", ".jpg", ".webp", ".gif"]

from docling.document_converter import DocumentConverter


def do_parse(
        input_file_path_list: list[str],
        output_dir,
        parse_method="auto",
        formula_enable=True,
        table_enable=True,
        start_page_id=0,
        end_page_id=None,
        **kwargs,
):
    logger.info(f'do_parse: \n input_file_path_list:{input_file_path_list} \n output_dir:{output_dir}')
    
    logger.info('------- do parse started --------')
    # source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
    # converter = DocumentConverter()
    # result = converter.convert(source)
    # print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"

    for file_path in input_file_path_list:
        source = file_path # document per local path or URL
        converter = DocumentConverter()
        result = converter.convert(source)
        print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"
        # Save HTML with externally referenced pictures
        doc_filename= Path(file_path).stem
        print(type(doc_filename))
        html_filename = Path(output_dir) / f"{doc_filename}-with-image-refs.html"
        result.document.save_as_markdown(html_filename, image_mode=ImageRefMode.REFERENCED)

    logger.info('------- do parse finished --------')
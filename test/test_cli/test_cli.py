import pytest
import os
from lib import common
import logging
from conf import conf

code_path = conf.conf["code_path"] 
output_path = conf.conf["pdf_res_path"]

class TestDocConversion:

    def test_convert_doc_to_md(self):
        """
        将DOC文件转换为Markdown
        """
        file_path = os.path.join(code_path, "datas/test01.doc")
        cmd = f"python {code_path}/magic_doc/cli.py --file-path {file_path} --output {output_path}"
        logging.info(cmd)
        common.check_shell(cmd)
        # 这里可以添加更多的检查函数来验证转换结果

    def test_convert_docx_to_md(self):
        """
        将DOCX文件转换为Markdown
        """
        file_path = os.path.join(code_path, "datas/test02.docx")
        cmd = f"python {code_path}/magic_doc/cli.py --file-path {file_path} --output {output_path}"
        logging.info(cmd)
        common.check_shell(cmd)
        # 这里可以添加更多的检查函数来验证转换结果

    def test_convert_html_to_md(self):
        """
        将HTML文件转换为Markdown
        """
        file_path = os.path.join(code_path, "datas/test03.html")
        cmd = f"python {code_path}/magic_doc/cli.py --file-path {file_path} --output {output_path}"
        logging.info(cmd)
        common.check_shell(cmd)
        # 这里可以添加更多的检查函数来验证转换结果

    def test_convert_pdf_to_md(self):
        """
        将PDF文件转换为Markdown
        """
        file_path = os.path.join(code_path, "datas/test04.pdf")
        cmd = f"python {code_path}/magic_doc/cli.py --file-path {file_path} --output {output_path}"
        logging.info(cmd)
        common.check_shell(cmd)
        # 这里可以添加更多的检查函数来验证转换结果

    def test_convert_ppt_to_md(self):
        """
        将PPT文件转换为Markdown
        """
        file_path = os.path.join(code_path, "datas/test05.ppt")
        cmd = f"python {code_path}/magic_doc/cli.py --file-path {file_path} --output {output_path}"
        logging.info(cmd)
        common.check_shell(cmd)
        # 这里可以添加更多的检查函数来验证转换结果

    def test_convert_pptx_to_md(self):
        """
        将PPTX文件转换为Markdown
        """
        file_path = os.path.join(code_path, "datas/test06.pptx")
        cmd = f"python {code_path}/magic_doc/cli.py --file-path {file_path} --output {output_path}"
        logging.info(cmd)
        common.check_shell(cmd)
        # 这里可以添加更多的检查函数来验证转换结果

if __name__ == "__main__":
    pytest.main(["-v", __file__])
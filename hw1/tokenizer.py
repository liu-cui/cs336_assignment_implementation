import regex
import json
import tiktoken
import numpy as np
from typing import Dict, List, Set, Tuple, Iterable, Iterator


def get_bytes_to_unicode_local():
    """
    字节转换为unicode
    """
    pass


class BPETokenizer:
    def __init__(self, vocab, merges, special_tokens=None):
        """
        :param vocab: 词汇表{Id: str}
        :param merges: 合并规则列表，每个元素是元组(bytes_token1, bytes_token2)
        :param special_tokens: 可选的特殊符号列表(字符串str)
        """
        self.vocab: Dict[int, bytes] = vocab
        self.merges: List[Tuple[bytes, bytes]]  = merges
        self.special_tokens: List[str] = special_tokens


    @classmethod
    def from_files(cls, vocab_filepath: str, merges_filepath: str,special_tokens: List[str] | None = None):
        """
        类方法: 从序列化的词汇表和合并列表文件构造并返回一个分词器实例
        :param vocab_filepath: 词汇表文件的路径
        :param merges_filepath: 合并规则文件的路径
        :param special_tokens: 可选的特殊符号的列表
        return: BPETokenizer的一个实例
        """
        pass

    def pre_tokenize(self, text:str) -> List[str]:
        """
        将文本预处理为字节块列表
        """
        pass

    def merge_tokens(self, token_bytes: bytes) -> List[bytes]:
        """
        字节块 拆成 字节，再根据 合并规则 合并为新的列表
        """
        pass

    def encode(self, text:str) -> list[int]:
        """
        将文本编码为token ID
        """
        pass

    def encode_iterable(self, iterable: Iterable[str]) -> Iterator[int]:
        """
        给定一个字符串可迭代对象，返回一个惰性产生token ID的生成器
        用来进行内存高效处理大文件
        """
        pass
    
    def decode(self, ids: list[int]) -> str:
        """
        token ID序列解码为文本
        """
        pass

    
 
    


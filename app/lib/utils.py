def is_isbn_or_key(word: str):
    """
    判断请求类型isbn或者分页查询
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    # 新isbn 13位0-9数字
    # 老isbn10 10个0-9数字，含有-
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in word:
        shor_word = word.replace('-', '')
        if len(shor_word) == 10 and shor_word.isdigit():
            isbn_or_key = 'isbn'
    return isbn_or_key

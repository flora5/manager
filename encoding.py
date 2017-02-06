#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 2.5.1
# Last Changed: 2009-06-10 14:27:40

def safe_iconv(text, from_code = 'UTF8', to_code = 'GBK'):
    '''无差错编码转换:对于非法编码的字符使用?代替
    @parm f:Convert characters from encoding
    @parm t:Convert characters to encoding
    '''
    while True:
        try:
            r = unicode(text, from_code)
            break
        except UnicodeDecodeError, e:
            text = e.object[:e.start] + '?'*(e.end - e.start) + e.object[e.end:]
    return r.encode(to_code)

#text = "中文测试"

#aa = safe_iconv(text, from_code = 'UTF8', to_code = 'GBK')
#print aa

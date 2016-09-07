# -*- iso:8859-1 -*-
# strformat.py
"""Módulo de formatação de strings.
"""

def frmt_bytes(bytes):
    """Formata um inteiro enviado em "bytes" para um
    forma mais bonitinha, GB, MB, enfim. [1]
    """
    if bytes < 1024:
        return '%dB' % (bytes)
    elif bytes < (1024 * 1024):
        return '%.1fKB' % (bytes / 1024.0)
    elif bytes < (1024 * 1024 * 1024):
        return '%.1fMB' % (bytes / 1024.0 / 1024.0)
    else:
        return '%.1fGB' % (bytes / 1024.0 / 1024.0 / 1024.0)

def strip_html(text):
    """Remove todo o html de uma determinada string. [2]
    """
    import re
    s = re.sub('<[^>]*>', '', text)
    return s

# Código de inicialização:
print "Inicializando módulo strformat"

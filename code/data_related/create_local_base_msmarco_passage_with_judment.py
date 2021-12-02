"""
Objetivo: criar base local msmarco-passage com julgamentos
"""
import requests
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
from util import util_elastic_search as util_es

util_es.create_doc_store(parm_language='pt')
#util_es.create_doc_store(parm_language='en')

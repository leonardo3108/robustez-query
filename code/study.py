"""
just to explore coding
"""
print('oi')
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath('.'))
    sys.path.append(os.path.abspath('.\.'))
import pandas as pd
from util import util_bd_dataframe as util_bd_pandas
from util import util_elastic_search as util_es

util_es.show_all_indexes()
exit()
doc_store = util_es.return_doc_store('en')


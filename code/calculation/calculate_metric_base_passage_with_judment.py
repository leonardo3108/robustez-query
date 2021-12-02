import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
from util import util_metric_calcutation as util_calc

language_context = 'pt'
#util_calc.calculate_metric_in_es('bm25', language_context)
util_calc.calculate_metric_in_es('dpr', language_context)
# util_calc.calculate_metric_in_es('rerank', language_context)



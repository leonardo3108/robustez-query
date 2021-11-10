import gzip





Como instalar elasticsearch local

wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.2-linux-x86_64.tar.gz -q
mkdir temp
mv elasticsearch-7.9.2-linux-x86_64.tar.gz temp
cd temp
tar -xzf elasticsearch-7.9.2-linux-x86_64.tar.gz
chown -R daemon:daemon elasticsearch-7.9.2
sudo chown -R daemon:daemon elasticsearch-7.9.2
cd elasticsearch-7.9.2/
# investigando se java_home está ok. Setar path sem o final "/bin/java"
echo $JAVA_HOME
java -version
sudo update-alternatives --config java
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
# para resolver o problema de iniciar não como root:
#   conceder grant
sudo chmod -R 777 .
#   não usar sudo ao ativar o serviço e
./bin/elasticsearch


Como iniciar serviço elasticsearch local


"""
! wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.2-linux-x86_64.tar.gz -q
! tar -xzf elasticsearch-7.9.2-linux-x86_64.tar.gz
! chown -R daemon:daemon elasticsearch-7.9.2
"""

import os
from subprocess import Popen, PIPE, STDOUT
es_server = Popen(['elasticsearch-7.9.2/bin/elasticsearch'],
                   stdout=PIPE, stderr=STDOUT,
                   preexec_fn=lambda: os.setuid(1)  # as daemon
                  )
# wait until ES has started

exit()

for i, line in enumerate(gzip.open('temp\collection.tar.gz', mode='rt')):
    fields = line.strip().split()
    if i > 10: break
    pid = fields[0]
    text = ' '.join(fields[1:])
    print(pid, text)

data_json = []
for i, line in enumerate(gzip.open('collection.tar.gz', mode='rt')):
    fields = line.strip().split()
    if i == 0: # pula primeiro registro
      pid = 0
      text = 'The presence of communication amid scientific minds was equally important to the success of the Manhattan Project as scientific intellect was. The only cloud hanging over the impressive achievement of the atomic researchers and engineers is what their success truly meant; hundreds of thousands of innocent lives obliterated.'
    else:
      pid = fields[0]
      text = ' '.join(fields[1:])
    json_docto = {
        'text': text,
        'id':pid,
        'meta': {
            'source': 'msmarco-passage'
        }
    }
    data_json.append(json_docto)
    if i <= 4:
        print(pid, 'text', text)



"""
import wget
url = 'https://msmarco.blob.core.windows.net/msmarcoranking/collection.tar.gz'
filename = wget.download(url, out='C:')

exit()
passage_text = {}

"""
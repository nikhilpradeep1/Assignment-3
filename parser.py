from operator import truediv
from goatools import obo_parser
import wget
import os
import networkx as nx

go_obo_url = 'http://current.geneontology.org/ontology/go.obo'
data_folder = os.getcwd() + '/Assignment 3'

# Check if we have the ./data directory already
if(not os.path.isfile(data_folder)):
    # Emulate mkdir -p (no error if folder exists)
    try:
        os.mkdir(data_folder)
    except OSError as e:
        if(e.errno != 17):
            raise e
else:
    raise Exception('Data path (' + data_folder + ') exists as a file. '
                   'Please rename, remove or change the desired location of the data path.')

# Check if the file exists already
if(not os.path.isfile(data_folder+'/go.obo')):
    go_obo = wget.download(go_obo_url, data_folder+'/go.obo')
else:
    go_obo = data_folder+'/go.obo'

go = obo_parser.GODag(go_obo)
go_dag = nx.DiGraph()
goStr = str(go)
nodes = []
for x in goStr.splitlines():
    if (x.__contains__("id:G")) and not (x.__contains__("item")):
        go_id = x[5:15]
        go_term = go[go_id]
        kDict = {
                    "id" : go_id,
                    "name" : go_term.name,
                    "namespace" : go_term.namespace
                }
        nodes.append(kDict)


for y in nodes:
    go_dag.add_node(y.get("id"), name = y.get("name"), namespace = y.get("namespace"))


#go_dag.nodes['GO:0000016']

f = open("Assignment 3\go.obo", "r")
saveID = ""
lines = f.readlines()
for line in lines:
    if line.__contains__("id: "):
        saveID = x[4:14]
    print(saveID)


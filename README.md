# Pfen-nig
small neural network to Predict Functions with Embedded Networks

## rdfScripts
### rdfMaker.sh
Creates the interactions between stringDBs orthologous groups from the COG.links file

### cogit.py
Creates the functions between the orthologous groups and the gene ontology GO file

### mergBigFile.py
Merges the two files together ready for the next stage (Groovy)


## Groovy
### groovy.sh
Runs the groovy command on the supplied RDF file


## Deepwalk
### sbatch_Program.sh
Runs the deepwalk algorithm on the outWrapper.txt file from Groovy

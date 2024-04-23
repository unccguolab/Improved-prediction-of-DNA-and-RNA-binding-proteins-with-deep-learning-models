# Improved prediction of DNA and RNA binding proteins with deep learning models
In this project, we generated accurate and robust datasets including Non-NABPs, DSBs and SSBs, and developed deep learning methods including both hierarchical and multi-class approaches to predict the types of NABPs for any given proteins.

## File description
Files in datasets: \


## Predict using our pre-trained models

### Dependencies
Tensorflow \
Blast/2.11.0+ \
Uniprotref90 database

### Step 1: 
Prepare proteins that need to be predicted in .fasta format
### Step 2: 
Run Psi-blast to get the .pssm file for each protein \
fl=myprotein.fa (Note: The file name must end with .fa) \
uniprot=path/to/Uniprotref90 database \
psiblast -query $fl -db $uniprot -num_iterations=3 -evalue=0.001 -out_ascii_pssm=$fl.pssm
### Step 3: 
Use our pre-trained model to predict \
pssm=path/to/pssm/files \
models=model/you/used/ (Note: Our pretrained models are saved in the /models directory.) \
python run_model.py $pssm $models
### Step 4: 
Output: \
The prediction results are summarized in the file "prediction.txt".


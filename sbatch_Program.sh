#!/bin/bash
#SBATCH -N 1
#SBATCH --partition=batch
#SBATCH -J Deepwalk
#SBATCH -o Deepwalk.%J.out
#SBATCH -e Deepwalk.%J.err
#SBATCH --mail-user=robert.radley@kaust.edu.sa
#SBATCH --mail-type=ALL
#SBATCH --time=14-00:00:00
#SBATCH --mem=100G
#SBATCH --gres=gpu:4
#SBATCH --constraint=[gpu]

#run the application:
#groovy.sh 
deepwalk --workers 64 --representation-size 256 --format edgelist --input outWrapper.txt  --output out_DEEPWALK.txt --window-size 5 --number-walks 500 --walk-length 40

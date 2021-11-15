#!/bin/bash
cd /home/

# download bert from GitHub reppo usign terminal
git clone https://github.com/google-research/bert.git

# download bert_base_cased
wget -c "https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip"

# unzip the file
unzip ./cased_L-12_H-768_A-12.zip -d ./

mkdir ./bert/data
mkdir ./bert/bert_output
echo "finished downloading files for bert"

# fine-tune bert
python3 /home/amazonebert.py
echo "finished extrecting tools"

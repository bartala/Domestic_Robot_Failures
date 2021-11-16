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

# data preperation for fine-tuning bert
python3 /home/1_amazonebert.py
echo "finished extrecting tools"

# fine tune the BERT_base_cased model
!python3 ./bert/run_classifier.py \
    --task_name=cola \
    --do_train=true \
    --do_eval=true \
    --do_predict=true \
    --do_lower_case=False \
    --data_dir=./bert/data \
    --vocab_file=./cased_L-12_H-768_A-12/vocab.txt \
    --bert_config_file=./cased_L-12_H-768_A-12/bert_config.json \
    --init_checkpoint=./cased_L-12_H-768_A-12/bert_model.ckpt \
    --max_seq_length=128 \
    --learning_rate=3e-5 \
    --train_batch_size=32 \
    --num_train_epochs=4.0 \
    --output_dir=./bert_output/
    
 python3 /home/2_amazonebert_results.py

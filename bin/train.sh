#!/usr/bin/env bash

PROBLEM=transformer_t2t
MODEL=transformer
HPARAMS=hparam_transformer_t2t

cd ..
BASEDIR=$(pwd)

EX_HOME=$(cat config.json | jq .EX_HOME)
EX_HOME=${EX_HOME:1:-1}

DATA_DIR=${EX_HOME}/tmp_data
TMP_DIR=${EX_HOME}/tmp_model

GPUs=$(cat config.json | jq .GPU)
BATCH=$(cat config.json | jq .BATCH)
EVAL_STEP=$(cat config.json | jq .EVAL)
TRAIN_STEP=$(cat config.json | jq .TRAIN)


mkdir -p  ${TMP_DIR}

python train.py \
    --data_dir=${DATA_DIR} \
    --output_dir=${TMP_DIR} \
    --problem=${PROBLEM} \
    --hparams_set=${HPARAMS} \
    --hparams="batch_size=${BATCH}" \
    --model=${MODEL} \
    --eval_steps=${EVAL_STEP} \
    --train_steps=${TRAIN_STEP} \
    --worker_gpu=${GPUs}

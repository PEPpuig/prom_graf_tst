source ~/venv/bin/activate



#!/bin/bash

# PROFILING: Activa PyTorch Profiler en vLLM workers
export VLLM_TORCH_PROFILER_DIR=/tmp/vllm_traces_py
export TORCH_LOGS="+dynamo"

# PROFILING: Nsight Systems para full trace (instala: sudo apt install nsight-systems)
nsys profile \
  --trace=cuda,nvtx,osrt \
  --stats=true \
  --force-overwrite=true \
  --output=/tmp/vllm_parallel_profile \
  --export=json \
  bash -c "


python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &
python3 model_init.py &


wait
"
echo echo "- Nsight JSON: /tmp/vllm_parallel_profile.json (Perfetto UI)"
echo "- PyTorch traces: /vllm_traces_py/*.json.gz (descomprime con gunzip)"

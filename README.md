# Transcribing amd Summarising AI Agent

### STEP 1 - Create a conda environment after creating the hithub repository
```bash
conda create -n venv python=3.9
```
```bash
conda activate venv
```
### STEP 2 - Install required packages
```bash
conda install -c conda-forge ffmpeg
```
```bash
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
```bash
pip install git+https://github.com/openai/whisper.git
```
```bash
pip install transformers
```
```bash
pip install moviepy
```
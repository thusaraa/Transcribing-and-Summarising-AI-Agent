conda create -n venv python=3.9

conda activate venv

conda install -c conda-forge ffmpeg

conda install pytorch torchvision torchaudio cpuonly -c pytorch

pip install git+https://github.com/openai/whisper.git


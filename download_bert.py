# download BERT multi-lingual
from utils import maybe_download
import os

BERT_MODELS_DIR = 'bert_models'
BERT_BASE_DIR = 'bert_models/multilingual_L-12_H-768_A-12'


BERT_MODEL_URL = 'https://storage.googleapis.com/bert_models/2018_11_03/'
BERT_BASE_MULTI_FILE = 'multilingual_L-12_H-768_A-12.zip'

if __name__ == '__main__':
    maybe_download(BERT_MODEL_URL, BERT_BASE_MULTI_FILE, BERT_MODELS_DIR)
    os.system("7z x bert_models/multilingual_L-12_H-768_A-12.zip -obert_models")

```shell
export FAIRSEQ_ROOT=/storage/LabJob/Projects/ToolkitLearn/fairseq_new/fairseq
export FAIRSEQ_PATH=/storage/LabJob/Projects/ToolkitLearn/fairseq_new/fairseq/fairseq/__init__.py
```

```python
import joblib
with open('model200.pkl', 'rb') as f:
    model200 = joblib.load(f)
model200.cluster_centers_.shape  # (200, 768)
```

## TO make sure

- [ ] 1. The layer of the Kmeans


----------------

# Note

```
.bin  cpc_km_200
.bin  hubert_km_100
.bin  hubert_km_200
.bin  hubert_km_50
.bin  logmel_km_100
.bin  logmel_km_200
.bin  logmel_km_50
.bin  mel_km_200
.bin  w2v2_km_100
.bin  w2v2_km_200
.bin  w2v2_km_50
.pt   cpc_big_ll6kh_top_ctc
.pt   hubert_base_ls960
.pt   wav2vec_vox_new
.py   prepare_model_sources
.sh   runner
.sh   todo
.tsv  train_clean_100
.txt  train_clean_100.hubert.km200
.yaml model_source_url
```

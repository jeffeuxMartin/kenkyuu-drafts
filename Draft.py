#!python

import pickle
import joblib
import numpy as np

# === load model
with open('km200.bin', 'rb') as f200: 
    # 200 cluster model
    model200 = joblib.load(f200)

assert model200.n_clusters == 200
assert model200.n_features_in_ == 768

model200.get_params()
model200.cluster_centers_
model200.cluster_centers_.shape

# === check features
x = np.load(
    '/storage/LabJob/Projects/Data'
    '/LibriSpeech_HubertFeats/LibriSpeech'
    '/dev-clean/84/121123'
    '/84-121123-0000.flac.hubert.npy'
)

x.shape  # (104, 768)

z = np.load(
    '/storage/LabJob/Projects/Data'
    '/LibriSpeech_FusedSpeechAlignment'
    '/dev-clean/84/121123'
    '/84-121123-0000.npz'
)

z.items()
z.fid
z.files  # ['feat', 'algn']

z['feat'].shape  # (104, 768)

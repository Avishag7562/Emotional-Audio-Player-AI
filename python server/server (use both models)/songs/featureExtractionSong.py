import os
import pandas as pd
import numpy as np
import librosa


def extract_feature_song(path):
    feature_set = pd.DataFrame()  # Feature Matrix

    id = 1
    tempo_vector = pd.Series()
    total_beats = pd.Series()
    average_beats = pd.Series()
    chroma_stft_mean = pd.Series()
    chroma_stft_std = pd.Series()
    chroma_stft_var = pd.Series()
    chroma_cq_mean = pd.Series()
    chroma_cq_std = pd.Series()
    chroma_cq_var = pd.Series()
    chroma_cens_mean = pd.Series()
    chroma_cens_std = pd.Series()
    chroma_cens_var = pd.Series()
    mel_mean = pd.Series()
    mel_std = pd.Series()
    mel_var = pd.Series()
    mfcc_mean = pd.Series()
    mfcc_std = pd.Series()
    mfcc_var = pd.Series()
    mfcc_delta_mean = pd.Series()
    mfcc_delta_std = pd.Series()
    mfcc_delta_var = pd.Series()
    rmse_mean = pd.Series()
    rmse_std = pd.Series()
    rmse_var = pd.Series()
    cent_mean = pd.Series()
    cent_std = pd.Series()
    cent_var = pd.Series()
    spec_bw_mean = pd.Series()
    spec_bw_std = pd.Series()
    spec_bw_var = pd.Series()
    contrast_mean = pd.Series()
    contrast_std = pd.Series()
    contrast_var = pd.Series()
    rolloff_mean = pd.Series()
    rolloff_std = pd.Series()
    rolloff_var = pd.Series()
    poly_mean = pd.Series()
    poly_std = pd.Series()
    poly_var = pd.Series()
    tonnetz_mean = pd.Series()
    tonnetz_std = pd.Series()
    tonnetz_var = pd.Series()
    zcr_mean = pd.Series()
    zcr_std = pd.Series()
    zcr_var = pd.Series()
    harm_mean = pd.Series()
    harm_std = pd.Series()
    harm_var = pd.Series()
    perc_mean = pd.Series()
    perc_std = pd.Series()
    perc_var = pd.Series()
    frame_mean = pd.Series()
    frame_std = pd.Series()
    frame_var = pd.Series()

    songname = path
    # Load an audio file as a floating point time series.
    y, sr = librosa.load(songname, duration=60)
    S = np.abs(librosa.stft(y))

    # Extracting Features
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr)
    chroma_cens = librosa.feature.chroma_cens(y=y, sr=sr)
    melspectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    rmse = librosa.feature.rms(y=y)[0]
    cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    contrast = librosa.feature.spectral_contrast(S=S, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    poly_features = librosa.feature.poly_features(S=S, sr=sr)
    tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    harmonic = librosa.effects.harmonic(y)
    percussive = librosa.effects.percussive(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    mfcc_delta = librosa.feature.delta(mfcc)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    frames_to_time = librosa.frames_to_time(onset_frames[:20], sr=sr)

    # Transforming Features
    tempo_vector.at[id] = tempo  # tempo
    total_beats.at[id] = sum(beats)  # beats
    average_beats.at[id] = np.average(beats)
    chroma_stft_mean.at[id] = np.mean(chroma_stft)  # chroma stft
    chroma_stft_std.at[id] = np.std(chroma_stft)
    chroma_stft_var.at[id] = np.var(chroma_stft)
    chroma_cq_mean.at[id] = np.mean(chroma_cq)  # chroma cq
    chroma_cq_std.at[id] = np.std(chroma_cq)
    chroma_cq_var.at[id] = np.var(chroma_cq)
    chroma_cens_mean.at[id] = np.mean(chroma_cens)  # chroma cens
    chroma_cens_std.at[id] = np.std(chroma_cens)
    chroma_cens_var.at[id] = np.var(chroma_cens)
    mel_mean.at[id] = np.mean(melspectrogram)  # melspectrogram
    mel_std.at[id] = np.std(melspectrogram)
    mel_var.at[id] = np.var(melspectrogram)
    mfcc_mean.at[id] = np.mean(mfcc)  # mfcc
    mfcc_std.at[id] = np.std(mfcc)
    mfcc_var.at[id] = np.var(mfcc)
    mfcc_delta_mean.at[id] = np.mean(mfcc_delta)  # mfcc delta
    mfcc_delta_std.at[id] = np.std(mfcc_delta)
    mfcc_delta_var.at[id] = np.var(mfcc_delta)
    rmse_mean.at[id] = np.mean(rmse)  # rmse
    rmse_std.at[id] = np.std(rmse)
    rmse_var.at[id] = np.var(rmse)
    cent_mean.at[id] = np.mean(cent)  # cent
    cent_std.at[id] = np.std(cent)
    cent_var.at[id] = np.var(cent)
    spec_bw_mean.at[id] = np.mean(spec_bw)  # spectral bandwidth
    spec_bw_std.at[id] = np.std(spec_bw)
    spec_bw_var.at[id] = np.var(spec_bw)
    contrast_mean.at[id] = np.mean(contrast)  # contrast
    contrast_std.at[id] = np.std(contrast)
    contrast_var.at[id] = np.var(contrast)
    rolloff_mean.at[id] = np.mean(rolloff)  # rolloff
    rolloff_std.at[id] = np.std(rolloff)
    rolloff_var.at[id] = np.var(rolloff)
    poly_mean.at[id] = np.mean(poly_features)  # poly features
    poly_std.at[id] = np.std(poly_features)
    poly_var.at[id] = np.var(poly_features)
    tonnetz_mean.at[id] = np.mean(tonnetz)  # tonnetz
    tonnetz_std.at[id] = np.std(tonnetz)
    tonnetz_var.at[id] = np.var(tonnetz)
    zcr_mean.at[id] = np.mean(zcr)  # zero crossing rate
    zcr_std.at[id] = np.std(zcr)
    zcr_var.at[id] = np.var(zcr)
    harm_mean.at[id] = np.mean(harmonic)  # harmonic
    harm_std.at[id] = np.std(harmonic)
    harm_var.at[id] = np.var(harmonic)
    perc_mean.at[id] = np.mean(percussive)  # percussive
    perc_std.at[id] = np.std(percussive)
    perc_var.at[id] = np.var(percussive)
    frame_mean.at[id] = np.mean(frames_to_time)  # frames
    frame_std.at[id] = np.std(frames_to_time)
    frame_var.at[id] = np.var(frames_to_time)

    # Concatenating Features into one csv and json format
    feature_set['tempo'] = tempo_vector  # tempo
    feature_set['total_beats'] = total_beats  # beats
    feature_set['average_beats'] = average_beats
    feature_set['chroma_stft_mean'] = chroma_stft_mean  # chroma stft
    feature_set['chroma_stft_std'] = chroma_stft_std
    feature_set['chroma_stft_var'] = chroma_stft_var
    feature_set['chroma_cq_mean'] = chroma_cq_mean  # chroma cq
    feature_set['chroma_cq_std'] = chroma_cq_std
    feature_set['chroma_cq_var'] = chroma_cq_var
    feature_set['chroma_cens_mean'] = chroma_cens_mean  # chroma cens
    feature_set['chroma_cens_std'] = chroma_cens_std
    feature_set['chroma_cens_var'] = chroma_cens_var
    feature_set['melspectrogram_mean'] = mel_mean  # melspectrogram
    feature_set['melspectrogram_std'] = mel_std
    feature_set['melspectrogram_var'] = mel_var
    feature_set['mfcc_mean'] = mfcc_mean  # mfcc
    feature_set['mfcc_std'] = mfcc_std
    feature_set['mfcc_var'] = mfcc_var
    feature_set['mfcc_delta_mean'] = mfcc_delta_mean  # mfcc delta
    feature_set['mfcc_delta_std'] = mfcc_delta_std
    feature_set['mfcc_delta_var'] = mfcc_delta_var
    feature_set['rmse_mean'] = rmse_mean  # rmse
    feature_set['rmse_std'] = rmse_std
    feature_set['rmse_var'] = rmse_var
    feature_set['cent_mean'] = cent_mean  # cent
    feature_set['cent_std'] = cent_std
    feature_set['cent_var'] = cent_var
    feature_set['spec_bw_mean'] = spec_bw_mean  # spectral bandwidth
    feature_set['spec_bw_std'] = spec_bw_std
    feature_set['spec_bw_var'] = spec_bw_var
    feature_set['contrast_mean'] = contrast_mean  # contrast
    feature_set['contrast_std'] = contrast_std
    feature_set['contrast_var'] = contrast_var
    feature_set['rolloff_mean'] = rolloff_mean  # rolloff
    feature_set['rolloff_std'] = rolloff_std
    feature_set['rolloff_var'] = rolloff_var
    feature_set['poly_mean'] = poly_mean  # poly features
    feature_set['poly_std'] = poly_std
    feature_set['poly_var'] = poly_var
    feature_set['tonnetz_mean'] = tonnetz_mean  # tonnetz
    feature_set['tonnetz_std'] = tonnetz_std
    feature_set['tonnetz_var'] = tonnetz_var
    feature_set['zcr_mean'] = zcr_mean  # zero crossing rate
    feature_set['zcr_std'] = zcr_std
    feature_set['zcr_var'] = zcr_var
    feature_set['harm_mean'] = harm_mean  # harmonic
    feature_set['harm_std'] = harm_std
    feature_set['harm_var'] = harm_var
    feature_set['perc_mean'] = perc_mean  # percussive
    feature_set['perc_std'] = perc_std
    feature_set['perc_var'] = perc_var
    feature_set['frame_mean'] = frame_mean  # frames
    feature_set['frame_std'] = frame_std
    feature_set['frame_var'] = frame_var
    return feature_set



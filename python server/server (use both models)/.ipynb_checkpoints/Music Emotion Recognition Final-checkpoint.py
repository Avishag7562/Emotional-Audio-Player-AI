import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
from PIL import ImageTk, Image
import librosa

df = pd.read_csv(r"C:\Users\Avishag\OneDrive\songs_data.csv")
df.head()
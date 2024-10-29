import numpy as np
import matplotlib.pyplot as plt

# Parameters
f = 200  
fs = 8000  # Sampling rate of 8kHz
duration = 0.5  
fs_new = 1000 #new Sampling rate of 1kHz
L = 8  # Number of quantization levels

t = np.arange(0, duration, 1/fs)
signal = np.sin(2 * np.pi * f * t)

# Downsample the signal to 1kHz
t_new = int(fs / fs_new)
signal_downsampled = signal[::t_new]
t_downsampled = t[::t_new]

# Quantization process (for L=8 levels)
min_val = np.min(signal_downsampled)
max_val = np.max(signal_downsampled)
quantization_step = (max_val - min_val) / (L - 1)
quantized_signal = np.round((signal_downsampled - min_val) / quantization_step) * quantization_step + min_val

# Plot the original and quantized signals
plt.figure(figsize=(12, 6))

# Original signal plot
plt.subplot(2, 1, 1)
plt.plot(t_downsampled, signal_downsampled, label='Original Downsampled Signal')
plt.title('Original Downsampled Signal (1kHz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Quantized signal plot
plt.subplot(2, 1, 2)
plt.plot(t_downsampled, quantized_signal, label='Quantized Signal', color='r')
plt.title(f'Quantized Signal with {L} Levels')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
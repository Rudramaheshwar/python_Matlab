
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample
frequency=200
duration=0.5
sampling_rate=8000
t=np.arange(0,duration,1/sampling_rate)
sine_wave=np.sin(2*np.pi*frequency*t)
new_sampling_rate=1000

new_samples=int(duration*new_sampling_rate)
sine_wave_resampled=resample(sine_wave,new_samples)
t_new=np.arange(0,duration,1/new_sampling_rate)
sine_wave_normalized = (sine_wave_resampled - np.min(sine_wave_resampled)) / (np.max(sine_wave_resampled) - np.min(sine_wave_resampled)) * 15
sine_wave_quantized = np.round(sine_wave_normalized).astype(int)

# Convert the quantized values to 4-bit binary representation
bit_stream = ''.join([f'{value:04b}' for value in sine_wave_quantized])

# Plot the original and resampled sine wave
plt.figure(figsize=(10, 4))
plt.plot(t_new, sine_wave_resampled, label='Resampled (1 kHz)')
plt.step(t_new, sine_wave_quantized / 15, label='Quantized (4-bit)', where='mid')
plt.title('Sine Wave - 200 Hz (Resampled and Quantized)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

# Print the bit stream
print(f"4-bit Quantized Bit Stream: {bit_stream}")

import rasterio
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# File paths (Windows)
# ===============================
red_band_path = r"C:\Users\AMSO\Desktop\B04.tif"
nir_band_path = r"C:\Users\AMSO\Desktop\B08.tif"

# ===============================
# Read Red band
# ===============================
with rasterio.open(red_band_path) as red_src:
    red = red_src.read(1).astype("float32")
    profile = red_src.profile

# ===============================
# Read NIR band
# ===============================
with rasterio.open(nir_band_path) as nir_src:
    nir = nir_src.read(1).astype("float32")

# ===============================
# Calculate NDVI
# ===============================
ndvi = (nir - red) / (nir + red)
ndvi[np.isinf(ndvi)] = np.nan

# ===============================
# Plot NDVI
# ===============================
plt.figure(figsize=(8, 6))
plt.imshow(ndvi, cmap="RdYlGn")
plt.colorbar(label="NDVI")
plt.title("NDVI Map (Sentinel-2)")
plt.axis("off")
plt.show()

# ===============================
# Save NDVI raster
# ===============================
profile.update(dtype=rasterio.float32, count=1)

output_path = r"C:\Users\AMSO\Desktop\ndvi.tif"

with rasterio.open(output_path, "w", **profile) as dst:
    dst.write(ndvi.astype(rasterio.float32), 1)

print("NDVI calculation completed successfully.")
print(f"Output saved at: {output_path}")

plt.figure(figsize=(8, 5))
plt.hist(ndvi_valid, bins=50)
plt.xlabel("NDVI value")
plt.ylabel("Number of pixels")
plt.title("NDVI Histogram")
plt.show()



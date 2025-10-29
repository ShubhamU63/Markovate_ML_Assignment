#  Edge Detection Evaluation — Classical vs CNN-Based

This script compares **classical edge detection algorithms** (Sobel, Canny) with a **learned CNN-based edge detector** trained earlier, using both **visual and quantitative** evaluations.

##  Overview

### Goal
To measure how well a **trained CNN edge detector** reproduces edge structures compared to classical methods.

### Key Steps
1. Load and preprocess a test image.
2. Generate edge maps using:
   - **Sobel Operator**
   - **Canny Edge Detector**
   - **CNN Learned Edge Model**
3. Compare and visualize outputs.
4. Compute **quantitative metrics** (MSE, PSNR, SSIM).

---

## Components

### **1️⃣ Classical Edge Detection**
- **Sobel:** Uses image gradients in x and y directions to detect edges.  
- **Canny:** Multi-stage algorithm involving Gaussian smoothing, gradient computation, and hysteresis thresholding.

### **2️⃣ CNN Edge Detection**
- Loads the **trained CNN model** (`SimpleEdgeCNN`) from:

"edge_detection/outputs/cnn_edge_model.pth"

- Converts test image to tensor and predicts learned edges.

---

## 📊 Metrics Used

| Metric | Description |
|---------|--------------|
| **MSE (Mean Squared Error)** | Measures pixel-wise difference. Lower = better. |
| **PSNR (Peak Signal-to-Noise Ratio)** | Indicates reconstruction quality. Higher = better. |
| **SSIM (Structural Similarity Index)** | Measures structural similarity. Higher = better. |

> Reference edge map: **Sobel output**

---

## 📈 Output & Visualization

### Generated Files
| File | Description |
|------|--------------|
| `edge_detection/outputs/edge_comparison.png` | 4-way visual comparison of Original, Sobel, Canny, and CNN outputs |
| `edge_detection/outputs/edge_metrics.txt` | Tabulated performance metrics |

### Example Visualization
Original | Sobel | Canny | CNN Learned

Each panel shows the edge-detected version of the test image for comparison.

=== Edge Detection Metric Comparison ===
Method MSE PSNR SSIM
Canny 32.14 28.55 0.812
CNN 24.88 29.90 0.871

> *Note: CNN typically shows slightly higher SSIM and PSNR values, indicating smoother, more structured edges.*

---

## 🧰 Dependencies

```bash
pip install torch torchvision opencv-python scikit-image matplotlib pillow numpy

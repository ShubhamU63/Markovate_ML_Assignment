# ⚙️ Model Optimization & Inference Benchmark — Edge Detection CNN

This script demonstrates how to **optimize** and **benchmark** the trained `SimpleEdgeCNN` model by exporting it to **ONNX format** and measuring its **inference latency** on CPU.

---

## Overview

### Purpose
- **Export** the trained PyTorch model to the **ONNX** (Open Neural Network Exchange) format for deployment.
- **Benchmark** inference latency on a real test image.
- Provide a foundation for **further optimizations** (e.g., quantization, pruning).

---

## Workflow

1. **Load & Preprocess Image**
   - Reads a test image in grayscale.
   - Resizes to `(64 × 64)`.
   - Normalizes pixel values to `[0,1]`.
   - Converts to PyTorch tensor of shape `[1, 1, 64, 64]`.

2. **Load Trained CNN Model**
   - Loads `SimpleEdgeCNN` weights from:
     ```
     edge_detection/outputs/cnn_edge_model.pth
     ```
   - Runs in `eval()` mode on CPU (can be switched to GPU if available).

3. **Export to ONNX**
   - Model is exported using:
     ```python
     torch.onnx.export()
     ```
   - Output file:
     ```
     optimization_monitoring/model.onnx
     ```
   - The ONNX file can be deployed to frameworks like TensorRT, OpenVINO, or ONNX Runtime.

4. **Benchmark Latency**
   - Runs one forward pass on the test tensor.
   - Measures CPU inference time in milliseconds.


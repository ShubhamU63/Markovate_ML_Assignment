#  Model Optimization: Quantization

**Quantization** is a model optimization technique that reduces the precision of numbers used to represent model parameters (weights and activations).  
Instead of using 32-bit floating-point (`float32`), the model uses lower precision formats such as 16-bit or 8-bit integers (`int8`).

Example:  float32 → int8

**Benefits:**
-  Smaller model size → less memory usage  
-  Faster inference → lighter matrix multiplications  
- Lower power consumption → ideal for IoT or mobile  
- Cheaper deployment → fewer hardware resources needed  

Quantization maps continuous high-precision values to a discrete set of low-precision values using a **scale factor**.

**Methods :**
**Post-Training Quantization (PTQ)**
**Quantization-Aware Training (QAT)** 
**Dynamic Quantization**
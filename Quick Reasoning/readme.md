# Conceptual Q&A - CNNs, Loss Functions, GenAI Fine-Tuning, Drift, and Overfitting/Underfitting

## Convolutional Neural Networks (CNNs)

**Q1. Why do CNNs use convolutional layers instead of fully connected ones?**  
Convolutional layers preserve spatial relationships and reduce parameters by using shared weights (kernels), making them efficient for image data.

**Q2. What is the role of pooling layers?**  
Pooling layers reduce spatial dimensions, control overfitting, and make features more invariant to translation or small distortions.

**Q3. What is the difference between stride and padding?**  
- **Stride:** How much the filter moves across the image.  
- **Padding:** Adds borders to preserve output dimensions after convolution.

**Q4. Why do CNNs use ReLU activations?**  
ReLU introduces non-linearity while avoiding the vanishing gradient problem common with sigmoid/tanh.

**Q5. What happens if we use too many convolution layers?**  
The model may overfit, learn redundant features, or suffer from vanishing gradients if not designed with normalization or skip connections.


##  Loss Functions

**Q6. What does a loss function measure?**  
It quantifies the difference between predicted outputs and actual targets — guiding weight updates during training.

**Q7. Give examples of loss functions for classification and regression.**  
- **Classification:** Cross-Entropy Loss  
- **Regression:** Mean Squared Error (MSE)

**Q8. Why is cross-entropy preferred over MSE for classification?**  
Cross-entropy penalizes incorrect confident predictions more effectively, leading to faster and more stable convergence.

**Q9. What is the purpose of regularization terms in a loss function?**  
To penalize overly complex models (large weights), reducing overfitting.

## GenAI Fine-Tuning

**Q10. What does “fine-tuning” mean in GenAI models like GPT or Stable Diffusion?**  
Adjusting pre-trained model weights on domain-specific data to specialize the model without training from scratch.

**Q11. What is the difference between full fine-tuning and parameter-efficient fine-tuning (PEFT)?**  
- **Full fine-tuning:** Updates all parameters.  
- **PEFT (e.g., LoRA, adapters):** Modifies a small subset for efficiency and stability.

**Q12. What is “prompt-tuning”?**  
Learning a small set of tokens (“soft prompts”) that guide the pre-trained model without changing its main weights.

**Q13. Why is catastrophic forgetting a risk in fine-tuning?**  
The model may lose knowledge from the original pre-training data when heavily optimized on a small new dataset.

##  Model Drift

**Q14. What is model drift?**  
When model performance degrades over time due to changes in data distribution or relationships (concept drift).

**Q15. What are the two main types of drift?**  
- **Data drift:** Input distribution changes (e.g., new feature values).  
- **Concept drift:** Relationship between input and target changes.

**Q16. How can we detect model drift?**  
By monitoring metrics, input distributions, or using statistical tests (e.g., KS test, PSI).

**Q17. How do we handle drift?**  
Re-train or fine-tune the model periodically using updated data and track performance in production.

## Overfitting & Underfitting

**Q18. What is overfitting?**  
The model learns noise and performs well on training data but poorly on unseen data.

**Q19. What is underfitting?**  
The model is too simple to capture underlying patterns, performing poorly on both training and test data.

**Q20. How to reduce overfitting?**  
Use regularization (L1/L2), dropout, early stopping, data augmentation, or more data.

**Q21. How to fix underfitting?**  
Increase model complexity, train longer, or reduce regularization.


###  Summary Table

| Concept | Key Risk | Fix |
|----------|-----------|-----|
| Overfitting | Too complex → memorizes noise | Regularization, dropout, more data |
| Underfitting | Too simple → misses patterns | Add layers, train longer, reduce regularization |
| Data Drift | Input stats shift | Monitor inputs, retrain |
| Concept Drift | Target meaning changes | Update model logic, retrain |

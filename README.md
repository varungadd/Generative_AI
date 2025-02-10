# Generative AI Tutorials

This repository contains the implementations and results of various tutorials focused on Generative AI techniques. The tutorials cover foundational and advanced concepts such as Generative Adversarial Networks (GANs), Autoencoders (AEs), Variational Autoencoders (VAEs), and regularization techniques to enhance model performance.

## Table of Contents
1. [Tutorial 1: Generative Adversarial Networks (GANs)](#tutorial-1-generative-adversarial-networks-gans)
2. [Tutorial 2: Autoencoder and Variational Autoencoder (VAE)](#tutorial-2-autoencoder-and-variational-autoencoder-vae)
3. [Tutorial 3: Exploring Latent Space and Interpolation](#tutorial-3-exploring-latent-space-and-interpolation)
4. [Tutorial 4: VAE on Fashion MNIST Dataset](#tutorial-4-vae-on-fashion-mnist-dataset)
5. [Tutorial 5: Apply Regularization Techniques to Improve VAE](#tutorial-5-apply-regularization-techniques-to-improve-vae)

---

## Tutorial 1: Generative Adversarial Networks (GANs)
**Objective:** Train a GAN to generate realistic images from the CIFAR-10 dataset.  
**Key Features:**
- Implementation of Generator and Discriminator networks.
- Training using adversarial loss.
- Visualizing generated images at different epochs.

---

## Tutorial 2: Autoencoder and Variational Autoencoder (VAE)
**Objective:** Understand and compare the functionality of AE and VAE on the CIFAR-10 dataset.  
**Key Features:**
- Reconstruction of images using AE and VAE.
- Introduction to KL divergence in VAE.
- Training loss and reconstruction quality comparison.

---

## Tutorial 3: Exploring Latent Space and Interpolation
**Objective:** Explore the latent space of VAE to understand its generative capabilities.  
**Key Features:**
- Visualizing the latent space using t-SNE.
- Generating new images through interpolation in latent space.
- Understanding smoothness and clustering in latent representations.

---

## Tutorial 4: VAE on Fashion MNIST Dataset
**Objective:** Train a VAE on grayscale images from the Fashion MNIST dataset.  
**Key Features:**
- Application of regularization techniques (dropout, batch normalization).
- Visualization of generated images from latent space.
- Analysis of reconstruction quality over training epochs.

---

## Tutorial 5: Apply Regularization Techniques to Improve VAE
**Objective:** Enhance the performance of VAE using various regularization techniques and compare performance with and without regularization.  
**Key Features:**
- Implementation of L1/L2 regularization, dropout, batch normalization, and Beta-VAE.
- Data augmentation for better generalization.
- Comprehensive evaluation: reconstruction loss, training loss curves, and image quality.
- Comparison of AE, VAE (with and without regularization), and Beta-VAE.

---

## Results and Key Takeaways
- **GANs:** Showed gradual improvement in generated image quality over epochs.
- **AE vs. VAE:** VAE provided structured latent spaces, while AE excelled in pure reconstruction tasks.
- **Regularized VAE:** Regularization improved stability and reconstruction quality.
- **Beta-VAE:** Demonstrated better latent space disentanglement, at the expense of slightly reduced reconstruction fidelity.

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/varungadd/Generative_AI.git

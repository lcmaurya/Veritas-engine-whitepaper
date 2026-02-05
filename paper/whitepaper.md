# Veritas Engine
## Deterministic Detection of Organic vs Coordinated Engagement  
### (Metadata-Only, Reproducible, Hash-Verifiable)

**Author:** Lal Chandra Maurya  
**Repository:** https://github.com/lcmaurya/Veritas-engine-whitepaper  
**Version:** v1.0 (Draft)  
**Date:** 2026

---

## Abstract

Veritas Engine is a deterministic, metadata-only analysis framework designed to
## Citation

If you use this work in academic research, policy analysis, or platform safety
engineering, please cite:

Maurya, L. C. (2026). *Veritas Engine: Deterministic, Proof-Based Detection of
Coordinated Online Activity*. GitHub repository.
https://github.com/lcmaurya/Veritas-engine-whitepaper
distinguish **organic human engagement** from **coordinated or automated activity**
in online conversation threads.

The system operates exclusively on **timestamps and structural metadata**,
excluding content, user identities, or behavioral profiling.
All outputs are reproducible, hash-verifiable, and privacy-preserving.

---

## 1. Motivation

Current bot-detection systems often rely on:
- Content analysis
- Account profiling
- Machine-learning black boxes
- Probabilistic scores

These approaches introduce privacy risks, bias, and non-reproducibility.

Veritas Engine addresses this gap by answering a narrower but critical question:

> *Does the temporal structure of engagement resemble natural human behavior,
or does it exhibit coordination/automation signatures?*

---

## 2. Design Principles

Veritas Engine is built on five non-negotiable principles:

1. **Metadata-only**  
   Uses timestamps and reply ordering only.

2. **Deterministic**  
   Same input → same output (no randomness, no ML weights).

3. **Reproducible**  
   Any third party can re-run the analysis independently.

4. **Hash-anchored**  
   Sorted timestamps are SHA-256 hashed to create evidence anchors.

5. **Privacy-preserving**  
   No content, no usernames, no identities.

---

## 3. Input Specification

The engine accepts a single JSON object:

```json
{
  "thread_id": "STRING",
  "replies": [
    { "timestamp": "ISO-8601-Z" }
  ]
}

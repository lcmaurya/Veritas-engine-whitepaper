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
distinguish **organic human engagement** from **coordinated or automated activity**
in online conversation threads.

The system operates exclusively on **timestamps and structural metadata**,
excluding content, user identities, behavioral profiling, or predictive models.
All outputs are fully reproducible, hash-verifiable, and privacy-preserving.

Veritas Engine prioritizes explainability and evidentiary rigor, making it suitable
for academic research, platform trust-and-safety analysis, and policy or
regulatory investigations.

---

## 1. Motivation

Current bot-detection and abuse-detection systems often rely on:

- Content analysis  
- Account-level profiling  
- Machine-learning black boxes  
- Probabilistic or opaque scoring  

These approaches introduce privacy risks, bias, and limited reproducibility.

Veritas Engine addresses a narrower but critical question:

> *Does the temporal structure of engagement resemble natural human behavior,
or does it exhibit coordination or automation signatures?*

---

## 2. Design Principles

Veritas Engine is built on five non-negotiable principles:

1. **Metadata-only**  
   Uses timestamps and reply ordering only.

2. **Deterministic**  
   Same input always produces the same output.

3. **Reproducible**  
   Any third party can independently verify results.

4. **Hash-anchored**  
   Sorted timestamps are SHA-256 hashed to create an evidence anchor.

5. **Privacy-preserving**  
   No content, no usernames, no identity inference.

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
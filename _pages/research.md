---
layout: page
permalink: /research/
title: research
#description: Research areas of the Computer Systems Security Lab.
nav: true
nav_order: 2
---

Our research focuses on **security and privacy across the computer systems stack** — from microarchitecture and operating systems to the cloud. We combine offensive security research (discovering new attacks) with defensive techniques (building systems resilient to those attacks).

---

## Microarchitectural Side-Channel Attacks

Modern CPUs and GPUs leak information through timing, caches, branch predictors, prefetchers, and thermal behavior. We develop new side-channel and transient-execution attacks that break isolation in commodity hardware and propose architectural or software-level mitigations.

*Representative works:*
- *SysBumps: Exploiting Speculative Execution in System Calls for Breaking KASLR in macOS for Apple Silicon* — **ACM CCS 2024** / Black Hat Europe 2024
- *DevIOus: Device-Driven Side-Channel Attacks on the IOMMU* — **IEEE S&P 2023**
- *Unveiling Hardware-based Data Prefetcher, a Hidden Source of Information Leakage* — **ACM CCS 2018**
- *T-Time: A Fine-grained Timing-based Controlled-Channel Attack against Intel TDX* — **ESORICS 2025**

## System Security

We look for security weaknesses in operating system kernels, system-call filtering, trusted execution environments (Intel SGX/TDX), and device drivers, and we design principled defenses.

*Representative works:*
- *MimicCall: Bypassing System Call Filters via Kernel Function Redundancy* — **ACSAC 2025**
- *SysDiver: Lightweight and Fast Static Analysis for Windows Kernel Drivers* — **ASIACCS 2026**
- *Vulnerable Intel GPU Context: Prohibit Complete Context Restore by Modifying Kernel Driver* — **ASIACCS 2025**

## Cloud and Container Security

As workloads move to shared infrastructure, we study how memory deduplication, co-location, and container scheduling can be abused, and how to strengthen isolation in cloud and Kubernetes environments.

*Representative works:*
- *PodBeater: Exploiting Multi-Value Affinity for Efficient Co-Location Attacks in Kubernetes* — **WISA 2025**
- *S-ZAC: Hardening Access Control of Service Mesh using Intel SGX for Zero Trust in Cloud* — **Electronics 2024**
- *Exploiting Memory Page Management in KSM for Remote Memory Deduplication Attack* — **WISA 2023**
- *Secure Data Deduplication with Dynamic Ownership Management in Cloud Storage* — **IEEE TSC 2020**

## Network Security

We analyze protocol-level vulnerabilities in TLS, HTTP, and IPsec, and study side-channel leakage in virtualized network functions.

*Representative works:*
- *PathFault: Automated Exploit Generator for Web Services via HTTP Message Parser Discrepancies* — **ICISC 2025**
- *Return of Version Downgrade Attack in the Era of TLS 1.3* — **ACM CoNEXT 2020**
- *Inferring Firewall Rules by Cache Side-channel Analysis in Network Function Virtualization* — **IEEE INFOCOM 2020**

## Binary Analysis and Fuzzing

Our group builds static and dynamic analyzers, fuzzers, and vulnerability-discovery tools for firmware, embedded systems, and kernel-space software.

*Representative works:*
- *Empirical Study on BMC Firmware Vulnerabilities: Root Causes and Architectural Insights* — **ICOIN 2026**
- *FuzzyBin: Enhanced Border Binary Identification by Leveraging Fuzzy Hashing Algorithms* — **IEEE Access 2025**
- *Fuzzing of Embedded Systems: A Survey* — **ACM Computing Surveys 2023**

---

Visit the [publications page]({{ '/publications/' | relative_url }}) for the full list of our research outputs.

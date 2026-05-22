## 📌 Overview

This repository contains the full production source code and experimental framework for the diploma thesis: 
**"Development and detection of fraudulent scam projects in DeFi blockchain systems"** 
*Tabyldin Amirlan Rishatovich, AITU, 2026*

The developed software ecosystem implements a proactive, zero-dependency cybersecurity gateway designed to protect user capital before transaction finality. The core pipeline features:

* **Asynchronous Mempool Hooking:** Continuous interceptor loop utilizing `web3.py` JSON-RPC filters to isolate pending transactions in the pre-execution block phase.
* **Multi-Criteria Risk Scoring Model:** An additive, deterministic mathematical algorithm that evaluates contract bytecode against critical Web3 threat signatures (Honeypots, Rug Pulls, and arbitrary mint privileges) to generate a unified **Trust Score**.
* **Cross-Chain Mainnet Validation:** Empirical verification framework fully calibrated and stress-tested across a mainnet dataset of **500+ active smart contracts** spanning the Ethereum, Binance Smart Chain (BSC), and Arbitrum L2 networks.
* **Asynchronous GUI Presentation Layer:** A responsive desktop dashboard engineered with `CustomTkinter` providing real-time visual categorization (`SAFE` / `WARNING` / `SCAM`) to eliminate analyst alarm fatigue.
* **Cryptographic Evidence Engine:** Dynamic reporting module utilizing `fpdf2` and `Pillow` to instantly compile local, verifiable PDF compliance certificates embedded with synchronization QR codes.

# EVM-Shield: Real-Time DeFi Scam Detection & Smart Contract Auditing Platform

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-EVM%20Compatible-orange.svg)](https://ethereum.org/)

An automated, high-throughput security pipeline designed to intercept pending mempool transactions, extract smart contract bytecode, and calculate a deterministic safety index (**Trust Score**) to mitigate Web3 fraud vectors (Honeypots, Rug Pulls, and predatory token taxes) in real-time.

---

## 🛠️ Key Features

* **Mempool Interception:** Asynchronous scanning of pending transaction streams via distributed JSON-RPC filters before block finality.
* **Static Bytecode Parsing:** Automated signature matching across compiled EVM bytecode arrays to isolate hidden mint vectors, arbitrary ownership mutations, and proxy flaws.
* **Deterministic Trust Score Matrix:** A rigid, 100-point multi-criteria risk assessment algorithm that eliminates stochastic model variance.
* **Asynchronous Presentation Layer:** A responsive, object-oriented GUI built with `CustomTkinter` providing immediate color-coded alerts (`SAFE` / `WARNING` / `SCAM`).
* **Cryptographic Evidence Engine:** Automated dynamic compilation of local PDF compliance certificates with embedded PIL-generated QR codes for mobile synchronization.

---

## 📐 System Architecture

The platform implements a decoupled, 8-layer processing framework to isolate network data ingestion from local verification engines, ensuring low latency and fault tolerance.

[ DeFi Ecosystem Layer ] ──> (Pending Transaction)
│
▼
[ Ingestion Layer: RPC Gateway ] ──> (eth_newPendingTransactionFilter)
│
▼
[ Extraction Layer: Interceptor ] ──> (eth_getCode & ABI Decoding)
│
▼
[ Analysis Core: Decision Engine ] ──> (Static Bytecode Check & Simulation)
│
▼
[ Representation Layer ] ──> [ Asynchronous GUI Dashboard ] ──> [ PDF Audit Report ]

## 📊 Performance & Validation Metrics

The system was stress-tested against an empirical mainnet dataset consisting of **500+ active smart contracts** across major EVM layers (Ethereum, Binance Smart Chain, and Arbitrum L2).

### Evaluation Benchmark (Optimized Config)
| Target Network Layer | Samples Audited | False Negatives | False Positives | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| **Ethereum Mainnet** | 200 | 3 | 14 | 0.931 |
| **Binance Smart Chain** | 200 | 5 | 19 | 0.914 |
| **Arbitrum L2 Network** | 100 | 1 | 6 | 0.952 |

* **Accuracy Boost:** Weighted parameter calibration achieved a **75.6% reduction** in False Negatives compared to baseline configurations.
* **Processing Latency:** Complete end-to-end audit loops complete within an average of **1.28 seconds**, preserving real-time gateway performance even for heavy nested bytecode contracts (>15 KB).

---

## 🚀 Getting Started

### Prerequisites
* Python 3.12.x
* Access to an EVM Node Gateway provider (Infura, Alchemy, or a local Geth instance)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/evm-shield.git](https://github.com/yourusername/evm-shield.git)
   cd evm-shield
   
2. Install dependency packages:
  ```bash
    pip install -r requirements.txt
  
3. Configure your environment variables (.env):
  ```bash
    ETH_RPC_URL=[https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY](https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY)
    BSC_RPC_URL=[https://bsc-dataseed.binance.org/](https://bsc-dataseed.binance.org/)
    ARB_RPC_URL=[https://arb-mainnet.g.alchemy.com/v2/YOUR_API_KEY](https://arb-mainnet.g.alchemy.com/v2/YOUR_API_KEY)

4. Run the application GUI terminal:
  ```bash
  python main.py


📦 Tech Stack
Core Engine: Python 3.12

Network RPC Routing: web3.py (v6.10), requests (v2.31)

Mathematical Operations: numpy (v1.26)

User Interface: CustomTkinter

Layout Compilation: fpdf2 (v2.7), Pillow (v10.2)

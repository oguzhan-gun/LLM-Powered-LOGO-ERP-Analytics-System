# LLM-Powered LOGO ERP Query and Analytics System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![LLM](https://img.shields.io/badge/LLM-Gemini%202.5-blue)
![RAG](https://img.shields.io/badge/RAG-Hybrid-green)
![SQL Server](https://img.shields.io/badge/Database-SQL%20Server-red)

An AI-powered assistant designed to enable natural language interaction with LOGO ERP systems, providing access to business data, analytics, and reporting workflows.

---

## Demo

### Complex Query Generation

**User Query**

> İşlem sayısı en yüksek ancak toplam ciroda ilk 3'e giremeyen müşteri kimdir?

<p align="center">
  <img src="assets/sql.gif" width="700">
</p>


---

### Analytics & Visualization

**User Query**

> En yüksek ciroyu oluşturan ürünleri karşılaştır ve görselleştir.

<p align="center">
  <img src="assets/chart_sql.gif" width="700">
</p>

---

## Overview

This project is an AI-powered query and analytics platform that enables users to interact with LOGO ERP systems using natural language.

By processing user queries, the system can perform analyses on LOGO ERP data, generate reports, and visualize results. It aims to simplify data access and decision-support processes without requiring technical expertise.


## Key Features

* Natural Language to SQL (NL2SQL)
* Intent and Subtype-Based Intelligent Query Routing
* Retrieval-Augmented Generation (RAG)
* Hybrid Retrieval (BM25 + Vector Embeddings)
* Multi-Agent LLM Architecture
* Dynamic Schema and Prompt Generation
* Dynamic Reporting and Analytics
* Automated Chart and Visualization Generation
* Context-Aware ERP Data Access

## Technologies Used

* Python
* Gemini 2.5 Flash-Lite
* Retrieval-Augmented Generation (RAG)
* BM25
* Vector Embeddings
* Natural Language to SQL (NL2SQL)
* SQL Server
* Multi-Agent Systems
* Data Visualization

## Results

* Evaluated on more than 500 ERP-related queries.
* Achieved over 95% satisfactory response accuracy across test scenarios.
* Typical response times range between 3–5 seconds.
* Supports complex business analytics scenarios through automated SQL generation, data analysis, and visualization capabilities.

## Demo Environment

> **Note:** This repository contains a demo version of the system, which uses SQLite for demonstration purposes. In the production environment, the system uses Microsoft SQL Server with T-SQL for ERP data querying and analytics.

## Disclaimer

This repository presents a high-level overview of the project. The full implementation, source code, proprietary business logic, datasets, and internal system components were developed within Harezmî and cannot be disclosed due to confidentiality agreements and intellectual property restrictions.

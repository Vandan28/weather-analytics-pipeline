# Real-Time Weather Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)
![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt)

An end-to-end ELT pipeline built to ingest live weather data from the Weatherstack API, load it into a PostgreSQL database, and prepare it for analytics. This project showcases a modern data stack using Docker for containerization and will be orchestrated with Apache Airflow.

---

## 🏛️ Project Architecture

1.  **Extract:** A Python script scheduled by Airflow fetches data from the Weatherstack API.
2.  **Load:** The raw JSON data is loaded into a `raw_data` schema in a PostgreSQL database.
3.  **Transform:** dbt models are triggered by Airflow to clean, transform, and model the raw data into analytics-ready tables.
4.  **Analyze:** An Apache Superset dashboard will be connected to the transformed data for visualization.

---

## 🛠️ Tech Stack & Tools

* **Containerization:** Docker, Docker Compose
* **Orchestration:** Apache Airflow
* **Data Warehouse:** PostgreSQL
* **Transformation:** dbt (Data Build Tool)
* **Data Ingestion:** Python (`requests`, `psycopg2`)
* **BI/Visualization:** Apache Superset
* **Development Environment:** Windows 11 with WSL (Ubuntu 24.04)

---

## Requirenments

* Docker Desktop
* WSL with Ubuntu installed
* Python 3.12

---

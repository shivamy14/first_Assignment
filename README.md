# 📸 Image Import System (Google Drive → MinIO)

## 🔗 Submission Links

### GitHub Repository URL
https://github.com/shivamy14/first_Assignment

###  Working Deployed Site URL (Backend Only)
https://first-assignment-1.onrender.com

---

## Project Overview
The **Image Import System** is a scalable backend application that imports images from a public Google Drive folder URL, stores them in an **S3-compatible object storage (MinIO)**, and saves image metadata in a **SQL database (PostgreSQL)**.

The deployed URL exposes **backend APIs only**.

## Objectives
- Import images from Google Drive public folders
- Store images in scalable object storage
- Persist image metadata in a relational database
- Provide REST APIs for importing and viewing images
- Ensure modular, clean, and maintainable code

## Architecture

## Client → Frontend → API Service → Google Drive → MinIO → PostgreSQL

## Technology Stack
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Object Storage:** MinIO
- **Frontend:** HTML, CSS, JavaScript
- **Containerization:** Docker & Docker Compose

## API Endpoints
- `POST /import/google-drive`
- `GET /images`
## ⚙️ Local Setup

```bash
git clone https://github.com/shivamy14/first_Assignment
cd first_Assignment
docker compose up --build



# CSCE 548 – Project 2-4 

## Overview
This project implements a layered architecture including a data layer, business layer, and service layer. A Flask-based microservice exposes CRUD operations which are tested using a console-based client application.

## Layers
- **Data Layer**: SQLite database with CRUD operations
- **Business Layer**: Exposes all data layer methods and applies basic validation
- **Service Layer**: Flask REST API invoking the business layer
- **Client**: Console-based tester invoking the service

## How to Run
1. Create and activate virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run service: `python service.py`
4. Run client in another terminal: `python client.py`

## Hosting
The service is hosted locally using Flask at:
http://127.0.0.1:5000

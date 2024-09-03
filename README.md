## architecture overview:
(![Screenshot from 2024-08-16 07-57-54](https://github.com/user-attachments/assets/02450048-dbd2-4f17-96a1-989e024c6cc4)

## whatsapp screenthot result: 
![WhatsApp Image 2024-08-25 at 8 37 46 PM](https://github.com/user-attachments/assets/45763a77-cb08-46a7-96be-21bcf5783fcc)


# Rasa Chatbot with Twilio WhatsApp Integration and PostgreSQL Database

This repository contains a Rasa chatbot integrated with Twilio's API for WhatsApp messaging and connected to a PostgreSQL database for data storage and retrieval. The project showcases how to build a conversational AI system that interacts with users over WhatsApp while leveraging a PostgreSQL database for persistent storage.

## Table of Contents

- [Introduction](#introduction)
- [Architecture](#architecture)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Chatbot](#running-the-chatbot)
- [Database Schema](#database-schema)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project demonstrates how to develop a Rasa chatbot that can communicate with users on WhatsApp using the Twilio API. The chatbot interacts with a PostgreSQL database to store and retrieve user data, making the conversation experience more personalized and efficient.

## Architecture

The architecture of the chatbot involves the following components:

1. **Rasa**: An open-source framework for building conversational AI.
2. **Twilio API**: Used to send and receive messages via WhatsApp.
3. **PostgreSQL**: A relational database system to store user data and conversation history.

The integration flow is as follows:
- Users send messages via WhatsApp.
- Twilio forwards these messages to the Rasa chatbot.
- Rasa processes the messages, interacts with the PostgreSQL database if needed, and sends a response back to Twilio.
- Twilio sends the response back to the user on WhatsApp.

## Features

- **WhatsApp Integration**: Communicate with the chatbot via WhatsApp using the Twilio API.
- **PostgreSQL Integration**: Store and retrieve user information, conversation history, and other data.
- **Custom Actions**: Perform complex operations within conversations using custom Rasa actions.
- **Scalable Architecture**: Easily deployable on cloud platforms.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7+
- PostgreSQL
- Rasa Open Source
- Twilio account with a verified WhatsApp number

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/rasa-twilio-whatsapp-postgres.git
   cd rasa-twilio-whatsapp-postgres
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the PostgreSQL database:**
   - Create a new PostgreSQL database.
   - Apply the provided schema (see [Database Schema](#database-schema)).

4. **Configure environment variables:**
   - Create a `.env` file with your Twilio API credentials and PostgreSQL connection details (see [Configuration](#configuration)).

## Configuration

The chatbot requires specific configurations for Twilio and PostgreSQL. Below is an example of the `.env` file:

```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+your_number

POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Update the `.env` file with your actual credentials.

## Running the Chatbot

1. **Start the PostgreSQL database:**
   ```bash
   sudo service postgresql start
   ```

2. **Run Rasa actions server:**
   ```bash
   rasa run actions
   ```

3. **Run the Rasa chatbot:**
   ```bash
   rasa run --enable-api
   ```

4. **Set up the Twilio webhook:**
   - In your Twilio console, set the webhook URL to point to your Rasa server. For example:
     ```
     https://your-domain.com/webhooks/twilio/webhook
     ```

## Database Schema

The database schema includes tables for storing user information, conversation history, and any additional data relevant to the chatbot's operations. Here is an example schema:

```sql
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE department (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    name VARCHAT(50)
    response TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Usage

Once the chatbot is running, users can interact with it through WhatsApp. The chatbot can respond to various queries, perform actions based on user input, and retrieve or store data in the PostgreSQL database.




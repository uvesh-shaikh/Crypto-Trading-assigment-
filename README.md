Markdown

# Binance Futures Trading Bot (Testnet)

This repository contains a Python-based trading bot developed as a technical assignment. The bot interacts with the **Binance Futures Testnet** to execute orders programmatically using the `python-binance` library.

It is designed with a focus on Object-Oriented Programming (OOP), robust error handling, and secure input validation.

## 📋 Project Overview

The application is a **Command-Line Interface (CLI)** tool that allows users to place **USDT-M Futures** orders. It abstracts the complexity of API interactions into a reusable class structure.

### Key Features
* **OOP Architecture:** Implements a `BasicBot` class to encapsulate API logic and state.
* **Order Management:** Supports both **Market** (instant) and **Limit** (price-triggered) orders.
* **Trade Directions:** Capable of executing **Long (Buy)** and **Short (Sell)** positions.
* **Safety Mechanisms:** * **Input Validation:** Prevents invalid data (e.g., negative numbers, empty strings) from reaching the API.
    * **Error Handling:** Catches and logs network errors and Binance API exceptions specifically.
* **Logging:** automatically records all API requests, responses, and errors to `trading_bot.log` for debugging and auditing.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Library:** [python-binance](https://python-binance.readthedocs.io/en/latest/)
* **API:** Binance Futures Testnet API
* **Format:** USDT-Margined Futures

## ⚙️ Prerequisites

Before running the bot, ensure you have:
1.  **Python 3.7+** installed.
2.  A **Binance Testnet Account**. You can generate API keys at the [Binance Futures Testnet](https://testnet.binancefuture.com/en/futures/BTCUSDT).

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```

2.  **Install dependencies:**
    ```bash
    pip install python-binance
    ```

## 💻 Usage

Run the main script from your terminal:

```bash
python trading_bot.py
Interactive Workflow
Authentication: The bot will prompt you for your Testnet API Key and API Secret.

Symbol: Enter the trading pair (e.g., BTCUSDT).

Side: Select BUY or SELL.

Type: Select MARKET or LIMIT.

Execution: The bot validates inputs, sends the request to Binance, and displays the execution result (Order ID and Status).

Example Output:

Plaintext

=== Binance Futures Testnet Trading Bot ===

Enter Symbol (e.g., BTCUSDT): BTCUSDT
Side (BUY/SELL): BUY
Type (MARKET/LIMIT): MARKET
Enter Quantity for BTCUSDT: 0.01

2024-12-14 17:30:00 - INFO - Attempting to place BUY MARKET order for 0.01 BTCUSDT...
2024-12-14 17:30:01 - INFO - Order placed successfully! Order ID: 123456789
📂 Project Structure
Plaintext

├── trading_bot.py     # Main application logic and BasicBot class
├── trading_bot.log    # Log file (generated automatically upon running)
└── README.md          # Project documentation
⚠️ Disclaimer
This bot is configured strictly for the Binance Testnet environment (https://testnet.binancefuture.com). Do not use real Binance API keys with this configuration. The author is not responsible for any financial losses incurred if the code is modified to trade on the mainnet.
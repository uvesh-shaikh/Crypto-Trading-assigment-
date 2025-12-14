import logging
import sys
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

# --- 1. Logging Setup ---
# Logs will be saved to 'trading_bot.log' and also shown in the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("trading_bot.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        """
        Initialize the Binance Client. 
        testnet=True automatically configures the client to use 
        https://testnet.binancefuture.com for futures calls.
        """
        try:
            self.client = Client(api_key, api_secret, testnet=testnet)
            logger.info("Binance Client initialized successfully (Testnet: %s)", testnet)
        except Exception as e:
            logger.error(f"Failed to initialize client: {e}")
            sys.exit(1)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        """
        Places an order on the Binance Futures (USDT-M) Testnet.
        Arguments:
            symbol (str): e.g., 'BTCUSDT'
            side (str): 'BUY' or 'SELL'
            order_type (str): 'MARKET' or 'LIMIT'
            quantity (float): Amount to trade
            price (float): Required for LIMIT orders, None for MARKET
        """
        try:
            logger.info(f"Attempting to place {side} {order_type} order for {quantity} {symbol}...")

            # Common parameters for both order types
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
            }

            # Add specific parameters for LIMIT orders
            if order_type == 'LIMIT':
                if price is None:
                    raise ValueError("Price must be provided for LIMIT orders.")
                params['price'] = price
                params['timeInForce'] = 'GTC'  # Good Till Cancelled

            # API Call to Binance Futures
            # Note: We use futures_create_order specifically for USDT-M Futures
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order placed successfully! Order ID: {response['orderId']}")
            logger.info(f"Order Details: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.status_code} - {e.message}")
            return None
        except BinanceRequestException as e:
            logger.error(f"Network/Request Error: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            return None

# --- 3. CLI Helper Functions (Input Validation) ---

def get_valid_string(prompt, valid_options=None):
    """Repeatedly asks for input until it matches valid options."""
    while True:
        user_input = input(prompt).upper().strip()
        if valid_options and user_input not in valid_options:
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")
            continue
        if not user_input:
            print("Input cannot be empty.")
            continue
        return user_input

def get_valid_float(prompt):
    """Repeatedly asks for input until a valid positive number is given."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a valid decimal.")

# --- 4. Main Execution Loop ---

def main():
    print("=== Binance Futures Testnet Trading Bot ===")
    
    # 1. Credentials (replace these with your actual Testnet keys if hardcoding)
    # Ideally, use environment variables, but for this assignment, we ask via CLI or hardcode.
    print("\nEnter your Binance Testnet Credentials:")
    api_key = input("API Key: ").strip()
    api_secret = input("API Secret: ").strip()

    if not api_key or not api_secret:
        print("Credentials missing. Exiting.")
        return

    # 2. Initialize Bot
    bot = BasicBot(api_key, api_secret, testnet=True)

    # 3. Interactive Loop
    while True:
        print("\n--- New Order ---")
        print("Type 'EXIT' at any prompt to quit.")
        
        try:
            # Get Symbol
            symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper().strip()
            if symbol == 'EXIT': break
            if not symbol: continue

            # Get Side
            side = get_valid_string("Side (BUY/SELL): ", ['BUY', 'SELL'])
            if side == 'EXIT': break

            # Get Type
            order_type = get_valid_string("Type (MARKET/LIMIT): ", ['MARKET', 'LIMIT'])
            if order_type == 'EXIT': break

            # Get Quantity
            quantity = get_valid_float(f"Enter Quantity for {symbol}: ")
            
            # Get Price (only if Limit)
            price = None
            if order_type == 'LIMIT':
                price = get_valid_float("Enter Limit Price: ")

            # Execute
            bot.place_order(symbol, side, order_type, quantity, price)

        except KeyboardInterrupt:
            print("\nBot stopped by user.")
            break

if __name__ == "__main__":
    main()

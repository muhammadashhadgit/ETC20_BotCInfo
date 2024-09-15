# Ethereum Contract Info Bot

This bot allows you to retrieve contract details from the Ethereum blockchain, such as the total supply of any ERC-20 token. It interacts with the Ethereum blockchain using Web3 and Etherscan APIs and can fetch specific token information based on user input.

## Features

- Fetch the total supply of any ERC-20 token on the Ethereum network.
- Works dynamically for any ERC-20 contract address.
- Integrates with the Telegram Bot API for user interaction.
- Uses the Infura API for connecting to the Ethereum network.
- Retrieves token decimals dynamically to correctly display the total supply.

## Prerequisites

Before running this bot, ensure you have the following installed and set up:

- Python 3.x
- `web3` Python library (`pip install web3`)
- `python-telegram-bot` library (`pip install python-telegram-bot`)
- An Infura project URL or Alchemy API URL
- An Etherscan API Key
- A Telegram bot token from BotFather

## Configuration

The bot uses a `config.py` file to manage sensitive information like the Telegram bot token and Ethereum API keys. Ensure your `config.py` file looks like this:

```python
# config.py

# Telegram bot token from BotFather
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'

# Etherscan API Key
ETHERSCAN_API_KEY = 'your_etherscan_api_key'

# Infura URL or Alchemy URL for Ethereum interaction
INFURA_URL = 'https://mainnet.infura.io/v3/your_infura_project_id'
```

Replace the placeholders with your actual API keys and tokens.

## Usage

1. Clone or download this repository.
2. Install the required Python dependencies using:
   ```bash
   pip install web3 python-telegram-bot
   ```
3. Update the `config.py` file with your API keys and Telegram bot token.
4. Run the bot using:
   ```bash
   python bot.py
   ```

### Telegram Commands

- `/start` - Starts the bot and provides a welcome message.
- `/contract` - Initiates the contract querying process. The bot will ask you to provide a contract address.
- `/supply` - Retrieves the total supply of the specified ERC-20 token.

### Example Interaction

```
User: /start
Bot: Hello! I can fetch Ethereum contract info for you. Use /contract to start.

User: /contract
Bot: Please enter the contract address you'd like to query.

User: 0xdAC17F958D2ee523a2206206994597C13D831ec7
Bot: What info would you like to retrieve? Send /supply to get total supply.

User: /supply
Bot: Total Supply: 4,000,000,000 USDT (example output)
```

## How It Works

The bot interacts with the Ethereum blockchain to fetch contract information using the following steps:

1. **Contract Query**: The user provides a valid ERC-20 contract address.
2. **Total Supply**: The bot queries the `totalSupply()` function of the contract.
3. **Token Decimals**: The bot queries the `decimals()` function to ensure the total supply is properly adjusted according to the token's precision.
4. **Display**: The bot sends the formatted total supply value back to the user.

### Error Handling

If the bot encounters any issues (e.g., invalid contract address or network issues), it will return an appropriate error message to the user, ensuring graceful failure.

## Contributing

Feel free to fork this repository, make improvements, and submit a pull request. Suggestions and feedback are welcome!

## License

This project is licensed under the MIT License.

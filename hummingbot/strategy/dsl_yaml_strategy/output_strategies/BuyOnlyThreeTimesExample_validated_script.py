"""
    A strategy to place only three buy orders.
    This Script strategy is generated with hbot-strategy-dsl.
    Author: Christos
"""

import logging
import time
from decimal import Decimal
from typing import List

from hummingbot.connector.utils import split_hb_trading_pair
from hummingbot.core.data_type.order_candidate import OrderCandidate
from hummingbot.core.event.events import OrderFilledEvent, OrderType, TradeType
from hummingbot.core.rate_oracle.rate_oracle import RateOracle
from hummingbot.strategy.script_strategy_base import ScriptStrategyBase


logger = logging.getLogger(__name__)


class BuyOnlyThreeTimesExampleStrategy(ScriptStrategyBase):
    """A strategy to place only three buy orders."""


order_amount_usd: float = 100  # Amount in USD for each order
orders_to_create: int = 3  # Total number of orders to create
base_asset: str = "ETH"  # Base asset symbol
quote_asset: str = "USDT"  # Quote asset symbol

    def __init__(self):
        """
            Initialize the strategy.

            This method sets up the initial state of the strategy upon instantiation.
            It initializes the markets that the strategy will interact with.

            The `super().__init__()` call ensures that the initialization logic of the
            base class (ScriptStrategyBase or any other relevant base class) is also executed,
            setting up essential components and configurations.
        """
        super().__init__()
        self.markets = {
            "kucoin_paper_trade": ['ETH-USDT'],
            "binance_paper_trade": ['BTC-USDT'],
            }
    
    def on_tick(self):
        """Main strategy operation executed periodically."""
        proposal = self._create_order_proposal()
        if proposal:
            self._execute_order_proposal(proposal)

    def _create_order_proposal(self) -> List[OrderCandidate]:
        """Generates order proposals based on strategy logic."""
        # Custom logic here...
        return []

    def _execute_order_proposal(self, proposal: List[OrderCandidate]):
        """Executes the given order proposal."""
        # Custom logic here...

    def did_fill_order(self, event: OrderFilledEvent):
        """Handles order filled events."""
        order_info = f"{event.trade_type.name} order of {event.amount} {event.trading_pair} at {event.price}"
        logger.info(f"Filled: {order_info}")
        self.notify_hb_app_with_timestamp(f"Filled: {order_info}")

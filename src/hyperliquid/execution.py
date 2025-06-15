"""Minimal wrapper around the hyperliquid-python-sdk for order execution."""
from hyperliquid.exchange import Exchange
from hyperliquid.utils.types import OrderType


class HyperliquidExecutor:
    def __init__(self, wallet):
        # `wallet` is an eth_account account used to sign orders.
        self.exchange = Exchange(wallet)

    def submit_limit_order(self, asset: str, is_buy: bool, size: float, price: float):
        """Submit a basic limit order."""
        return self.exchange.order(
            name=asset,
            is_buy=is_buy,
            sz=size,
            limit_px=price,
            order_type={"limit": {"tif": "Ioc"}},
        )

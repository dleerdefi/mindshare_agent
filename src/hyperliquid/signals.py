"""Simple signal abstraction for Hyperliquid trading ideas."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class TradeIdea:
    asset: str
    direction: str
    confidence: float
    ttl: int


class SignalService:
    """Stub signal ranking service."""

    def rank_event(self, event: dict) -> Optional[TradeIdea]:
        """Convert a raw event to a TradeIdea if confidence is high enough."""
        confidence = event.get("score", 0)
        if confidence < 0.5:
            return None
        return TradeIdea(
            asset=event["asset"],
            direction=event["direction"],
            confidence=confidence,
            ttl=60,
        )

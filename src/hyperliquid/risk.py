from dataclasses import dataclass

@dataclass
class RiskEnvelope:
    """Simple container for user risk limits."""
    max_leverage: float
    max_notional: float
    stop_loss_pct: float


class RiskEngine:
    """Return static risk envelopes for a given tier."""

    TIERS = {
        "conservative": RiskEnvelope(max_leverage=2, max_notional=1_000, stop_loss_pct=0.02),
        "balanced": RiskEnvelope(max_leverage=5, max_notional=5_000, stop_loss_pct=0.05),
        "degen": RiskEnvelope(max_leverage=10, max_notional=10_000, stop_loss_pct=0.1),
    }

    def __init__(self, tier: str = "balanced") -> None:
        self.tier = tier

    def get_risk_envelope(self) -> RiskEnvelope:
        """Return the configured risk envelope."""
        return self.TIERS.get(self.tier, self.TIERS["balanced"])

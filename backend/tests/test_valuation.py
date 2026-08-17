"""Valuation math, hand-computed from the fact store (same discipline as
test_metrics_engine.py: every expected value traced to a source document)."""
import pytest

from app.services.valuation import compute_valuation


def test_market_cap(facts_by_period):
    v = compute_valuation(facts_by_period)
    # 8.24 (close, 3 Jul 26) x 3,022,372 shares (listing PR p.3) = 24,904,345
    assert v["market_cap"] == pytest.approx(24904345, abs=1)


def test_enterprise_value_uses_hy26_net_cash(facts_by_period):
    v = compute_valuation(facts_by_period)
    # HY26 bank debt 102,475 - cash 985,155 = net cash -882,680
    assert v["net_debt"] == pytest.approx(-882680, abs=1)
    # EV = 24,904,345 - 882,680 = 24,021,665
    assert v["enterprise_value"] == pytest.approx(24021665, abs=1)


def test_ev_ltm_revenue_multiple(facts_by_period):
    v = compute_valuation(facts_by_period)
    # LTM revenue to Dec-25 = 1,121,568 - 456,848 + 475,449 = 1,140,169
    assert v["ltm_revenue"] == pytest.approx(1140169, abs=1)
    # 24,021,665 / 1,140,169 = 21.07x
    assert v["ev_ltm_revenue"] == pytest.approx(21.07, abs=0.01)


def test_price_vs_admission_ties_to_market_export(facts_by_period):
    v = compute_valuation(facts_by_period)
    # 8.24 / 6.869 - 1 = 19.96% — independently ties to the 52w change printed
    # in the performance export (validated by listing_price_change_ties)
    assert v["price_vs_admission"] == pytest.approx(0.1996, abs=1e-3)


def test_guidance_path_multiple_compression(facts_by_period):
    v = compute_valuation(facts_by_period)
    path = {r["year"]: r["implied_ev_revenue"] for r in v["guidance_path"]}
    # FY26E revenue 1,682,352 (1,121,568 x 1.5) -> 24,021,665 / 1,682,352 = 14.28x
    assert path["FY26"] == pytest.approx(14.28, abs=0.01)
    # FY30E revenue 8,516,907 -> 2.82x if the 50% CAGR commitment is delivered
    assert path["FY30"] == pytest.approx(2.82, abs=0.01)


def test_degrades_without_market_facts(facts_by_period):
    stripped = {k: v for k, v in facts_by_period.items() if k != "MKT"}
    v = compute_valuation(stripped)
    assert v["available"] is False

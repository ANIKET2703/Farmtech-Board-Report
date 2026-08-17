"""Every expected value below was hand-computed from the source documents
(docs/FINANCIAL_FACTS.md) — this is how we stand over the outputs."""
import pytest

from app.services import metrics_engine as m


def test_revenue_growth_fy25(facts_by_period):
    g = m.revenue_growth(facts_by_period["FY25"], facts_by_period["FY24"], "FY25")
    # (1,121,568 - 922,345) / 922,345 = 21.60%
    assert g.value == pytest.approx(0.21600, abs=1e-4)


def test_revenue_growth_hy26(facts_by_period):
    g = m.revenue_growth(facts_by_period["HY26"], facts_by_period["HY25"], "HY26")
    # (475,449 - 456,848) / 456,848 = 4.07%  (PR states "up 4.1%")
    assert g.value == pytest.approx(0.0407, abs=1e-3)


def test_gross_margin_fy25(facts_by_period):
    gm = m.gross_margin(facts_by_period["FY25"], "FY25")
    # 868,923 / 1,121,568 = 77.47% (InfoDoc states 77.5%)
    assert gm.value == pytest.approx(0.7748, abs=1e-3)


def test_gross_margin_hy26_matches_pr(facts_by_period):
    gm = m.gross_margin(facts_by_period["HY26"], "HY26")
    # PR states 81.7%
    assert gm.value == pytest.approx(0.817, abs=1e-3)


def test_ebitda_fy25(facts_by_period):
    e = m.ebitda(facts_by_period["FY25"], "FY25")
    # -849,151 + 27,311 = -821,840
    assert e.value == pytest.approx(-821840, abs=1)


def test_ebitda_margin_fy24(facts_by_period):
    em = m.ebitda_margin(facts_by_period["FY24"], "FY24")
    # (-1,515,177 + 26,012) / 922,345 = -161.45%
    assert em.value == pytest.approx(-1.6145, abs=1e-3)


def test_working_capital_hy26(facts_by_period):
    wc = m.working_capital(facts_by_period["HY26"], "HY26")
    # (252,120 + 985,155) - 518,721 = 718,554 (excl. contingent consideration)
    assert wc.value == pytest.approx(718554, abs=1)


def test_current_ratio_fy25(facts_by_period):
    cr = m.current_ratio(facts_by_period["FY25"], "FY25")
    # (164,824 + 187,781) / 326,754 = 1.079
    assert cr.value == pytest.approx(1.079, abs=1e-3)


def test_net_debt_fy25_is_net_cash_negative(facts_by_period):
    nd = m.net_debt(facts_by_period["FY25"], "FY25")
    # debt 112,098 + 13,550 = 125,648; cash 187,781 -> net cash 62,133
    assert nd.value == pytest.approx(-62133, abs=1)


def test_dscr_fy25_negative_with_caveat(facts_by_period):
    d = m.dscr(facts_by_period["FY25"], "FY25")
    # EBITDA -821,840 / (2,779 + 13,550) = -50.33x
    assert d.value == pytest.approx(-50.33, abs=0.05)
    assert d.caveat is not None


def test_roce_fy25(facts_by_period):
    r = m.roce(facts_by_period["FY25"], "FY25")
    # EBIT -849,151 / capital employed (65,376+164,824+187,781-326,754=91,227)
    assert r.value == pytest.approx(-849151 / 91227, abs=0.01)
    assert r.caveat is not None


def test_cash_runway_hy26(facts_by_period):
    f = facts_by_period["HY26"]
    runway = m.cash_runway(f["cash"], f["cf_operating"], f["cf_investing"], 6, "HY26")
    # burn (549,790+11,390)/6 = 93,530/mo; 985,155 / 93,530 = 10.53 months
    assert runway.value == pytest.approx(10.53, abs=0.05)


def test_fcf_bridge_fy25_ties_to_cashflow_statement(facts_by_period):
    bridge = m.ebitda_to_fcf_bridge(facts_by_period["FY25"], "FY25")
    # FCF = op CF -502,259 + capex -5,964 + disposal 1,340 = -506,883
    assert bridge["fcf"] == pytest.approx(-506883, abs=1)
    assert bridge["steps"][0]["value"] == pytest.approx(-821840, abs=1)


def test_ltm_revenue(facts_by_period):
    ltm = m._ltm_revenue(facts_by_period["FY25"], facts_by_period["HY25"],
                         facts_by_period["HY26"])
    # 1,121,568 - 456,848 + 475,449 = 1,140,169
    assert ltm == pytest.approx(1140169, abs=1)


def test_farmtech2030_progress():
    p = m.required_cagr_progress(1121568, 1140169, 0.5)
    # required at Dec-25 (0.5y): 1,121,568 * 1.5^0.5 = 1,373,635 -> 83.0%
    assert p.value == pytest.approx(0.830, abs=0.005)


def test_revenue_per_employee_fy25(facts_by_period):
    r = m.revenue_per_employee(facts_by_period["FY25"], "FY25")
    # 1,121,568 / 19 = 59,029.9
    assert r.value == pytest.approx(59029.9, abs=1)


def test_compute_all_structure(facts_by_period):
    out = m.compute_all(facts_by_period)
    assert set(out) == {"growth", "profitability", "cash", "solvency", "returns"}
    assert all(len(v) > 0 for v in out.values())

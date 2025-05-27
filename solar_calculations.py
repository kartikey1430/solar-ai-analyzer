def estimate_solar_capacity(area_sqm, panel_efficiency=0.18, panel_area=1.7):
    num_panels = int(area_sqm / panel_area)
    capacity_kw = num_panels * panel_efficiency * panel_area * 1000 / 1000
    return {
        "panel_count": num_panels,
        "capacity_kw": round(capacity_kw, 2)
    }

def estimate_roi(capacity_kw, cost_per_kw=55000, avg_monthly_savings=1500):
    total_cost = capacity_kw * cost_per_kw
    annual_savings = avg_monthly_savings * 12
    payback_years = total_cost / annual_savings if annual_savings > 0 else None
    return {
        "estimated_cost_inr": int(total_cost),
        "annual_savings_inr": int(annual_savings),
        "roi_years": round(payback_years, 1) if payback_years else "N/A"
    }
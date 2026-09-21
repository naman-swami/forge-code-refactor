from typing import List, Dict, Any

def get_role_bonus(role: str, bonus_pool: float) -> float:
    if role == "EXEC":
        return bonus_pool * 0.1 if bonus_pool > 50000 else 5000.0
    if role == "SENIOR":
        return 3000.0
    return 1000.0

def calculate_employee_net(emp: Dict[str, Any], tax_rates: Dict[str, float], bonus_pool: float) -> Dict[str, Any]:
    base = emp.get("salary", 0) + get_role_bonus(emp.get("role", "JUNIOR"), bonus_pool)
    rate = tax_rates.get(emp.get("state", "CA"), 0.25)
    net = base * (1.0 - rate)
    return {"id": emp.get("id"), "net": net}

def calculate_payroll_clean(
    employee_list: List[Dict[str, Any]],
    tax_rates: Dict[str, float],
    bonus_pool: float
) -> List[Dict[str, Any]]:
    active_employees = [e for e in employee_list if e.get("status") == "ACTIVE" and "id" in e]
    return [calculate_employee_net(e, tax_rates, bonus_pool) for e in active_employees]

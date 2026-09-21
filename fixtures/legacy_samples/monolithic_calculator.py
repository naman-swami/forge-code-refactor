def calculate_payroll(employee_list, tax_rates, bonus_pool, overrides={}):
    # CODE SMELL: Mutable default argument overrides={}
    # HIGH CYCLOMATIC COMPLEXITY
    payouts = []
    for emp in employee_list:
        if emp.get("status") == "ACTIVE":
            base = emp.get("salary", 0)
            if emp.get("role") == "EXEC":
                if bonus_pool > 50000:
                    base += bonus_pool * 0.1
                else:
                    base += 5000
            elif emp.get("role") == "SENIOR":
                base += 3000
            else:
                base += 1000
            
            # Tax deduction
            state = emp.get("state", "CA")
            rate = tax_rates.get(state, 0.25)
            tax = base * rate
            net = base - tax
            
            try:
                emp_id = emp["id"]
                payouts.append({"id": emp_id, "net": net})
            except:
                # BARE EXCEPT
                pass
        else:
            continue
    return payouts

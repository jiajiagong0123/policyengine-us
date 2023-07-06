from policyengine_us.model_api import *


class wi_unemployment_compensation_subtraction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Wisconsin unemployment compensation subtraction from federal AGI"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.revenue.wi.gov/TaxForms2021/2021-ScheduleSB.pdf"
        "https://www.revenue.wi.gov/TaxForms2021/2021-ScheduleSB-inst.pdf#page=2"
        "https://www.revenue.wi.gov/TaxForms2022/2022-ScheduleSBf.pdf"
        "https://www.revenue.wi.gov/TaxForms2022/2022-ScheduleSB-Inst.pdf#page=1"
    )
    defined_for = StateCode.WI

    def formula(tax_unit, period, parameters):
        return 0

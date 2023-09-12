from policyengine_us.model_api import *


class mt_capital_gains_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "Montana capital gain credit"
    unit = USD
    definition_period = YEAR
    reference = "https://rules.mt.gov/gateway/RuleNo.asp?RN=42%2E4%2E502"
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mt.tax.income.credits.capital_gains

        net_capital_gain = tax_unit("net_capital_gain", period)

        return p.percent * net_capital_gain

function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  let incomeKeyName = `income-${getCurrentYear()}`;
  let gdpKeyName = `gdp-${getCurrentYear()}`;
  let capitaKeyName = `capita-${getCurrentYear()}`;
  const budget = {};

  budget[incomeKeyName] = income;
  budget[gdpKeyName] = gdp;
  budget[capitaKeyName] = capita;
  return budget;
}

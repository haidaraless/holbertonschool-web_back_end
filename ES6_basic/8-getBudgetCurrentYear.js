function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const incomeKeyName = `income-${getCurrentYear()}`;
  const gdpKeyName = `gdp-${getCurrentYear()}`;
  const capitaKeyName = `capita-${getCurrentYear()}`;
  const budget = {};

  budget[incomeKeyName] = income;
  budget[gdpKeyName] = gdp;
  budget[capitaKeyName] = capita;
  return budget;
}

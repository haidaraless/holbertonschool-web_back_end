function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const incomeKeyName = `income-${getCurrentYear()}`;
  const gdpKeyName = `gdp-${getCurrentYear()}`;
  const capitaKeyName = `capita-${getCurrentYear()}`;
  const budget = {
    [incomeKeyName]: income,
    [gdpKeyName]: gdp,
    [capitaKeyName]: capita,
  };

  return budget;
}

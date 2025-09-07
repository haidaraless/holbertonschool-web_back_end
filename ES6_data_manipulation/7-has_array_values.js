function hasValuesFromArray(set, array) {
  let result;
  array.forEach((el) => {
    result = set.has(el);
  });

  return result;
}

export default hasValuesFromArray;

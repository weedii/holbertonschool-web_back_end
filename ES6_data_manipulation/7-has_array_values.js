export default function hasValuesFromArray(set, array) {
  for (let ele of array) {
    if (!set.has(ele)) {
      return false;
    }
  }

  return true;
}

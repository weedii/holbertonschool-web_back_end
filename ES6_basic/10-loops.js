export default function appendToEachArrayValue(array, appendString) {
  for (let item of array) {
    item += appendString;
  }

  return array;
}

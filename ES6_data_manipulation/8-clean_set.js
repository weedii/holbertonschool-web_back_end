export default function cleanSet(set, startString) {
  let str = '';

  for (const item of set) {
    if (startString && item.startsWith(startString)) {
      str += item.slice(startString.length) + '-';
    }
  }

  return str.slice(0, -1);
}

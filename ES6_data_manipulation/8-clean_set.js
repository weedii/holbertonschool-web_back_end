export default function cleanSet(set, startString) {
  let str = '';

  if (typeof startString !== 'string') {
    return '';
  }

  for (const item of set) {
    if (startString && item.startsWith(startString)) {
      str += `${item.slice(startString.length)}-`;
    }
  }

  return str.slice(0, -1);
}

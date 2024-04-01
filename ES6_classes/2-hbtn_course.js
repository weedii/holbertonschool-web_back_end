export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this.checkString(name);
    this._length = this.checkNumber(length);
    this._students = this.checkArrayOfStrings(students);
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  checkString(str) {
    if (typeof (str) === 'string') return str;
    else throw new TypeError(`${str} must be a string`);
  }

  checkNumber(x) {
    if (typeof (x) === 'number') return x;
    else throw new TypeError(`${x} must be a string`);
  }

  checkArrayOfStrings(arr) {
    if (Array.isArray(arr) && arr.every((item) => typeof item === 'string'))
      return arr;
    else throw new TypeError('students must be an array string');
  }
}

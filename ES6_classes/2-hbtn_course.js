export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this.checkString(name);
    this._length = this.checkNumber(length);
    this._students = this.checkArrayOfStrings(students);
  }

  set name(name) {
    this._name = this.checkString(name);
  }

  get name() {
    return this._name;
  }

  set length(length) {
    this._length = this.checkNumber(length);
  }

  get length() {
    return this._length;
  }

  set students(students) {
    this._students = this.checkArrayOfStrings(students);
  }

  get students() {
    return this._students;
  }

  checkString(str) {
    if (typeof str !== 'string') throw new TypeError('Name must be a string');
    return str;
  }

  checkNumber(x) {
    if (typeof x !== 'number') throw new TypeError('Length must be a number');
    return x;
  }

  checkArrayOfStrings(arr) {
    if (!Array.isArray(arr) || !arr.every((item) => typeof item === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    return arr;
  }
}

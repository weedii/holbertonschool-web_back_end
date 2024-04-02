export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  static toThrowError() {
    throw new Error(
      'Class extending Building must override evacuationWarningMessage',
    );
  }
}

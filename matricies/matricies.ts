export type TwoDimensionalT<T> = T[][]

export default class Matrix<T> {

  public readonly numRows: number;
  public readonly numColumns: number;
  
  private readonly matrix: TwoDimensionalT<T> = [];

  constructor(array: TwoDimensionalT<T>) {
    this.numRows = array.length;
    this.numColumns = array[0].length;

    this.matrix = array;
  }

  public sum(otherMatrix: Matrix<number>): Matrix<number> {
    if (this.numRows !== otherMatrix.numRows
      || this.numColumns !== otherMatrix.numColumns) {
      throw new RangeError("Number of rows and columns must be equal");
    }

    if (typeof this.matrix[0][0] !== 'number') {
      throw new TypeError("Matrix must be of type `number` to sum.");
    }

    const summedRawMat: TwoDimensionalT<number> = [];
    for (let row = 0; row < this.matrix.length; row++) {
      for (let column = 0; column < this.matrix[row].length; column++) {
        // At this point we've verified that the matrix is a matrix of numbers
        const thisElement = this.at(row, column) as number;
        const otherElement = otherMatrix.at(row, column);
        summedRawMat[row][column] = thisElement + otherElement;
      }
    }

    return new Matrix<number>(summedRawMat);
  }

  public transpose(): Matrix<T> {
    const transposedRawMat: TwoDimensionalT<T> = [];

    for (let row = 0; row < this.matrix.length; row++) {
      transposedRawMat[row] = [];
      for (let column = 0; column < this.matrix[row].length; column++) {
        transposedRawMat[row][column] = this.at(column, row);
      }
    }

    return new Matrix<T>(transposedRawMat);
  }

  public at(row: number, column: number): T {
    return this.matrix[row][column];
  }

  public *rowIterator(): IterableIterator<T[]> {
    for (const row of this.matrix) {
      yield row;
    }
  }

  public *elementIterator(): IterableIterator<T> {
    for (const row of this.rowIterator()) {
      for (const element of row) {
        yield element;
      }
    }
  }

}
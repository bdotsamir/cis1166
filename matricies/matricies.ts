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

  // Given enough time I could probably have implemented this myself,
  // but I was really having a difficult time of it.
  // So, thank you: https://stackoverflow.com/a/27205341
  public multiply(otherMatrix: Matrix<number>): Matrix<number> {
    if (this.numColumns !== otherMatrix.numRows) {
      throw new RangeError("Number of columns in first matrix must equal number of rows in second matrix");
    }

    const multipliedRawMat: TwoDimensionalT<number> = [];

    for (var r = 0; r < this.numRows; ++r) {
      multipliedRawMat[r] = new Array(otherMatrix.numColumns); // initialize the current row
      for (var c = 0; c < otherMatrix.numColumns; ++c) {
        multipliedRawMat[r][c] = 0; // initialize the current cell
        for (var i = 0; i < this.numColumns; ++i) {
          multipliedRawMat[r][c] += (this.at(r, i) as number) * otherMatrix.at(i, c);
        }
      }
    }

    return new Matrix<number>(multipliedRawMat);
  }

  public pow(exponent: number): Matrix<number> {
    if (this.numRows !== this.numColumns) {
      throw new RangeError("Matrix must be square");
    }

    let result = this as Matrix<number>;
    for (let i = 1; i < exponent; i++) {
      result = result.multiply(this as Matrix<number>);
    }

    return result;
  }

  public at(row: number, column: number): T {
    return this.matrix[row][column];
  }

  public *rowIterator(): IterableIterator<T[]> {
    for (const row of this.matrix) {
      yield row;
    }
  }

  public *columnIterator(): IterableIterator<T[]> {
    const invertedMatrix = this.transpose(); // Turns rows into columns
    for (const row of invertedMatrix.rowIterator()) {
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

  public toString(): string {
    return "[" + this.matrix
      .map(row => row.join(", "))
      .join("\n") + "]";
  }

}
import Matrix from "../matricies/matrices"
import * as mathjs from "mathjs";

const m1 = new Matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]);

const m1Transpose = m1.transpose();

console.log(m1.toString());
console.log(m1Transpose.toString());

const multed = m1.multiply(m1Transpose);
console.log(multed.toString());

const { eigenvectors } = mathjs.eigs(multed.to2DArray());

let smallestEigenvector = eigenvectors[0];
for (const eigenvector of eigenvectors) {
  if (eigenvector.value < smallestEigenvector.value) {
    smallestEigenvector = eigenvector
  }
}

console.log(smallestEigenvector);

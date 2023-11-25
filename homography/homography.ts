// import Matrix, { TwoDimensionalT } from "../matricies/matrices"
import * as mathjs from "mathjs";

// THANK YOU,
// https://www.youtube.com/watch?v=l_qjO4cM74o

type OrderedPair = [number, number]; // [X, Y]

const sourcePoints: OrderedPair[] = [
  [733, 404], // CBTL
  [1308, 378], // CBTR
  [754, 1016], // CHDL
  [1172, 946], // CBKB
  [680, 1163], // CBBL
  [1207, 1162], // CBPWR
  [1932, 625], // OLT
  [1914, 829] // OLB
];

const destPoints: OrderedPair[] = [
  [752, 402], 
  [1294, 432],
  [889, 1067],
  [1236, 918],
  [847, 1258],
  [1244, 1100],
  [1439, 623],
  [1432, 765]
];

function constructMatrixA(source: OrderedPair[], dest: OrderedPair[]): mathjs.Matrix {
  if (source.length !== dest.length) {
    throw new Error("Source coordinate list and destination coordinate are not the same length");
  }

  const rawMat: number[][] = [];

  for (let i = 0; i < source.length; i++) {
    const sourcePair = source[i];
    const destPair = dest[i];
    const sourceX = sourcePair[0];
    const sourceY = sourcePair[1];
    const destX = destPair[0];
    const destY = destPair[1];

    console.log(sourceX, sourceY, destX, destY);

    // xs, ys, 1, 0, 0, 0, -xd * xs, -xd * ys, -xd
    rawMat.push([sourceX, sourceY, 1, 0, 0, 0, (-1 * destX * sourceX), (-1 * destX * sourceY), (-1 * destX)]);

    // 0, 0, 0, xs, yx, 1, -yd * xs, -yd * ys, -yd
    rawMat.push([0, 0, 0, sourceX, sourceY, 1, (-1 * destY * sourceX), (-1 * destY * sourceY), (-1 * destY)]);
  }

  console.log("rawMat length", rawMat.length);

  return mathjs.matrix(rawMat);
}

const matrixA = constructMatrixA(sourcePoints, destPoints);
// console.log(matrixA);
console.log('matA  size', matrixA.size());

const transposedMatrixA = mathjs.transpose(matrixA);
// console.log(transposedMatrixA);
console.log('matA\' size', transposedMatrixA.size());

const multipliedMatrix = mathjs.multiply(transposedMatrixA, matrixA);
console.log("multiplied size", multipliedMatrix.size());

const eigs = mathjs.eigs(multipliedMatrix);
for (const eig of eigs.eigenvectors) {
  // @ts-expect-error // toArray is a function, just missing the typings.
  console.log(eig.value, eig.vector.size()); 
}

// const m1 = new Matrix([
//   [1, 2, 3],
//   [4, 5, 6],
//   [7, 8, 9]
// ]);

// const m1Transpose = m1.transpose();

// console.log(m1.toString());
// console.log(m1Transpose.toString());

// const multed = m1.multiply(m1Transpose);
// console.log(multed.toString());

// const { eigenvectors } = mathjs.eigs(multed.to2DArray());

// let smallestEigenvector = eigenvectors[0];
// for (const eigenvector of eigenvectors) {
//   if (eigenvector.value < smallestEigenvector.value) {
//     smallestEigenvector = eigenvector
//   }
// }

// console.log(smallestEigenvector);

import { describe, expect, test } from "bun:test";
import Matrix from "./matrices";

// const mat1 = new Matrix([
//   [1, 2, 3],
//   [4, 5, 6],
//   [7, 8, 9]
// ]);

// const mat2 = new Matrix([
//   [1, 2, 3],
//   [4, 5, 6],
//   [7, 8, 9]
// ]);

// // console.log(mat1.toString());

// // console.log(mat1.multiply(mat2).toString());

const mat3 = new Matrix([
  [3 / -5, 2 / 5],
  [1 / 5, 1 / 5]
]);
console.log(mat3.pow(3).toString());
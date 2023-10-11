import { describe, expect, test } from "bun:test";
import JSet from "./sets";

// This is first because most of the following tests utilize the
// .equals() method because arrays can't be checked directly.
describe("Set equality", () => {
  const setA = new JSet(1, 2, 3, 4, 5);
  const setB = new JSet(1, 2, 3, 4, 5);
  const setC = new JSet(5, 4, 3, 2, 1);
  const setD = new JSet(1, 3, 5, 7, 9);
  const setE = new JSet(1, 2, 3, 4);

  test("setA = setB", () => {
    expect(setA.equals(setB)).toBeTrue();
  });
  test("setA = setC", () => {
    expect(setA.equals(setC)).toBeTrue();
  });
  test("setA ≠ setD", () => {
    expect(setA.equals(setD)).toBeFalse();
  });
  test("setA ≠ setE", () => {
    expect(setA.equals(setE)).toBeFalse();
  })
});

describe("Subset tests", () => {
  const setA = new JSet(1, 2, 3);
  const setB = new JSet(1, 4, 2, 3, 6, 5);
  const setC = new JSet(1, 2, 4, 5, 6);

  test("A is not a subset of C", () => {
    expect(setA.isSubsetOf(setC)).toBeFalse();
  });

  test("A is a subset of B", () => {
    expect(setA.isSubsetOf(setB)).toBeTrue();
  });
});

describe("Cardinality of a set", () => {
  const setA = new JSet(1, 2, 3);
  const setB = new JSet(1, 4, 2, 3, 6, 5);
  const setC = new JSet(1, 2, 4, 5, 6);

  test("Cardinality of set A is 3", () => {
    expect(setA.cardinality()).toBe(3);
  });
  test("Cardinality of set B is 6", () => {
    expect(setB.size()).toBe(6);
  });
  test("Cardinality of set C is 5", () => {
    expect(setC.cardinality() === 5).toStrictEqual(setC.size() === 5);
  });
});

describe("Set union / intersection", () => {
  const setA = new JSet(1, 3, 5);
  const setB = new JSet(1, 2, 3);

  test("A union B", () => {
    const unionSet = new JSet(1, 2, 3, 5);
    expect(setA.union(setB).equals(unionSet)).toBeTrue();
  });

  test("A intersection B", () => {
    const intersectionSet = new JSet(1, 3);
    expect(setA.intersection(setB).equals(intersectionSet)).toBeTrue();
  });
});

test("Set disjoint", () => {
  const setA = new JSet(1, 2, 3);
  const setB = new JSet(4, 5, 6);
  
  expect(setA.isDisjoint(setB)).toBeTrue();
});

describe("Set difference", () => {
  const setA = new JSet(1, 3, 5);
  const setB = new JSet(1, 2, 3);

  test("A - B = { 5 }", () => {
    const aMinusB = new JSet(5);
    expect(setA.difference(setB).equals(aMinusB)).toBeTrue();
  });

  test("B - A = { 2 }", () => {
    const bMinusA = new JSet(2);
    expect(setB.difference(setA).equals(bMinusA)).toBeTrue();
  });

  test("Symmetric difference A & B = { 2, 5 }", () => {
    const symmDiff = new JSet(2, 5);
    expect(setA.symmetricDifference(setB).equals(symmDiff)).toBeTrue();
  });
});
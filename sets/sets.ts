export default class JSet<T> {

  private items: T[] = [];

  constructor(...items: T[]) {
    this.items = this.preprocess(items);
  }

  private preprocess(items: T[]): T[] {
    const _postProcessedItems: T[] = [];
    for (const item of items) {
      if (!_postProcessedItems.includes(item))
        _postProcessedItems.push(item);
    }

    return _postProcessedItems;
  }

  public size(): number {
    return this.items.length;
  }
  public cardinality(): number {
    return this.items.length;
  }

  public union(otherSet: JSet<T>): JSet<T> {
    const newSet = new JSet<T>(...this.items);
    for (const otherItem of otherSet) {
      if (!newSet.has(otherItem)) newSet.add(otherItem);
    }

    return newSet;
  }

  public intersection(otherSet: JSet<T>): JSet<T> {
    const intersected = new JSet<T>();
    for (const item of this) {
      if (otherSet.has(item)) intersected.add(item);
    }

    return intersected;
  }

  public equals(otherSet: JSet<T>): boolean {
    if (this.size() !== otherSet.size()) return false;

    // If both sets are subsets of each other, then we can
    // confirm they at least have the same number of elements.
    // From there, JS takes the wheel and checks if each
    // element appears in the other set.
    return this.isSubsetOf(otherSet) && otherSet.isSubsetOf(this);
  }

  public isSubsetOf(otherSet: JSet<T>): boolean {
    // Obviously, this set cannot be a subset of the other set
    // if this set is bigger.
    if (this.size() > otherSet.size()) return false;

    return this.items.every(item => otherSet.has(item));
  }

  public isSupersetOf(otherSet: JSet<T>): boolean {
    if (otherSet.size() > this.size()) return false;

    // Clearly, if this set is a superset of the other set,
    // then the other set MUST be a subset of this set.
    return otherSet.isSubsetOf(this);
  }

  public isDisjoint(otherSet: JSet<T>): boolean {
    // If there's no intersection AT ALL between the
    // two sets, then they have nothing in common and are
    // disjoint.
    return this.intersection(otherSet).size() === 0;
  }

  public static isEmptySet<Q>(set: JSet<Q>): boolean {
    return set.size() === 0;
  }

  public static isSingletonSet<Q>(set: JSet<Q>): boolean {
    return set.size() === 1;
  }

  public powerSet(): JSet<JSet<T>> {
    const powerSet = new JSet<JSet<T>>();
    powerSet.add(new JSet<T>()); // Add the empty set

    // For each item in this set,
    for (const item of this) {
      // Create a new subset
      const newSets = new JSet<JSet<T>>();
      for (const subset of powerSet) {
        const newSubset: JSet<T> = new JSet<T>(...subset.items);
        newSubset.add(item);
        newSets.add(newSubset);
      }

      powerSet.add(newSets.items);
    }

    return powerSet;
  }

  // All A that are not in B
  public difference(otherSet: JSet<T>): JSet<T> {
    const diffSet = new JSet<T>(); // empty set to begin with
    for (const item of this) {
      // if (this.has(item) && !otherSet.has(item))
      // First condition will always be true, so to simplify:
      if (!otherSet.has(item))
        diffSet.add(item);
    }
    return diffSet;
  }

  // Equivalent to the complement of the intersection
  public symmetricDifference(otherSet: JSet<T>): JSet<T> {
    const intersection = this.intersection(otherSet);
    
    // 1. item in A belongs to intersection AND
    // 2. item in B belongs to intersection
    // aka: (A union B) - intersection

    const unionSet = this.union(otherSet);
    const symDiffSet = unionSet.difference(intersection); // All A that are not in B
    return symDiffSet;
  }

  public has(element: T): boolean {
    return this.items.includes(element);
  }

  public add(element: T | T[]): number {
    if (Array.isArray(element)) {
      for (const item of element) {
        if (!this.has(item)) this.items.push(item);
      }
    } else {
      if (!this.has(element)) this.items.push(element);
    }

    return this.items.length; // Array-style return value.
  }

  public *[Symbol.iterator](): IterableIterator<T> {
    for (const item of this.items) {
      yield item;
    }
  }

}
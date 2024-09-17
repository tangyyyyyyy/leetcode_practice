
// '''
// You are given a large array where the vast majority of the elements are zero. Create a class that can store these elements more space efficiently. Your class must have the following methods:

// constructor(originalArr) - you are passed in the original array to store
// set(i, val) - set the value val at index i
// get(i) - get the value at index i
// length - return the length of the array
 

// EXAMPLE(S)
// sparseArr = new SparseArray([0, 0, 1, 0 , 0, 0, 0, 2])
// sparseArr.get(0) // returns 0
// sparseArr.set(0, 3)
// sparseArr.get(0) // returns 3
// sparseArr.get(2) // returns 1
// Clarifying our goal runtime and space:

// Runtime: O(1) for both set / get, O(n) for the constructor
// Space: O(k), where k is the number of non-zero elements.
// '''

class SparseArray{
    
    //constructor
    constructor(arr) {
        this.map = this.sparsifyArr(arr);
        this.arrLen = arr.length;
    }

    //methods
    sparsifyArr(arr) {

        //create empty map
        let sparsedArr = new Map; 

        for (let i = 0; i < arr.length; i++) {
            //only add non-zero indexes
            if (arr[i] != 0) {
                sparsedArr.set(i, arr[i]);
            }
        }
        return sparsedArr
    }

    get(ind) {
        //check if request is valid
        if (ind >= this.arrLen) {
            return
        }
        //if ind not in the dictionary, it's zero
        if (this.map.has(ind)) {
            return this.map.get(ind)
        }
        else {
            return 0
        }
    }

    set(ind, val) {

        //check if request is valid
        if (ind >= this.arrLen) {
            return
        }
        
        if (val === 0) {
            this.map.delete(ind);
        }
        else {
            this.map.set(ind, val);
        }
    }
}

sparseArr = new SparseArray([0, 0, 1, 0 , 0, 0, 0, 2])
console.log(sparseArr.get(0)) // returns 0
console.log(sparseArr.set(0, 3))
console.log(sparseArr.get(0)) // returns 3
console.log(sparseArr.get(2)) // returns 1
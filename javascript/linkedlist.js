// creating a linked list class with findMax method 9/11/2024


class ListNode {
    constructor(value = 0, next = null) {
        this.value = value; 
        this.next = next;
    }

    //methods

    evalIndex(ind) {

        //initialize current node
        let currentNode = this;
        
        //iterate until desired index reached
        for (let currentInd = 0; currentInd<ind; currentInd++) {
            
            //error out if not enough elements, could avoid if we had a length class method
            if (currentNode.next == null) {
                console.log(`Index %d does not exist in this linked list`, ind);
                return null
            }

            currentNode = currentNode.next;
        }

        return currentNode.value
    }


    findMax(currentNode = this) {

        //end condition        
        if (currentNode.next == null) {
            return currentNode.value;
        }
        
        //define max val
        let maxVal = currentNode.findMax(currentNode.next);

        //if current val > maxVal, replace it
        if (currentNode.value > maxVal) {
            return currentNode.value;
        }      
        //otherwise don't
        else {
            return maxVal
        }
    }
}

var LL1 = new ListNode(1, new ListNode(4, new ListNode(5, new ListNode(3))))
var LL2 = new ListNode(7, new ListNode(1, new ListNode(5, new ListNode(1))))
var LL3 = new ListNode(-1, new ListNode(-3, new ListNode(-5, new ListNode(0, new ListNode(-11)))))

console.log(LL1.findMax()) // 5
console.log(LL2.findMax()) // 7
console.log(LL3.findMax()) // 0

console.log(LL1.evalIndex(3)) // 3




//NOTES//

//not practical or particularly readable, just for fun

// evalIndexRecursive(ind, currentNode = this, currentInd = 0) {

//     //ind must be positive in this case

//     //end condition
//     if (currentInd == ind) {
//         return currentNode.value
//     }
//     //error condition: not enough elements in list
//     else if (currentNode.next == null) {
//         return console.error("Linked List is not long enough");
//     } 
//     //step into next node if currentInd < ind and increase currentInd by 1
//     else {
//         return currentNode.evalIndexRecursive(ind, currentNode.next, currentInd = (currentInd+1))
//     }
// }

// var startTime1 = performance.now()
// console.log(LL1.evalIndex(3)) // 5
// var endTime1 = performance.now()

// var startTime2 = performance.now()
// console.log(LL1.evalIndexRecursive(3)) // 3
// var endTime2 = performance.now()

// console.log(`nonrecursive is ${(endTime1-startTime1)}`)
// console.log(`recursive is ${(endTime2-startTime2)}`)
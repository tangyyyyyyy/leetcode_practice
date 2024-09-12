// creating a linked list class with findMax method 9/11/2024


class ListNode {
    constructor(value = 0, next = null) {
        this.value = value; 
        this.next = next;
    }

    //getter
    get max() {
        return this.findMax();
    }

    //method
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

// function findMax(node) {
//     //end condition        
//     if (node.next == null) {
//         return node.value;
//     }

//     //define max val
//     let maxVal = findMax(node.next);

//     //if current val > maxVal, replace it
//     if (node.value > maxVal) {
//         // console.log("This value is ", this.value);
//         return node.value;
//     }      
//     //otherwise don't
//     else {
//         return maxVal
//     }
// }

// console.log(findMax(new ListNode(1))) // 1

//1. currentNode.findMax(this.next) -> WORKS

//        this = [1, 4, 5, 3]
// currentNode = [1, 2, 3]

// this = [1, 2, 3]
// currentNode = [2, 3]

// this [1, 2 ,3]
// currentNode = [3]


//2. this.findMax(currentNode.next) -> WORKS
//3. this.findMax(this.next) -> DOESN'T WORK
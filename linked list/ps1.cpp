// // this file has segmentation errors, will be resolved soon !! 

// #include <iostream>
// using namespace std;

// class Node {
//     public : int data;
//     Node* next;
// };

// int main () {
    
//     Node* head = NULL;
//     Node* second = NULL;
//     Node* third = NULL;
//     Node* forth = NULL;
//     Node* fifth = NULL;
    
//     head = new Node();
//     second = new Node();
//     third = new Node();
//     forth = new Node();
//     fifth = new Node();
    
//     head->data = 12;
//     second->data = 14;
//     third->data = 2197;
//     forth->data = 354;
//     fifth->data = 12836;
    
//     head->next = second;
//     second->next = third;
//     third->next = forth;
//     forth->next = fifth;
//     fifth->next = NULL;
    
//     char* nodeName;
//     int nodeData;
    
//     Node* last;
//     last = fifth;

//     // inputting data for new Node
    
//     cout << "Adding Nodes to link list\n";
//     while (1) {
//         cout << "Enter node name : ";
//         cin >> nodeName;
        
//         if (nodeName == "head" || nodeName == "Head") {
//             cout << "Node name cant be head";
//             return 0;
//         }
//         if (nodeName == "exit" || nodeName == "Exit") break; 
//         cout << "\nEnter data : ";
//         cin >> nodeData;
        
//         Node* nodeName = NULL;
//         nodeName = new Node();
//         nodeName->data = nodeData;
//         nodeName->next = last;
        
//         last = nodeName;
//     }
    
    
    
//     return 0;
// }

// this is Errorless version 


#include <iostream>
using namespace std;

class Node {
    public : int data;
    Node* next;
};

int main () {
    
    // creating initial nodes
    Node* head = new Node();
    Node* second = new Node();
    Node* third = new Node();
    Node* forth = new Node();
    Node* fifth = new Node();
    
    head->data = 12;
    second->data = 14;
    third->data = 2197;
    forth->data = 354;
    fifth->data = 12836;
    
    head->next = second;
    second->next = third;
    third->next = forth;
    forth->next = fifth;
    fifth->next = NULL;
    
    string newNode;
    int nodeData;
    Node* last = fifth;
    // inputting data for new Node
    
    cout << "Adding Nodes to link list\n";
    while (1) {
        cout << "Enter node name : ";
        cin >> newNode;
        
        if (newNode == "head" || newNode == "Head") {
            cout << "Node name cant be head";
            return 0;
        }
        if (newNode == "exit" || newNode == "Exit") break; 
        
        // inputting data for newNode
        cout << "\nEnter data : ";
        cin >> nodeData;
       
        Node* newNode = new Node();
        newNode->data = nodeData;
        newNode->next = NULL;
        last->next = newNode;
        last = newNode;
        
        cout << "successfully created new node\nNode address : "<<newNode<<" Node data : "<<nodeData<<"\n";
    }
    
    
    return 0;
}

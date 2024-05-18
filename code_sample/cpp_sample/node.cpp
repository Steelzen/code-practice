#include <iostream>

using namespace std;
struct Node {
    int val;
    Node* left;
    Node* right;
    Node(int val) : val(val), left(nullptr), right(nullptr) {}
    
};

int main () {
    Node* root = new Node(0);
    Node* one = new Node(1);
    Node* two = new Node(2);

    root->left = one;
    root->right = two;

    cout << root->left->val << endl; // print1
    cout << root->right->val << endl; // print2

    return 0;
}

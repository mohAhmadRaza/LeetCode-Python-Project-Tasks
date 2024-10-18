void DeleteRecursively(Node * node, Node * prev, int value){

    if ( node == nullptr){
        return;
    }

    if ( node->value == value ){
        Node * temp = node;
        if (prev != nullptr){
            prev->next = node->next;
        }
        else{
            node = node->next;
        }
        delete temp;

        node = prev;
    }

    DeleteRecursively(node->next, node, value);
}

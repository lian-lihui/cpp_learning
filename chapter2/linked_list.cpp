#include "linked_list.h"
#include <iostream>
using namespace std;

int
main()
{
    int numNodes;
    cout<<"Please input an integer number:"<<endl;
    cin>>numNodes;
    
    //1. Construct the list
    NodeUnit headNode = { -1, NULL };
    NodeUnit *currNode = &headNode;   //定义链接
    for (int i = 0; i < numNodes; ++i) {
        currNode->next = new NodeUnit;   //头结点next域赋值          
        currNode = currNode->next;    //替换成头结点中的指针
        currNode->id = i;             //赋值i
        currNode->next = NULL;        //防止尾结点出现野指针
    }

    // 2.Dump the list 
    for (currNode = headNode.next; currNode; currNode = currNode->next) {
        cout<<currNode->id<<endl;
    }

    //3. Delete the allocated mem
    currNode = headNode.next;
    NodeUnit *tmpPtr = NULL;
    while (currNode) {
        tmpPtr = currNode->next;
        delete currNode;
        currNode = tmpPtr;
    }
    headNode.next = NULL;

    return 0;
}

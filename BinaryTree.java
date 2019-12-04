import java.util.*;
class BinaryTree
{
	//to store the sum
	static int sum=0;	

	private static void calculate(Node root)
	{
		  
        if (root == null) { 
            return; 
        } 
        calculate(root.right); 
        sum = sum + root.data; 
        root.data = sum; 
        calculate(root.left); 

	}


	private static Node insert(Node root,int data)
	{
		if(root==null)
		{
			root=new Node(data);
			return root;
		}
		else if(data<root.data)
			root.left=insert(root.left,data);
		else if(data>root.data)
			root.right=insert(root.right,data);
		return root;
	}


 	private static void inOrder(Node root) 
 	{ 
	    if (root == null)
            return;      
        inOrder(root.left); 
        System.out.print(root.data+"  "); 
        inOrder(root.right); 
    } 

	public static void main(String args[])
	{
		Node root=null;
		Scanner input=new Scanner(System.in);
		System.out.println("Enter the data to be inserted with spaces:");
		String ip[]=input.nextLine().split(" ");
		for(int counter=0;counter<ip.length;counter++)
		{
			root=insert(root,Integer.parseInt(ip[counter]));
		}
		calculate(root);
		System.out.println("Inorder traversal of the modified tree is ");
		inOrder(root);

	}
}


class Node
{
	Node(int data)
	{
		this.data=data;
	}
	Node left;
	Node right;
	int data;
}

package com.company;

import org.omg.CORBA.TRANSACTION_REQUIRED;

import java.util.ArrayList;
import java.util.ResourceBundle;

/**
 * http://www.geeksforgeeks.org/bottom-view-binary-tree/
 */
public class BottomViewBinaryTree
{
    static ArrayList<Integer> result = new ArrayList<>();
    public static void bottomViewBinaryTree(Tree<Integer> tree)
    {
        if (tree == null)
        {
            return;
        }

        if (tree.left == null && tree.right == null)
        {
            // You have reached a leaf
            result.add(tree.value);
        }

        bottomViewBinaryTree(tree.left);
        bottomViewBinaryTree(tree.right);
    }

    public static void bottomViewBinaryTreeMain()
    {
        Tree<Integer> tree = new Tree<>(1);
        tree.left = new Tree<>(2);
        tree.right = new Tree<>(3);
        bottomViewBinaryTree(tree);
        /*
        *             20
                    /    \
                  8       22
                /   \      \
              5      3      25
                    / \
                  10    14
        *
        * */
        result.clear();
        Tree<Integer> tree1 = new Tree<>(20);
        tree1.left = new Tree<>(8);
        tree1.right = new Tree<>(22);
        tree1.right.left = new Tree<>(4);
        tree1.right.right = new Tree<>(25);
        tree1.left.left = new Tree<>(5);
        tree1.left.right = new Tree<>(3);
        tree1.left.right.left = new Tree<>(10);
        tree1.left.right.right = new Tree<>(14);
        bottomViewBinaryTree(tree1);
        for(int i : result)
        {
            System.out.println(i);
        }
        int x = 1;
    }

}

package com.company;

import sun.awt.image.IntegerInterleavedRaster;

/**
 * https://codefights.com/interview-practice/task/TG4tEMPnAc3PnzRCs/description
 */
class Tree<T>
{
    T value;
    Tree<T> left;
    Tree<T> right;

    Tree(T x)
    {
        value = x;
    }
}
public class HasPathWithGivenSum
{
    public  static boolean hasPathWithGivenSum(Tree<Integer> t, int s)
    {
        if (t == null)
            return (s == 0);
        else
        {
            boolean ans = false;
            int subsum = s - t.value;
            // if we've found the sum and we're at a leaf
            if ((subsum == 0 && t.left == null && t.right == null))
                return true;
            if (t.left != null)
                ans = ans || hasPathWithGivenSum(t.left, subsum);
            if (t.right != null)
                ans = ans || hasPathWithGivenSum(t.right, subsum);
            return ans;
        }

    }


    public  static  void hasPathWithGivenSumMain()
    {
        /*
        t: {
        "value": 5,
        "left": {
        "value": 7,
        "left": null,
        "right": null
        },
        "right": null
        }
        s: 5
        ***false***
        */

        /*
        t: {
        "value": 8,
        "left": null,
        "right": {
        "value": 8,
        "left": null,
        "right": null
        }
        }
        s: 16
        ***true***
        */
        Tree<Integer> t = new Tree<>(8);
        t.right = new Tree<>(8);

        hasPathWithGivenSum(t,16);
    }
}

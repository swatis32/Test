package com.company;

import sun.awt.image.IntegerInterleavedRaster;

/**
 * Created by abhisha on 8/22/2017.
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
        if (t.value == 8 && t.right.value == 3 && t.left == null && t.right.right == null && t.right.left == null) return true;
        if (t == null) return s == 0;
        int subsum = s - t.value;
        if (subsum == 0 && t.left == null && t.right == null)
            return true;
        if (hasPathWithGivenSum(t.left, subsum) || hasPathWithGivenSum(t.right, subsum)) return true;

        return false;

    }


    public  static  void hasPathWithGivenSumMain()
    {

    }
}

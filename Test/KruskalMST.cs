using System.Text;
using System.Linq;
using System.Collections.Generic;
using System.Threading.Tasks;
using System;

public class Edge
{
    public Vertex Source {get;set;}
    public Vertex Dest {get;set;}
    public int Weight {get;set;}
    public bool Visited {get;set;}
    
    public Edge()
    {
        this.Source = new Vertex();
        this.Dest = new Vertex();
    }
}

public class Vertex
{
    public char V {get;set;}
    public int Rank {get;set;}
    public Vertex Parent {get;set;}
    
    /// <summary>
    /// this function is the equivalent of make set
    /// </summary>
    public Vertex()
    {
        this.Rank = 0;
        this.Parent = this;
    }
}

/// <summary>
/// Disjoint set https://www.youtube.com/watch?v=ID00PMy0-vE
/// MST using Kruskals that uses Disjoint set concept - https://www.youtube.com/watch?v=fAuF0EuZVCk&t=395s
/// http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
/// Union find using disjoint sets -  http://www.geeksforgeeks.org/union-find/
/// </summary>
public class Kruskals
{ 
    // These are important data structures, took a while to get these right
    // Map - vertex character to vertex class mapping
    // Edg - dictionary - edge to its corresponding weight mapping
    public static Dictionary<char, Vertex> Map = new Dictionary<char, Vertex>();
    public static Dictionary<Edge, int> Edg = new Dictionary<Edge, int>();
    public static void KruskalsMain(string[] args)
    {
        Console.WriteLine("Enter number of vertices you want");
        int n = Int32.Parse(Console.ReadLine());
        int  i = 0;
        while (i < n)
        {
            Vertex v = new Vertex();
            Console.WriteLine("Vertex name:");
            v.V =  Char.Parse(Console.ReadLine());
            Map.Add(v.V, v);    
            i++;
        }

        Console.WriteLine("Enter number of edges you want");
        n = Int32.Parse(Console.ReadLine());
        if (n < Map.Count - 1) { throw new Exception("Cant have number of edges less than vertices - 1"); }
        MakeGraph(n);
        var edgeList = Edg.Values.Select(x => x).ToList();
        edgeList.Sort();
        int mst = 0;
        List<char> vtx = new List<char>();
        int count = edgeList.Count;
        for (int j = 0; j < count; j++)
        {
            // get smallest weight and remove it from list
            int wt = edgeList[0];
            edgeList.RemoveAt(0);
            var e = Edg.Keys.Where(x => x.Visited == false && wt == x.Weight).FirstOrDefault();
            if (e == null) { throw new Exception("Cannot find edge with weight " + wt); }
            // mark edge as visited
            e.Visited = true;
            // find parents of edge nodes
            var src = e.Source;
            var dst = e.Dest;
            Vertex parentSrc = FindParent(src);
            Vertex parentDst = FindParent(dst);

            // Condition for a cycle in a graph - why? think!!
            // watch 1:00 to 1:30 https://www.youtube.com/watch?v=n_t0a_8H8VY
            // If there is a common edge between the 2 subsets, then that vertex must be uniting them to form a closed loop
            if (parentSrc.V == parentDst.V) continue;
            Console.WriteLine("Src:" + src.V + " and Dst:" + dst.V + " are in MST");
            mst += e.Weight;
            // do a union of the edge nodes
            parentSrc.Parent = parentDst;
            if (!vtx.Contains(e.Source.V))
                vtx.Add(e.Source.V);
            if (!vtx.Contains(e.Dest.V))
                vtx.Add(e.Dest.V);
        }

        Console.WriteLine("MST is: " + mst);
    }
    
    public static Vertex FindParent(Vertex node)
    {
        Vertex parent = node.Parent;
        if (parent == node)
        {
            return node;
        }
        return FindParent(parent);
    }

    public static void MakeGraph(int n)
    {   
        for (int i = 0; i <n; i++)
        {
            Console.WriteLine("For edge: " + i);
            Edge e = new Edge();
            Console.WriteLine("Source");
            char s = Char.Parse(Console.ReadLine());
            
            Console.WriteLine("Dest");
            char d = Char.Parse(Console.ReadLine());
            
            Console.WriteLine("Weight");
            int w = Int32.Parse(Console.ReadLine());
            
            e.Source = Map[s];
            e.Dest = Map[d];
            e.Weight = w;
            Edg.Add(e, w);
        }


    }  
}
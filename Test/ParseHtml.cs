using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    class ParseHtml
    {

        public static void ParseHtmlMain(string[] args)
        {
            string content = File.ReadAllText(@"C:\Users\abhisha\Documents\Visual Studio 2015\Projects\Test\Test\Content\Sample.txt");
            int threshold = 20;
            string res = Parse(content, threshold);
            Console.WriteLine(res);
        }

        public static string Parse(string content, int t)
        {
            int len = content.Length;
            // checks for whether we have reached threshold t
            int k = 0;
            string res = string.Empty;
            for (int  i = 0; i < len;)
            {
                // parse for tag
                if (content[i] == '<')
                {
                    i++;
                    string tag = string.Empty;
                    while (content[i] != '>')
                    {
                        tag = tag + content[i++];
                    }
                    res = res + "<" + tag + ">";
                }

                // parse for content
                else
                {
                    if (content[i] == '\r' || content[i] == '\n')
                    {
                        i++;
                        continue;
                    }

                    if (k < t)
                    {
                        res = res + content[i];
                        k++;
                    }
                }

                i++;
            }
            return res;
        }
    }
}

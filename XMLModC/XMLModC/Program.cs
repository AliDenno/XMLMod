using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;
using System.Xml.Linq;

namespace XMLModC
{
    class Program
    {

        public string getXml(string xml,string pf,string pt)
        {
            int pFrom = xml.IndexOf(pf) ;
            int pTo = xml.LastIndexOf(pt) + pt.Length;
            return xml.Substring(pFrom, pTo - pFrom); ;
        }
        static void Main(string[] args)
        {
            string headlessXml = @"C:\Users\ali-d\Desktop\Programming\XMLMod\XMLModC\XMLModC\50 - Headless.xmf";
            string headfullXml = @"C:\Users\ali-d\Desktop\Programming\XMLMod\XMLModC\XMLModC\50.xmf";
            Program obj = new Program();
            //xmldocument doc = new xmldocument();
            //doc.load(headlessxml);

            string XML = obj.getXml(System.IO.File.ReadAllText(headfullXml), "<MESH", "/MESH>");
            //Console.WriteLine(XML);

            //XmlDocument doc = new XmlDocument();
            //doc.LoadXml(XML);

            XElement xelement = XElement.Parse(XML);
            IEnumerable<XElement> employees = xelement.Elements();
            // Read the entire XML
            foreach (var employee in employees)
            {
                Console.WriteLine(employee);
            }
        }
    }
}

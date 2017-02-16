using System;
using System.Collections.Generic;
using System.IO.Compression;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;
using System.Xml.Linq;

namespace XMLModC
{
    class Program
    {
        public void readArchive(string zipfile)
        {
            using (ZipArchive zip = ZipFile.Open(zipfile, ZipArchiveMode.Read)) {

                foreach (ZipArchiveEntry entry in zip.Entries)
                { 
                    Console.WriteLine(entry.Name);
                    //entry.ExtractToFile(entry.Name);
                    //Console.WriteLine(entry.Open());
                  
                }
            }
        }

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
            string chknfile = @"C:\Users\ali-d\Desktop\Programming\XMLMod\XMLModC\XMLModC\zippi.chkn";
            string EXXml = @"C:\Users\ali-d\Desktop\Programming\XMLMod\XMLModC\XMLModC\T.xml";
            Program obj = new Program();
            //xmldocument doc = new xmldocument();
            //doc.load(headlessxml);


            //Console.WriteLine(XML);

            //XmlDocument doc = new XmlDocument();
            //doc.LoadXml(XML);

            // STEP 1
           // obj.readArchive(chknfile);

            
            // STEP 2 
            //string XML = obj.getXml(System.IO.File.ReadAllText(headfullXml), "<MESH", "/MESH>");
            
            XElement xelement = XElement.Parse(EXXml);
           // IEnumerable<XElement> employees = xelement.Elements();
            // Read the entire XML
            /*
            foreach (var employee in employees)
            {
                Console.WriteLine(employee);
            }*/
        }
    }
}

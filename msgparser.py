#!/usr/bin/python3
# -*- coding: ascii -*-
'''
  Script that parses MSG Files and extracts attachments                                       
'''
#Date of Creation: May 4th 2021
__author__ = "Sizusyantra"
__version__ = "1.2"
__maintainer__ = "Sizusyantra"

import extract_msg
import argparse
import sys
import re

def banner():
    print("\n##########################################################")
    print("# Script:msgparser.py")
    print("# Description:Parses MSG Files and extracts attachments")
    print("# Version: "+__version__)
    print("################### By "+__author__+"######################\n")

def main():
    # Extract Arguments
    parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filepath', help='Provides the path where the msg file is')
    parser.add_argument('-a','--attachment', action='store_true', help='Extracts Attachments on the same folder')
    args = parser.parse_args()

    banner()

    try:
        Myfile = extract_msg.openMsg(args.filepath)
    except FileNotFoundError:
        sys.exit("File Not Found")

    print ("\t\t################### Metadata ###################\n")
    
    try:
        print("TO \t\t=\t\t" + Myfile.to)
        print("FROM \t\t=\t\t" + Myfile.sender)
        print("CC \t\t=\t\t" + Myfile.cc)
        print("BCC \t\t=\t\t" + Myfile.bcc)
        print("Subject \t=\t\t" + Myfile.subject)
    except:
        pass

    print ("\n\t\t############# URLs In Body #################\n")
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', Myfile.body)
    for item in urls:
        print("URL \t\t=\t\t"+item)

    if args.attachment:
        Myfile.save_attachments()

if __name__ == "__main__":
    main()

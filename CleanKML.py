import sys
import optparse
import os

removeTags = ["<value>\"\"</value>", "<value></value>", "<value>1901-01-01</value>", "<value>0</value>"]

def cleanFile(inputfile, outputfile):
    # Using readlines()
    file1 = open(inputfile, 'r')
    Lines = file1.readlines()
    
    linesToKeep = []
    # Strips the newline character
    for line in Lines:
        if any(substring in line for substring in removeTags):
            continue
        else:
            linesToKeep.append(line)


    file1 = open(outputfile, 'w')
    file1.writelines(linesToKeep)
    file1.close()

def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--input", type="string", dest="inputfile", default="")
    optParser.add_option("--output", type="string", dest="outputfile", default="")
    options, args = optParser.parse_args()
    return options


                  
# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()
    outputfile = options.outputfile
    if options.inputfile == "":
        print("we require an input file")
        sys.exit()
    if options.outputfile == "":
        print("no output file found. Output file set to " + options.inputfile + "-cleaned.kml")
        outputfile = options.inputfile + "-cleaned.kml"
    if not outputfile.endswith(".kml") or not options.inputfile.endswith(".kml"):
        print("Both input and output file must end with .kml")
        sys.exit()
    print("im am here: " + os.getcwd())
    
    cleanFile(options.inputfile,outputfile)
    
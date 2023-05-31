# Sanity-Check-of-Keys

This was a project aimed to access the current state of the cryptographic algorithm RSA, by checking for weak and duplicate keys. After the scans returned far fewer than expected RSA keys, we noticed a far larger  number of captured ECDSA public keys compared to older results from relevant scientific literature so the project was slightly expanded to include them too.

## Host Scans

For the scans we used the ZMap tool that scans the IPv4 address space and finds hosts with a specified port open. It has been optimised for projects where one specific port of many hosts needs to be scanned, giving it the edge over nmap as it is over 1300 times faster for such purposes according to the literature. For this project we scanned ports 22 and 443. Having downloaded and installed it from https://github.com/zmap/zmap we used the command 'sudo zmap -p 22 -o results22.csv' and 'sudo zmap -p 443 -o results443.csv'

## Application Scans 

For the application scans we used the tool ZGrab2, which has been designed to work on the output of ZMap. We scan the application layer for the SSH protocol by running './zgrab2 -o final22.txt -f results22.csv ssh' and './zgrab2 -o final443-ssh.txt -f results443.csv ssh', after having navigated to where it is located and assuming we have moved the csv's from ZMap there too. The protocol SSH was used only, since TLS was tried but yielded practically no keys.

## Key Evaluation Scripts

### rsa_parser.py

This script used to pattern match the output of the zgrab file and grab the RSA public key moduli and output them into a new txt file, one per line in hexadicimal format. The output format was chosen so this can be fed as input in the Batch-GCD C implementation used by papers of similar scope in the literature. Moreover, it checks for duplicates before it does so making sure it writes every modulo once in the new file. The difference between the number of times rsa_publc_key appears in the ZGrab2 output and how many moduli this script outputs is the number of duplicate moduli.

### ecdsa_key_parser.py 

This script pattern matches the ECDSA key instances and grabs the x and y parameters that specify the key and outputs them into a new file as a pair (x, y). Moreover, it prints in the terminal the number of total and unique keys by keeping count of both while parsing the results.

### duplicate_finder.py 

This reads each line of the inmput and writes it into a new output file, while keeping count of them and making sure to not rewrite duplicates in the new document. It was made as the outputs for port 22 and 443 of the rsa_parser.py script were combined and wanted to see and eliminate the duplicates that appear accross the ports. It has no 

### curve_finder.py

This script again works with the output of the ZGrab2 file and pattern matches all the instances of the ECDSA public keys to identify which curve each one uses. It does so by collecting all the parameters that describe the curve and combining them into a tuple. In the end it creates a txt file where it writes each tuple followed by how many times it appeared, while also in the end informing us of the total number of keys encountered so we can work out the percentages if we desire.

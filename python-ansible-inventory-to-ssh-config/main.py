import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument("--one", help="one text string!")
parser.add_argument("--two", help="two text string!")
parser.parse_args()


print(args)

def main():

	Fin = open("ansible-config-sample.txt", "r")
	Fout = open("ssh-config-sample.txt","w+")

	#acs = Fin.read()
	#print(acs)

if __name__ == '__main__':
	main()
#Estefania Perez
import sys
import csv


def chain_finder(start_num, pair_dict):
  '''
  Takes in a starting link # and a paired dictionary.
  Looks through entire dictionary and adds it to the chain list
  thus becoming the new # to look for.
  '''
  curr_num = start_num
  chain_list = []
  while curr_num in pair_dict:
    chain_list.append(str(curr_num))
    curr_num = pair_dict[curr_num]
    if curr_num == start_num:
      break
  chain_list.append(str(curr_num))
  return chain_list

if __name__== '__main__':

  longest_chain = []
  longest_length = 0

  #File is taken from command line and opened.
  if len(sys.argv) != 2:
    print('Usage: python pa1.py <input-csv-file>')
    sys.exit(1)
  file = sys.argv[1]

  #Puts the data from the file into a dictionary
  with open(file, 'r') as data:
    reader = csv.reader(data)
    pair_dict = dict(reader)

  #Loops through the dictionary keys and calls the chain_finder function
  for key in pair_dict:
    finding_chain = chain_finder(key, pair_dict)
    #Checks which chain is the longest link

    if len(finding_chain) >= longest_length:
      longest_chain = finding_chain
      longest_length  = len(finding_chain)
      
  #Prints the longest_chain and the length of it
  print(f'{longest_chain} with length {str(longest_length)}')


  

  
    

 
    
      


      

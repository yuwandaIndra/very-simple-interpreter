import os
from time import sleep
while True:
	
	print("========================================================")
	print("                 very simple compiler                   ")
	print("                                                        ")
	print("syntax   # cetak doublequote helloworld doublequote;    ")
	print("output : helloworld                                     ")
	print("                                                        ")
	print("shutdown compiler                                       ")
	print("# selesai;")
	print("-Yuwanda")
	print("========================================================")
	print("                                                        ")
	print("                                                        ")
	# Get input from user
	userInput = input("")
	text = userInput

	# Make the text a list
	text = list(text)

	# Show list of text
	# print(text)

	# Set current state as None
	currentState = None

	# Set start state from 0
	startState = 0

	# Set final state to {11}
	finalStates = {11}

	# Set status to False
	status = False

	# Initialize States
	states = dict()

	# State 0
	states[(0, '#')] = 1

	# State 1
	states[(1, ' ')] = 2

	# State 2
	states[(2, 'c')] = 3
	states[(2, 's')] = 12

	# State 3
	states[(3, 'e')] = 4

	# State 4
	states[(4, 't')] = 5

	# State 5
	states[(5, 'a')] = 6

	# State 6
	states[(6, 'k')] = 7

	# State 7
	states[(7, ' ')] = 8

	# State 8
	states[(8, '\"')] = 9

	# State 9
	states[(9, '\"')] = 10
	# Generate all character except '"'
	for ch in range(ord(' '), ord('~')+1):
		if ch is not ord('\"') and (ch < ord('A') or ch > ord('Z')):
			states[(9, chr(ch))] = 9

	# State 10
	states[(10, ';')] = 11

	# State 11
	# Final State

	# State 12
	states[(12, 'e')] = 13

	# State 13
	states[(13, 'l')] = 14

	# State 14
	states[(14, 'e')] = 15

	# State 15
	states[(15, 's')] = 16

	# State 16
	states[(16, 'a')] = 17

	# State 17
	states[(17, 'i')] = 10

	# Print States
	# print(states)

	# Assign currentState with startState
	currentState = startState

	# Loop for every character in text
	# print("State\tCharacter")
	for ch in text:
		# Check if state is None
		if currentState is None:
			# If state is none then break the loop
			break
		
		# Set current state to next of current state with conditional character
		currentState = states.get((currentState, ch.lower()))
		# print(currentState, "\t", ch)
		
		# Check if state is final state
		if currentState in finalStates:
			# If state is final state then set status to True and break the loop
			status = True
			break

	# Show status
	# print("\nStatus : %r" % status)
	
	lower = userInput.lower()
	if status:
		if "selesai" in lower:
			print("          ")
			print(">", "Terima kasih sudah menggunakan compiler ini.")
			sleep(4)
			os.system('cls')
			break
		elif "cetak" in lower:
			output = ''.join(text[text.index('\"')+1:text.index(';')-1])
			print("   ")
			print(">", output)
			sleep(4)
			os.system('cls')
		
	else:
		print(">", "Kode tidak sesuai dengan peraturan.")
	
def main():
	print("1. Jouer")
	print("2. Quittez")
	menu_input = input("Choisissez votre chemin: ")
	menu_input = int(menu_input)
	if menu_input == 1:
		play_one_game()
	else:
		print()
		print("Vous n'êtes pas digne de nous affronter")



# Vérifie si le jeu est fini
def jeu_fini(game_string):
	first_four_symbols = game_string[0:4] 
	if first_four_symbols == "$$$$":
		return True
		
	return False
	
# Lance la partie
def play_one_game():
	player_num = 1
	
	partie_finie = False
	game_string = create_game_string()
	
	
	while partie_finie == False:
		display_game_string(game_string)
		position_num = get_user_position_num(player_num)
		move_num = get_num_to_move()
		game_string = move_dollar_to_the_left(game_string, position_num, move_num)
		partie_finie = jeu_fini(game_string)
	
		if partie_finie:
			display_game_string(game_string)
			féliciter_joueur_gagnant(player_num)
		else:
			player_num = get_next_player_num(player_num)
		
def create_game_string():
	game_line = " $ $ $ $ "
	return game_line	

def jumble_game_line(game_string):
	import random
	random_pos = random.randrange(0,9) 
	randomize = game_string[0:random_pos] + game_string[random_pos+1:] + game_string[random_pos]
	for i in range(7):
		randomize
	return randomize
	
def random_game_string(game_string):
	return jumble_game_line(game_string)

def display_game_string(game_string):
	linesv2 = "||  " + "   |  " * 8+"   ||"
	game_list = list(game_string)
	lines_list = list(linesv2)
	lines_list[4] = game_list [0]
	lines_list[10] = game_list[1]
	lines_list[16] = game_list[2]
	lines_list[22] = game_list[3]
	lines_list[28] = game_list[4]
	lines_list[34] = game_list[5]
	lines_list[40] = game_list[6]
	lines_list[46] = game_list[7]
	lines_list[52] = game_list[8]
	join_list = "".join(lines_list)
	join_list = str(join_list)
	print()
	print('    1','2','3','4','5','6','7','8','9', sep="     ")
	print(linesv2)
	print(join_list)
	print(linesv2)
	print()
	return
	
def get_user_position_num(player_num):
	print("PLAYER NUMBER: ", player_num)
	position_number = input("Entrez le numéro de la position: ")
	return position_number

def get_num_to_move():
	move_number = input("Entrez le numéro du mouvement choisie: ")
	move_number = int(move_number) 
	return move_number
	
def move_dollar_to_the_left(game_string, position_number, move_num):
	position_number = int(position_number) - 1
	index_move_number = position_number - move_num 
	game_string = list(game_string)
	game_string[position_number] = game_string[index_move_number]
	game_string[index_move_number] = "$" 
	new_game_string = "".join(game_string)
	return new_game_string
	
	
def get_next_player_num (player_num):
	while player_num == 1:
		return 2 
	else: 
		return 1 
		
def féliciter_joueur_gagnant(player_num):	
	winning_message = "** V O U S  A V E Z  G A G N E R **"
	print("=" * len(winning_message))
	print(winning_message)
	print("     PLAYER NUMBER:", player_num)
	print(winning_message)
	print("=" * len(winning_message))
	
main() 
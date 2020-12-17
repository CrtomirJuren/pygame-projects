"""
Lists & Tic Tac Toe Game - Python 3 Programming Tutorial p.3
user: sentdex
playlist: https://www.youtube.com/playlist?list=PLQVvvaa0QuDeAams7fkdcwOGBpGdHpXln
link: https://www.youtube.com/watch?v=tf3ezjeTpfI

stayed here: https://www.youtube.com/watch?v=BYpSfx7I6x4
"""

game = [[1,2,3],
		[4,5,6],
		[7,8,9]]

def game_board(game_map, player=0, row=0, column=0, just_display = False):
	try:
		#print column names
		print("   a  b  c")
		if not just_display:
			game_map[row][column] = player

		for count,row in enumerate(game_map):
			print(count,row)

		return game_map

	except IndexError as e:
		print("Error: make sure you input row/column as 0,1,2", e)

	except Exception as e:
		print("something went very wrong",e)

def win(current_game):
	#check horizontal row for same [1,1,1]"""
	for row in current_game:
		if row.count(row[0]) == len(row) and row[0] != 0:
			#print(f"wineer")

	#check vertical column for same [1,1,1]"""

	for column in current_game:
		print(game[column])

game = game_board(game, just_display = True)
#game = game_board(game, player=1, row=2, column=1)
win(game)
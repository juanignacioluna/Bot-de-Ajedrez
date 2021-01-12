import tweepy
import requests
import os
import random
from datetime import datetime
import time



 
board = [[" " for x in range(8)] for y in range(8)]
piece_list = ["R", "N", "B", "Q", "P"]
 
 
def place_kings(brd):
	while True:
		rank_white, file_white, rank_black, file_black = random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7)
		diff_list = [abs(rank_white - rank_black),  abs(file_white - file_black)]
		if sum(diff_list) > 2 or set(diff_list) == set([0, 2]):
			brd[rank_white][file_white], brd[rank_black][file_black] = "K", "k"
			break
 
def populate_board(brd, wp, bp):
	for x in range(2):
		if x == 0:
			piece_amount = wp
			pieces = piece_list
		else:
			piece_amount = bp
			pieces = [s.lower() for s in piece_list]
		while piece_amount != 0:
			piece_rank, piece_file = random.randint(0, 7), random.randint(0, 7)
			piece = random.choice(pieces)
			if brd[piece_rank][piece_file] == " " and pawn_on_promotion_square(piece, piece_rank) == False:
				brd[piece_rank][piece_file] = piece
				piece_amount -= 1
 
def fen_from_board(brd):
	fen = ""
	for x in brd:
		n = 0
		for y in x:
			if y == " ":
				n += 1
			else:
				if n != 0:
					fen += str(n)
				fen += y
				n = 0
		if n != 0:
			fen += str(n)
		fen += "/" if fen.count("/") < 7 else ""
	return fen
 
def pawn_on_promotion_square(pc, pr):
	if pc == "P" and pr == 0:
		return True
	elif pc == "p" and pr == 7:
		return True
	return False
 
 
def start():
	piece_amount_white, piece_amount_black = random.randint(0, 15), random.randint(0, 15)
	place_kings(board)
	populate_board(board, piece_amount_white, piece_amount_black)
	

	urlRandom = "https://chessboardimage.com/"+fen_from_board(board)+".png"

	return urlRandom





def tuitear():

	consumer_key="UQQupAw4KKnSPXlFNh1aAFSnm"

	consumer_secret="PO25HI9e0a22AWdGZtkexGvJVqf2wrhpnAMDrpoDntvFgWBEEe"

	key = "1325706116056145920-yxA6OPMxQ2T6sMvJDkX4YfDVaItjy1"

	secret="Q1KqGQ0tS9VJv4EnQkQIUq156yePe3PNA5UjnCLHdM9LJ"


	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(key, secret)

	api = tweepy.API(auth)



	filename = 'temp.png'
	request = requests.get(start(), stream=True)
	if request.status_code == 200:
		with open(filename, 'wb') as image:
			for chunk in request:
				image.write(chunk)

		api.update_with_media(filename, status="#chess #Chessbrah #botezlive #check #checkmate #queensgambit")
		os.remove(filename)
	else:
		print("Unable to download image")





def tweet_check():
	minutes = datetime.now().minute
	seconds = datetime.now().second

	if (minutes == 0 or minutes == 10 or minutes == 20 or minutes == 30 or minutes == 40 or minutes == 50):
		tuitear()
		print("tuiteado")
		time.sleep(120)



if __name__ == '__main__':

	while True:
		board = [[" " for x in range(8)] for y in range(8)]
		piece_list = ["R", "N", "B", "Q", "P"]
		tweet_check()
        